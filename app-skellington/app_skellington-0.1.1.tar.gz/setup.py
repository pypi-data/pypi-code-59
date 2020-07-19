#!/usr/bin/env python
#
# Usage:
# 
#   First, enable the python environment you want to install to, or if installing
#   system-wide then ensure you're logged in with sufficient permissions
#   (admin or root to install to system directories)
#
#   installation:
#
#       $ ./setup.py install
#
#   de-installation:
#
#       $ pip uninstall app_skellington


from setuptools import setup
import os

__project__ = 'app_skellington'
__version__ = '0.1.1'
__description__ = 'A high-powered command line menu framework.'

long_description = __description__
readme_filepath = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'README.md'
)
with open(readme_filepath, encoding='utf-8') as fp:
    long_description = fp.read()

setup(
    name             = __project__,
    version          = __version__,
    description      = 'A high-powered command line menu framework.',
    long_description = long_description,
    author           = 'Mathew Guest',
    author_email     = 't3h.zavage@gmail.com',
    url              = 'https://git-mirror.zavage.net/Mirror/app_skellington',
    license          = 'MIT',

    python_requires  = '>=3',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities'
    ],

    # Third-party dependencies; will be automatically installed
    install_requires = (
      'appdirs',
      'configobj',
      'colorlog',
    ),

    # Local packages to be installed (our packages)
    packages = (
        'app_skellington',
    ),
)

