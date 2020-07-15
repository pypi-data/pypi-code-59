from setuptools import setup, find_packages

# read the contents from README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='upmath',
  version='1.2',
  description='This package provides universal precision number and standard math functions that support\
 mathematical operations on the universal precision number.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='',
  author='A K M Aminul Islam',
  author_email='aminul71bd@gmail.com',
  license='NEWTONIA FREEWARE LICENSE',
  packages=find_packages(),
  data_files = [("", ["LICENSE"])],
  zip_safe=False
)
