import json
from .base_configuration import configuration


@configuration('json_file_path')
def from_json(json_file_path: str):
    with open(json_file_path, 'r') as fh:
        return json.load(fh)