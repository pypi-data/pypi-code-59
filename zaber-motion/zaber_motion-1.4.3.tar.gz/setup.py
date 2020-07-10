from setuptools import setup, find_packages

from os import path


def read_from_file(*filename):
    with open(path.join(*filename), 'r') as f:
        return f.read()


setup(
    name='zaber_motion',
    version='1.4.3',
    packages=find_packages(exclude=["test*", "test_*", "*_test*"]),
    package_data={
        '': ['*.pyi']
    },
    description='A library for communicating with Zaber devices',
    long_description=read_from_file('DESCRIPTION.md'),
    long_description_content_type="text/markdown",
    url='https://gitlab.com/ZaberTech/zaber-motion-lib',
    author='Zaber Technologies Inc.',
    author_email='contact@zaber.com',
    license='Apache Software License v2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='',
    python_requires='>=3.5',
    install_requires=[
        'protobuf==3.12.2',
        'rx>=3.0.0'
    ],
    extras_require={
        'dev': [
            'pytest',
            'pylint',
            'pycodestyle',
            'setuptools',
            'wheel',
            'twine==1.15.0'
        ],
        ':platform_system=="Windows"': [
            'zaber_motion_bindings_windows==1.4.3'
        ],
        ':platform_system=="Linux"': [
            'zaber_motion_bindings_linux==1.4.3'
        ],
        ':platform_system=="Darwin"': [
            'zaber_motion_bindings_darwin==1.4.3'
        ]
    }
)
