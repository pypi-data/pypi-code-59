from os import environ
from pkg_resources import get_distribution, DistributionNotFound

__VERSION__ = '0.1.0'

try:
    __VERSION__ = get_distribution(__name__).version
except DistributionNotFound:
    pass