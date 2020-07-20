import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pastures", # Replace with your own username
    version="2.2.0",
    author="William Stella",
    author_email="william.a.stella@gmail.com",
    description="A small data structures library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wastella/Pasture",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
