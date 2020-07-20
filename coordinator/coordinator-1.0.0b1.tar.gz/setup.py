import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coordinator",  # Replace with your own username
    version="1.0.0-beta.1",
    author="Joseph Geis",
    author_email="juniorrubyist@gmail.com",
    description="An experimental Python hook-based task runner.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juniorrubyist/coordinator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['huey', 'gevent'])
