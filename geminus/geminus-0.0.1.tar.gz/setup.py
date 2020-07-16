import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geminus",
    version="0.0.1",
    author="Geminus.ai, Inc",
    author_email="info@geminus.ai",
    description="Geminus platform client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Geminus-AI/geminus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.18.0',
        'pandas>=1.0.0',
        'xlrd>=1.2.0',
        'scipy>=1.1.0',
    ]
)
