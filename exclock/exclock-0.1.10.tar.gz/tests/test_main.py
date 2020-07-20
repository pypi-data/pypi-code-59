#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import StringIO

import freezegun
import pytest

from exclock.main import (
    check_raw_clock,
    get_real_sound_filename,
    get_ring_filename,
    get_time,
    get_title_from_json_filename,
    show_list_main,
)

GET_TITLE_FROM_JSON_FILENAME_PARAMS = [
    ("abc.json5", "Abc"), ("abc", "Abc"), ("~/repo/abc.json", "Abc")
]


@pytest.mark.parametrize("json_filename, expect", GET_TITLE_FROM_JSON_FILENAME_PARAMS)
def test_get_title_from_json_filename(json_filename: str, expect: str):
    assert get_title_from_json_filename(json_filename) == expect


CHECK_RAW_CLOCK_EXCEPTION_PARAMS = [
    (
        {
            "sounds": {
                "0": {
                    "message": "dummy",
                    "sound_filename": "/tmp/dummy_tmp",
                }
            },
            "loop": 1
        },
        FileNotFoundError,
        "is not found",
    ),
    ("abcdef", ValueError, "doesn't mean dict"),
    ({
        "message": "dummy",
        "loop": 1
    }, ValueError, "doesn't include sounds property"),
    ({
        "sounds": 0,
        "loop": 1
    }, ValueError, "sounds is not dict object"),
    (
        {
            "sounds": {
                "abc": {
                    "message": "dummy",
                    "sound_filename": "silent.mp3"
                }
            },
            "loop": 1
        }, ValueError, "is not time"),
    ({
        "sounds": {
            "0": []
        },
        "loop": 1
    }, ValueError, "is not dict object"),
    (
        {
            "sounds": {
                "0": {
                    "sound_filename": "silent.mp3"
                },
            },
            "loop": 1
        }, ValueError, "message is not defined"),
    (
        {
            "sounds": {
                "0": {
                    "sound_filename": "silent.mp3"
                },
            },
            "loop": 1
        }, ValueError, "message is not defined"),
    (
        {
            "sounds": {
                "0": {
                    "message": 3,
                    "sound_filename": "silent.mp3"
                },
            },
            "loop": 1
        }, ValueError, "message is not str object"),
    (
        {
            "sounds": {
                "0": {
                    "message": "test message",
                },
            },
            "loop": 1
        }, ValueError, "sound_filename is not defined"),
    (
        {
            "sounds": {
                "0": {
                    "sound_filename": 3,
                    "message": "test message",
                },
            },
            "loop": 1
        }, ValueError, "sound_filename is not str object"),
    (
        {
            "sounds": {
                "0": {
                    "sound_filename": "warning.mp3",
                    "message": "test message",
                },
            },
            "loop": "1",
        }, ValueError, "loop is not int object"),
    (
        {
            "sounds": {
                "0": {
                    "sound_filename": "warning.mp3",
                    "message": "test message",
                },
            },
            "loop": None,
        }, None, ""),
]


@pytest.mark.parametrize("d, err_cls, match", CHECK_RAW_CLOCK_EXCEPTION_PARAMS)
def test_check_raw_clock_exception(d, err_cls: type, match: str):
    if err_cls:
        with pytest.raises(err_cls, match=match):
            check_raw_clock(d)
    else:
        check_raw_clock(d)


def test_show_list_main():
    stdout = StringIO()
    show_list_main(stdout=stdout)
    outputs = set(stdout.getvalue().split('\n'))
    assert 'pomodoro' in outputs
    assert 'clock_in_sys.json' in outputs


GET_TIME_PARAMS = [
    ("12", 12),
    ("12s", 12),
    ("1m2s", 1 * 60 + 2),
    ("2m", 60 * 2),
    ("abc", None),
    ("00:01", 60),
    ("23:59", 23 * 60 * 60 + 59 * 60),
]


@freezegun.freeze_time('2020-01-01')
@pytest.mark.parametrize("s, expect", GET_TIME_PARAMS)
def test_get_time(s, expect):
    assert get_time(s) == expect


GET_RING_FILENAME_PARAMS = [
    (None, "__warning.mp3"),
    ("__silent.mp3", "__silent.mp3"),
]


@pytest.mark.parametrize("ring_filename, sound_filename", GET_RING_FILENAME_PARAMS)
def test_get_ring_filename(ring_filename, sound_filename):
    assert get_ring_filename(ring_filename) == get_real_sound_filename(sound_filename)
