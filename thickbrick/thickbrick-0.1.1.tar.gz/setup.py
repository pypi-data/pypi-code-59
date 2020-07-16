import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="thickbrick",
	version="0.1.1",
	author="Prasanth Shyamsundar",
	author_email="prasanth.s.cmi@gmail.com",
	description="A data analysis package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://prasanthcakewalk.gitlab.io/thickbrick",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		'Development Status :: 3 - Alpha',
	],
	python_requires='>=3.6',
	license='MIT',
	keywords="thick brick taab autocategorizer",
	platforms=['any'],
	install_requires=['numpy']
)
