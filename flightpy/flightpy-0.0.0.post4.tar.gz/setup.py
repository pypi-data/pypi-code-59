"""
setup script for flightpy
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = "0.0.0-4" #NOTE: please blame pypy for the weird version numbers...

setup(
    name='flightpy',
    version=version,
    description="a modern python web framework with super powers",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dsikes/flight',
    author='Dan Sikes',
    author_email='dansikes7@gmail.com',
    keywords='python, framework, web framework',
    packages=[
        'flight',
        'flight.cli'
    ],
    install_requires=[
        'click',
        'cerberus',
        'tabulate',
        'pyaml',
        'munch',
        'werkzeug',        
    ],
    entry_points = {
        'console_scripts': ['flight=flight.cli:main'],
    },
    
    project_urls={
        'Source': 'https://github.com/dsikes/flight',
    },
)