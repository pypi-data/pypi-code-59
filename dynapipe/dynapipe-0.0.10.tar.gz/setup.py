import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynapipe", 
    version="0.0.10",
    author="Tony Dong",
    author_email="tonyleidong@gmail.com",
    description="DynaPipe (Dynamic Pipeline) helps data scientists to build models in ensemble way, and automate Machine Learning workflow with simple coding.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tonyleidong/dynapipe",
    keywords = ['AUTO MACHINE LEARNING', 'FEATURES SELECTION', 'MODEL SELECTION'],
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'statsmodels',
        'scipy',
        'joblib',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',

)

