import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monk_test1", # Replace with your own username
    version="0.0.1",
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
        'numpy',
        'scipy',
        'tqdm',
        'pillow',
        'opencv-python',
        'cython',
        'jupyter',
        'notebook',
        'pandas',
        'matplotlib',
        'xmltodict',
        'mxnet-cu90',
        'gluoncv',
    ],
    dependency_links=[
        'https://github.com/abhi-kumar/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI'
    ],
    python_requires='>=3.6'
)

