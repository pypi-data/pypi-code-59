#! /usr/bin/env python
from __future__ import absolute_import

import codecs
import os

from setuptools import find_packages, setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# get __version__ from _version.py
ver_file = os.path.join("weles", "_version.py")
with open(ver_file) as f:
    exec(f.read())

DISTNAME = "weles"
DESCRIPTION = "Supplementary scikit-learn package with methods developed in W4K2."
MAINTAINER = "P. Ksieniewicz"
MAINTAINER_EMAIL = "pawel.ksieniewicz@pwr.edu.pl"
URL = "https://github.com/w4k2/weles"
LICENSE = "GPL-3.0"
DOWNLOAD_URL = "https://github.com/w4k2/weles"
VERSION = __version__
INSTALL_REQUIRES = ["numpy", "scipy", "scikit-learn", "imblearn", "tabulate", "tqdm"]
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.7",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name=DISTNAME,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=CLASSIFIERS,
)
