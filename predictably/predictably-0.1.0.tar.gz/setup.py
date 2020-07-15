import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='predictably',
    version='0.1.0',
    packages=setuptools.find_packages(exclude=('test', 'test_R')),
    url='https://rnkuhns.github.io/predict-ably/',
    license='BSD-3',
    author='Ryan Kuhns',
    author_email='rnkuhns@gmail.com',
    description='Scikit-learn compatible Pyton forecasting module',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - Planning"
    ],
    install_requires=['numpy', 'scipy', 'pmdarima', 'statsmodels', 'scikit-learn'],
    tests_require=['pytest'],
    extras_require={
        'dev': ['pip-tools', 'rpy2'],
    }
)