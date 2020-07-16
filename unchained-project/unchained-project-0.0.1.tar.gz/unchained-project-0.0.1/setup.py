import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unchained-project",
    version="0.0.1",
    author="Vitalii Abetkin",
    author_email="abvit89@gmail.com",
    description="django async",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.8',
)