"""Module dedicated to faces."""

from enum import Enum


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


class Face:
    """A data class that represents a gem face."""

    def __init__(self, position: FacePosition, label: str):
        self.position: FacePosition = position
        self.label: str = label

    def __str__(self):
        return '%s: %s' % (self.position.name, self.label)
