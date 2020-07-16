# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:00:10 2020

@author: LOKSUNDAR
"""


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lokstats",
    version="0.0.1",
    author="LOK SUNDAR GANTHI",
    author_email="loksundar000@gmail.com",
    description="it is for advanced statistics calculations of partial and multiple correlations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/loksundar/partial_multiple_correlation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
) 