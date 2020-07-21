#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import cjy

# import numpy as np
# import cv2
# import numpy
# from PIL import Image, ImageDraw, ImageFont
# import copy
# import random
# import shutil
# import os

setup(
    name="cjy",
    version="1.6",
    author="FudanOCR team",
    author_email="19210240232@fudan.edu.cn",
    description="Make your own character using radical sequences!",
    long_description="Make your own character using radical sequences!\n"
                     "import cjy\n"
                     "from cjy.generator import Generator\n"
                     "funny = Generator()\n"
                     "funny.help()\n"
                     "funny.generate()\n",
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/JinGyeSetBirdsFree/RadicalMaker",
    packages=find_packages(),
    install_requires=[

        "pillow","numpy","opencv-python"
        ],
    classifiers=[
        "Topic :: Games/Entertainment ",
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Games/Entertainment :: Board Games',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
