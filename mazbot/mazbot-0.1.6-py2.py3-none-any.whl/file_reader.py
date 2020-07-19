class FileReader:
    """
    Reads file with instructions
    """

    def __init__(self, file_path: str):
        self._file_path = file_path

    def get_all_instruction_lines(self):
        with open(self._file_path) as f:
            instruction_lines = [line.strip() for line in f]

        return instruction_lines
