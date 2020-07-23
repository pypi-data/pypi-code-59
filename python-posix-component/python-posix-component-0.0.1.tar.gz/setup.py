import os
import re
from setuptools import setup

setup(name='python-posix-component',
      version='0.0.1',
      description='一些在 Unix & Linux 系统上编程的通用组件',
      author="Neeky",
      author_email="neeky@live.com",
      maintainer='Neeky',
      maintainer_email='neeky@live.com',
      packages=['ppc'],
      url='https://github.com/Neeky/ppc',
      python_requires='>=3.6.*',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8']
      )
