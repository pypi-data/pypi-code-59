import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="otest-oriont",
    version="0.0.2",
    author="Elijah Tarr",
    author_email="elijahotarr@gmail.com",
    description="A simple package to manage assertions well",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eoriont/otest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
