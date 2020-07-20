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

def test_invalid_type_of_command_raises_value_error(runner_object):
    with pytest.raises(ValueError):
        runner_object._validate_command_lines("INVALIDCOMMAND")

def test_invalid_type_of_facing_raises_value_error(runner_object):
    with pytest.raises(ValueError):
        runner_object._validate_command_lines("PLACE 0,0,INVALIDFACING")

def test_invalid_x_coord_raises_value_error(runner_object):
    with pytest.raises(ValueError):
        runner_object._validate_command_lines("PLACE x,0,NORTH")

def test_invalid_y_coord_raises_value_error(runner_object):
    with pytest.raises(ValueError):
        runner_object._validate_command_lines("PLACE y,0,NORTH")

def test_invalid_spacing_raises_value_error(runner_object):
    with pytest.raises(ValueError):
        runner_object._validate_command_lines("PLACE 1, 0,NORTH")

def test_empty_command_raises_Value_error(runner_object):
    with pytest.raises(ValueError):
        runner_object._validate_command_lines([])