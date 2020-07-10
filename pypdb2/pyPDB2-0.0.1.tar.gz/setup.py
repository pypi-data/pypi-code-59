from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pyPDB2',
  version='0.0.1',
  description='Dialog Boxes',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Jack Boyd',
  author_email='boydypug@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Dialog, Box', 
  packages=find_packages(),
  install_requires=['pygame'] 
)