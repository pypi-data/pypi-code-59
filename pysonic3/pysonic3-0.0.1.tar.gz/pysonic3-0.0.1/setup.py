#!/usr/bin/env python

'''
This package contains wrappers for accessing the LIBSONIC API from Python.
'''

from setuptools import setup
from setuptools.extension import Extension
from sys import version

pysonic_version = '0.0.1'

if __name__ == '__main__':
    setup(
        name = 'pysonic3',
        version = pysonic_version,
        description = 'libsonic bindings',
        long_description = __doc__,
        author = 'Bing',
        author_email='byan@openailab.com',
        maintainer = 'Bing',
        maintainer_email = 'byan@openailab.com',
        license='PSF',
        platforms=['posix'],
        url='http://eaidk.openailab.com',
        classifiers = [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Python Software Foundation License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',    
            'Topic :: Multimedia :: Sound/Audio',
            ],
        ext_modules=[Extension('sonic', sources=["pysonic.c","wave.c"], 
                               libraries=['sonic'])]
    )
