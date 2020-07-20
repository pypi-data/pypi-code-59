import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='R0State',  
     version='0.3',
     author="Lukas Merkle",
     author_email="lukas.merkle@tum.de",
     description="Returning interpolated R0_BOL",
     long_description=long_description,
   		long_description_content_type="text/markdown",
     url="https://github.com/___empty/___empty",
     packages=setuptools.find_packages(),
     package_data={'R0State': ['data/Means_BOL_ICD1_ICD2.csv']},
     include_package_data=True,
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