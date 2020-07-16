from functools import lru_cache, partial
from socket import timeout as sock_timeout
from time import strftime
from string import Formatter
from subprocess import check_output, CalledProcessError
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from typing import Dict, Callable

from pretf_helpers import _log as log


_GIT_UPSTREAM = "origin"
_DT_FORMAT = "%Y%m%d%H%M%S"
_TESTCONN_URL = "http://www.neverssl.com"


class GitError(CalledProcessError):
    pass


def _ceko(cmd, strip: bool = True) -> str:
    if isinstance(cmd, str):
        cmd = cmd.split()
    rslt = check_output(cmd).decode()
    return rslt.strip() if strip else rslt


def _gitdirty(warn: bool = True) -> bool:
    try:
        dirty = bool(_ceko("git status --short"))
    except CalledProcessError:
        raise GitError
    if warn and dirty:
        log.warn("WARNING: git repo is dirty! Don't forget to commit!")
    return dirty


@lru_cache(maxsize=1)
def _getgitcommit() -> str:
    try:
        commit_id = _ceko("git rev-parse --short HEAD")
    # If not a git repo, git will return with non-zero code, raising CalledProcessError
    except CalledProcessError:
        return "NotGit"

    if _gitdirty():
        return f"{commit_id} DIRTY"
    else:
        return commit_id


@lru_cache(maxsize=1)
def _getusername() -> str:
    return _ceko("whoami").split("\\")[-1]


@lru_cache(maxsize=1)
def _getreponame() -> str:
    try:
        return (
            _ceko(f"git remote get-url {_GIT_UPSTREAM}".split())
                .split("/")[-1]
                .replace(".git", "")
        )
    except CalledProcessError:
        # If not a git repo, or there is no remote of the specified name,
        # git will return with non-zero code, raising CalledProcessError
        return f"local:{Path.cwd().name}"


def _test_connection():
    try:
        with urlopen(_TESTCONN_URL, timeout=3.0) as http:
            _ = http.read()
    except (HTTPError, URLError, sock_timeout):
        log.warn("No internet connection detected!")


class TemplateDecoder:
    def __init__(self, error_on_unknown: bool = False):
        self._eunk = error_on_unknown
        self.funcs: Dict[str, Callable[[], str]] = {
            "CURRENT_USER": _getusername,
            "CURRENT_REPO": _getreponame,
            "CURRENT_DATETIME": partial(strftime, _DT_FORMAT),
        }

    def _getval(self, name: str) -> str:
        if name in self.funcs:
            return self.funcs[name]()

        if self._eunk:
            raise KeyError(f"Unknown Template Key {{{{{name}}}}}")
        else:
            return "{{" + name + "}}"

    def keys(self):
        return self.funcs.keys()

    def render(self, template: str):
        sf = Formatter()
        rd = {vn: self._getval(vn) for _, vn, _, _ in sf.parse(template) if vn}
        return sf.format(template, **rd)
