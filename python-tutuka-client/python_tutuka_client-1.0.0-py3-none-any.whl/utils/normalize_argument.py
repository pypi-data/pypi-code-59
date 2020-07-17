from datetime import datetime

from tutuka_client.utils import iso8601_without_underscore


def normalize_argument(argument):
    if isinstance(argument, str):
        return argument
    if isinstance(argument, datetime):
        return iso8601_without_underscore(argument)
    if isinstance(argument, int):
        return str(argument)
    raise TypeError('cant normalize argument')
