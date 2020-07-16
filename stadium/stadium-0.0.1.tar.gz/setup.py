from setuptools import setup, find_packages

exec(open('stadium/_version.py').read())

VERSION = __version__


setup(name='stadium',
      version=VERSION,
      description='Stadium',
      long_description="Stadium",
      classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7'
      ],
      author='Allen Institute for Artificial Intelligence',
      author_email='stadium@allenai.org',
      license='Apache',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=[ ],
      include_package_data=False)
