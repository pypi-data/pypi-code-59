import setuptools


with open("Documentation.rst") as f:
    description = f.read()

setuptools.setup(
    author="Jash Shah",
    author_email="shahjash271@gmail.com",
    name="shortenIt",
    license="MIT",
    description=f"Package for summarizing Text ",
    version="v0.0.3",
    long_description=description,
    url="https://github.com/Jash271/SummarizeIt",
    packages=setuptools.find_packages(),
    python_requires=">=3.6.8",
    install_requires=[
     "nltk"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
    include_package_data=True,
)
