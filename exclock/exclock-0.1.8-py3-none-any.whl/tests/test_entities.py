#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from exclock.entities import ClockTimer, Sound, confirm_dummy, get_time_delta_from_str, inner_str

GET_TIME_FROM_STR_PARAMS = [
    ("0", 0), ("12s", 12), ("2m12s", 2 * 60 + 12), ("25m", 25 * 60), ("30s", 30)
]


@pytest.mark.parametrize("s, expect", GET_TIME_FROM_STR_PARAMS)
def test_get_time_delta_from_str(s: str, expect: int):
    assert get_time_delta_from_str(s) == expect


def test_inner_str():
    d = {"count": 3}
    s = "abc{count*5}def{count*7}ghi"
    assert inner_str(s, d) == "abc15def21ghi"


def test_Sound_init():
    sound = Sound(message="DummyLabel", sound_filename="abc.mp3", confirm_f=confirm_dummy)
    assert sound.message == "DummyLabel"
    assert sound.sound_filename.endswith("abc.mp3")


def test_Sound_from_dict():
    arg = {"message": "dummy_label", "sound_filename": "dummy_sound.mp3", "confirm": ""}
    expected = Sound(
        message="dummy_label", sound_filename="dummy_sound.mp3", confirm_f=confirm_dummy)
    sound = Sound.from_dict(arg)

    assert expected.message == sound.message
    assert expected.sound_filename == sound.sound_filename


def test_ClockTimer_from_dict():
    arg = {
        "sounds": {},
        "loop": 1,
        "title": "abc",
    }
    clock_timer = ClockTimer.from_dict(arg)

    assert clock_timer.sounds == {}
    assert clock_timer.loop == 1


def test_ClockTimer_from_dict2():
    arg = {
        "sounds":
            {
                "10":
                    {
                        "message": "dummy_label",
                        "sound_filename": "dummy_sound.mp3",
                        "confirm": ""
                    },
                "20":
                    {
                        "message": "dummy_label2",
                        "sound_filename": "dummy_sound2.mp3",
                        "confirm": ""
                    }
            },
        "loop": 2,
        "title": "abc",
    }
    clock_timer = ClockTimer.from_dict(arg)

    assert clock_timer.sounds == {
        10:
            Sound(
                message="dummy_label", sound_filename="dummy_sound.mp3", confirm_f=confirm_dummy),
        20:
            Sound(
                message="dummy_label2", sound_filename="dummy_sound2.mp3",
                confirm_f=confirm_dummy),
    }
    assert clock_timer.loop == 2
