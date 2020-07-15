#!/usr/bin/env python

import setuptools
# We use numpy distutils to compile and wrap f90 code via f2py
from numpy.distutils.core import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="softspot", 
    version="1.0.0",
    author="David Richard, Geert Kapteijns",
    author_email="ghkapteijns@gmail.com",
    description="softspot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/davricha/softspot",
    packages=['softspot'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    install_requires = ["numpy", "scipy", "macopt"],
    ext_modules=[Extension(
        name='softspot.softspot_wrap',
        sources=['softspot/softspot.f95'],
        # f2py -c --fcompiler=gfortran  --opt='-O3 -ftree-vectorize' tensor_tools.f95 -m tensor_tools_lib
        extra_f90_compile_args=["-O3", "-ftree-vectorize"])
    ]
)
