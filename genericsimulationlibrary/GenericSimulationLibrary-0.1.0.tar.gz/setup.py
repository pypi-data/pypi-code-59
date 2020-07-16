from distutils.core import setup

# Read the version from the file, so we define it only in one place
version=open('src/version.py').read().split("=")[1].replace('"','')

# Use the README for the long description
long_description=open('README.md').read()

setup(
    name='GenericSimulationLibrary',
    version=version,
    author='Sebastian Flores',
    author_email='sebastiandres@gmail.com',
    packages=['src'],
    scripts=[],
    url='https://github.com/sebastiandres/GenericSimulationLibrary',
    license='MIT',
    description='A simple but functional simulation interface.',
    long_description=long_description,
)
