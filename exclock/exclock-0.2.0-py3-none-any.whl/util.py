#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import basename as _path_basename
from pathlib import Path
from shlex import quote
from time import sleep as time_sleep
from typing import List, Tuple

from tqdm import tqdm

ASSET_DIR_IN_PROG = Path(__file__).parent.absolute().joinpath("assets")
CLOCK_DIR_IN_PROG = ASSET_DIR_IN_PROG / "clock"
SOUND_DIR_IN_PROG = ASSET_DIR_IN_PROG / "sound"
ASSET_DIR_IN_SYS = Path(Path.home(), ".exclock")
CLOCK_DIR_IN_SYS = Path(os.getenv('EXCLOCK_CLOCK_DIR', str(ASSET_DIR_IN_SYS / "clock"))).absolute()
SOUND_DIR_IN_SYS = Path(os.getenv('EXCLOCK_SOUND_DIR', str(ASSET_DIR_IN_SYS / "sound"))).absolute()


def get_clock_basenames() -> List[str]:
    clock_paths = set(CLOCK_DIR_IN_SYS.glob("**/*"))
    clock_paths |= set(CLOCK_DIR_IN_PROG.glob("**/*"))

    basenames = set()
    for clock_file in clock_paths:
        clock_filename = clock_file.name
        if clock_filename.endswith(".json5"):
            clock_filename = clock_filename[:-len(".json5")]
        basenames.add(_path_basename(clock_filename))

    return sorted(list(basenames))


def is_time_delta_str(s: str) -> bool:
    if s == "":
        return False

    if s.isdigit():
        return True

    mind = s.find("m")
    if mind != -1:
        s = s[mind + 1:]

    sind = s.find("s")
    if sind != -1:
        s = s[sind + 1:]

    return s == ""


def get_time_delta_from_str(s: str) -> int:
    if s.isdigit():
        return int(s)
    else:
        sec = 0
        m_ind = s.find("m")
        if m_ind != -1:
            sec += 60 * int(s[:m_ind])

        s_ind = s.find("s")
        if s_ind == -1:
            return sec
        sec += int(s[m_ind + 1:s_ind])
        return sec


def is_specific_time_str(s: str) -> bool:
    number_strs = s.split(":")
    number_strs = [s.replace(" ", "") for s in number_strs]

    if len(number_strs) not in (2, 3):
        return False

    for s in number_strs:
        if not s.isdigit():
            return False

    numbers = list(map(int, number_strs))
    hour, min_, *secs = numbers
    sec = 0 if secs == [] else int(secs[0])

    return 0 <= sec < 60 and 0 <= min_ < 60


def get_specific_time_from_str(s: str) -> Tuple[int, int, int]:
    number_strs = s.split(":")
    number_strs = [s.replace(" ", "") for s in number_strs]

    numbers = list(map(int, number_strs))
    hour, min_, *secs = numbers
    sec = 0 if secs == [] else int(secs[0])

    return (hour, min_, sec)


def convert_specific_time_to_time_delta(
        time_: Tuple[int, int, int], now_: Tuple[int, int, int]) -> int:
    sec = (time_[0] - now_[0]) * 60 * 60 + (time_[1] - now_[1]) * 60 + (time_[2] - now_[2])
    if sec < 0:
        sec += 24 * 60 * 60

    return sec


def get_real_json_filename(path: str) -> str:
    path = str(Path(path).expanduser())

    if not Path(path).exists() and not (CLOCK_DIR_IN_SYS /
                                        path).exists() and Path(path).suffix == '':
        path += ".json5"

    if Path(path).exists():
        return path

    if CLOCK_DIR_IN_SYS.exists():
        filename = CLOCK_DIR_IN_SYS / path
        if filename.exists():
            return str(filename)

    while path.startswith("_"):
        path = path[1:]
    path = str(CLOCK_DIR_IN_PROG / path)

    return path


def get_real_sound_filename(path_: str) -> str:
    path = Path(path_).expanduser()

    if path.exists():
        return str(path)

    if SOUND_DIR_IN_SYS.exists():
        filename = SOUND_DIR_IN_SYS / path
        if filename.exists():
            return str(filename)

    path_name = str(path)
    while path_name.startswith("_"):
        path_name = path_name[1:]

    return str(SOUND_DIR_IN_PROG / path_name)


def notify(title: str, message: str) -> None:
    message = quote(title + "\n" + message)
    os.system(f'(xmessage -nearmouse -timeout 20 -buttons Close {message}) &')


def notify_all(
    title: str,
    message: str,
    spend_time: int,
    is_first: bool,
) -> None:
    tqdm_f = (lambda i: i) if spend_time == 0 else lambda i: tqdm(
        i, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} ")
    for _ in tqdm_f(range(spend_time)):
        time_sleep(1)

    if not is_first:
        notify(title=title, message=message)

    print(message)
