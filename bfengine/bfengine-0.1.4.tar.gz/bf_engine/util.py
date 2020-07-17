import random
import string


def random_str(length):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, length))

    return salt
