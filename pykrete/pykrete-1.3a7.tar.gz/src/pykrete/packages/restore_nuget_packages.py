"""
Python package installation
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from pykrete.calls import CheckedCall
from pykrete.patterns import pykrete_externals


def make_nuget_command(params, nuget_config=None):
    """
    :param params: NuGet parameters
    :param nuget_config: (optional) NuGet configuration file path
    :return: NuGet command vector
    """
    nuget_exe = 'nuget.exe'
    command = [f'"{pykrete_externals(nuget_exe)}"'] + params
    if nuget_config:
        command = command + ['-ConfigFile', nuget_config]
    return command


def restore_nuget_packages(sln_path, nuget_config=None, is_update=False):
    """Restores NuGet package
    """
    commands = ['restore'] + (['update'] if is_update else [])
    for command in commands:
        CheckedCall(make_nuget_command([command, sln_path], nuget_config)) \
            .assert_success('failed to run nuget ' + command)
