import click
from .runner import Runner


@click.command()
@click.option('--input-file', required=True,  help="Path to file with commands for robot (e.g. 'input_files/input_file_1.txt')")
def run_robot(input_file: str):
    """
    Main entry function. Pass input_file to Runner to execute

    Args:
        input_file (str): Path to file with commands
    """
    runner = Runner()
    runner.run(input_file)

# pylint: disable=no-value-for-parameter
if __name__ == "__main__":
    run_robot()
