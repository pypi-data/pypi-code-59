# -*- coding: utf-8 -*-

"""
@date: 2020/7/21 下午9:27
@file: setup.py.py
@author: zj
@description: 
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ParseAnno",
    version="0.1.0",
    author="zj",
    author_email="wy163zhuj@163.com",
    description="Script for annotation data processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zjZSTU/ParseAnno",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
