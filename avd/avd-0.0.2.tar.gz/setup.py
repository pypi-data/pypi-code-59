# encoding: utf-8

import pip

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'avd',
]


def get_reqs():
    return ["requests"]


setup(
    name='avd',
    version='0.0.2',
    url="http://avd.apsara9.com",
    description='Apsara vulnerability database library',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Apsara9 Team",
    author_email = "avd@apsara9.com",
    packages=packages,
    install_requires=get_reqs(),
)
