#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import sys
from optparse import OptionParser

from exclock import __VERSION__
from exclock.mains.play_clock_main import main as play_clock_main
from exclock.mains.show_list_main import main as show_list_main
from exclock.mains.specified_time_main import main as specified_time_main

# check whether there exists vlc command or not
try:
    import vlc  # noqa: F401
except OSError:
    print("vlc not found.", file=sys.stderr)
    sys.exit(1)


def execulatable_xmessage() -> None:
    if not shutil.which("xmessage"):
        print("xmessage not found.", file=sys.stderr)
        sys.exit(1)


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


def main() -> None:
    execulatable_xmessage()

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
