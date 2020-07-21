import setuptools
import sys

from pathlib import Path
from setuptools import find_packages

if sys.version_info < (3, 6):
    sys.exit(f'Python < 3.6 will not be supported.')

PACKAGE: str = 'monoclparse'


def this_version() -> str:
    """Read the variable `__version__` from the module itself."""
    contents = Path('monoclparse/_version.py').read_text()
    *_, version = contents.strip().split()
    return version.strip('\'')


setuptools.setup(
    name=PACKAGE,
    version=this_version(),
    author='clintval',
    author_email='valentine.clint@gmail.com',
    description='Parse Monocl Excel business report documents and intersect them!',
    url=f'https://github.com/clintval/{PACKAGE}',
    download_url=f'https://github.com/clintval/{PACKAGE}/archive/v{this_version()}.tar.gz',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=setuptools.find_packages(where='./'),
    install_requires=['pandas'],
    keywords='monocl business report',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    project_urls={
        'Documentation': f'https://{PACKAGE}.readthedocs.io',
        'Issue Tracker': f'https://github.com/clintval/{PACKAGE}/issues',
    },
    zip_safe=False,
)
