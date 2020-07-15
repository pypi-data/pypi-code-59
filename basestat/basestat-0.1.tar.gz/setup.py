from distutils.core import setup
setup(
  name = 'basestat',         # How you named your package folder (MyLib)
  packages = ['basestat'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A simple, light-weight library to use basic Statistics functions like Mean, Median and Mode.',   # Give a short description about your library
  author = 'Akash Mahajan',                   # Type in your name
  author_email = 'akashmahajan025@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/thisisakashmahajan/basestat',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/thisisakashmahajan/basestat/archive/v_0.1.tar.gz',    # I explain this later on
  keywords = ['basestat', 'statistics', 'python statistics', 'basic statistics'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
