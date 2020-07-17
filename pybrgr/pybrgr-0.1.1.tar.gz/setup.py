from setuptools import setup, find_packages
from pybrgr import __version__


long_description = ''
with open('./README.md') as f:
    long_description = f.read()

install_requires = []
with open('./requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(name='pybrgr',
    version=__version__,
    description='A pybrgr python package.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pybrgr/pybrgr',
    author='Chris Pryer',
    author_email='christophpryer@gmail.com',
    license='PUBLIC',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points ={ 
            'console_scripts': [ 
                'pybrgr = pybrgr.main:main'
            ] 
        },
    zip_safe=False)