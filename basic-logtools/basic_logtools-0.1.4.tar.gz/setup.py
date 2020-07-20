from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).resolve().parent

with open(this_directory/'README.md', encoding='utf-8') as f:
    readme = f.read()

with open(this_directory/'VERSION') as version_file:
    version = version_file.read().strip()

setup(name='basic_logtools',
      version=version,
      description='Some useful tools for asycnio Tasks: async while, the Scheduler and Assignator classes',
      url='https://logtools.readthedocs.io/en/latest/',
      author='David Pineda Osorio',
      author_email='dpineda@uchile.cl',
      license='GPL3',
      long_description=readme,
      long_description_content_type='text/markdown',
      zip_safe=False)
