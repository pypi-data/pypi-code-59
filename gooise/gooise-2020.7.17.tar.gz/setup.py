from setuptools import setup, find_packages

setup(
    name="gooise",
    version="2020.7.17",
    description="Search for similar images on Google using Selenium",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="scpketer",
    author_email="scpketer@protonmail.ch",
    packages=find_packages(),
    install_requires=(
        "selenium==3.141.0",
        "requests==2.24.0"
    ),
    entry_points={
        "console_scripts": (
            "gooise = gooise.__main__:main",
        )
    },
    classifiers=(
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search"
    )
)
