#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'chibi-requests>=0.6.1' ]

setup(
    author="dem4ply",
    author_email='dem4ply@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="lib for use the XL Deploy api",
    entry_points={
        'console_scripts': [
            'chibi_xl_deploy=chibi_xl_deploy.cli:main',
        ],
    },
    install_requires=requirements,
    license="WTFPL",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='chibi_xl_deploy',
    name='chibi_xl_deploy',
    packages=find_packages(include=['chibi_xl_deploy', 'chibi_xl_deploy.*']),
    url='https://github.com/dem4ply/chibi_xl_deploy',
    version='0.0.1',
    zip_safe=False,
)
