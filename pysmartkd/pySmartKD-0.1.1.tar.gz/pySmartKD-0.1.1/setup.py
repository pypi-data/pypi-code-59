from setuptools import setup

setup(name='pySmartKD',
      version = '0.1.1',
      description = 'Functions to analyze and plot geochemical data and to predict distribution coefficients',
      long_description ='see documentation',
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

         

