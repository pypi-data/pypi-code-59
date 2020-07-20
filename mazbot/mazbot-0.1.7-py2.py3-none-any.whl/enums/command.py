from enum import Enum


class Command(Enum):
    """
    Enum to represent commands that can be sent to robot

    Args:
        Enum ([type]): Enum to represent commands that can be sent to robot
    """
    PLACE = 1
    MOVE = 2
    LEFT = 3
    RIGHT = 4
    REPORT = 5