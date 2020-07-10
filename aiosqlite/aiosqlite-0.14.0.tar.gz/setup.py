#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['aiosqlite', 'aiosqlite.tests']

package_data = \
{'': ['*']}

install_requires = \
['typing_extensions']

setup(name='aiosqlite',
      version='0.14.0',
      description='asyncio bridge to the standard sqlite3 module',
      author='John Reese',
      author_email='john@noswap.com',
      url='https://aiosqlite.omnilib.dev',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      python_requires='>=3.6',
     )
