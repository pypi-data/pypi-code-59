import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nodescape",
    version="0.0.1.15",
    author="Michael E. Vinyard",
    author_email="vinyard@g.harvard.edu",
    description="nodescape package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mvinyard/nodescape",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
