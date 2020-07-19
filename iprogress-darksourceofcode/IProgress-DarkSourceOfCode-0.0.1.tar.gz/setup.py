import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IProgress-DarkSourceOfCode", # Replace with your own username
    version="0.0.1",
    author="Jayanta Banik",
    author_email="sciencenerd1609@gmail.com",
    description="Iprogress is an IPython shell progress checker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jayanta-banik/IProgress",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)