import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyBinF",
    version="0.1.0",
    author="Frank Lin",
    author_email="W_126mail@126.com",
    description="Python binary files parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usr8820/PyBinF/",
    packages=['PyBF'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    install_requires=['PyErrs']
)