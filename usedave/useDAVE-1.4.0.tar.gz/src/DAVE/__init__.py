# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound

from . import auto_download

from .scene import *
# from .gui.nodeA import Gui
# from .jupyter import screenshot, show
from .rigging import create_shackle_gphd


