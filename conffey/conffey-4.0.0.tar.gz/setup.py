# coding=utf-8

from setuptools import setup

setup(
    name='conffey',
    version='v4.0.0',
    description=(
        'A library that encapsulates various functions of Python.'
    ),
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author='C.Z.F.',
    author_email='3023639843@qq.com',
    maintainer='C.Z.F.',
    maintainer_email='3023639843@qq.com',
    license='BSD License',
    packages=[
        'conffey'
    ],
    install_requires=[
        'xpinyin>=0.5.6',
        'Pillow>=7.0.0'
    ],
    platforms=["all"],
    url='https://github.com/super-took/Conffey',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ]
)
