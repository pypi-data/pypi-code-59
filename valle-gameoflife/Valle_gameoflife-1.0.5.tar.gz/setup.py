import os

import setuptools
from setuptools import setup

setup(
    name='Valle_gameoflife',
    version='1.0.5',
    description='Conway\'s Game of Life for ESGI Python project.',
    url='https://github.com/LeDixiemeHomme/Python-Game-Of-Life',
    author='2ndGroupe',
    packages=setuptools.find_packages(),
    scripts=[
        'bin/gameoflife/',
        'bin/gameoflife.bat',
    ],
    zip_safe=False,
    install_requires=[
        'pygame'
    ]
)
