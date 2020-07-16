import setuptools
from pathlib import Path

setuptools.setup(
    name="publish_pypi",
    version=1.0,
    long_description=Path("README.md").read_text(),
    # specify packages
    # find packages finds all packages
    # we pass the folders to exclude from search as arguments
    packages=setuptools.find_packages(exclude=["tests", "data"]),
)
