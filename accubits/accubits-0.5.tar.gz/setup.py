import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='accubits',
    version='0.5',
    packages=['accubits'],
    description="CLI Tool to create front end web apps from boilerplate code",
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    license='MIT',
    download_url='https://github.com/accubits-tech/accubits-cli/archive/0.5.tar.gz',
    author = 'Nithi',
    author_email = 'bearnithi@gmail.com',
    keywords = ['Accubits Cli', 'Front end boilerplates', 'angular boilerplate'],
    install_requires=[
        'Click',
        'gitpython'
    ],
    entry_points='''
        [console_scripts]
        accubits=accubits.main:cli
    ''',
)