#!/usr/bin/env python
from setuptools import setup
import sys
import os

version = '1.0.0'

long_description = open('README.md').read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='darbird',
    version=version,
    packages=['darbird'],
    description='Official Darbird Python SDK',
    data_files=[('', ['README.md'])],
    license='MIT',
    author='Darbird',
    install_requires=[
        'requests>=v2.18.4',
        'schema>=0.6.7'
    ],
    python_requires=">=2.7.10",
    author_email='developers@darbird.com',
    url='https://github.com/darbird/darbird-python',
    download_url='https://github.com/darbird/darbird-python/archive/1.0.tar.gz/',
    keywords='voice sms sender_id darbird',
    classifiers=[],
    long_description=long_description,
    long_description_content_type='text/markdown'
)