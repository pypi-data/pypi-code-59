#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import sys
from datetime import datetime
from optparse import OptionParser
from os import getenv
from pathlib import Path, PurePath
from sys import stderr
from time import sleep as time_sleep
from typing import Optional

import json5 as json

from exclock import __VERSION__
from exclock.entities import ClockTimer
from exclock.util import (
    convert_specific_time_to_time_delta,
    get_clock_basenames,
    get_real_json_filename,
    get_real_sound_filename,
    get_specific_time_from_str,
    get_time_delta_from_str,
    is_specific_time_str,
    is_time_delta_str,
    notify_all,
)

try:
    import vlc
except OSError:
    print("vlc not found.", file=sys.stderr)
    sys.exit(1)


def get_title_from_json_filename(json_filename: str) -> str:
    basename = PurePath(json_filename).name
    return basename.split('.')[0].capitalize()


def check_raw_clock(d) -> None:
    if type(d) != dict:
        raise ValueError("clock file err: doesn't mean dict.")

    if "sounds" not in d:
        raise ValueError("clock file err: doesn't include sounds property.")

    if type(d["sounds"]) != dict:
        raise ValueError("clock file err: sounds is not dict object.")

    if "loop" not in d:
        raise ValueError("clock file err: doesn't include loop property.")

    if type(d["loop"]) != int and d["loop"] is not None:
        raise ValueError("clock file err: loop is not int object more than or equal to zero.")

    if type(d.get("title", "")) != str:
        raise ValueError("clock file err: title is not str object.")

    for time_s, sound in d["sounds"].items():
        if not is_time_delta_str(time_s):
            raise ValueError(f"clock file err: {time_s} is not time.")
        if type(sound) != dict:
            raise ValueError(f"clock file err: sound at {time_s} is not dict object.")
        if "message" not in sound:
            raise ValueError(f"clock file err: message is not defined at {time_s}.")
        if type(sound["message"]) != str:
            raise ValueError(f"clock file err: message is not str object at {time_s}")
        if "sound_filename" not in sound:
            raise ValueError(f"clock file err: sound_filename is not defined at {time_s}.")
        if type(sound["sound_filename"]) != str:
            raise ValueError(f"clock file err: sound_filename is not str object at {time_s}")

        filename = get_real_sound_filename(sound["sound_filename"])
        if not Path(filename).exists():
            raise FileNotFoundError(f"clock file err: {sound['sound_filename']} is not found.")


def get_option_parser():
    usage = "exclock [options] {clock-filename}"
    parser = OptionParser(usage=usage, version=__VERSION__)
    parser.add_option(
        "-l",
        "--list",
        action="store_true",
        default=False,
        dest="show_list",
        help="show clock names in your PC and exit",
    )
    parser.add_option(
        "-t",
        "--time",
        dest="specified_time",
        action="store",
        help="Time which spends until or to specified",
    )
    parser.add_option(
        "-r",
        "--ring-filename",
        dest="ring_filename",
        action="store",
        help="filename which is used for alarm",
    )
    parser.add_option(
        "--trace",
        "--traceback",
        default=False,
        action="store_true",
        dest="with_traceback",
        help="show traceback",
    )

    return parser


def show_list_main(stdout=sys.stdout) -> None:
    for basename in get_clock_basenames():
        print(basename, file=stdout)


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


def specified_time_main(opt, args) -> None:
    time_sec = get_time(opt.specified_time)
    if time_sec is None:
        print("time format is illegal.", file=sys.stderr)
        sys.exit(1)

    try:
        ring_sound_filename = get_ring_filename(opt.ring_filename)
        if not Path(ring_sound_filename).exists():
            print("Ring filename is not found.", file=sys.stderr)
            sys.exit(1)

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


def play_clock_main(opt, args) -> None:
    if len(args) != 1:
        print("Length of argument should be 1.", file=sys.stderr)
        sys.exit(1)

    json_filename = get_real_json_filename(args[0])
    try:
        with open(json_filename) as f:
            jdata = json.load(f)
    except ValueError as err:
        print(
            f"{json_filename} is Incorrect format for json5:\n" + f"    {err.args[0]}",
            file=stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"{args[0]} is not found.", file=sys.stderr)
        sys.exit(1)

    try:
        check_raw_clock(jdata)
    except Exception as err:
        print(err.args[0], file=stderr)
        sys.exit(1)

    jdata['title'] = jdata.get('title', get_title_from_json_filename(json_filename))
    clock_timer = ClockTimer.from_dict(jdata)
    try:
        clock_timer.run()
    except KeyboardInterrupt:
        ...
    finally:
        print('bye')


def check_requirements() -> None:
    if not shutil.which("xmessage"):
        print("xmessage not found.", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    check_requirements()

    opt, args = get_option_parser().parse_args()

    if opt.show_list:
        show_list_main()
        sys.exit()
    if opt.specified_time is not None:
        specified_time_main(opt, args)
        sys.exit()

    play_clock_main(opt, args)


if __name__ == '__main__':
    main()
