import setuptools


setuptools.setup(
    name="statechartx",
    version="0.0.2",
    author="Panu P",
    author_email="panuph@gmail.com",
    description="A trivial extension to Python UML statechart framework",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/panuph/statechartx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"],
    install_requires=[
    ],
    zip_safe=False
)
