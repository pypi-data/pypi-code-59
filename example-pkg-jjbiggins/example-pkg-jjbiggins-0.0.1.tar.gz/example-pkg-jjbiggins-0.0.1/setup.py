import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-jjbiggins", # Replace with your own username
    version="0.0.1",
    author="Joe Biggins",
    author_email="jjbiggins@joebiggins.io",
    description="Stock Quote CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jjbiggins/stock-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
