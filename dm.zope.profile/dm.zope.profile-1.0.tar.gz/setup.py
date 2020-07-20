from os.path import abspath, dirname, join
try:
  # try to use setuptools
  from setuptools import setup
  setupArgs = dict(
      include_package_data=True,
      install_requires=[
        'setuptools', # to make "buildout" happy
        'Zope>=4',
        'z3c.form',
        'dm.reuse',
      ] ,
      namespace_packages=['dm', 'dm.zope',
                          ],
      zip_safe=False,
      entry_points = dict(
        ),
      )
except ImportError:
  # use distutils
  from distutils import setup
  setupArgs = dict(
    )

cd = abspath(dirname(__file__))
pd = join(cd, 'dm', 'zope', 'profile')

def pread(filename, base=pd): return open(join(base, filename)).read().rstrip()


setup(name='dm.zope.profile',
      version=pread('VERSION.txt').split('\n')[0],
      description="Profiling Zope applications (for Zope >= 4)",
      long_description=pread('README.txt'),
      classifiers=[
#        'Development Status :: 3 - Alpha',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Framework :: Zope',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        ],
      author='Dieter Maurer',
      author_email='dieter@handshake.de',
      url='https://pypi.org/project/dm.zope.profile',
      packages=['dm', 'dm.zope', 'dm.zope.profile'],
      license='BSD',
      keywords='profiling zope',
      **setupArgs
      )
