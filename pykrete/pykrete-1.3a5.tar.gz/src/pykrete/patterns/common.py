"""
Common module
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""


def assert_true(target, error):
    """Assert success of target

    :param target: target with bool success attribute
    :param error: error message in case of failure
    """
    if not target:
        raise AssertionError(error)
