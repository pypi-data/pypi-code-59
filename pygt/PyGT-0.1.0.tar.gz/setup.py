import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyGT", # Replace with your own username
    version="0.1.0",
    author="TD Swinburne",
    author_email="swinburne@cinam.univ-mrs.fr",
    description="Python implementation of graph transformation techniques to analyze metastable Markov chains",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomswinburne/PyGT",
    packages=setuptools.find_packages(),
    install_requires=['scipy','numpy','matplotlib','tqdm','pathos'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
