"""
Python package installation
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import logging
import os
from pykrete.calls import CheckedCall


def restore_nuget_packages():  # sln_path, nuget_config=None, is_update=False):
    """Restores NuGet package
    """
    _logger = logging.getLogger(__name__)
    _logger.debug(__file__)
    CheckedCall(os.path.join('externals', 'nuget.exe')).assert_success('failed to run nuget')
