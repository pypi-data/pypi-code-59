from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vidlist',
    version='0.0.4',
    author="Sharad Raj Singh Maurya",
    author_email="iamsharadraj@gmail.com",
    url="https://github.com/sharadcodes/vidlist",
    description='A python utility for generating a listing of all the videos in the subfolders so that you can watch them in browser',
    long_description_content_type="text/markdown",
    long_description=long_description,
    py_modules=['vidlist'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    entry_points={ "console_scripts": ['vidlist=vidlist:main'] }
)
