import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="libgen",
    version="0.0.1",
    description="Command line tool for downloading files from library genesis",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/amalshaji/libgen-cli",
    author="Amal Shaji",
    author_email="amalshajid@tutanota.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["libgen"],
    include_package_data=True,
    install_requires=["beautifulsoup4", "tqdm", "requests", "pprint", "argparse"]
)
