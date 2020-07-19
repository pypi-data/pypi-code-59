from setuptools import setup
from setuptools import find_packages


def get_package_attribute(name):
    """Retrieve package attributes from the package itself."""
    with open("darwin/__init__.py") as init_file:
        for line in init_file:
            if line.startswith(name):
                return eval(line.split("=")[-1])


def get_readme():
    """Return the contents of the README.md file."""
    with open("README.md") as readme_file:
        return readme_file.read()


setup(
    name=get_package_attribute('__title__'),
    version=get_package_attribute('__version__'),
    description="Python package providing an API to Darwin, an online database for German Shepherds owned and maintained by the VDH.",
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    author=get_package_attribute('__author__'),
    author_email=get_package_attribute('__email__'),
    license=get_package_attribute('__license__'),
    url="https://github.com/roaldnefs/python-darwin",
    packages=find_packages(),
    install_requires=["lxml>=4.5.2", "requests>=2.24.0"],
    python_requires=">=3.6.0",
    entry_points={"console_scripts": ["darwin = darwin.cli:main"]},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8", 
    ],
    extra_require={},
)

