import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="powerfuldeveloper_base",  # Replace with your own username
    version="0.0.1",
    author="Hussein Mirzaki",
    author_email="husseinmirzaki@gmail.com",
    description="Basic Foundation of All created by him",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
)
