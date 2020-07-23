"""Module dedicated to faces."""

from enum import Enum
from typing import NamedTuple


class FacePosition(Enum):
    """An enumeration of all cardinal points used to define gems position."""

    N = 'north'
    NE = 'north_east'
    E = 'east'
    SE = 'south_east'
    S = 'south'
    SW = 'south_west'
    W = 'west'
    NW = 'north_west'


class Face(NamedTuple):
    """A data class that represents a gem face."""

    position: FacePosition
    label: str = ''
