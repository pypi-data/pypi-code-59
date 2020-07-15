from functools import wraps

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