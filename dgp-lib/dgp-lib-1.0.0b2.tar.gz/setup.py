# coding: utf-8

from setuptools import setup

requirements = [
    'numpy==1.19.0',
    'pandas==1.0.5',
    'tables==3.6.1',
    'scipy==1.5.1'
]

setup(
    name='dgp-lib',
    version='1.0.0b2',
    packages=['dgplib', 'dgplib.ingest', 'dgplib.transform'],
    url='https://github.com/dynamicgravitysystems/dgp-lib',
    author='Zachery Brady, Chris Bertinato',
    author_email='bradyzp@dynamicgravitysystems.com',
    description='Library of functions for importing and processing gravity data',
    install_requires=requirements,
    python_requires='>=3.6.*',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: GIS',
    ]
)
