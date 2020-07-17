# -*- coding: utf-8 -*-
import os

from setuptools import setup
from setuptools import find_packages

'''
Semantic Versioning
Source: https://semver.org/

Given a version number MAJOR.MINOR.PATCH, increment the:

MAJOR version when you make incompatible API changes,
MINOR version when you add functionality in a backwards compatible manner, and
PATCH version when you make backwards compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions
to the MAJOR.MINOR.PATCH format.
'''
__VERSION__ = '0.1.0'

f = open( os.path.join( os.getcwd(), 'README.md' ), encoding= 'utf-8' )
__README__ = f.read()

setup(
    name = 'B3Parser',

    version = __VERSION__,

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        'pymongo',
    ],

    packages = find_packages(
        exclude = [
            'tests',
            '*.tests',
            '*.tests.*',
            'tests.*'
        ]
    ),

    # metadata to display on PyPI
    author = 'Diogo L. Rebouças',
    author_email = 'diogolr@gmail.com',
    description = 'Um parser para os arquivos de histórico de cotações da B3.',
    long_description = __README__,
    long_description_content_type = 'text/markdown',
    keywords = 'Cotações Históricas B3 COTAHIST',
    url = 'https://github.com/diogolr/b3parser',   # project home page, if any
    classifiers = [
        'License :: OSI Approved :: GNU Lesser General Public License '
        'v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    license = 'LGPL v3'
)