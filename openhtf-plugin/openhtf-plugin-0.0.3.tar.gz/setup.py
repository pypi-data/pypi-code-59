import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openhtf-plugin", 
    version="0.0.3",
    author="Kevin Pulley",
    author_email="kpulley@imaginecommunications.com",
    description="Simple Kiwi-TCMS plugin for OpenHTF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UndyingScroll",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
       "tcms-api"
   ],
    python_requires='>=3.6',
)
