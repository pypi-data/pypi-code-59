from setuptools import setup

setup(name='fortinetapi',
      version='0.1',
      description='Fortinet API',
      url='https://gitlab.com/elevenpaths/fortinet-api',
      author='Henrique Caires',
      author_email='henrique@caires.net.br',
      license='MIT',
      packages=['fortinetapi'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
