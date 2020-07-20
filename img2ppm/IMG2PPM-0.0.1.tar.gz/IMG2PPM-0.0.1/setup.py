import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IMG2PPM",
    version="0.0.1",
    author="lirc572",
    author_email="e0424619@comp.nus.edu.sg",
    description="A small tool to convert images to a special PPM format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/img2ppm/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Free To Use But Restricted",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
