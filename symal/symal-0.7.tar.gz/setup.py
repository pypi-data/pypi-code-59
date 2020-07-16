
from setuptools import setup, find_packages

setup(name='symal',
	version=0.7,
	description='learning to publish packages',
	author='Igor Paim',
	author_email='igorpaim8@gmail.com',
	url='https://github.com/igrorp/',
	license='MIT',
	classifiers=[
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Bio-Informatics',
		'Programming Language :: Python :: 3',
	],
	keywords='nothing',
	packages=find_packages(),
	install_requires=[
		'matplotlib',
		'scikit-learn',
		'numpy',
		'svglib',
		'svgwrite',
		'pandas',
		'seaborn',
	],
	#   install_requires=[
	#       'matplotlib==3.2.1',
	#       'scikit-learn==0.22.2',
	#       'numpy>=1.14.6',
	#       'svglib==1.0.0',
	#       'svgwrite==1.4',
	#       'pandas==1.0.3',
	#   ],
	scripts=[
		'symal/symalscript',
	],
	long_description='a',
	dependency_links=['https://www.tbi.univie.ac.at/RNA/download/sourcecode/2_4_x/ViennaRNA-2.4.9.tar.gz'],
)
