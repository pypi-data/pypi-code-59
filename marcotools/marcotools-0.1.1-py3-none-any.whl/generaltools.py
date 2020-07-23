import json
import datetime
import logging

from functools import wraps
from time import sleep


def with_retry(retries_and_sleep):
    retries, sleep_sec = retries_and_sleep or (3, 1)

    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                result = function(*args, **kwargs)
                if result:
                    return result
                sleep(sleep_sec)
        return wrapper
    return real_decorator


def msg_maker(*argv) -> str:
    msg = ""
    for arg in argv:
        msg += arg + "\n"
    return msg


def msg_maker_dic(dic) -> str:
    msg = ''
    for key, value in dic.items():
        msg = f'{key}: {value}\n' + msg
    return msg


def now_log(log):
    now = datetime.datetime.now()
    now = now.strftime("%y/%m/%d %H:%M:%S - ") + log
    print(now)


def json_to_dict(json_str: str) -> dict:
    try:
        return json.loads(json_str)
    except:
        logging.error("The argument has not json format.")
        return None


def datetime_to_str(datetimeobj) -> str:
    if isinstance(datetimeobj, datetime.datetime):
        return datetimeobj.__str__()
