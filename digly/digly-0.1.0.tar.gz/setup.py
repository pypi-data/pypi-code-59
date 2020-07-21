
from setuptools import setup
from os import path


from io import open as io_open
import re


summary = "Tool for automated Instagram interactions"
project_homepage = "https://github.com/CMSHostingLLC/digly"

here = path.abspath(path.dirname(__file__))


def readall(*args):
    with io_open(path.join(here, *args), encoding="utf-8") as fp:
        return fp.read()


with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

documentation = readall("README.md")
metadata = dict(
    re.findall(r"""__([a-z]+)__ = "([^"]+)""", readall("digly", "__init__.py"))
)

setup(
    name="digly",
    version=metadata["version"],
    description=summary,
    long_description=documentation,
    long_description_content_type="text/markdown",
    author="Digly",
    maintainer="Digly",
    license="GPLv3",
    url=project_homepage,
    download_url=(project_homepage + "/archive/master.zip"),
    project_urls={
        "Source": (project_homepage + "/tree/master/digly")
    },
    packages=["digly"],
    # include_package_data=True,  # <- packs every data file in the package
    package_data={  # we need only the files below:
        "digly": [
            "firefox_extension/*",
            "plugins/*",
        ]
    },
    keywords=(
        "digly instagram automation \
         marketing promotion bot selenium"
    ),
    classifiers=[
        "Environment :: Console",
        "Environment :: MacOS X",
        "Environment :: Web Environment",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Programming Language :: SQL",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=dependencies,
    extras_require={"test": ["tox", "virtualenv", "tox-venv"]},
    python_requires=">=3, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    platforms=["linux", "linux2", "darwin"],
    zip_safe=False,
    entry_points={"console_scripts": []},
)
