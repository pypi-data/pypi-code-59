import os
from .utils import safe_json_load
from .base_configuration import configuration

OPTIONS = [
    'node_module_name',
    'node_name',
    'input_module_name',
    'input_name',
    'output_module_name',
    'output_name',
    'node_arguments',
    'input_arguments',
    'output_arguments',
]

@configuration(OPTIONS)
def from_cli(**kwargs):
    return {k: safe_json_load(v) for k, v in kwargs.items()}
