from typing import List


class FileReader:
    """
    Reads file with instructions
    """

    def __init__(self, file_path: str):
        """
        Constructor of FileReader class

        Args:
            file_path (str): Path to file with instructions for robot
        """
        self._file_path = file_path

    def get_all_command_lines(self) -> List:
        """
        Return a list of strings, one string per line in input file

        Returns:
            List: list of strings, one string per line in input file
        """
        try:
            with open(self._file_path) as f:
                instruction_lines = [line.strip() for line in f]
        except IOError:
            raise

        return instruction_lines
