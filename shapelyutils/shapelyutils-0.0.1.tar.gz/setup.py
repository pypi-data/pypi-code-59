import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shapelyutils",
    version="0.0.1",
    author="Mikko Virkkilä",
    author_email="mikko.virkkila@steerpath.com",
    description="Utilities to make life with shapely easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.com/steerpath/shapelyutils-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
)
