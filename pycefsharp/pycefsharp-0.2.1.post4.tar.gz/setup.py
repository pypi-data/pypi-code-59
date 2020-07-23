#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore
from pycefsharp import __version__

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="eseunghwan",
    author_email="shlee0920@naver.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Win32 (MS Windows)",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="python binding for CefSharp",
    entry_points={"console_scripts": ["pycefsharp=pycefsharp.cli:main",],},
    install_requires=open("requirements.txt", "r", encoding = "utf-8").readlines(),
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={
        "": [
            "*.dll",
            "*.pak",
            "*.exe",
            "*.dat",
            "*.bin",
            "*.ico"
        ]
    },
    include_package_data=True,
    keywords=["pythonnet", "cef"],
    name="pycefsharp",
    packages=["pycefsharp", "pycefsharp/cefsharp", "pycefsharp/cefsharp/locales", "pycefsharp/cefsharp/swiftshader"],
    setup_requires=[],
    url="https://github.com/eseunghwan/pycefsharp",
    version=__version__,
    zip_safe=False,
)
