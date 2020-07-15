# coding: utf-8


from setuptools import setup, find_packages  # type: ignore

import arcor2_kinali

setup(
    name='arcor2_kinali',
    version=arcor2_kinali.version(),
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={"arcor2_kinali": ["py.typed"]},
    url='',
    license='',
    author='Robo@FIT',
    author_email='imaterna@fit.vut.cz',
    description='',
    install_requires=[
        'dataclasses',
        'dataclasses-jsonschema[fast-validation]',
        'arcor2==0.7.1',
        'Pillow'
    ],
    zip_safe=False,
)
