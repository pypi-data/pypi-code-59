import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imonke",
    version="0.1.1",
    author="Tobi",
    author_email="tobiisdumb@gmail.com",
    description="a iMonke api wrapper",
    long_description=long_description,
    license = "unlicense",
    long_description_content_type="text/markdown",
    url="https://github.com/TobiisDumb/iMonke",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules = ["requests", "colorama"]
)