"""Setup script for image-pcd"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="image-pcd",
    version="1.3.0",
    description="A engine which detects prominent colors from the image.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/divy9881/prominent-colors-detector",
    author="Divy Patel",
    author_email="divy9881@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["pcd"],
    include_package_data=True,
    install_requires=[
        "tensorflow", "sklearn", "matplotlib"
    ]
)