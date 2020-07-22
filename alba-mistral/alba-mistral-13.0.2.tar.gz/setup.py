#!/usr/bin/env python

from setuptools import setup, find_packages

# mistral setup.py for usage of setuptools

# The version is updated automatically with bumpversion
# Do not update manually
__version = '13.0.2'

long_description = """This project has been developd at ALBA Synchrotron 
Light Source, and it is mainly used for image processing purposes at 
BL09-Mistral Tomography Beamline.
"""

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    "Natural Language :: English",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
]

dependencies=['numpy', 'h5py', 'olefile', 'tinydb', 'opencv-python',
              'joblib', 'mrcfile']
# for testing: git, parameterized, 

setup(
    name='alba-mistral',
    version=__version,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'automosaic2nexus = alba.mistral.scripts.automosaic2nexus:main',
            'autonormalize = alba.mistral.scripts.autonormalize:main',
            'autotxrm2nexus = alba.mistral.scripts.autotxrm2nexus:main',
            'copy2proc = alba.mistral.scripts.copy2proc:main',
            'ctbio = alba.mistral.scripts.ctbio:main',
            'ctbiopartial = alba.mistral.scripts.ctbiopartial:main',
            'energyscan = alba.mistral.scripts.energyscan:main'            
            'img = alba.mistral.scripts.image_operate:main',
            'img2stack = alba.mistral.scripts.img2stack:main',
            'magnetism = alba.mistral.scripts.magnetism:main',
            'magnify = alba.mistral.scripts.magnify:main',
            'manyalign = alba.mistral.scripts.manyalign:main',
            'manyaverage = alba.mistral.scripts.manyaverage:main',
            'manycrop = alba.mistral.scripts.manycrop:main',
            'manynorm = alba.mistral.scripts.manynorm:main',
            'manytomos2nexus = alba.mistral.scripts.manytomos2nexus:main',
            'manyxrm2h5 = alba.mistral.scripts.manyxrm2h5:main',
            'manyxrm2norm = alba.mistral.scripts.manyxrm2norm:main',
            'mosaic2nexus = alba.mistral.scripts.mosaic2nexus:main',
            'normalize = alba.mistral.scripts.normalize:main',
            'txrm2nexus = alba.mistral.scripts.txrm2nexus:main',
            'xrm2h5 = alba.mistral.scripts.xrm2h5:main',
            'xrm2nexus = alba.mistral.scripts.xrm2nexus:main',
            'xtendof = alba.mistral.scripts.xtendof:main',
        ]
    },
    author='Marc Rosanes, Carlos Falcon, Zbigniew Reszela, '
           'Carlos Pascual, Gabriel Jover-Manas',
    author_email='mrosanes@cells.es, cfalcon@cells.es, zreszela@cells.es, '
                 'cpascual@cells.es, gjover@cells.es',
    maintainer='ctgensoft',
    maintainer_email='ctgensoft@cells.es',
    url='https://git.cells.es/controls/mistral/mistral',
    keywords='APP',
    license='GPLv3',
    description='Specific software for Mistral beamline at ALBA Synchrotron',
    long_description=long_description,
    requires=['setuptools (>=1.1)'],
    install_requires=dependencies,
    classifiers=classifiers
)

