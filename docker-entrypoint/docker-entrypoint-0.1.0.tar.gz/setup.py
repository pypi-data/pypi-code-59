#!python
# coding=utf-8

__author__ = "Garrett Bates"
__copyright__ = "© Copyright 2020, Tartan Solutions, Inc"
__credits__ = ["Garrett Bates"]
__license__ = "Apache 2.0"
__version__ = "0.1.0"
__maintainer__ = "Garrett Bates"
__email__ = "garrett.bates@tartansolutions.com"
__status__ = "Development"

from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='docker-entrypoint',
    version='0.1.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
    ],
    entry_points='''
        [console_scripts]
        entrypoint=entrypoint.main:main
    ''',
    python_requires='>=3.7',
)
