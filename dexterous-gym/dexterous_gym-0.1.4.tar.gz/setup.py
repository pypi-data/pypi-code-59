from setuptools import setup
import setuptools

setup(name='dexterous_gym',
      version='0.1.4',
      description='Challenging extensions to openAI Gyms hand manipulation environments',
      url='http://github.com/henrycharlesworth/dexterous_gym',
      author='Henry Charlesworth',
      author_email='H.Charlesworth@warwick.ac.uk',
      packages=setuptools.find_packages(),
      package_data={'dexterous_gym.envs': ['hand/*'],
                    'dexterous_gym.envs': ['stls/hand/*'],
                    'dexterous_gym.envs': ['textures/*']},
      zip_safe=False)
