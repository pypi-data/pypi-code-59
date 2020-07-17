import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lazyml", # Replace with your own username
    version="0.0.1",
    author="Navendu Pottekkat",
    author_email="navendupottekkat@gmail.com",
    description="Train and Test your data on multiple sklearn models!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/navendu-pottekkat/lazyml",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)