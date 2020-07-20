#!/usr/bin/env python
import re

from setuptools import find_packages, setup

install_require = [
    "attrs>=18.0.0",
    "cached-property>=1.5.0",
    "cryptography>=2.8",
    "lxml>3.0",
    "pytz",
    "python-dateutil>=2.0.0",
    "requests>=2.22.0",
    "pytz>=2019.3",
    "xmlsec>=1.3.0",
]

docs_require = []

tests_require = [
    "freezegun==0.3.15",
    "requests-mock==1.8.0",
    "pytest-cov==2.8.1",
    "pytest>=6.0.0rc1",
    "coverage[toml]==5.2",
    # Linting
    "isort==4.2.5",
    "flake8==3.8.3",
    "flake8-blind-except==0.1.1",
    "flake8-debugger==1.4.0",
    "flake8-imports",
]


with open("README.md") as fh:
    long_description = re.sub(
        "<!-- start-no-pypi -->.*<!-- end-no-pypi -->\n",
        "",
        fh.read(),
        flags=re.M | re.S,
    )


setup(
    name="idin",
    version="0.2.0",
    description="IDIN Module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/labd/python-idin",
    author="Lab Digital",
    author_email="opensource@labdigital.nl",
    install_requires=install_require,
    tests_require=tests_require,
    extras_require={"docs": docs_require, "test": tests_require},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    zip_safe=False,
)
