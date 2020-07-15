import os

def compute():
    return 42


def path_to_data_file(file_name):
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "data", file_name)
