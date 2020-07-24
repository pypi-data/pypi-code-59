import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="randcw-Renz420", # Replace with your own username
    version="0.0.1",
    author="Rene",
    author_email="ren@voiro.com",
    description="Package for uploading data to cloudwatch using python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rene-Voiro/Randtocw.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)