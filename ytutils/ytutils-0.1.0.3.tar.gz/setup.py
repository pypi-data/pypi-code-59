from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
  name = 'ytutils',
  packages = ['ytutils'],
  version = '0.1.0.3',
  license='MIT',
  description = 'YouTube Extractor',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Sanjay Developer',
  author_email = 'sureshsanjay805@gmail.com',
  url = 'https://github.com/SanjayDevTech/ytutils',
  keywords = ['youtube', 'youtube video', 'youtube channel'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)