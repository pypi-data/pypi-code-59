import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SyncAsyncRetry",
    version="1.0.0",
    author="Antas",
    author_email="",
    description="Retry decorator for both synchronous and asynchronous functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/monk-after-90s/SyncAsyncRetry.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
