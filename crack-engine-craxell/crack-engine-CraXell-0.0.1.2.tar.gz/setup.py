import setuptools
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crack-engine-CraXell", # Replace with your own username
    version="0.0.1.2",
    author="CraXell",
    author_email="craxell.tv@gmail.com",
    description="A package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CraXell/crack-engine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)