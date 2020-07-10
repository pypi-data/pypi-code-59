#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'yaspin>=0.17.0','requests>=2.0.1' ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Daniel Furtado",
    author_email='daniel@dfurtado.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="CLI for creating releases on GitHub.",
    entry_points={
        'console_scripts': [
            'github-releaser=github_releaser:cli',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='github-releaser',
    name='github-releaser',
    packages=find_packages(include=['github_releaser', 'github_releaser.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dfurtado/github-releaser',
    version='0.2.0',
    zip_safe=False,
)
