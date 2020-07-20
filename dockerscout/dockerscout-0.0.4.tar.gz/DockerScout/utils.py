import re

time_re = re.compile(r"(\d+)([hmsdw]*)")
space_re = re.compile(r"(\d+)([mg]*)")


def time_suffix(text):
    """
    Return the time string "10s" "3h" as seconds
    :param text:
    :return: number of seconds
    """
    m = re.match(time_re, text)
    multiply = 1
    if len(m.groups()) == 2:
        suffix = m.group(2)

        if suffix == "h":
            multiply = 60 * 60
        if suffix == "m":
            multiply = 60
        if suffix == "d":
            multiply = 60 * 60 * 24
        if suffix == "w":
            multiply = 60 * 60 * 24 * 7
        number = int(m.group(1))
    else:
        raise ValueError("Expected a string with a suffix eg (10s, 3h)")

    return multiply * number


def space_suffix(text):
    """
    Return the disk space string "10g" "100m" in megabytes
    :param text:
    :return:
    """
    m = re.match(space_re, text)
    multiply = 1
    if len(m.groups()) == 2:
        suffix = m.group(2)

        if suffix == "g":
            multiply = 1024

        number = int(m.group(1))
    else:
        raise ValueError("Expected a string with a suffix eg (10g, 300m)")

    return multiply * number
