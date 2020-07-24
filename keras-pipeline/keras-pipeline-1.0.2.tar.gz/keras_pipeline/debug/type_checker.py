from typing import *

import inspect
import functools    

# TODO: custom class

def positive(name, value: int):
  if value < 0:
    raise ValueError(name + ' must be positive')

def check_params(f):
  @functools.wraps(f)
  def wrapper(*args, **kwargs):
    if True: # TODO: if flag:
      signature = inspect.signature(f)
      binding = signature.bind(*args, **kwargs)
      for name, value in binding.arguments.items():
        annotation = signature.parameters[name].annotation
        if annotation is inspect.Signature.empty:
          continue
        print(annotation, name, value)
        if isinstance(annotation, type):
          print('type')
          # TODO: if isinstance(annotation, custom_class): ...
          if isinstance(annotation, GenericMeta):
            print('Typing type')
          elif not isinstance(value, annotation):
            raise TypeError('...')
        elif inspect.isfunction(annotation):
          print('func')
          annotation(name, value)
        else:
          print('Went wrong')
          print(type(annotation))
    return f(*args, **kwargs)
  return wrapper


class c:
  pass
  
@check_params
def procedural_noise(width: int, height: c, seed: positive):
  pass