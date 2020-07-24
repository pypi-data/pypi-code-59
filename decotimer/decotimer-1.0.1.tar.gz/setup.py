import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decotimer",
    version="1.0.1",
    author="excp281",
    author_email="excp281@gmail.com",
    description="decotimer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/excp281/decotimer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)