import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="valknut",
    version="0.0.2",
    author="Meyer Daniel",
    author_email="meyer.daniel67@protonmail.com",
    description="markdown to GSS converter, SQLite3 management system and Micro WSGI Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daniel67-py/Valknut_Project",
    packages=setuptools.find_packages(),
    scripts = ["valknut/valknut.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
