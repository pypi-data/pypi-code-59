from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='Python-PDF-Extractor',
    version='0.0.1',
    author="James Crone",
    author_email="jmcrone98@gmail.com",
    description='PDF text extractor',
    py_modules=["PDF_Extractor"],
    package_dir={'PDF_Text_Extractor': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.7',
)
