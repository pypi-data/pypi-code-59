from distutils.core import setup

setup(
    name="dockerscout",
    version="0.0.1",
    description="Service to prevent unused docker images filling your disk",
    author="Ian Norton",
    author_email="inorton@gmail.com",
    url="https://gitlab.com/inorton/docker-scout",
    packages=["DockerScout"],
    platforms=["any"],
    license="License :: OSI Approved :: MIT License",
    long_description="Service to prevent unused docker images filling your disk by monitoring docker container startup events"
)
