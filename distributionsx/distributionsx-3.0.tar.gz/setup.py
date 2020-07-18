# from setuptools import setup

# setup(name='probabilityx',
#       version='1.0',
#       description='Gaussian distributions',
#       packages=['distributions'],
#       author='sidra',
#       email='codehappysf@gmail.com',
#       zip_safe=False)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="distributionsx", 
    version="3.0",
    author="Sidra Muntaha",
    author_email="codehappysf@gmail.com",
    description="A package to calculate distributions (normal or binomial) sum, plot, mean and standard deviation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)