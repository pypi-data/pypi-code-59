import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moma", 
    version="0.0.0",
    author="Bo Zhang",
    author_email="zhangbo11@xiaomi.com",
    description="moma",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xiaomi-automl/moma",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
