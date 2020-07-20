import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opendt", # Replace with your own username
    version="1.0",
    author="BAYANGMBE MOUNMO",
    author_email="bayangp0@gmail.com",
    description="Librairy to make a data augmmentation using tensorflow2.x and python3.x",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bm777/Data_augmentation",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)