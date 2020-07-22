from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name        = "sqlflex",
    version     = "0.0.2",
    description = "Extract Hardcoded Value's and the related Column Names from the SQL Query",
    py_modules  = ["sql_flex"],
    package_dir = {"":"src"}, 
    install_requires=[
        'pandas',
    ],
    extras_require = {
        "dev": [
            "pandas",
        ]
    },
    author='shashishekhar',
    author_email='shashishekhar1001@gmail.com',
    url='https://github.com/shashishekhar1001/flex_sql',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    ]
)