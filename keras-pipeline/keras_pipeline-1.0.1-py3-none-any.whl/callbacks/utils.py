from typing import *

def logs_safe_update(logs: Dict[str, Any], dictionary: Dict[str, Any]) -> None:
  for key in dictionary.keys():
    if key in logs:
      raise ValueError(f'Key {key} already found in logs')
  
  logs.update(dictionary)