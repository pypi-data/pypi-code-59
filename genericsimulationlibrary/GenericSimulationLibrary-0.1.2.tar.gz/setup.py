from distutils.core import setup

def library_version():
    """"Reads the src/version.py file and returns the version in the
    format X.Y.Z (without ' nor ").
    Steps: (1) Open the file (2) Get the version (3) Clean the string

    :return: Current version
    :rtype: string
    """
    filepath = 'src/version.py'
    filecontent = open(filepath, "r").read()
    current_version = filecontent.split("=")[1].replace('"','').replace("\n","")
    return current_version

# Read the version from the file, so we define it only in one place
current_version = library_version()
print("Current Library Version:", current_version)
# Use the README for the long description
long_description=open('README.rst').read()

setup(
    name='GenericSimulationLibrary',
    version=current_version,
    author='Sebastian Flores',
    author_email='sebastiandres@gmail.com',
    packages=['src'],
    scripts=[],
    url='https://github.com/sebastiandres/GenericSimulationLibrary',
    license='MIT',
    description='A simple but functional simulation interface.',
    long_description=long_description,
)
