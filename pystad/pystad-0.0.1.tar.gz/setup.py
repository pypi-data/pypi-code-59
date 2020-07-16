#!/usr/bin/env python

from setuptools import setup
import codecs
import os
import re

HERE = os.path.abspath(os.path.dirname(__file__))

with open('README.md') as readme_file:
    readme = readme_file.read()

def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(HERE, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name='pystad',
    version=find_version('stad', '__init__.py'),
    description='Dimensionality reduction through Simplified Topological  Abstraction of Data',
    long_description=readme,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['stad'],
    author='Jelmer Bot',
    author_email='jelmer.bot@uhasselt.be',
    url='https://gitlab.com/JelmerBot/pystad2',
    extras_require={
        'testing': [ # `pip install -e ".[testing]"``
            'pytest', 
            'networkx',
            'matplotlib',
            'scikit-learn'
        ],
        'examples': [ # `pip install -e ".[examples]"``
            'jupyterlab',
            'ipywidgets',
            'panel',
            'networkx',
            'matplotlib',
            'scikit-learn'
        ]
    },
    install_requires = [
    'numpy',
    'scipy',
    'pandas',
    'python-igraph',
    ],
    python_requires='>=3.7',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3.7",
    ]
)