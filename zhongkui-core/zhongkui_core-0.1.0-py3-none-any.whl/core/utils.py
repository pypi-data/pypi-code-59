import math
from functools import wraps
from collections import Counter

_INSTANCE = {}


def singleton(cls):
    ''''singleton by inner'''
    @wraps(cls)
    def inner(*args, **kwargs):
        if cls not in _INSTANCE:
            _INSTANCE[cls] = cls(*args, **kwargs)
        return _INSTANCE[cls]

    return inner


class Singleton(type):
    '''Singleton by metaclass'''
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton,
                                       cls).__call__(*args, **kwargs)
        return cls._instance[cls]


def calculateEntropy(data):
    """calcuate the entropy of a chunk of data"""
    cnt = Counter(bytearray(data))
    entropy = 0.0
    for i in cnt.values():
        p_i = float(i) / len(data)
        entropy -= p_i * math.log(p_i, 2)

    return entropy