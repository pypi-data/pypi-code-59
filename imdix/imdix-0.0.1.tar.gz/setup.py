import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

with open('requirements.txt') as f: 
    requirements = f.readlines() 

# This call to setup() does all the work
setup(
    name="imdix",
    version="0.0.1",
    description="Dynamic image resizing tool",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/amalshaji/imdix",
    author="Amal Shaji",
    author_email="amalshajid@tutanota.com",
    license="MIT",
    packages = find_packages(),
    entry_points = {
        'console_scripts': [ 
                'libgen = dynamix.main:main'
        ] 
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent", 
    ],
    include_package_data=True,
    install_requires=requirements,
    zip_safe = False
)
