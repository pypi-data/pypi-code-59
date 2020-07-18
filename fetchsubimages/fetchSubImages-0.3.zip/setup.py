from distutils.core import setup

setup(
  name = 'fetchSubImages',
  packages = ['fetchSubImages'],
  version = '0.3',
  license='MIT',
  description = 'Fetch image post\'s content from any given subreddit',
  author = 'Marco Antonio Ribeiro de Toledo',
  author_email = 'marcoantonioribeirodetoledo@gmail.com',
  url = 'https://github.com/Ocramoi/fetchSubImages',
  download_url = 'https://github.com/Ocramoi/fetchSubImages/archive/v0.3-beta.tar.gz',
  keywords = ['reddit', 'image', 'scrape'],
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta', # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)