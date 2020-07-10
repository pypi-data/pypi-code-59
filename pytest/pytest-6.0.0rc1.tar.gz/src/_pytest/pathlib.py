import atexit
import contextlib
import fnmatch
import importlib.util
import itertools
import os
import shutil
import sys
import uuid
import warnings
from enum import Enum
from functools import partial
from os.path import expanduser
from os.path import expandvars
from os.path import isabs
from os.path import sep
from posixpath import sep as posix_sep
from types import ModuleType
from typing import Iterable
from typing import Iterator
from typing import Optional
from typing import Set
from typing import TypeVar
from typing import Union

import py

from _pytest.compat import assert_never
from _pytest.outcomes import skip
from _pytest.warning_types import PytestWarning

if sys.version_info[:2] >= (3, 6):
    from pathlib import Path, PurePath
else:
    from pathlib2 import Path, PurePath

__all__ = ["Path", "PurePath"]


LOCK_TIMEOUT = 60 * 60 * 3


_AnyPurePath = TypeVar("_AnyPurePath", bound=PurePath)


def get_lock_path(path: _AnyPurePath) -> _AnyPurePath:
    return path.joinpath(".lock")


def ensure_reset_dir(path: Path) -> None:
    """
    ensures the given path is an empty directory
    """
    if path.exists():
        rm_rf(path)
    path.mkdir()


def on_rm_rf_error(func, path: str, exc, *, start_path: Path) -> bool:
    """Handles known read-only errors during rmtree.

    The returned value is used only by our own tests.
    """
    exctype, excvalue = exc[:2]

    # another process removed the file in the middle of the "rm_rf" (xdist for example)
    # more context: https://github.com/pytest-dev/pytest/issues/5974#issuecomment-543799018
    if isinstance(excvalue, FileNotFoundError):
        return False

    if not isinstance(excvalue, PermissionError):
        warnings.warn(
            PytestWarning(
                "(rm_rf) error removing {}\n{}: {}".format(path, exctype, excvalue)
            )
        )
        return False

    if func not in (os.rmdir, os.remove, os.unlink):
        if func not in (os.open,):
            warnings.warn(
                PytestWarning(
                    "(rm_rf) unknown function {} when removing {}:\n{}: {}".format(
                        func, path, exctype, excvalue
                    )
                )
            )
        return False

    # Chmod + retry.
    import stat

    def chmod_rw(p: str) -> None:
        mode = os.stat(p).st_mode
        os.chmod(p, mode | stat.S_IRUSR | stat.S_IWUSR)

    # For files, we need to recursively go upwards in the directories to
    # ensure they all are also writable.
    p = Path(path)
    if p.is_file():
        for parent in p.parents:
            chmod_rw(str(parent))
            # stop when we reach the original path passed to rm_rf
            if parent == start_path:
                break
    chmod_rw(str(path))

    func(path)
    return True


def ensure_extended_length_path(path: Path) -> Path:
    """Get the extended-length version of a path (Windows).

    On Windows, by default, the maximum length of a path (MAX_PATH) is 260
    characters, and operations on paths longer than that fail. But it is possible
    to overcome this by converting the path to "extended-length" form before
    performing the operation:
    https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file#maximum-path-length-limitation

    On Windows, this function returns the extended-length absolute version of path.
    On other platforms it returns path unchanged.
    """
    if sys.platform.startswith("win32"):
        path = path.resolve()
        path = Path(get_extended_length_path_str(str(path)))
    return path


def get_extended_length_path_str(path: str) -> str:
    """Converts to extended length path as a str"""
    long_path_prefix = "\\\\?\\"
    unc_long_path_prefix = "\\\\?\\UNC\\"
    if path.startswith((long_path_prefix, unc_long_path_prefix)):
        return path
    # UNC
    if path.startswith("\\\\"):
        return unc_long_path_prefix + path[2:]
    return long_path_prefix + path


def rm_rf(path: Path) -> None:
    """Remove the path contents recursively, even if some elements
    are read-only.
    """
    path = ensure_extended_length_path(path)
    onerror = partial(on_rm_rf_error, start_path=path)
    shutil.rmtree(str(path), onerror=onerror)


def find_prefixed(root: Path, prefix: str) -> Iterator[Path]:
    """finds all elements in root that begin with the prefix, case insensitive"""
    l_prefix = prefix.lower()
    for x in root.iterdir():
        if x.name.lower().startswith(l_prefix):
            yield x


def extract_suffixes(iter: Iterable[PurePath], prefix: str) -> Iterator[str]:
    """
    :param iter: iterator over path names
    :param prefix: expected prefix of the path names
    :returns: the parts of the paths following the prefix
    """
    p_len = len(prefix)
    for p in iter:
        yield p.name[p_len:]


def find_suffixes(root: Path, prefix: str) -> Iterator[str]:
    """combines find_prefixes and extract_suffixes
    """
    return extract_suffixes(find_prefixed(root, prefix), prefix)


def parse_num(maybe_num) -> int:
    """parses number path suffixes, returns -1 on error"""
    try:
        return int(maybe_num)
    except ValueError:
        return -1


def _force_symlink(
    root: Path, target: Union[str, PurePath], link_to: Union[str, Path]
) -> None:
    """helper to create the current symlink

    it's full of race conditions that are reasonably ok to ignore
    for the context of best effort linking to the latest test run

    the presumption being that in case of much parallelism
    the inaccuracy is going to be acceptable
    """
    current_symlink = root.joinpath(target)
    try:
        current_symlink.unlink()
    except OSError:
        pass
    try:
        current_symlink.symlink_to(link_to)
    except Exception:
        pass


def make_numbered_dir(root: Path, prefix: str) -> Path:
    """create a directory with an increased number as suffix for the given prefix"""
    for i in range(10):
        # try up to 10 times to create the folder
        max_existing = max(map(parse_num, find_suffixes(root, prefix)), default=-1)
        new_number = max_existing + 1
        new_path = root.joinpath("{}{}".format(prefix, new_number))
        try:
            new_path.mkdir()
        except Exception:
            pass
        else:
            _force_symlink(root, prefix + "current", new_path)
            return new_path
    else:
        raise OSError(
            "could not create numbered dir with prefix "
            "{prefix} in {root} after 10 tries".format(prefix=prefix, root=root)
        )


def create_cleanup_lock(p: Path) -> Path:
    """crates a lock to prevent premature folder cleanup"""
    lock_path = get_lock_path(p)
    try:
        fd = os.open(str(lock_path), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    except FileExistsError as e:
        raise OSError("cannot create lockfile in {path}".format(path=p)) from e
    else:
        pid = os.getpid()
        spid = str(pid).encode()
        os.write(fd, spid)
        os.close(fd)
        if not lock_path.is_file():
            raise OSError("lock path got renamed after successful creation")
        return lock_path


def register_cleanup_lock_removal(lock_path: Path, register=atexit.register):
    """registers a cleanup function for removing a lock, by default on atexit"""
    pid = os.getpid()

    def cleanup_on_exit(lock_path: Path = lock_path, original_pid: int = pid) -> None:
        current_pid = os.getpid()
        if current_pid != original_pid:
            # fork
            return
        try:
            lock_path.unlink()
        except OSError:
            pass

    return register(cleanup_on_exit)


def maybe_delete_a_numbered_dir(path: Path) -> None:
    """removes a numbered directory if its lock can be obtained and it does not seem to be in use"""
    path = ensure_extended_length_path(path)
    lock_path = None
    try:
        lock_path = create_cleanup_lock(path)
        parent = path.parent

        garbage = parent.joinpath("garbage-{}".format(uuid.uuid4()))
        path.rename(garbage)
        rm_rf(garbage)
    except OSError:
        #  known races:
        #  * other process did a cleanup at the same time
        #  * deletable folder was found
        #  * process cwd (Windows)
        return
    finally:
        # if we created the lock, ensure we remove it even if we failed
        # to properly remove the numbered dir
        if lock_path is not None:
            try:
                lock_path.unlink()
            except OSError:
                pass


def ensure_deletable(path: Path, consider_lock_dead_if_created_before: float) -> bool:
    """checks if a lock exists and breaks it if its considered dead"""
    if path.is_symlink():
        return False
    lock = get_lock_path(path)
    if not lock.exists():
        return True
    try:
        lock_time = lock.stat().st_mtime
    except Exception:
        return False
    else:
        if lock_time < consider_lock_dead_if_created_before:
            # wa want to ignore any errors while trying to remove the lock such as:
            # - PermissionDenied, like the file permissions have changed since the lock creation
            # - FileNotFoundError, in case another pytest process got here first.
            # and any other cause of failure.
            with contextlib.suppress(OSError):
                lock.unlink()
                return True
        return False


def try_cleanup(path: Path, consider_lock_dead_if_created_before: float) -> None:
    """tries to cleanup a folder if we can ensure it's deletable"""
    if ensure_deletable(path, consider_lock_dead_if_created_before):
        maybe_delete_a_numbered_dir(path)


def cleanup_candidates(root: Path, prefix: str, keep: int) -> Iterator[Path]:
    """lists candidates for numbered directories to be removed - follows py.path"""
    max_existing = max(map(parse_num, find_suffixes(root, prefix)), default=-1)
    max_delete = max_existing - keep
    paths = find_prefixed(root, prefix)
    paths, paths2 = itertools.tee(paths)
    numbers = map(parse_num, extract_suffixes(paths2, prefix))
    for path, number in zip(paths, numbers):
        if number <= max_delete:
            yield path


def cleanup_numbered_dir(
    root: Path, prefix: str, keep: int, consider_lock_dead_if_created_before: float
) -> None:
    """cleanup for lock driven numbered directories"""
    for path in cleanup_candidates(root, prefix, keep):
        try_cleanup(path, consider_lock_dead_if_created_before)
    for path in root.glob("garbage-*"):
        try_cleanup(path, consider_lock_dead_if_created_before)


def make_numbered_dir_with_cleanup(
    root: Path, prefix: str, keep: int, lock_timeout: float
) -> Path:
    """creates a numbered dir with a cleanup lock and removes old ones"""
    e = None
    for i in range(10):
        try:
            p = make_numbered_dir(root, prefix)
            lock_path = create_cleanup_lock(p)
            register_cleanup_lock_removal(lock_path)
        except Exception as exc:
            e = exc
        else:
            consider_lock_dead_if_created_before = p.stat().st_mtime - lock_timeout
            # Register a cleanup for program exit
            atexit.register(
                cleanup_numbered_dir,
                root,
                prefix,
                keep,
                consider_lock_dead_if_created_before,
            )
            return p
    assert e is not None
    raise e


def resolve_from_str(input: str, root):
    assert not isinstance(input, Path), "would break on py2"
    root = Path(root)
    input = expanduser(input)
    input = expandvars(input)
    if isabs(input):
        return Path(input)
    else:
        return root.joinpath(input)


def fnmatch_ex(pattern: str, path) -> bool:
    """FNMatcher port from py.path.common which works with PurePath() instances.

    The difference between this algorithm and PurePath.match() is that the latter matches "**" glob expressions
    for each part of the path, while this algorithm uses the whole path instead.

    For example:
        "tests/foo/bar/doc/test_foo.py" matches pattern "tests/**/doc/test*.py" with this algorithm, but not with
        PurePath.match().

    This algorithm was ported to keep backward-compatibility with existing settings which assume paths match according
    this logic.

    References:
    * https://bugs.python.org/issue29249
    * https://bugs.python.org/issue34731
    """
    path = PurePath(path)
    iswin32 = sys.platform.startswith("win")

    if iswin32 and sep not in pattern and posix_sep in pattern:
        # Running on Windows, the pattern has no Windows path separators,
        # and the pattern has one or more Posix path separators. Replace
        # the Posix path separators with the Windows path separator.
        pattern = pattern.replace(posix_sep, sep)

    if sep not in pattern:
        name = path.name
    else:
        name = str(path)
        if path.is_absolute() and not os.path.isabs(pattern):
            pattern = "*{}{}".format(os.sep, pattern)
    return fnmatch.fnmatch(name, pattern)


def parts(s: str) -> Set[str]:
    parts = s.split(sep)
    return {sep.join(parts[: i + 1]) or sep for i in range(len(parts))}


def symlink_or_skip(src, dst, **kwargs):
    """Makes a symlink or skips the test in case symlinks are not supported."""
    try:
        os.symlink(str(src), str(dst), **kwargs)
    except OSError as e:
        skip("symlinks not supported: {}".format(e))


class ImportMode(Enum):
    """Possible values for `mode` parameter of `import_path`"""

    prepend = "prepend"
    append = "append"
    importlib = "importlib"


class ImportPathMismatchError(ImportError):
    """Raised on import_path() if there is a mismatch of __file__'s.

    This can happen when `import_path` is called multiple times with different filenames that has
    the same basename but reside in packages
    (for example "/tests1/test_foo.py" and "/tests2/test_foo.py").
    """


def import_path(
    p: Union[str, py.path.local, Path],
    *,
    mode: Union[str, ImportMode] = ImportMode.prepend
) -> ModuleType:
    """
    Imports and returns a module from the given path, which can be a file (a module) or
    a directory (a package).

    The import mechanism used is controlled by the `mode` parameter:

    * `mode == ImportMode.prepend`: the directory containing the module (or package, taking
      `__init__.py` files into account) will be put at the *start* of `sys.path` before
      being imported with `__import__.

    * `mode == ImportMode.append`: same as `prepend`, but the directory will be appended
      to the end of `sys.path`, if not already in `sys.path`.

    * `mode == ImportMode.importlib`: uses more fine control mechanisms provided by `importlib`
      to import the module, which avoids having to use `__import__` and muck with `sys.path`
      at all. It effectively allows having same-named test modules in different places.

    :raise ImportPathMismatchError: if after importing the given `path` and the module `__file__`
        are different. Only raised in `prepend` and `append` modes.
    """
    mode = ImportMode(mode)

    path = Path(str(p))

    if not path.exists():
        raise ImportError(path)

    if mode is ImportMode.importlib:
        module_name = path.stem

        for meta_importer in sys.meta_path:
            spec = meta_importer.find_spec(module_name, [str(path.parent)])
            if spec is not None:
                break
        else:
            spec = importlib.util.spec_from_file_location(module_name, str(path))

        if spec is None:
            raise ImportError(
                "Can't find module {} at location {}".format(module_name, str(path))
            )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)  # type: ignore[union-attr]
        return mod

    pkg_path = resolve_package_path(path)
    if pkg_path is not None:
        pkg_root = pkg_path.parent
        names = list(path.with_suffix("").relative_to(pkg_root).parts)
        if names[-1] == "__init__":
            names.pop()
        module_name = ".".join(names)
    else:
        pkg_root = path.parent
        module_name = path.stem

    # change sys.path permanently: restoring it at the end of this function would cause surprising
    # problems because of delayed imports: for example, a conftest.py file imported by this function
    # might have local imports, which would fail at runtime if we restored sys.path.
    if mode is ImportMode.append:
        if str(pkg_root) not in sys.path:
            sys.path.append(str(pkg_root))
    elif mode is ImportMode.prepend:
        if str(pkg_root) != sys.path[0]:
            sys.path.insert(0, str(pkg_root))
    else:
        assert_never(mode)

    importlib.import_module(module_name)

    mod = sys.modules[module_name]
    if path.name == "__init__.py":
        return mod

    ignore = os.environ.get("PY_IGNORE_IMPORTMISMATCH", "")
    if ignore != "1":
        module_file = mod.__file__
        if module_file.endswith((".pyc", ".pyo")):
            module_file = module_file[:-1]
        if module_file.endswith(os.path.sep + "__init__.py"):
            module_file = module_file[: -(len(os.path.sep + "__init__.py"))]

        try:
            is_same = os.path.samefile(str(path), module_file)
        except FileNotFoundError:
            is_same = False

        if not is_same:
            raise ImportPathMismatchError(module_name, module_file, path)

    return mod


def resolve_package_path(path: Path) -> Optional[Path]:
    """Return the Python package path by looking for the last
    directory upwards which still contains an __init__.py.
    Return None if it can not be determined.
    """
    result = None
    for parent in itertools.chain((path,), path.parents):
        if parent.is_dir():
            if not parent.joinpath("__init__.py").is_file():
                break
            if not parent.name.isidentifier():
                break
            result = parent
    return result
