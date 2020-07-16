import os
import os.path

from setuptools import find_packages
from setuptools import setup


def find_requires():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    requirements =[]
    with open ('{0}/requirements.txt'.format(dir_path), 'r') as reqs:
        requirements =reqs.readlines()
    return requirements

if __name__ == "__main__":
    setup(
            name = "a2conn",
            version = "0.1.0",
            description = 'my cool package',
            packages = find_packages(),
            install_requires = find_requires(),
            include_package_data = True,
            entry_points = {
                'console_scripts': [
                    'a2conn = a2conn.zebra:main',
                ],
            },
        )
