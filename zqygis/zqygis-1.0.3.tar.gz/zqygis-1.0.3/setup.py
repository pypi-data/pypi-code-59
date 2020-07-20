# coding: utf-8
import codecs
import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

"""
打包的用的setup必须引入，
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 

import sys
if sys.version_info < (2, 5):
    sys.exit('Python 2.5 or greater is required.')
 
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
 
 
 
with open('README.rst', 'rb') as fp:
    readme = fp.read()
 
# 版本号，自己随便写
VERSION = "1.0.3"

LICENSE = "zqy"

 
setup(
    name='zqygis',
    version=VERSION,
    description=(
        'gis'
    ),
    long_description=readme,
    author='zqy',
    author_email='252238741@qq.com',
    maintainer='<zqy',
    maintainer_email='252238741@qq.com',
    license=LICENSE,
    #packages=find_packages(),
    platforms=["all"],
    url='https://www.baidu.com',
    #install_requires=[  ]
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ],
)