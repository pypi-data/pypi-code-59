"""
Python package installation
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from pykrete.calls import CheckedCall
from pykrete.patterns import pykrete_externals


def restore_nuget_packages():  # sln_path, nuget_config=None, is_update=False):
    """Restores NuGet package
    """
    CheckedCall(pykrete_externals('nuget.exe')).assert_success('failed to run nuget')
