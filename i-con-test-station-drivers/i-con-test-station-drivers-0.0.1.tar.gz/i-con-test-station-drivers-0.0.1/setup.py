import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="i-con-test-station-drivers",
    version="0.0.1",
    author="Gabriel Bornstein",
    author_email="Gabe.Bornstein@i-con.com",
    description="Hardware drivers for testing stations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://i-con.visualstudio.com/Libraries/_git/drivers-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
