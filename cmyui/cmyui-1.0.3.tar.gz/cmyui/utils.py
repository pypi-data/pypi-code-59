# -*- coding: utf-8 -*-

from time import time
from collections.abc import Callable
from typing import Any

__all__ = (
    'for_all_methods',
    'log_performance'
)

def log_performance(min_time: float = 0.0) -> Callable:
    def decorate(func: Callable, *args, **kwargs) -> Callable:
        st, res = time(), func(*args, **kwargs)
        if (taken := 1000 * (time() - st)) >= min_time:
            print(f'{func.__name__}: {taken:,.2f}ms')
        return res
    return decorate

# Wrap a function around each
# callable within a class.
def for_all_methods(func: Callable, *args, **kwargs):
    def decorate(cls):
        for k in cls.__dict__:
            attr = getattr(cls, k)
            if isinstance(attr, Callable):
                setattr(cls, k, func(attr, *args, **kwargs))
        return cls
    return decorate

@for_all_methods(log_performance())
class Server:
    def __init__(self):
        pass

#Server = for_all_methods(log_performance(0.0))(Server)
#s = Server()
