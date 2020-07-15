from os import environ
from pkg_resources import get_distribution, DistributionNotFound

__VERSION__ = environ.get('MajorMinorPatch', '0.1.0')

try:
    __VERSION__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    try:
        with open('../LOCAL-VERSION') as f:
            __VERSION__ = __VERSION__ + f.readline().strip()
    except IOError:
        pass
