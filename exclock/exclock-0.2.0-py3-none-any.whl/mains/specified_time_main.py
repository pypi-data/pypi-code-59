#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from os import getenv
from pathlib import Path
from sys import exit, stderr
from time import sleep as time_sleep
from typing import Optional

import vlc

from exclock.util import (
    convert_specific_time_to_time_delta,
    get_real_sound_filename,
    get_specific_time_from_str,
    get_time_delta_from_str,
    is_specific_time_str,
    is_time_delta_str,
    notify_all,
)


def get_time(time_: str) -> Optional[int]:
    if is_specific_time_str(time_):
        now_ = datetime.now()
        time_info = get_specific_time_from_str(time_)
        return convert_specific_time_to_time_delta(
            time_info, (now_.hour, now_.minute, now_.second))
    elif is_time_delta_str(time_):
        return get_time_delta_from_str(time_)

    return None


def get_ring_filename(ring_sound_filename: Optional[str]) -> str:

    def _get_ring_filename() -> str:
        ring_filename_in_sys = getenv('EXCLOCK_RING_FILENAME')
        if ring_sound_filename is None and ring_filename_in_sys is None:
            return "__warning.mp3"
        elif ring_sound_filename is None:
            return str(ring_filename_in_sys)
        else:
            return str(ring_sound_filename)

    return get_real_sound_filename(_get_ring_filename())


def main(opt, args) -> None:
    time_sec = get_time(opt.specified_time)
    if time_sec is None:
        print("time format is illegal.", file=stderr)
        exit(1)

    try:
        ring_sound_filename = get_ring_filename(opt.ring_filename)
        if not Path(ring_sound_filename).exists():
            print("Ring filename is not found.", file=stderr)
            exit(1)

        message = f"Specified time is passed(sec={time_sec})."
        notify_all(title="Exclock", message=message, spend_time=time_sec, is_first=False)

        p = vlc.MediaPlayer(ring_sound_filename)
        p.play()
        while p.get_state() != vlc.State.Ended:
            time_sleep(0.2)
    except KeyboardInterrupt:
        ...
    finally:
        print('bye')
