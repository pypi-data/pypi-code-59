# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


with open("README.md") as f:
    description = f.read()

setup(
    name="alba",
    author="ALBA Synchrotron computing team",
    author_email="computing@cells.es",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    packages=find_packages(),
    description="ALBA controls meta package",
    long_description=description,
    long_description_content_type="text/markdown",
    keywords="ALBA, synchrotron, controls",
    url="https://github.com/alba-synchrotron/alba",
    version="0.1.1",
    python_requires=">=3.5",
)
