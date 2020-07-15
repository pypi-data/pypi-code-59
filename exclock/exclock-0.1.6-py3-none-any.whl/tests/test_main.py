#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from exclock.main import check_raw_clock, get_title_from_json_filename

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
                    "sound_filename": 3,
                    "message": "test message",
                },
            },
            "loop": "1",
        }, ValueError, "loop is not int object"),
]


@pytest.mark.parametrize("d, err_cls, match", CHECK_RAW_CLOCK_EXCEPTION_PARAMS)
def test_check_raw_clock_exception(d, err_cls: type, match: str):
    with pytest.raises(err_cls, match=match):
        check_raw_clock(d)
