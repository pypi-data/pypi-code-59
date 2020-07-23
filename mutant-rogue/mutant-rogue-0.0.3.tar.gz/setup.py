
from setuptools import setup, find_packages
from rogue.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='mutant-rogue',
    version=VERSION,
    description='Rogue Cli',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Pedrinho',
    author_email='pedro.carvalho@mutantbr.com',
    url='https://bitbucket.org/unearsa/rogue-cli',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'mutant-rogue': ['templates/*']},
    include_package_data=True,
    python_requires='>=3.6',
    entry_points="""
        [console_scripts]
        rogue = rogue.main:main
    """,
)
