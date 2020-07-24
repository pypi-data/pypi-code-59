from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'evekeys',
  packages = ['evekeys'],
  version = '0.0.2',
  description = 'A set of functions that uses sklearn to conduct a TF-IDF analysis to generate keywords from event-based / grouped textual corpus.',
  author = 'Chris A. Lindgren',
  author_email = 'chris.a.lindgren@gmail.com',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url = 'https://github.com/lingeringcode/evekeys/',
  download_url = 'https://github.com/lingeringcode/evekeys/',
  install_requires = ['pandas', 'sklearn', 'tqdm'],
  keywords = ['tf-idf', 'keyword extraction', 'event-based corpus'],
  classifiers = [],
  include_package_data=True
)
