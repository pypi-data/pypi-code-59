import setuptools
from pathlib import Path

setuptools.setup(
    name='prashpdf',
    version=1.0,
    longdescription=Path('README.md').read_text(),
    # below method will look at our project and automaticaly detects the package defined
    # as 2 files don't contain source code(tests and data) ,hence we need to exclude them
    packages=setuptools.find_packages(exclude=['tests', 'data'])
)
