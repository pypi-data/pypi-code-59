from setuptools import setup, find_packages

setup(
    name='index2rc',
    version='1.0.0',
    description='Creates illumina samplesheet with the reverse complement of the second index (index2).',
    url='https://github.com/ssi-dk/index2rc',
    author="Martin Basterrechea",
    author_email="mbas@ssi.dk",
    packages=find_packages(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'index2rc=index2rc:main'
        ]
    },
)
