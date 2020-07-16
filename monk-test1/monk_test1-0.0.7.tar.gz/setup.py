import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monk_test1", # Replace with your own username
    version="0.0.7",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: GPU :: NVIDIA CUDA :: 9.0",
    ],
    install_requires=[
        'requests',
        'numpy==1.19.0'
    ],
    python_requires='>=3.6'
)

