from setuptools import setup

setup(
    name="realdebrid",
    version="0.0.2",
    description="RealDebrid REST API library",
    url="https://github.com/xwhiz/realdebrid",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    packages=["realdebrid"],
    include_package_data=True,
    install_requires=["requests"],
)