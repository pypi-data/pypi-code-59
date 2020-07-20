import platform
from distutils.core import setup

deps = []
pkgs = ["DockerScout"]
if platform.system() == "Windows":
    deps.append("pywin32")
pkgs.append("DockerScout.win32service")

setup(
    name="dockerscout",
    version="0.0.3",
    description="Service to prevent unused docker images filling your disk",
    author="Ian Norton",
    author_email="inorton@gmail.com",
    url="https://gitlab.com/inorton/docker-scout",
    packages=pkgs,
    install_requires=deps,
    platforms=["any"],
    license="License :: OSI Approved :: MIT License",
    long_description="Service to prevent unused docker images filling your disk by monitoring docker container startup events"
)
