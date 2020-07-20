#!/usr/bin/env python

"""Tests for `mazbot` package Table class."""

import pytest

from mazbot.robot.table import Table

@pytest.fixture
def table_object():
    return Table()

def test_valid_location_returns_true(table_object):
    assert table_object.is_position_valid((2,3)) == True

def test_invalid_location_returns_false(table_object):
    assert table_object.is_position_valid((7,7)) == False
