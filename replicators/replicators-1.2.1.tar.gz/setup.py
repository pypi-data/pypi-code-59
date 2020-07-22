"""
This is the file used for creating the package
"""

import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open("README.md") as fid:
    README = fid.read()

setup(
    name="replicators",
    version="1.2.1",
    description="abstraction for concurrency and multithreading",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bclipp/replicators",
    author="Brian Lipp",
    author_email="bclipp770@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["replicators"],
    include_package_data=False,
    entry_points={"console_scripts": ["replicators=replicant.__main__:main"]},
)
