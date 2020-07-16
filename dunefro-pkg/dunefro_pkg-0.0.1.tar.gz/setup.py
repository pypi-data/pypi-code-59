import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dunefro_pkg",
    version="0.0.1",
    author="Vedant Pareek",
    author_email="dunefro@gmail.com",
    description="A small test package for pip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dunefro/syg_pip.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)