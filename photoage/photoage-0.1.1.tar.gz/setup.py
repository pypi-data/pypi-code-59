import os
from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='photoage',
    version='0.1.1',
    description='Calculate the age of a photo.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='johnlinp',
    author_email='johnlinp@gmail.com',
    url='https://github.com/johnlinp/photoage',
    license='New BSD License',
    install_requires=[
        'exifread',
    ],
    packages=[
        'photoage',
    ],
    scripts=[
        'bin/photoage',
    ],
)
