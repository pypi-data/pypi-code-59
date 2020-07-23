#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : setup.py
# Author            : Joe Biggins <jjbiggins@joebiggins.io>
# Date              : 22.07.2020
# Last Modified Date: 22.07.2020
# Last Modified By  : Joe Biggins <jjbiggins@joebiggins.io>

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="code_snippets-pkg-jjbiggins", # Replace with your own username
    version="0.0.1",
    author="Joe Biggins",
    author_email="jjbiggins@joebiggins.io",
    description="Stock Quote CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jjbiggins/code_snippets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

