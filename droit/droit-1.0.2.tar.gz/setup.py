from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='droit',
	version='1.0.2',
	description='Simple library for creating bots',
	long_description=long_description,
    long_description_content_type="text/markdown",
	url='https://github.com/jarinox/python-droit',
	author='Jakob Stolze',
	author_email='jarinox@wolke7.de',
	license='LGPLv2.1',
	packages=['droit', 'droit.io'],
	install_requires=['parse'],
	include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
	zip_safe=False
)
