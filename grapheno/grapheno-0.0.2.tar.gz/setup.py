import setuptools

setuptools.setup(
    name="grapheno", # Replace with your own username
    version="0.0.2",
    license="MIT",
    author="Erik Burlingame",
    author_email="erik.burlingame@gmail.com",
    description="GPU-boosted PhenoGraph for fast single-cell phenotyping",
    url="https://gitlab.com/eburling/grapheno",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'rapids==0.14.0',
        'cupy==7.2.0'
    ]
)