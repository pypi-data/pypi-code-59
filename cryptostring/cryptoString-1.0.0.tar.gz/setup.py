#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='cryptoString',
    version='1.0.0',
    author='andy6804tw',
    author_email='andy6804tw@yahoo.com.tw',
    url='https://github.com/1010code/cryptoString',
    description='A module that returns alphanumeric strings.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['cryptoString'],
    install_requires=[],
    entry_points={
        'consoleScripts': [
            'cryptoString=cryptoString:version'
        ]
    }
)