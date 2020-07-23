from setuptools import find_packages
from setuptools import setup

setup(
    name="lung",
    version="0.0.1",
    author="MinRegret",
    author_email="minregret@minimizingregret.com",
    url="https://github.com/MinRegret/Ventilator-Dev",
    description="Lung simulation",
    install_requires=[
        "numpy",
        "pandas",
        "h5py"
    ],
    packages=find_packages()
)
