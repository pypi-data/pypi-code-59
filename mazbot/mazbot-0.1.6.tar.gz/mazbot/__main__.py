from .file_reader import FileReader
from .robot import Robot
from .facing import Facing
import re
import click


@click.command()
@click.option('--input-file', required=True,  help="Path to file with instructions for robot (e.g. 'input_files/input_file_1.txt')")
def run_robot(input_file):
    file_reader = FileReader(input_file)
    instruction_lines = file_reader.get_all_instruction_lines()

    robot = Robot()
    for instruction_line in instruction_lines:
        instruction_elements = re.split('[\s,]', instruction_line)
        command = instruction_elements[0]

        if command == "PLACE":
            position = (int(instruction_elements[1]), int(
                instruction_elements[2]))
            facing_str = instruction_elements[3]
            robot.process_command(command, coords=position,
                                  facing=Facing[facing_str])
        else:
            robot.process_command(command)


# pylint: disable=no-value-for-parameter
if __name__ == "__main__":
    run_robot()
