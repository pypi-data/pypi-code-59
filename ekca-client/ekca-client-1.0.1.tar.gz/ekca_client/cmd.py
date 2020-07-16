"""
client for EKCA service -- SSH shell commands
"""

import os.path
import shlex

from collections import UserList

__all__ = [
    'ShellCommand',
    'SSH_ADD_PWPROMPT',
    'SSH_ADD_WAIT',
]

SSH_ADD_WAIT = 0.4


class ShellCommand(UserList):
    """
    wrapper class for list of shell-quoted command-line arguments
    """

    def __str__(self):
        return ' '.join(shlex.quote(arg) for arg in self)
