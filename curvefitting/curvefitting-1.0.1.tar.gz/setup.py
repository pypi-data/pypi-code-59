#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Fan Peilin
# Mail: fanpeilin123@126.com
# Created Time:  2020-7-18 13:14:00
#############################################


from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="curvefitting",
    version="1.0.1",
    keywords=["pip", "curvefitting", "cftool", "curve fitting tool", "curve-fit"],
    description="A MATLAB-like graphical curve fitting tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",

    url="https://github.com/Hamlet-Fansion/curvefitting",
    author="Fan Peilin",
    author_email="fanpeilin123@126.com",

    packages=['curvefitting'],
    package_dir={'curvefitting': 'curvefitting'},
    package_data={'curvefitting': ['curvefitting/language/*.qm', 'curvefitting/ui/*.py']},
    include_package_data=True,
    platforms="any",
    install_requires=["PyQt5", "numpy", "matplotlib", "scipy", "configparser", "pyqtgraph"],
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
