#!/usr/bin/env python

"""Tests for `mazbot` package Runner class."""

import pytest

from mazbot.runner import Runner
from mazbot.robot.robot import Robot
from mazbot.robot.robot import Table
from mazbot.enums.facing import Facing

@pytest.fixture
def runner_object():
    return Runner()

def test_process_command_line_with_one_place_command(runner_object):
    table = Table()  
    robot = Robot(table)

    returned = runner_object._process_command_line(robot, "PLACE 0,0,NORTH")
    expected = {"position": (0, 0), "facing": Facing.NORTH}

    assert returned == expected

def test_process_command_lines_sequence_1(runner_object):
    returned = runner_object._process_command_lines(["PLACE 0,0,NORTH", "MOVE", "REPORT"])
    expected = {"position": (0, 1), "facing": Facing.NORTH}

    assert returned == expected

def test_process_command_lines_sequence_2(runner_object):
    returned = runner_object._process_command_lines(["PLACE 0,0,NORTH", "LEFT", "REPORT"])
    expected = {"position": (0, 0), "facing": Facing.WEST}

    assert returned == expected

def test_process_command_lines_sequence_3(runner_object):
    returned = runner_object._process_command_lines(["PLACE 1,2,EAST", "MOVE", "MOVE", "LEFT", "MOVE", "REPORT"])
    expected = {"position": (3, 3), "facing": Facing.NORTH}

    assert returned == expected

def test_with_file_1(runner_object):
    file_path = 'input_files/input_file_1.txt'

    returned = runner_object.run(file_path)
    expected = {"position": (0, 1), "facing": Facing.NORTH}

    assert returned == expected

def test_with_file_2(runner_object):
    file_path = 'input_files/input_file_2.txt'

    returned = runner_object.run(file_path)
    expected = {"position": (0, 0), "facing": Facing.WEST}

    assert returned == expected

def test_with_file_3(runner_object):
    file_path = 'input_files/input_file_3.txt'

    returned = runner_object.run(file_path)
    expected = {"position": (3, 3), "facing": Facing.NORTH}

    assert returned == expected

def test_with_file_4(runner_object):
    file_path = 'input_files/input_file_4.txt'

    returned = runner_object.run(file_path)
    expected = {"position": (2, 3), "facing": Facing.WEST}

    assert returned == expected