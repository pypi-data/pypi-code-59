from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

__version__ = '0.0.2'

setup(
    name="strtypes",
    version=__version__,
    packages=find_packages(),
    author="Ibrahim Gadzhimagomedov",
    author_email="ibragdzh@gmail.com",
    description="Python library for managing string types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ibrag8998/strtypes.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
