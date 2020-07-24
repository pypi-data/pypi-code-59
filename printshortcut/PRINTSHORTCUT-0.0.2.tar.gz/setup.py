import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PRINTSHORTCUT", # Replace with your own username
    version='0.0.2',
    author="KESHARI NANDANA PRATAP",
    author_email='kesharipratap52@gmail.com',
    description="Print and input shortcut",
    long_description=open('README.MD').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type="text/markdown",
    url="https://knpjg.blogspot.com/2020/07/my-own-python-shortcutio-libiary.html",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)