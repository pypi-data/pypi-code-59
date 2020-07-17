import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monk_obj_test2", # Replace with your own username
    version="0.0.11",
    author="Tessellate Imaging",
    author_email="abhishek@tessellateimaging.com",
    description="Monk Object Detection's 2_pytorch_finetune",
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
        'torchvision==0.5.0',
        'torch==1.4.0',
        'pycocotools'
    ],
    python_requires='>=3.6',

)

