import logging
import logging.config
from mazbot.conf.logging_conf import logging_config
from typing import Dict
from mazbot.facing import Facing

logger = logging.getLogger(__name__)
logging.config.dictConfig(logging_config)


class Robot:
    """
    This class will maintain the state of the Robot, and will be able to respond to commands sent to it
    """

    def __init__(self):
        """
        Robot class constructor
        """
        self._position = (-1, -1)  # TODO abstract away to Coord class
        self._facing = None
        self._is_on_table = False

    def _report(self):
        """
        Print the position of the robot along with the direction it is facing. 
        Will be called by self.process_command
        """
        print(f"{self._position[0]},{self._position[1]},{self._facing.name}")

    def _place(self, position, facing):
        if not self._is_fall(position):
            self._position = position
            self._facing = facing
            self._is_on_table = True

    def _move(self):
        (x, y) = self._position
        move_output = {Facing.NORTH: (x, y+1), Facing.EAST: (x+1, y), 
                       Facing.SOUTH: (x, y-1), Facing.WEST: (x-1, y)}
        next_position = move_output[self._facing]

        if not self._is_fall(next_position):
            self._position = next_position

    def _rotate(self, rotate_direction: str):  # TODO can do better than str?
        """        
        Rotate the robot in the given direction. Will be called by self.process_command

        Args:
            rotate_direction (str): [description]
        """
        # TODO assert facing is not None,
        left_rotate_output = {Facing.NORTH: Facing.WEST, Facing.WEST: Facing.SOUTH,
                              Facing.SOUTH: Facing.EAST, Facing.EAST: Facing.NORTH}
        right_rotate_output = {Facing.WEST: Facing.NORTH, Facing.SOUTH: Facing.WEST,
                               Facing.EAST: Facing.SOUTH, Facing.NORTH: Facing.EAST}

        if rotate_direction == "LEFT":
            self._facing = left_rotate_output[self._facing]
        else:
            self._facing = right_rotate_output[self._facing]

    # TODO take out of robot class
    def _is_fall(self, coords):
        table_length = 5
        table_width = 5

        (x, y) = coords
        return (x < 0 or x > table_width - 1) or (y < 0 or y > table_length - 1)

    # TODO can do better than str?
    def process_command(self, command: str, **command_params):
        if self._is_on_table == False and command != "PLACE":  # Ignore commands if not on table
            logger.info(
                f"{command} ignored since robot is not yet on the table")
            return None

        # TODO improve to possibly switch, remove magic strings
        if command == "PLACE":
            # TODO validate kwargs
            self._place(command_params['coords'], command_params['facing'])
        elif command == "MOVE":
            self._move()
        elif command == "LEFT":
            self._rotate("LEFT")
        elif command == "RIGHT":
            self._rotate("RIGHT")
        elif command == "REPORT":
            self._report()
        else:
            raise ValueError(f"Invalid command {command} sent to robot")

        # return new state of robot after each command
        return {"position": self._position, "facing": self._facing}
