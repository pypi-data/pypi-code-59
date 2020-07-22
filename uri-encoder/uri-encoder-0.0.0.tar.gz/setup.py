from setuptools import setup, find_packages

setup(
  name='uri-encoder',
  version='0.0.0',
  author='Tony O\'Dell',
  author_email='tony.odell+python@live.com',
  package_dir={'': 'src'},
  packages=find_packages(where='src'),
  url='https://github.com/tony-o/python-uri-encoder',
  license='LICENSE',
  description='A uri component encoder/decoder',
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  install_requires=[],
);
