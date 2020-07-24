"""from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='',
  version='0.0.1',
  description='print in Differnt shortcuts',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://knpjg.blogspot.com/',  
  author='KESHARI NANDANA PRATAP',
  author_email='kesharipratap52@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Shortcut,System', 
  packages=find_packages(),
  install_requires=[''] 
)"""
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SHORTCUTIO", # Replace with your own username
    version='0.0.1',
    author="KESHARI NANDANA PRATAP",
    author_email='kesharipratap52@gmail.com',
    description="Print and input shortcut",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://knpjg.blogspot.com/2020/07/my-own-python-shortcutio-libiary.html",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)