import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='mkwcs',
      version='0.1',
      description='script that makes a WCS solution for a regular image (N up, E left) with some additional rotation.',
      long_description=README,
      long_description_content_type="text/markdown",
      install_requires=['astropy','astroquery','matplotlib','photutils','numpy'],
      url='https://github.com/carlos-contreras-velasquez/mkwcs',
      scripts=['mkwcs/bin/mkwcs_with_angle','mkwcs/bin/mkwcs_with_angle_range','mkwcs/bin/get_angle'],
      author='Carlos Contreras Velasquez',
      author_email='carlos.contreras.velasquez@gmail.com',
      license='Free to use for everyone.',
      packages=['mkwcs'],
      zip_safe=False)
