from contextlib import contextmanager
from os import environ
from typing import Callable, Generator, Optional, Union


EnvValue = Optional[str]


def _set_env(
    key: str, value: Union[EnvValue, Callable[[EnvValue], EnvValue]]
) -> EnvValue:
    last: EnvValue
    try:
        last = environ[key]
    except KeyError:
        last = None

    if callable(value):
        value = value(last)

    if value is not None:
        environ[key] = value
    elif last is not None:
        del environ[key]
    return last


@contextmanager
def push_env(
    key: str, value: Union[EnvValue, Callable[[EnvValue], EnvValue]]
) -> Generator[EnvValue, None, None]:
    saved = _set_env(key, value)

    try:
        yield saved
    finally:
        _set_env(key, saved)
