import logging
import logging.config
from typing import List, Dict
import re
from mazbot.utils.file_reader import FileReader
from mazbot.robot.robot import Robot, Table
from mazbot.conf.logging_conf import logging_config
from mazbot.enums.facing import Facing
from mazbot.enums.command import Command

logger = logging.getLogger(__name__)
logging.config.dictConfig(logging_config)

class Runner:
    """
    Runs robot end to end (reads from file, executes commands and writes out to stdout) 
    """

    def __init__(self):
        pass

    def run(self, input_file: str)->Dict:
        """
        Main entry point of Runner

        Args:
            input_file (str): input file which contains instructions for robot

        Returns:
            Dict: state of robot after running all commands (position and facing)
        """
        try:
            file_reader = FileReader(input_file)
            command_lines = file_reader.get_all_command_lines()
            self._validate_command_lines(command_lines)
            returned_state = self._process_command_lines(command_lines)

            return returned_state
        except Exception as e:
            print(e)
            logging.exception('')

    
    def _validate_command_lines(self, command_lines: List[str]):
        """
        Check if each command line consists of either PLACE, MOVE, LEFT, RIGHT or REPORT,
        and if it is a PLACE command whether it follows the PLACE 0,0,NORTH type format

        Args:
            command_lines (List[str]): command lines as read from input file
        """
        valid_commands = ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]

        if command_lines == []:
            raise ValueError(f"No commands found")

        for command_line in command_lines:
            is_valid = True

            command_elements = re.split(r'[\s,]', command_line)
            if len(command_elements) == 0:
                is_valid = False

            command_str = command_elements[0]
            if command_str not in valid_commands:
                is_valid = False

            if command_str == "PLACE" and re.match(r"^\s*PLACE \d,\d,(NORTH|EAST|SOUTH|WEST)\s*$", command_line) is None:
                is_valid = False

            if is_valid == False:
                raise ValueError(
                    f"Invalid command line {command_line} found in file")


    def _process_command_lines(self, command_lines: List[str]):
        """
        Process each command line in input file, and send off command to robot
        for execution

        Args:
            command_lines (List[str]): List of strings, where each string is a 
            command to the robot
        """
        table = Table()  
        robot = Robot(table)
        for command_line in command_lines:
            returned_state = self._process_command_line(robot, command_line)

        return returned_state

    def _process_command_line(self, robot: Robot, command_line: str)->Dict:
        """
        Process a single command line and execute on robot

        Args:
            robot (Robot): The robot to execute the command on
            command_line (str): A single command to be executed on the robot
        """
        command_elements = re.split(r'[\s,]', command_line)
        command_str = command_elements[0]

        try:
            command = Command[command_str]
            if command is Command.PLACE:
                position = (int(command_elements[1]), int(command_elements[2]))
                facing_str = command_elements[3]
                returned_state = robot.process_command(
                    command, coords=position, facing=Facing[facing_str])
            else:
                returned_state = robot.process_command(command)

            return returned_state
        except:
            raise