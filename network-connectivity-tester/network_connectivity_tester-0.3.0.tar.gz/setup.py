#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open("requirements.txt") as f:
    requirements = f.read().strip().split("\n")

with open("requirements_dev.txt") as f:
    test_requirements = f.read().strip().split("\n")

setup(
    author="revenants-cie",
    author_email='dev@revenants.net',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Test network connections between multiple instances and the internet using standard unit tests",
    entry_points={
        'console_scripts': [
            'network-connectivity-tester-aws-client=network_connectivity_tester.cli.awsclient:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='network_connectivity_tester',
    name='network_connectivity_tester',
    packages=find_packages(include=['network_connectivity_tester', 'network_connectivity_tester.*']),
    setup_requires=test_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/revenants-cie/network_connectivity_tester',
    version='0.3.0',
    zip_safe=False,
)
