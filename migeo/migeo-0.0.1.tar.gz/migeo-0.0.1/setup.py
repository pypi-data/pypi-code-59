import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="migeo", # Replace with your own username
    version="v0.0.1",
    author="Projeto EM UFPA/Petrobrás",
    author_email="isadora.s.macedo@gmail.com",
    description="Modelagem e inversão eletromagnética por volumes finitos: MT e MCSEM.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/projetoemBR/migeo-master",
    download_url="https://github.com/projetoemBR/migeo-master/archive/v0.0.1.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    install_requires=[
        "numpy>=1.7",
        "scipy>=1.4.0",
        "pymatsolver>=0.1.1",
        "matplotlib",
        "properties>=0.5.2",
        "vectormath>=0.2.0",
        "discretize>=0.4.0",
        "geoana>=0.0.4",
        "empymod>=2.0.0",
        "pandas",
        "numba>=0.45.0",
        "pyvista",
    ],

    python_requires='>=3.7',
)

