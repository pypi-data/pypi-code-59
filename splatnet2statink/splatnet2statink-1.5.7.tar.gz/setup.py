from __future__ import print_function

import distutils.spawn
import shlex
import subprocess
import sys

import setuptools


version = "1.5.7"


if sys.argv[1] == "release":
    if not distutils.spawn.find_executable("twine"):
        print(
            "Please install twine:\n\n\tpip install twine\n", file=sys.stderr
        )
        sys.exit(1)

    commands = [
        "git pull origin master",
        "git tag v{:s}".format(version),
        "git push origin master --tag",
        "python setup.py sdist",
        "twine upload dist/splatnet2statink-{:s}.tar.gz".format(version),
    ]
    for cmd in commands:
        subprocess.check_call(shlex.split(cmd))
    sys.exit(0)


def get_long_description():
    with open("README.md") as f:
        long_description = f.read()


def get_install_requires():
    install_requires = []
    with open("requirements.txt") as f:
        return [req.strip() for req in f]


def main():
    setuptools.setup(
        name="splatnet2statink",
        version=version,
        python_version=">=3.5",
        packages=setuptools.find_packages(),
        install_requires=get_install_requires(),
        description="Upload battle data from to stat.ink from SplatNet2",
        long_description=get_long_description(),
        long_description_content_type="text/markdown",
        author="frozenpandaman",
        url="http://github.com/wkentaro/splatnet2statink",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3 :: Only",
        ],
        entry_points={
            "console_scripts": [
                "splatnet2statink=splatnet2statink.__main__:main"
            ]
        },
    )


if __name__ == "__main__":
    main()
