import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hexagen",
    version="1.1",
    author="Clemens-Alexander Brust",
    author_email="ikosa.de@gmail.com",
    description="Generates random hexadecimal digits and prints them to standard output.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cabrust/hexagen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
    python_requires=">=3.6",
)
