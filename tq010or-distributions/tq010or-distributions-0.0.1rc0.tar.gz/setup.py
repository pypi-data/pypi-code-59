from setuptools import setup, find_packages

with open("README.md") as fr:
    long_description = fr.read()

with open("requirements.txt") as fr:
    install_requires = list(map(lambda x: x.strip(), fr.readlines()))

setup(
    name="tq010or-distributions",
    author="Bo HAN",
    author_email="bohan.academic@gmail.com",
    version="0.0.1rc0",
    description="This is a package for common distributions, e.g. Gaussian, Binomial",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/tq010or/distributions",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)
