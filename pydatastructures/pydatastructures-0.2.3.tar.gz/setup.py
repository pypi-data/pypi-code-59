from distutils.core import setup

setup(
  name = 'pydatastructures',         
  packages = ['pydatastructures'],   # Chose the same as "name"
  version = '0.2.3',      
  license='MIT',       
  description = 'This is a python library to implement data structures and algorithms',
  author = 'Juan Pablo Montoya',                   
  author_email = 'A01251887@itesm.mx',      
  url = 'https://github.com/JuanPabloMontoya271/pydatastructures.git',   
  download_url = "https://github.com/JuanPabloMontoya271/pydatastructures/archive/v_02.3.tar.gz",

  keywords = ['python', 'data structures'],
  install_requires=[            # I get to this in a second
          'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
