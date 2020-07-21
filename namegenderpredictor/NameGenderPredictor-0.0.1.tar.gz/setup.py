# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:51:32 2020

@author: Hadrien
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NameGenderPredictor", # Replace with your own username
    version="0.0.1",
    author="Hadrien Van Lierde",
    author_email="hadrien.vanlierde@gmail.com",
    description="Prediction of gender probabilities for English names.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xiaoha798/py-NameGenderPredictor",
    packages=setuptools.find_packages(),
    package_data={"":['nameGenderUSSSA.db']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)