from os import getenv, getcwd
from pathlib import Path
from typing import Optional

from git import Repo, exc


def strtobool(s) -> Optional[bool]:
    """
    Convert a string into a boolean value or None

    True is returned when yes, true or 1 is called
    False is returned when no, false or 0 is called
    None is returned on any other value, we do this because we want to know if we are passing an
    invalid value
    """
    if s.lower() in ("yes", "true", "1"):
        return True
    elif s.lower() in ("no", "false", "0"):
        return False
    else:
        return None


def prompt(s=None) -> None:
    """Prompt the user with some information

    Args:
        s (str, optional): string that has the information to show. Defaults to None.
    """
    if s is not None:
        print(s)
    input("Press Enter to continue...")


def create_dir(path: Path) -> Path:
    """Create or re-create a directory with 700 permissions, and its parents

    Args:
        path (Path): full path to the directory to be created

    Returns:
        Path: full path to the directory that was created
    """
    if path.exists() and not path.is_dir():
        path.unlink()

    path.mkdir(mode=0o700, parents=True, exist_ok=True)
    return path


def create_file(path: Path) -> Path:
    """Create a file or re-creates it with 600 permissions, create parent directories with 700
    permissions

    Args:
        path (Path): full path to the file to be created

    Returns:
        Path: full path to the file that was created
    """
    # Get the parent
    create_dir(path.parent)

    # If the file exists but is not a file then remove
    # it is as well
    if path.exists() and not path.is_file():
        path.unlink()

    # Create it with nice permissions for a file that
    # hold secrets
    path.touch(mode=0o600)
    return path


def find_config(p: Optional[str]) -> Path:
    """Create a configuration file, respecting XDG_CONFIG_HOME

    Args:
        p (Optional[str]): a pre-determined path, if not None it will return the created file

    Raises:
        ValueError: If we can't find a proper location of the config, see message

    Returns:
        Path: path to created config file
    """
    xdgpath: Optional[str]  # Value of XDG_CONFIG_HOME, can be none if unset
    homepath: Optional[str]  # Value of HOME, required if xdgpath is None

    if p is not None:
        path = Path(p)
        return create_file(path)

    xdgpath = getenv("XDG_CONFIG_HOME")
    if xdgpath is not None:
        path = Path(xdgpath)
        return create_file(path / "mkmr" / "config")

    homepath = getenv("HOME")
    if homepath is None:
        raise ValueError("Neither XDG_CONFIG_HOME or HOME are set, please set XDG_CONFIG_HOME")

    if xdgpath is None:
        path = Path(homepath)
        return create_file(path / ".config" / "mkmr" / "config")


def find_cache() -> Path:
    """Create a cache directory, respecting XDG_CACHE_HOME

    Raises:
        ValueError: if neither HOME or XDG_CACHE_HOME are set then we error out

    Returns:
        Path: [description]
    """
    xdgpath: Optional[str]  # Value of XDG_CACHE_HOME, can be none if unset
    homepath: Optional[str]  # Value of HOME, required if xdgpath is None

    xdgpath = getenv("XDG_CACHE_HOME")
    if xdgpath is not None:
        path = Path(xdgpath)
        return create_dir(path / "mkmr")

    homepath = getenv("HOME")
    if homepath is None:
        raise ValueError("Neither XDG_CACHE_HOME or HOME are set, please set XDG_CACHE_HOME")

    if homepath is not None:
        path = Path(homepath)
        return create_dir(path / ".cache" / "mkmr")


def init_repo(path=None) -> Optional[Repo]:
    """Initialize a git repo and return its object

    Args:
        path (Path, optional): path to the git repo. Defaults to None.

    Returns:
        Optional[Repo]: Repo object that can be used to run git commands
    """
    if path is None:
        path = Path(getcwd())

    def _init_repo(path) -> Repo:
        try:
            repo = Repo(path)
        except exc.InvalidGitRepositoryError:
            if path == Path("/"):
                raise
            return _init_repo(path=path.parent)
        else:
            return repo

    try:
        return _init_repo(path)
    except exc.InvalidGitRepositoryError:
        print("Failed to start repo at {} or any of its parent directories".format(path))
        return None
