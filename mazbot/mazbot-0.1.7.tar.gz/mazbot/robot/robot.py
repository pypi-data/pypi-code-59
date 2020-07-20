import logging
import logging.config
from typing import Dict, Tuple
from enum import Enum
from mazbot.conf.logging_conf import logging_config
from mazbot.enums.facing import Facing
from mazbot.enums.command import Command
from mazbot.robot.table import Table

logger = logging.getLogger(__name__)
logging.config.dictConfig(logging_config)


class RotateDirection(Enum):
    """
    Enum to describe direction robot should rotate. Separate enum specific
    to Robot class to decouple interface for processing commands 
    from the functions executing commands

    Args:
        Enum ([type]): Enum to describe direction robot should rotate
    """
    LEFT = 1
    RIGHT = 2


class Robot:
    """
    This class will maintain the state of the robot, and will be able to respond to commands sent to it
    """

    def __init__(self, table: Table):
        """
        Constructor of Robot class. Table object needs to be passed in since robot
        needs to ask table whether a given position is on the table

        Args:
            table (Table): Table object passed in since robot needs to ask table whether
            a given position is on the table
        """
        self._position = (-1, -1)
        self._facing = None
        self._is_on_table = False
        self._table = table

    def _report(self):
        """
        Print the position of the robot along with the direction it is facing. 
        Will be called by self.process_command.
        """
        print(f"{self._position[0]},{self._position[1]},{self._facing.name}")

    def _place(self, position: Tuple[int, int], facing: Facing):
        """
        Place the robot on the table, if the coordinates provided through the position
        argument are within the table.

        Args:
            position (Tuple[int, int]): Coordinates on where to place robot
            facing (Facing): Which direction (orientation) to place the robot in
        """
        if self._table.is_position_valid(position):
            self._position = position
            self._facing = facing
            self._is_on_table = True

    def _move(self):
        """
        Move the robot (in the direction that it is currentl facing). Will not
        update the position (i.e. state of this class) if the move will result in
        the robot moving out of the table.
        """
        (x, y) = self._position
        move_output = {Facing.NORTH: (x, y+1), Facing.EAST: (x+1, y),
                       Facing.SOUTH: (x, y-1), Facing.WEST: (x-1, y)}
        next_position = move_output[self._facing]

        if self._table.is_position_valid(next_position):
            self._position = next_position

    def _rotate(self, rotate_direction: RotateDirection):
        """
        Rotate the robot in the given direction. 

        Args:
            rotate_direction (RotateDirection): which direction (Left or Right)
            to rotate the robot in
        """
        left_rotate_output = {Facing.NORTH: Facing.WEST, Facing.WEST: Facing.SOUTH,
                              Facing.SOUTH: Facing.EAST, Facing.EAST: Facing.NORTH}
        right_rotate_output = {Facing.WEST: Facing.NORTH, Facing.SOUTH: Facing.WEST,
                               Facing.EAST: Facing.SOUTH, Facing.NORTH: Facing.EAST}

        if rotate_direction is RotateDirection.LEFT:
            self._facing = left_rotate_output[self._facing]
        else:
            self._facing = right_rotate_output[self._facing]

    def process_command(self, command: Command, **command_params) -> Dict:
        """
        Interface to outside world for robot, only executes commands if the robot
        is on the table

        Args:
            command (Command): Which command to execute on the robot

        Kwargs:
            coords (Tuple[int, int]): coordinates for a PLACE command
            facing (Facing): direction (orientation) to PLACE the robot

        Raises:
            ValueError: Raised if the command passed is invalid

        Returns:
            Dict: Returns state of robot after processing command
        """
        try:
            self._validate_command(command, **command_params)

            # Ignore commands if not on table
            if self._is_on_table == False and command is not Command.PLACE:
                logger.info(
                    f"{command} ignored since robot is not yet on the table")
                return None

            if command is Command.PLACE:
                self._place(command_params['coords'], command_params['facing'])
            elif command is Command.MOVE:
                self._move()
            elif command is Command.LEFT:
                self._rotate(RotateDirection.LEFT)
            elif command is Command.RIGHT:
                self._rotate(RotateDirection.RIGHT)
            elif command is Command.REPORT:
                self._report()

            if self._is_on_table:
                logger.info(
                    f"After command {command.name}, position is {self._position} and facing {self._facing.name}")
            else:
                logger.info(
                    f"After command {command.name}, table is not on the table")

            return {"position": self._position, "facing": self._facing}
        except:
            raise

    def _validate_command(self, command: Command, **command_params) -> bool:
        """
        Validates whether command is valid (e.g. checks for types and whether facing values
        passed in are valid)

        Args:
            command (Command): Which command to execute on the robot

        Kwargs:
            coords (Tuple[int, int]): coordinates for a PLACE command
            facing (Facing): direction (orientation) to PLACE the robot

        Returns:
            bool: returns True if valid command

        Raises:
            ValueError
        """
        if command is Command.PLACE:
            if isinstance(command_params['coords'], tuple) and command_params['facing'] in Facing:
                return True
        elif command in Command:
            return True
        else:
            raise ValueError(
                f"Invalid command parameters {command_params} sent to process_command")
