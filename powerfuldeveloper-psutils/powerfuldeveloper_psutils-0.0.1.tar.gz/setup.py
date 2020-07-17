import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="powerfuldeveloper_psutils",  # Replace with your own username
    install_requires=[
        "powerfuldeveloper_base",
    ],
    version="0.0.1",
    author="Hussein Mirzaki",
    author_email="husseinmirzaki@gmail.com",
    description="You can use this to control command line based stuff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
)
