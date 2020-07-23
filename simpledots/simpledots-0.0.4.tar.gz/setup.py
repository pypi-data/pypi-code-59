'''
setup.py for simpledots.py
Lincoln Ombelets 2020
'''

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

setup(
    name='simpledots',
    version='0.0.4',
    description='Analysis package for smFISH and puncta-like images, focused on simplicity and ease of use.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/lincdog/simpledots',
    license='MIT',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License'
    ],
    #package_dir={'': 'simpledots'},
    packages=find_packages(),
    python_requires='>=3.5',
    author='Lincoln Ombelets',
    install_requires=install_requires,
    author_email='lombelets@caltech.edu'
)
