from setuptools import setup, find_packages

from pathlib import Path

path = Path(__file__).resolve().parent
with open(path/'README.md', encoding='utf-8') as f:
    long_description = f.read()

with open(path/'VERSION') as version_file:
    version = version_file.read().strip()


setup(name='datadbs',
      version=version,
      description='DataDBS are some class to manage data NoSQL type',
      url='http://www.gitlab.com/dpineda/datadbs',
      author='David Pineda Osorio',
      author_email='dpineda@csn.uchile.cl',
      license='GPLv3',
      packages=['datadbs'],
      install_requires=['networktools', 'basic-logtools'],
      package_dir={'datadbs': 'datadbs'},
      package_data={
          'datadbs': ['../doc', '../docs', '../requeriments.txt']},
      include_package_data=True,
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False)
