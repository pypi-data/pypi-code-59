import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graphalgorithmplayer",
    version="0.1.0",
    author="Edwige Gros",
    author_email="edwige.gros@laposte.net",
    description="A Player to display graph processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.u-psud.fr/edwige.gros/GraphAlgorithmPlayer/tree/master/GraphAlgorithmPlayer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["timer", "ipywidgets","valueplayerwidget","networkx","traitlets", "bqplot", "matplotlib"],
    python_requires=">=3.6",
)
