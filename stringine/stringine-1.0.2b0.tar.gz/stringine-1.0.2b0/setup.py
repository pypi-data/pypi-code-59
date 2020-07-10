import pathlib
from setuptools import setup
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="stringine",
    version="1.0.2-beta",
    description="A simple cross-platform string manipulation utility.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kantondev/stringine",
    author="KantonDev Group",
    author_email="anton@tuomainen.org",
    license="LIECENSE",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("python",)),
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": []
    },
)