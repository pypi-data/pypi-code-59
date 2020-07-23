"""uActor setuptools script."""
"""
uActor: Process Actor Model
===========================

See README.md provided in source distributions or available
at the `project repository <https://gitlab.com/ergoithz/uactor>`_.

License
-------

Copyright (c) 2020, Felipe A Hernandez.

MIT License (see `LICENSE`_).

.. _LICENSE: https://gitlab.com/ergoithz/uactor/-/blob/master/LICENSE

"""

import datetime
import io
import os
import re

from setuptools import setup

repository = 'https://gitlab.com/ergoithz/uactor'

with io.open('README.md', 'rt', encoding='utf8') as f:
    content = f.read()
    readme = re.sub(
        r'(?P<prefix>!?)\[(?P<text>[^]]+)\]\(\./(?P<src>[^)]+)\)',
        lambda match: (
            '{prefix}[{text}]({repository}/-/{view}/master/{src})'.format(
                repository=repository,
                view='raw' if match.group('prefix') == '!' else 'blob',
                **match.groupdict(),
                )),
        content,
        )

with io.open('uactor.py', 'rt', encoding='utf8') as f:
    content = f.read()
    __author__, __email__, __license__, __version__ = filter(None, (
        re.search(rf"__{name}__ = '([^']+)'", content).group(1)
        for name in ('author', 'email', 'license', 'version')
        ))
    version = (
        __version__
        if os.getenv('TWINE_REPOSITORY') == 'pypi' else
        '{}a{}'.format(__version__, datetime.date.today().strftime('%Y%m%d'))
        )

setup(
    name='uactor',
    version=version,
    url=repository,
    license=__license__,
    author=__author__,
    author_email=__email__,
    description='uActor: Process Actor Model',
    long_description=readme,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Hardware :: Symmetric Multi-processing',
        ],
    python_requires='>=3.6.0',
    extras_require={
        'codestyle': [
            'flake8',
            'flake8-blind-except',
            'flake8-bugbear',
            'flake8-builtins',
            'flake8-commas',
            'flake8-docstrings',
            'flake8-import-order',
            'flake8-logging-format',
            'flake8-rst-docstrings',
            ],
        'coverage': [
            'coverage',
            ],
        'docs': [
            'recommonmark',
            'sphinx',
            ],
        'release': [
            'wheel',
            'twine',
            ],
        'tests': [
            'coverage',
            ],
        },
    keywords=['actor', 'multiprocessing'],
    py_modules=['uactor'],
    test_suite='tests',
    platforms='any',
    zip_safe=True,
    )
