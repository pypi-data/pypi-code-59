#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from exclock.util import is_time_str

IS_TIME_STR_PARAMS = [
    ("1", True), ("abc", False), ("17m", True), ("12s", True), ("17m12s", True),
    ("17m12sklm", False)
]


@pytest.mark.parametrize("s, expect", IS_TIME_STR_PARAMS)
def test_is_time_str(s: str, expect: bool):
    assert is_time_str(s) is expect
