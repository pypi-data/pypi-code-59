#!/usr/bin/env python

"""Tests for `mazbot` package FileReader class."""

import pytest

from mazbot.utils.file_reader import FileReader
from mazbot.enums.facing import Facing


def test_read_input_file_1():
    file_reader = FileReader('input_files/input_file_1.txt')
    returned = file_reader.get_all_command_lines()
    expected = ["PLACE 0,0,NORTH", "MOVE", "REPORT"]
    assert returned == expected


def test_read_non_existent_file_raises_value_error():
    with pytest.raises(Exception):
        file_reader = FileReader(
            'input_files/input_file_that_does_not_exist.txt')
        file_reader.get_all_command_lines()


def test_read_invalid_file_raises_value_error():
    with pytest.raises(Exception):
        file_reader = FileReader('input_files/input_file_13.txt')
        file_reader.get_all_command_lines()
