import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="barbareeka-engine-python",
    version="0.0.95",
    author="Nishant Sharma",
    author_email="thenishant3@gmail.com",
    description="barbareeka-client for optimusCloud reporting engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/testvagrant/optimus-pleiades/optimus-cloud/barbareeka-engine-python",
    packages=setuptools.find_packages(),
    include_package_data=True,
    # install_requires=["polling", "retrying", "requests", "pika", "atomos", "selenium", "Appium-Python-Client"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
