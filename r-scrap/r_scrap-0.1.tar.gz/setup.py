from distutils.core import setup
setup(
  name = 'r_scrap',     
  packages = ['r_scrap'],
  version = '0.1',
  license='MIT',
  description = 'A quick reddit scrapper to get subreddits and submissions (PRAW doesn`t provide a good solution for that)',
  author = 'independent.variable2',
  author_email = 'independent.variable2@gmail.com',
  url = 'https://github.com/independentvariable2/r_scrap',  
  download_url = '',
  keywords = ['Reddit', 'subreddit', 'submission', 'PRAW'],
  install_requires=[
          'certifi',
          'idna',
          'urllib3',
          'chardet',
          'requests'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Libraries',
    'License :: Freeware',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'

  ],
)
