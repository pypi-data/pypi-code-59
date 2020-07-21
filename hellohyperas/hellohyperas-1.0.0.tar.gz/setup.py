from setuptools import setup
from setuptools import find_packages

setup(name='hellohyperas',
      version='1.0.0',
      description='custom notebook filepath enabled, hyperas 0.4.1',
      url='http://github.com/maxpumperla/hyperas',
      download_url='https://github.com/maxpumperla/hyperas/tarball/0.4.1',
      author='Max Pumperla',
      author_email='max.pumperla@googlemail.com',
      install_requires=['keras', 'hyperopt', 'entrypoints', 'jupyter', 'nbformat', 'nbconvert'],
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
