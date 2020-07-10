import re
import os

from setuptools import setup


def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(name='replication',
      version=get_version("replication"),
      description='A prototype object replication lib',
      url='https://gitlab.com/slumber/replication',
      author='Swann Martinez',
      author_email='swann.martinez@pm.me',
      license='GPL3',
      packages=['replication'],
      entry_points={
          'console_scripts': [
              'replication.serve = replication.server:cli'
          ]
      },
      install_requires=parse_requirements("requirements.txt"),
      test_suite='tests',
      tests_require=['nose'],
      zip_safe=False,)
