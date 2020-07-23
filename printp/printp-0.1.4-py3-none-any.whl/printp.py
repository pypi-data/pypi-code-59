
from input_util import I
from print_dict import print_dict


def printp(arg):

    if I(arg).is_dict:
        print_dict(arg)

    else:
        print(arg)

    return True


def pp(arg):
    return printp(arg)
