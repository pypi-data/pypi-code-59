"""Module dedicated to input handling."""

from enum import Enum

from amethyst.face import FacePosition


class Input(Enum):
    """
    Enumeration of inputs, among a numeric identifier, obtained from key one key or a combinations of two keys.
    The key order for each input correspond to a serialised set(): `'-'.join([k.name for k in {Key.up}])`.
    """

    up = FacePosition.N
    up_right = FacePosition.NE
    right = FacePosition.E
    right_down = FacePosition.SE
    down = FacePosition.S
    down_left = FacePosition.SW
    left = FacePosition.W
    up_left = FacePosition.NW
