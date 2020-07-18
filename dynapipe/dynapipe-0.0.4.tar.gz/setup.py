import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynapipe", 
    version="0.0.4",
    author="Tony Dong",
    author_email="tonyleidong@gmail.com",
    description="DynaPipe means Dynamic Pipeline, which is a tool to automate the Machine Learning classification/regression with dynamic functional modules.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tonyleidong/dynapipe",
    keywords = ['AUTO MACHINE LEARNING', 'PIPELINE', 'FEATURES SELECTION','MODEL SELECTION'],
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'statsmodels',
        'scipy',
        'joblib',
        'logging',
        'xgboost',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)

