
import setuptools

def readme():
	with open('README.md') as f:
		return f.read()

setuptools.setup(name='mihkelBayesian',
	version='0.0.2',
	author='Mihkel Kaarel Raidal',
	author_email = 'm.k.raidal@gmail.com',
	description = 'Machine learning hyperparameter optimiser using the Bayesian model',
	long_description_content_type='text/markdown',
	long_description=readme(),
	license = 'MIT',
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/mihkelKR/mihkelBayesian",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    extras_required={ "dev": ["pytest>=3.7",],   },




	)

