import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="midas-engine",
    version="0.0.1",
    author="Brandon Eo",
    author_email="eohyungk@gmail.com",
    description="Trading Engine for Binance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eohyungk/midas-engine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)