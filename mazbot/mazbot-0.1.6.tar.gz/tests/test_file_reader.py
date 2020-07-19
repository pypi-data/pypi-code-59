#!/usr/bin/env python

"""Tests for `mazbot` package FileReader class."""

import pytest

from mazbot.file_reader import FileReader
from mazbot.facing import Facing


def test_read_input_file_1():
    file_reader = FileReader('input_files/input_file_1.txt')
    returned = file_reader.get_all_instruction_lines()
    expected = ["PLACE 0,0,NORTH", "MOVE", "REPORT"]
    assert returned == expected
