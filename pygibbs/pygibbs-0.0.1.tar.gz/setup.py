import numpy
import os, sys , re
from setuptools import setup, Extension


with open("README.md", "r") as fh:
    long_description = fh.read()


cwd = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(cwd, 'pygibbs', '__init__.py')) as fp:
    for line in fp:
        m = re.search(r'^\s*__version__\s*=\s*([\'"])([^\'"]+)\1\s*$', line)
        if m:
            version = m.group(2)
            break
    else:
        raise RuntimeError('Unable to find own __version__ string')


setup(
    name='pygibbs',
    version=version,
    url='https://github.com/rajeshrinet/pygibbs',
    author='The PyGibbs team',
    license='MIT',
    description='PyGL is a numerical library for simulations of field theories in Python.',
    long_description=long_description,
    platforms='tested on LINUX and macOS',
    libraries=[],
    packages=['pygibbs'],
    install_requires=['numpy','scipy'],
    extras_require={
            'plotting': ['matplotlib'],
            'notebook': ['jupyter', 'nbconvert']},
)
