from setuptools import setup

setup(
    name='elePyant',
    version='0.0.1',
    author='Fraser Goldsworth',
    author_email='fraser.goldsworth@physics.ox.ac.uk',
    packages=['elePyant', 'elePyant.test'],
    scripts=[],  # ['bin/<<script_name>>]
    url='https://github.com/fraserwg/elePyant/releases/tag/v0.0.1',
    download_url = 'https://github.com/fraserwg/elePyant/archive/v0.0.1.tar.gz',
    license='LICENSE',
    description='Package that performs compression by rounding.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=['xarray', 'numpy', 'h5netcdf'],  # Need to add requirements
)
