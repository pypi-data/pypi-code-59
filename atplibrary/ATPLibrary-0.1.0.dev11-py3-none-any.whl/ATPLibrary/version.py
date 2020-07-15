from os import environ
from pkg_resources import get_distribution, DistributionNotFound

version_suffix = ''
__VERSION__ = '0.1.0'

try:
    __VERSION__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    try:
        with open('../LOCAL-VERSION') as f:
            version_suffix = f.readline().strip()
    except IOError:
        pass

__VERSION__ = __VERSION__ + version_suffix
