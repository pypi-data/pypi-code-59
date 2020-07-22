"""
    Sagemaker Utils
        - this is a fork of sagemaker.utils found here:
        https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/utils.py
"""
import time

def sagemaker_timestamp():
    """Return a timestamp with millisecond precision."""
    moment = time.time()
    moment_ms = repr(moment).split(".")[1][:3]
    return time.strftime("%Y-%m-%d-%H-%M-%S-{}".format(moment_ms), time.gmtime(moment))


def sagemaker_short_timestamp():
    """Return a timestamp that is relatively short in length"""
    return time.strftime("%y%m%d-%H%M")

def name_from_base(base, max_length=63, short=False):
    """Append a timestamp to the provided string.
    This function assures that the total length of the resulting string is
    not longer than the specified max length, trimming the input parameter if
    necessary.
    Args:
        base (str): String used as prefix to generate the unique name.
        max_length (int): Maximum length for the resulting string.
        short (bool): Whether or not to use a truncated timestamp.
    Returns:
        str: Input parameter with appended timestamp.
    """
    timestamp = sagemaker_short_timestamp() if short else sagemaker_timestamp()
    trimmed_base = base[: max_length - len(timestamp) - 1]
    return "{}-{}".format(trimmed_base, timestamp)
