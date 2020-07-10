# -*- encoding: utf8 -*-
import os
from setuptools import setup, find_packages


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
from cms.bin.main import __version__, __author__, __author_email__


setup(
    name='novo-cms',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description='CMS Crawler for Novogene',
    long_description=open(os.path.join(BASE_DIR, 'README.md')).read(),
    long_description_content_type="text/markdown",
    url='https://github.com/suqingdong/cms',
    license='BSD License',
    install_requires=open(os.path.join(BASE_DIR, 'requirements.txt')).read().split(),
    packages=find_packages(),
    include_package_data=True,
    # scripts=['cms/bin/main.py'],
    entry_points={'console_scripts': [
        'cms = cms.bin.main:main',
    ]},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries'
    ]
)
