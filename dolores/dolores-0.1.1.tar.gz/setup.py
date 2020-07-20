import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
    name="dolores",
    version="0.1.1",
    author="Dolores Abernathy",
    author_email="malcolmcyber@gmail.com",
    description="A small prompt getter package to better achieve responses from the GPT-X models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mmnavarr/dolores",
    # download_url='https://pypi.org/project/dolores/'
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)