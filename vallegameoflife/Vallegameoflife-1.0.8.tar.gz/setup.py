import os

from setuptools import setup

setup(
    name='Vallegameoflife',
    version='1.0.8',
    description='Conway\'s Game of Life for ESGI Python project.',
    url='https://github.com/LeDixiemeHomme/Python-Game-Of-Life',
    author='2ndGroupe',
    packages=['Vallegameoflife','Vallegameoflife/screens', 'Vallegameoflife/game'],
    scripts=[
        'bin/Vallegameoflife',
        'bin/Vallegameoflife.bat',
    ],
    zip_safe=False,
    install_requires=[
        'pygame'
    ]
)
