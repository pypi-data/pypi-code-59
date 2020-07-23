import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CANoe_Python",
    version="0.0.2",
    author="Claudiu Albu",
    author_email="claudiu.albu@hotmail.com",
    description="CANoe COM Interface Python API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/claudiualbu/CANoe_Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)