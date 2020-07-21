import os

from setuptools import setup

setup(
    name='Valle_gameoflife',
    version='1.0.1',
    description='Conway\'s Game of Life for ESGI Python project.',
    url='https://github.com/LeDixiemeHomme/Python-Game-Of-Life',
    author='2ndGroupe',
    packages=['gameoflife'],
    scripts=[
        'bin/gameoflife',
        'bin/gameoflife.bat',
    ],
    zip_safe=False,
    install_requires=[
        'pygame'
    ]
)
