from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='bilinator',
  version='0.0.2',
  description='Creates bil files from fits files via tiff files. ',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/YatinAdityaT/bilinator',  
  author='Yatin Aditya Tekumalla',
  author_email='yatint5@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='bil', 
  packages=find_packages(),
  install_requires=['gdal','numpy','astropy','pillow'] 
)