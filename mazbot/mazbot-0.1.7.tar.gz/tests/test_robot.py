#!/usr/bin/env python

"""Tests for `mazbot` package Robot class."""

import pytest
from unittest.mock import patch, Mock, MagicMock

from mazbot.robot.robot import Robot
from mazbot.robot.table import Table
from mazbot.enums.facing import Facing
from mazbot.enums.command import Command


@pytest.fixture
def robot_object():
    table = Mock()
    table.is_position_valid = Mock(return_value=True)
    return Robot(table)


@pytest.fixture
def robot_object_table_invalid():
    table = Mock()
    table.is_position_valid = Mock(return_value=False)
    return Robot(table)


@pytest.fixture
def placed_robot_object_origin():
    table = Mock()
    table.is_position_valid = Mock(return_value=True)
    rbt = Robot(table)
    rbt._position = (0, 0)
    rbt._facing = Facing.NORTH
    rbt._is_on_table = True
    return rbt


@pytest.fixture
def placed_robot_object_non_origin():
    table = Mock()
    table.is_position_valid = Mock(return_value=True)
    rbt = Robot(table)
    rbt._position = (1, 2)
    rbt._facing = Facing.WEST
    rbt._is_on_table = True
    return rbt


def test_process_command_returns_none_if_not_on_table(robot_object):
    assert robot_object.process_command(Command.MOVE) == None


def test_placing_in_origin_facing_north_returns_correct_robot_state(robot_object):
    coord_value = (0, 0)
    facing_value = Facing.NORTH

    robot_object._place(coord_value, facing_value)

    result = {"position": robot_object._position,
              "facing": robot_object._facing, "is_on_table": robot_object._is_on_table}
    expected = {"position": coord_value,
                "facing": facing_value, "is_on_table": True}

    assert result == expected


def test_placing_in_non_origin_location_returns_correct_robot_state(robot_object):
    coord_value = (1, 2)
    facing_value = Facing.WEST

    robot_object._place(coord_value, facing_value)

    result = {"position": robot_object._position,
              "facing": robot_object._facing, "is_on_table": robot_object._is_on_table}
    expected = {"position": coord_value,
                "facing": facing_value, "is_on_table": True}

    assert result == expected


def test_placing_outside_table_is_ignored(robot_object_table_invalid):
    coord_value = (10, 7)
    facing_value = Facing.WEST

    robot_object_table_invalid._place(coord_value, facing_value)

    result = {"position": robot_object_table_invalid._position,
              "facing": robot_object_table_invalid._facing, "is_on_table": robot_object_table_invalid._is_on_table}
    expected = {"position": (-1, -1), "facing": None, "is_on_table": False}

    assert result == expected


def test_one_move_from_robot_placed_on_origin(placed_robot_object_origin):
    placed_robot_object_origin._move()

    result = {"position": placed_robot_object_origin._position, "facing": placed_robot_object_origin._facing,
              "is_on_table": placed_robot_object_origin._is_on_table}
    expected = {"position": (
        0, 1), "facing": Facing.NORTH, "is_on_table": True}

    assert result == expected


def test_two_moves_from_robot_placed_on_origin(placed_robot_object_origin):
    placed_robot_object_origin._move()
    placed_robot_object_origin._move()

    result = {"position": placed_robot_object_origin._position, "facing": placed_robot_object_origin._facing,
              "is_on_table": placed_robot_object_origin._is_on_table}
    expected = {"position": (
        0, 2), "facing": Facing.NORTH, "is_on_table": True}

    assert result == expected
