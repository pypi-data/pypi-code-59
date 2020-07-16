# -*- coding: utf-8 -*-
"""
package/install module package ekca-client
"""

import sys
import os
from setuptools import setup, find_packages

PYPI_NAME = 'ekca-client'

BASEDIR = os.path.dirname(os.path.realpath(__file__))

sys.path.insert(0, os.path.join(BASEDIR, 'ekca_client'))
import __about__

setup(
    name=PYPI_NAME,
    license=__about__.__license__,
    version=__about__.__version__,
    description='EKCA client tool',
    author=__about__.__author__,
    author_email=__about__.__mail__,
    maintainer=__about__.__author__,
    maintainer_email=__about__.__mail__,
    url='https://ekca.stroeder.com',
    download_url='https://pypi.python.org/pypi/'+PYPI_NAME,
    keywords=['PKI', 'SSH', 'SSH-CA', 'Certificate'],
    packages=find_packages(exclude=['tests']),
    package_dir={'': '.'},
    test_suite='tests',
    python_requires='>=3.4.*',
    include_package_data=True,
    data_files=[],
    install_requires=[
        'setuptools',
        'PyNaCl>=1.2',
        'pywin32; platform_system=="Windows"',
        'ptyprocess; platform_system!="Windows"',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ekca-ssh-init = ekca_client.sshinit:sshinit',
        ],
    }
)
