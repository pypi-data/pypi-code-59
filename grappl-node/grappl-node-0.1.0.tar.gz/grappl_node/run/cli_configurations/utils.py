import json
from typing import Union

def safe_json_load(data: str) -> Union[str, dict, list, int, float]:
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return data
