import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="vintools", # Replace with your own username
    version="0.0.0.5",
    author="Michael Edward Vinyard",
    author_email="vinyard@g.harvard.edu",
    description="general personal utils",
    long_description="This package contains various functions used often by MEV.",
    long_description_content_type="text/markdown",
    url="https://github.com/mvinyard/mev-utils/vintools",
    packages=setuptools.find_packages(),
    py_modules=['_update_manager'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
