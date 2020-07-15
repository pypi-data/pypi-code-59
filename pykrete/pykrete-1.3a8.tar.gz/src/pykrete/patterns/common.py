"""
Common module
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import os


def assert_true(target, error):
    """Assert success of target

    :param target: target with bool success attribute
    :param error: error message in case of failure
    """
    if not target:
        raise AssertionError(error)


def pykrete_root():
    """
    :return: this package's installation root
    """
    package = 'pykrete'
    this_file = str(__file__)
    root = this_file[0:this_file.rfind(package)+len(package)]
    return root


def pykrete_externals(filename):
    """
    :param filename: file under 'externals' folder
    :return: path to an externals file in this package's intallation folder
    """
    return os.path.join(pykrete_root(), 'externals', filename)
