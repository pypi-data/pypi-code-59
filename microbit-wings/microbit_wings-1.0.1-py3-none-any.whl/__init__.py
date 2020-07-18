#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .microbit import Microbit
from .images import *
from .toolbox import *
from time import sleep

microbit = Microbit()

__version__ = '1.0.1'


def get_version():
    return __version__

# use for course development
# from .image_creator import leds_2_image, find_files_4_gif, images_2_gif, leds_2_image_outro, images_2_solution
