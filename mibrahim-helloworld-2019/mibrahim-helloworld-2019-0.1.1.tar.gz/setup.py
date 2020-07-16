from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="mibrahim-helloworld-2019",
    version="0.1.1",
    description="Project template",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/RobertoPrevato/PythonTemplate",
    author="RobertoPrevato",
    author_email="roberto.prevato@gmail.com",
    keywords="template",
    license="MIT",
    packages=[
        "helloworld",
    ],
    install_requires=[],
    include_package_data=True,
)