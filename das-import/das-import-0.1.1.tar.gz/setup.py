import pathlib
from setuptools import find_packages, setup

ROOT_DIR = pathlib.Path(__file__).parent

setup(
    name="das-import",
    packages=find_packages(),
    include_package_data=True,
    version="0.1.1",
    description="Decks Against Society card importer",
    long_description=(ROOT_DIR / "README.md").read_text(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=("requests", "tqdm",),
    entry_points={"console_scripts": ["das-import = das_import.cli:main",],},
    author="Krzysztof Socha",
    author_email="github+das-import@ksocha.com",
    url="https://github.com/chaosk/das-import",
)
