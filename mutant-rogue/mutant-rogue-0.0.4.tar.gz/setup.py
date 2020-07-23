
from setuptools import setup, find_packages
from rogue.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

requirements = [
'cement==3.0.4',
'jinja2',
'pyyaml',
'colorlog',
'pytest',
'pytest-cov',
'coverage',
'twine>=1.11.0',
'setuptools>=38.6.0',
'wheel>=0.31.0',
'requests>=2.22.0',
'termcolor>=1.1.0',
'tabulate>=0.8.7'
]

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
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        rogue = rogue.main:main
    """,
)
