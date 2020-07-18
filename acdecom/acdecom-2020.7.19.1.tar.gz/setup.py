import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acdecom", # Replace with your own username
    version="2020.07.19.1",
    author="Stefan Sack, Royal Institute of Technology, Stockholm, Sweden",
    author_email="ssack@kth.se",
    description="A python module for acoustic wave decomposition",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src'},
    py_modules=["acdecom"],
    python_requires='>=3.7',
    install_requires=['numpy','scipy']
)