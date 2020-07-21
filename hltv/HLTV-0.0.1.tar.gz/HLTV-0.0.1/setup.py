from setuptools import setup

setup(
    name="HLTV",
    version="0.0.1",
    description="A package to extract info from HLTV.org to use in your python code",
	py_modules=["urllib",  "datetime", "bs4"],
	package_dir={'': 'src'},
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)