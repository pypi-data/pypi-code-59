#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from exclock.util import get_clock_basenames, is_time_str

GET_CLOCK_BASENAMES_PARAMS = [
    ("pomodoro", True),
    ("3", True),
    ("not_exists", False),
]


@pytest.mark.parametrize("basename, expect", GET_CLOCK_BASENAMES_PARAMS)
def test_get_clock_basenames(basename: str, expect: bool):
    assert (basename in get_clock_basenames()) is expect


IS_TIME_STR_PARAMS = [
    ("1", True), ("abc", False), ("17m", True), ("12s", True), ("17m12s", True),
    ("17m12sklm", False)
]


@pytest.mark.parametrize("s, expect", IS_TIME_STR_PARAMS)
def test_is_time_str(s: str, expect: bool):
    assert is_time_str(s) is expect
