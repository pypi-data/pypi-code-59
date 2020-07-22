from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        name="requests-skip-verify",
        packages=find_packages("src"),
        package_dir={"": "src"},
        version="0.0.2",
        author="Tsuuko",
        description="Skip SSL verification for requests.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="MIT",
        classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent"],
    )
