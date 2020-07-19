#!/usr/bin/env python

"""Tests for `mazbot` package Robot class."""

import pytest

from mazbot.robot import Robot
from mazbot.facing import Facing


@pytest.fixture
def robot_object():
    return Robot()


@pytest.fixture
def placed_robot_object_origin():
    rbt = Robot()
    rbt._position = (0, 0)
    rbt._facing = Facing.NORTH
    rbt._is_on_table = True
    return rbt


@pytest.fixture
def placed_robot_object_non_origin():
    rbt = Robot()
    rbt._position = (1, 2)
    rbt._facing = Facing.WEST
    rbt._is_on_table = True
    return rbt


def test_process_command_returns_none_if_not_on_table(robot_object):
    assert robot_object.process_command("MOVE") == None


def test_placing_in_origin_facing_north_returns_correct_robot_state(robot_object):
    coord_value = (0, 0)
    facing_value = Facing.NORTH
    returned = robot_object.process_command(
        "PLACE", coords=coord_value, facing=facing_value)
    expected = {"position": coord_value, "facing": facing_value}
    assert returned == expected


def test_placing_in_non_origin_location_returns_correct_robot_state(robot_object):
    coord_value = (1, 2)
    facing_value = Facing.WEST
    returned = robot_object.process_command(
        "PLACE", coords=coord_value, facing=facing_value)
    expected = {"position": coord_value, "facing": facing_value}
    assert returned == expected


def test_placing_outside_table_is_ignored(robot_object):
    pass


def test_one_move_from_origin(placed_robot_object_origin):
    returned = placed_robot_object_origin.process_command("MOVE")
    expected = {"position": (0, 1), "facing": Facing.NORTH}
    assert returned == expected


def test_two_moves_from_origin(placed_robot_object_origin):
    placed_robot_object_origin.process_command("MOVE")
    returned = placed_robot_object_origin.process_command("MOVE")
    expected = {"position": (0, 2), "facing": Facing.NORTH}
    assert returned == expected
