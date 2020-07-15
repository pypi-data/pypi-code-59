import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpeg_octree_mt", # Replace with your own username
    version="0.0.1",
    author="Diego Miranda",
    author_email="dmiranda@ufpa.br",
    description="SimPeg package with modification to incorporate octree meshes with MT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(exclude=['tests*']),
    install_requires=[
        'numpy>=1.7',
        'scipy>=0.13',
        'pymatsolver>=0.1.1',
        'matplotlib',
        'properties>=0.5.2',
        'vectormath>=0.2.0',
        'discretize>=0.4.0',
        'geoana>=0.0.4'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
