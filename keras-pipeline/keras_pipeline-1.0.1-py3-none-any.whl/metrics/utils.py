from typing import *

def get_function_name(function: Callable) -> str:
  try:
    return function.__name__
  except AttributeError:
    return function.name