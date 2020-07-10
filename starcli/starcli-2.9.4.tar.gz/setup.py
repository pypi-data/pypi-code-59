""" setup """

import io

from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    LONG_DESC = f.read()

VERSION = "2.9.4"

# This call to setup() does all the work
setup(
    name="starcli",
    version=VERSION,
    description="Browse popular repos on github by star trends from your command line!",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    url="https://github.com/hedythedev/starcli",
    author="Hedy Li",
    author_email="hedyhyry@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["starcli"],
    include_package_data=True,
    install_requires=[
        "Click>=7.0",
        "colorama>=0.4.3",
        "requests>=2.22.0",
        "rich>=2.1.0",
    ],
    entry_points={"console_scripts": ["starcli=starcli.__main__:cli",]},
)
