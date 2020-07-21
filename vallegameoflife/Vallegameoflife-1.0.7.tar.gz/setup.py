import os

from setuptools import setup

setup(
    name='Vallegameoflife',
    version='1.0.7',
    description='Conway\'s Game of Life for ESGI Python project.',
    url='https://github.com/LeDixiemeHomme/Python-Game-Of-Life',
    author='2ndGroupe',
    packages=['gameoflife','gameoflife/screens', 'gameoflife/game'],
    scripts=[
        'bin/gameoflife',
        'bin/gameoflife.bat',
    ],
    zip_safe=False,
    install_requires=[
        'pygame'
    ]
)
