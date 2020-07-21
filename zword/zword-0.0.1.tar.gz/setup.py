from setuptools import setup

with open("README.md", 'r') as f:
  long_description = f.read()

with open('requirements.txt') as f:
  install_requires = f.read().splitlines()

setup(
  author="zuroc",
  author_email="zsp042@gmail.com",
  description="从维基百科抽取中文语料",
  include_package_data=True,
  install_requires=install_requires,
  name='zword',
  packages=['zword'],
  url="https://gitee.com/znlp/zword",
  version="0.0.1",
  zip_safe=True,
  long_description_content_type='text/markdown',
  long_description=long_description,
  scripts=["wiki_txt",
           "zscat"]
)
