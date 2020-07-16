import time
from typing import Tuple
import setuptools


_GITLAB_ADDR: str = "https://gitlab.com/pepoluan/pretf_helpers"
_SEMVER: Tuple[int, int, int] = (0, 2, 8)


def _derive_version() -> str:
    verstr: str = ".".join(map(str, _SEMVER))
    if _SEMVER[-1] & 1:
        verstr += "+"
        verstr += time.strftime("%Y%m%d%H%M")
    return verstr


with open("README.md", "r") as fin:
    long_description = fin.read()

setuptools.setup(
    name="pretf_helpers",
    version=_derive_version(),
    author="Pandu POLUAN",
    author_email="pepoluan@gmail.com",

    description="Helper functions and classes for the pretf package",
    keywords="terraform pretf provisioning cloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Systems Administration",
    ],

    url=_GITLAB_ADDR,
    project_urls={
        "Bug Tracker": f"{_GITLAB_ADDR}/-/issues",
        "Source Code": f"{_GITLAB_ADDR}/-/tree/master",
        "Documentation": f"{_GITLAB_ADDR}/-/wikis/home",
    },

    packages=setuptools.find_packages(),
    zip_safe=True,
    python_requires='>=3.6',
    install_requires=[
        "pretf", "pretf.aws", "configparser", "ruamel.yaml",
    ],
)
