from setuptools import setup, find_packages

    
setup(
    name='ts_insights',
    version='0.2.0',
    description='Python package to get time series insights',
    long_description="from ts_insights import trend_identification   help(trend_identification)",
    long_description_content_type="text/markdown",
    keywords=['time series', 'insights', 'analysis'],
    url='',
    author='Nikhil Bankar',
    author_email='bankarniikhiil@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['pandas', 'dateinfer'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3.6',
    ],
    package_data={
        # If any package contains *.txt files, include them:
        #         '': ['*.sav'],
        # And include any *.dat files found in the 'data' subdirectory
        # of the 'mypkg' package, also:
        #'customer_models': ['model_objs/*.sav'],
    })