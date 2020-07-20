
import setuptools

def readme():
	with open('README.md') as f:
		return f.read()

setuptools.setup(name='mihkelBayesian',
	version='0.0.1',
	author='MKR',
	description = 'Machine learning hyperparameter optimiser using the Bayesian model',
	long_description=readme(),
	long_description_content_type='text/markdown',
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/mihkeKR/mihkelBayesian",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    extras_required={ "dev": ["pytest>=3.7",],   },




	)

