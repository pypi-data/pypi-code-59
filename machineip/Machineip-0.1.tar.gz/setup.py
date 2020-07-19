from distutils.core import setup
setup(
  name = 'Machineip',         
  packages = ['Machineip'],   
  version = '0.1',      
  license='MIT',        
  description = 'a small python module that returns the hosts public and local IP',   
  author = 'pytXploiter',                   
  author_email = 'pyXploiter@gmail.com',     
  url = '',   
  download_url = 'https://github.com/pytXploiter/machineIP/archive/v0.1.tar.gz',    
  keywords = ['WAN IP', 'LAN IP', 'Public IP', 'Local IP'],   
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.8',
  ],
)