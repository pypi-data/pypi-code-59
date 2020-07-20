import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="prettysleeper",
    version="1.1.0",
    description="psleep; A sleep function with Emoji's. It shows a countdown, progress clock (switching emoji's), and my favorite, the Wizard.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/NamasteJasutin/wizprint",
    author="NamasteJasutin",
    author_email="justin.duijn@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent"
    ],
    packages=["prettysleeper"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "psleep=prettysleeper.console:main",
        ]
    },
)