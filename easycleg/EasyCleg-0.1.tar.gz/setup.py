from distutils.core import setup
setup(
  name = 'EasyCleg',         # How you named your package folder (MyLib)
  packages = ['EasyCleg'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Get the best ML models for regression and classification with tuned parameters',   # Give a short description about your library
  author = 'Ishan Jain',                   # Type in your name
  author_email = 'ishan.jain0099@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/bitsofishan',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/bitsofishan/EasyCleg/archive/v1.0.tar.gz',    # I explain this later on
  keywords = ['AutoML', 'Regression', 'Classification'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
          'matplotlib',
          'sklearn',
          
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.6',
  ],
)
