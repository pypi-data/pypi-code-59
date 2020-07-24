from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: MacOS :: MacOS X',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Aalmond',
  version='0.1',
  description='Functions for Dataframe Vital Stats, Outliers Detection, Sectional Data View from Mid, Mid Q1, Mid Q3 of a Dataframe',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Manoj S Bhave',
  author_email='manojsbhave@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Data Science, Data Analysis, EDA, Vital Stats, Outliers, Impute, IQR, Zscore, Sectional Dataframe View',
  packages=find_packages(),
  install_requires=[''] 
)