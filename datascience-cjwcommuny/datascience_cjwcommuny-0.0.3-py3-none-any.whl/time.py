from datetime import date
import datetime

def today() -> str:
    """
    :return date like "2019.09.27"
    """
    return date.today().strftime("%Y.%m.%d")


def now() -> str:
    """
    :return time like 15:38:36
    """
    return datetime.datetime.now().strftime('%H:%M:%S')

