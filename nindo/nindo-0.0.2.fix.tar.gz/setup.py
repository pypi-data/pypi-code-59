with open("README.md", "r") as fh:
    long_description = fh.read()

import setuptools
setuptools.setup(
    name="nindo",
    version="0.0.2",
    author="Marc Hauck",
    author_email="marchauck04@gmail.com",
    description="Unofficial API for https://nindo.de",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)