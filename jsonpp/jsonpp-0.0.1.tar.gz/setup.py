import io
from setuptools import setup, find_packages


def dependencies(file):
    with open(file) as f:
        return f.read().splitlines()


with io.open("README.md", encoding='utf-8') as infile:
    long_description = infile.read()

setup(
    name="jsonpp",
    version="0.0.1",
    license='MIT',
    packages=find_packages(),
    author="Sahil Gupta",
    author_email="sahil865gupta@gmail.com",
    description="JSON prettyprint in commandline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sahil865gupta/jsonpp',
    entry_points={
        'console_scripts': ['jsonpp=jsonpp.command_line:main'],
    },
    keywords=[
        "command-line",
        "pretty-print",
        "colorful"
    ],
    install_requires=dependencies('requirements.txt')
)
