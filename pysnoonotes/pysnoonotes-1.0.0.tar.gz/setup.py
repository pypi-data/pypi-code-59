import setuptools

with open("README.md", "r") as readme:
    description = readme.read()

setuptools.setup(
    name="pysnoonotes",
    version="1.0.0",
    author="mmshivesh",
    author_email="mmshivesh@gmail.com",
    description="A Python wrapper for the Snoonotes API",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/mmshivesh/pysnoonotes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
