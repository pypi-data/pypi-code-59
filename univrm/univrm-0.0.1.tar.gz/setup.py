import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="univrm", # Replace with your own username
    version="0.0.1",
    author="Icelain",
    author_email="xerneas965@gmail.com",
    description="A very minimal script packaged as a cli which can both files and directories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    entry_points ={ 
            'console_scripts': [ 
                'univrm = univrm_main.univrm:main'
            ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.2',
)
