from abc import ABCMeta, abstractmethod

from pretf import workflow

# noinspection PyProtectedMember
from pretf.workflow import CompletedProcess

import pretf_helpers._log as log
from pretf_helpers.utils import _gitdirty, GitError


# For custom workflows wit
_DIRTYWARN = {"apply", "init"}
_DIRTYNOTWARN = {"validate"}


class CustomWorkflow(metaclass=ABCMeta):
    def __init__(self, quiet: bool = False):
        if not quiet:
            log.ok(f"CustomWorkflow: {self.__class__.__name__}")

    @abstractmethod
    def __call__(self):
        pass


class DefaultDirtyWarn(CustomWorkflow):
    def __init__(self, quiet: bool = False):
        super().__init__(quiet=quiet)

    def __call__(self):
        result: CompletedProcess = workflow.default()
        if result.args[1] not in _DIRTYNOTWARN:
            try:
                _gitdirty(warn=True)
            except GitError:
                pass
        return result
