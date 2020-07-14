from setuptools import find_packages, setup


setup(name='e2e',
      version='0.1.0',
      description='e2e',
      author='sbneto',
      install_requires=[],
      include_package_data=True,
      packages=find_packages('src'),
      package_dir={'': 'src/'},
      )
