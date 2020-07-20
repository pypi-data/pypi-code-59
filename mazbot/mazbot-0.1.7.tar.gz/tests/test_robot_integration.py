#!/usr/bin/env python

"""Integration Tests for `mazbot` package Robot class."""

import pytest
from unittest.mock import patch, Mock

from mazbot.robot.robot import Robot
from mazbot.robot.robot import Table
from mazbot.enums.facing import Facing
from mazbot.enums.command import Command


@pytest.fixture
def robot_object():
    table = Table()
    return Robot(table)


def test_command_sequence_1(robot_object):
    robot_object.process_command(
        Command.PLACE, coords=(0, 0), facing=Facing.NORTH)
    robot_object.process_command(Command.MOVE)
    returned = robot_object.process_command(Command.REPORT)
    expected = {"position": (0, 1), "facing": Facing.NORTH}
    assert returned == expected


def test_command_sequence_2(robot_object):
    robot_object.process_command(
        Command.PLACE, coords=(0, 0), facing=Facing.NORTH)
    robot_object.process_command(Command.LEFT)
    returned = robot_object.process_command(Command.REPORT)
    expected = {"position": (0, 0), "facing": Facing.WEST}
    assert returned == expected


def test_command_sequence_3(robot_object):
    robot_object.process_command(
        Command.PLACE, coords=(1, 2), facing=Facing.EAST)
    robot_object.process_command(Command.MOVE)
    robot_object.process_command(Command.MOVE)
    robot_object.process_command(Command.LEFT)
    robot_object.process_command(Command.MOVE)
    returned = robot_object.process_command(Command.REPORT)
    expected = {"position": (3, 3), "facing": Facing.NORTH}
    assert returned == expected


def test_invalid_place_command_ignored(robot_object):
    robot_object.process_command(Command.MOVE)
    robot_object.process_command(
        Command.PLACE, coords=(6, 2), facing=Facing.EAST)
    robot_object.process_command(Command.MOVE)
    robot_object.process_command(Command.MOVE)
    robot_object.process_command(Command.LEFT)
    robot_object.process_command(
        Command.PLACE, coords=(1, 1), facing=Facing.EAST)
    robot_object.process_command(Command.MOVE)
    returned = robot_object.process_command(Command.REPORT)
    expected = {"position": (2, 1), "facing": Facing.EAST}
    assert returned == expected


def test_invalid_place_and_move_commands_ignored(robot_object):
    robot_object.process_command(Command.MOVE)
    robot_object.process_command(
        Command.PLACE, coords=(6, 2), facing=Facing.EAST)
    robot_object.process_command(Command.MOVE)
    robot_object.process_command(Command.MOVE)
    robot_object.process_command(Command.LEFT)
    robot_object.process_command(
        Command.PLACE, coords=(1, 1), facing=Facing.EAST)
    robot_object.process_command(Command.RIGHT)
    robot_object.process_command(Command.MOVE)
    robot_object.process_command(Command.MOVE)
    returned = robot_object.process_command(Command.REPORT)
    expected = {"position": (1, 0), "facing": Facing.SOUTH}
    assert returned == expected
