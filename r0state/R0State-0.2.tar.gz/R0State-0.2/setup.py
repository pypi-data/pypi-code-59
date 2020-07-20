import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='R0State',  
     version='0.2',
     author="Lukas Merkle",
     author_email="lukas.merkle@tum.de",
     description="Returning interpolated R0_BOL",
     long_description=long_description,
   		long_description_content_type="text/markdown",
     url="https://github.com/___empty/___empty",
     packages=setuptools.find_packages(),
     # package_data={'dt_access': ['.aws_api_key.txt']},
     # include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=[
     "pandas",
     "numpy"
		]
 )