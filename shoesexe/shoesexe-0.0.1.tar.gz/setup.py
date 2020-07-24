from setuptools import find_packages, setup


DESCRIPTION = "Running shoes."

try:
    with open("README.md") as doc_md:
        LONG_DESCRIPTION = doc_md.read()
    LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
except Exception:
    LONG_DESCRIPTION = None
    LONG_DESCRIPTION_CONTENT_TYPE = None


setup(
    name='shoesexe',
    version='0.0.1',
    author='Kfir Nissim',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    install_requires=[],
    packages=find_packages()
)
