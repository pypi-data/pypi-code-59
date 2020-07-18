import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyStruct-williamstella", 
    version="0.0.1",
    author="William Stella",
    author_email="william.a.stella@gmail.com",
    description="A small data-structures library in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wastella/PyStruct",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
