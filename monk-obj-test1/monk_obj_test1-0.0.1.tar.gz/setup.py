import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monk_obj_test1", # Replace with your own username
    version="0.0.1",
    author="Tessellate Imaging",
    author_email="abhishek@tessellateimaging.com",
    description="Monk Object Detection's 1_gluoncv_finetune",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tessellate-Imaging/Monk_Object_Detection",
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

