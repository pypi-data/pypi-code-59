"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
import os
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    PKG_DESCRIPTION = f.read()

# Read the API version from disk. This file should be located in the package
# folder, since it's also used to set the pkg.__version__ variable.
version_path = os.path.join(here, 'fhir', '_version.py')
version_ns = {
    '__file__': version_path
}
with open(version_path) as f:
    exec(f.read(), {}, version_ns)



# Setup the package
setup(
    name='py-fhir',
    version=version_ns['__version__'],
    description='FHIR classes for Python',
    long_description=PKG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/mellesies/py-fhir',
    # author='Melle Sieswerda',
    # author_email='',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3',
    install_requires=[
        'python-dateutil',
        'formencode',
        'jsondiff',
        'packaging',
        'pyyaml',
        'termcolor',
        'xmldiff',
    ],
    extras_require={
        'dev': [
            'twine',
        ]
    },
    package_data={
        "": ["__build__"]
    },
    entry_points={},
)
