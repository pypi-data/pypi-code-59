from setuptools import setup

setup(name='uswapper',
      version='0.27',
      description='Simple wrapper for uniswap graphql api',
      license='MIT',
      packages=['uswapper'],
      install_requires=[
              'pandas>=1.05',
              'requests>=2.23.0',
              'python_graphql_client',
              'six>=1.14.0'
              ],
      zip_safe=False)
