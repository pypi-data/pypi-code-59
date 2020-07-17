from setuptools import setup, find_packages

VERSION_MAJOR = '0'
VERSION_MINOR = '0'
VERSION_PATCH = '1'


with open('README.md') as f:
    long_description = f.read()

setup(
    name='salure_preprocessors',
    version='{}.{}.{}'.format(
        VERSION_MAJOR,
        VERSION_MINOR,
        VERSION_PATCH),
    python_requires='>=3.5',
    description='Contains some more SKLearn Preprocessors',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Salure',
    author_email='bi@salure.nl',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=[
        'scikit-learn>=0.21.0,<0.23',
        'pandas>=1.0.1,<1.1'
    ],
    zip_safe=False
)
