import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read()

setuptools.setup(
    name="grappl-node",
    version="0.1.0",
    author="jonirap",
    author_email="joni.rapoport@gmail.com",
    description="Writing nodes for the grappl framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tipshim/grappl-node",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8.2",
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        grappl_node=grappl_node.run.cli:execute_cli
    """,
)