from setuptools import setup, find_packages
from fingafrog import __version__


long_description = ''
with open('./README.md') as f:
    long_description = f.read()

install_requires = []
with open('./requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(name='fingafrog',
    version=__version__,
    description='A fingafrog python package.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fingafrog/fingafrog',
    author='Chris Pryer',
    author_email='christophpryer@gmail.com',
    license='PUBLIC',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points ={ 
            'console_scripts': [ 
                'fingafrog = fingafrog.main:main'
            ] 
        },
    zip_safe=False)