# Copyright (c) 2019 Jonathan Sambrook and Codethink Ltd.
#
#    This file is part of Topplot.
#
#    Topplot is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Topplot is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Topplot.  If not, see <https://www.gnu.org/licenses/>.
#
# ------------------------------------------------------------------------------

import re
import sys
import tkinter as tk

# ------------------------------------------------------------------------------
# Exit with error, displaying msg to stderr


def die(msg):
    print(f"ERR: {msg}", file=sys.stderr)
    sys.exit(1)


# ------------------------------------------------------------------------------
# Convert DD:HH:MM:SS to seconds (re based to flexibly handle optional day/hour/minutes)
# Dies on failure to parse!


def dhms_to_sec(text):
    m = re.match(
        "^((?P<d>\d+):){0,1}?((?P<h>\d+):){0,1}?((?P<m>\d+):){0,1}?(?P<s>\d\d)$", text
    )
    if m:
        groups = m.groupdict()
        d = int(groups["d"]) if groups["d"] else 0
        h = int(groups["h"]) if groups["h"] else 0
        m = int(groups["m"]) if groups["m"] else 0
        s = int(groups["s"])
        # print(f"{text} → d: {d}  h: {h}  m: {m}  s: {s}")
        return d * 24 * 3600 + h * 3600 + m * 60 + s
    else:
        die(f"'{text}' doesn't parse as a timestamp with format [[[D:]HH:]MM:]SS")


# ------------------------------------------------------------------------------


def get_curr_screen_geometry():
    """
    Workaround to get the size of the current screen in a multi-screen setup.

    Returns:
        geometry (str): The standard Tk geometry string.
            [width]x[height]+[left]+[top]
    """
    root = tk.Tk()
    root.update_idletasks()
    root.attributes("-fullscreen", True)
    root.state("iconic")
    geometry = root.winfo_geometry()
    root.quit()
    root.destroy()
    return geometry


# ------------------------------------------------------------------------------


def get_curr_screen_dimensions(scale=1.0):
    geometry = get_curr_screen_geometry()
    m = re.match(r"^(?P<width>\d+)x(?P<height>\d+)\+(?P<position>\d+\+\d+)", geometry)
    groups = m.groupdict()
    return f'{int(int(groups["width"])*scale)}x{int(int(groups["height"])*scale)}'


# ------------------------------------------------------------------------------
# vi: sw=4:ts=4:et
