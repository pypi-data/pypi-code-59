from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='parserBI',
    version='0.0.1',
    description='A python module to parse source code for retro-documentation',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Nicolas Bouillette, Guillaume Hurvois, Julien Mendes, Adam Wang',
    author_email='nbouillette@bi-consulting.com, '
    'ghurvois@bi-consulting.com, '
    'jmendes@bi-consulting.com, '
    'awang@bi-consulting.com',
    url='https://bitbucket.org/stage_2020/parser/src/master/',
    packages=find_packages(exclude=('tests')),
    python_requires='>=3.7'
)
