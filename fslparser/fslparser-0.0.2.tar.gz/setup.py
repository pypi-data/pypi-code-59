# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:26:24 2020

@author: Fatemeh
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fslparser",
    version="0.0.2",
    author="Fatemeh",
    author_email="",
    description="fsl-parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['fslparser',],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[ 'pandas>=0.20.3',],
)