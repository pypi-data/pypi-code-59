"""Module dedicated to GUI objects used whichever the GUI library used."""

from enum import IntEnum
from typing import NamedTuple


class GuiLib(IntEnum):
    """Enumeration of GUI libraries that could be used."""

    no = 0
    pyglet = 1
    qt = 2


class Key(IntEnum):
    """Enumeration keyboard keys to listen."""

    up = 0
    right = 1
    down = 2
    left = 3
    escape = 4


class Geometry(NamedTuple):
    """Defines a width and a height. May be used for window or screen size."""
    width: int = -1
    height: int = -1
