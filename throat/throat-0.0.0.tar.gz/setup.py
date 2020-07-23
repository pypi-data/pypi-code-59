import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="throat",  # Replace with your own username
    version="0.0.0",
    author="Phuks LLC",
    author_email="admin@phuks.co",
    description="Open source link aggregator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Phuks-co/throat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Flask",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
