import setuptools
import os
import glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name="MGEmasker",
    version="0.1.1",
    author="Anthony Underwood",
    author_email="au3@sanger.ac.uk",
    long_description=read("README.md"),
    license="GPLv3",
    packages=setuptools.find_packages(),
    package_data={'mge_masker': ['mge_patterns.txt']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'maskMGEs=mge_masker.run_find_MGEs:main'
        ]
    },
    python_requires='>=3',
    install_requires=['biopython'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)