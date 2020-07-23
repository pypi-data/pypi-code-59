# TODO: Fill out this file with information about your package

# HINT: Go back to the object-oriented programming lesson "Putting Code on PyPi" and "Exercise: Upload to PyPi"

# HINT: Here is an example of a setup.py file
# https://packaging.python.org/tutorials/packaging-projects/

from setuptools import setup

setup(name='Modelpair',
      version='1.5',
      description='This is a Python package that is designed to compare different machine learning model performance on a dataset. Currently it can only deal with csv file dataset in a certain format, and it only has a few models available. It is still in progress',
      packages=['Modelpair'],
      zip_safe=False)
