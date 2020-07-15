from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="calcibj",
    version="1.0.0",
    description="A Python calci",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="",
    author="Abhinav Jain",
    author_email="jain.abhinav14@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
   
)