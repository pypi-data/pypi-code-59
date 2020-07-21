import os
import re
# from setuptools.command.install import install
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


NAME = EXE = PACKAGE = "scanloop"
VERSION = re.search("[0-9.]+", read("{}/version.py".format(PACKAGE))).group(0)

setup(
    name=NAME,
    version=VERSION,
    author="Ernesto Alfonso",
    author_email="erjoalgo@gmail.com",
    description=(
        "A scanner front-end to efficiently scan several multi-page documents."),
    license="GPLv3",
    keywords="scanner imagemagick",
    url="https://github.com/erjoalgo/scanloop",
    packages=[PACKAGE],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
    ],
    entry_points={
        'console_scripts': [
            '{}={}.main:main'.format(EXE, PACKAGE),
        ]
    }
)


# Local Variables:
# compile-command: "python setup.py install --user"
# End:
