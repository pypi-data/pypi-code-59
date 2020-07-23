#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
from pathlib import Path

from setuptools import find_packages, setup


# Package meta-data.
NAME = 'regression_model'
DESCRIPTION = 'Train and deploy regression model.'
URL = 'https://github.com/The-Jyotiram-Koratkar/MyRegJK_V2.0'
download_url = 'https://github.com/The-Jyotiram-Koratkar/MyRegJK_V2.0/archive/V2.0.tar.gz'
EMAIL = 'jyotiramsakshi10@gmail.com'
AUTHOR = 'jyotiram koratkar'
REQUIRES_PYTHON = '>=3.6.0'


# What packages are required for this module to be executed?
def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()


# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the
# Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# Load the package's __version__.py module as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    download_url = 'https://github.com/The-Jyotiram-Koratkar/MyRegJK_V2.0/archive/V2.0.tar.gz',
    packages=find_packages(exclude=('tests',)),
    package_data={'regression_model': ['VERSION']},
    install_requires=[# production requirements
    'numpy==1.16.5'
    'scikit-learn==0.20.2'
    'pandas==0.23.4'

     #packaging
    'setuptools==41.0.0'
    'wheel==0.32.3'

    #testing requirements
    'pytest>=4.6.6,<5.0.0'
    ],
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
         #Trove classifiers
         #Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)