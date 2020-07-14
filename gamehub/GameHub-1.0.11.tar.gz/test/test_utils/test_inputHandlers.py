"""
tests all the input handling functions
"""
import pytest

from utils import inputHandlers


@pytest.mark.parametrize("string,expected",
                         [
                             ("1", True),
                             ("", True),
                             ("09.5", True),
                             ("hello", False)
                         ])
def test_input_handler_strings(string: str, expected: bool) -> None:
    """
    tests if 'check_for_bad_input_strings' can detect these bad inputs
    :param string: the string that is inputted
    :param expected: the expected output of the function
    :return: whether or not this function works
    """
    actual_output = inputHandlers.check_for_bad_input_strings(string)
    assert actual_output == expected


@pytest.mark.parametrize("user_input, list_of_bad_inputs, expected",
                         [("a", [3, 6, 2], True),
                          ("", [3, 6, 2], True),
                          ("3", [3, 6, 2], True),
                          ("11", [3, 6, 2], True),
                          ("?@", [3, 6, 2], True),
                          ("7", [3, 6, 2], False)])
def test_check_for_bad_inputs_bad_input_int(user_input: str, list_of_bad_inputs: list, expected: bool) -> None:
    """
    testing that it returns False if there is a bad input
    """
    actual_output = inputHandlers.check_for_bad_input_int(user_input, list_of_bad_inputs, 10)
    assert actual_output == expected
