import os
from .utils import safe_json_load
from .base_configuration import configuration


@configuration
def from_env():
    return {k: safe_json_load(v) for k, v in os.environ.items()}
