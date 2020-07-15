import setuptools
import os
from ATPLibrary.version import __VERSION__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ATPLibrary",
    version=__VERSION__,
    license="MIT",
    author="Wayne Vera",
    author_email="wayne.vera@expleogroup.com",
    description="Robotframework ATP Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://sqsglobal.visualstudio.com/ATP/_git/ATP.RobotFramework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Robot Framework",
        "Framework :: Robot Framework :: Library",
        "Natural Language :: English",
        "Topic :: Software Development :: Testing"
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2',
        'robotframework>=3'
    ],
    setup_requires=[
        'setupext-gitversion'
    ],
    package_data={
        "": ["KeyMappings.xml"]
    }
)