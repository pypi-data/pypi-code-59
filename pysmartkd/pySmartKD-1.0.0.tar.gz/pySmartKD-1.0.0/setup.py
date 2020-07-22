import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(name='pySmartKD',
      version = '1.0.0',
      description = 'Functions to analyze and plot geochemical data and to predict distribution coefficients',
      long_description = README,
      long_description_content_type = "text/markdown",
      author_email ='jzouabe@berkeley.edu',
      license ="MIT",
      packages=[],
      install_requires=[
        'csv',
        'pandas',
        'numpy',
        'seaborn',
        'matplotlib',
        'sklearn',
        'scipy',
        'pprint',
        'warnings'],
      include_package_Data=True
      )

         

