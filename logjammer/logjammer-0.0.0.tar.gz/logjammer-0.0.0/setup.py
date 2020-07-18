import setuptools

setuptools.setup(
    name="logjammer",
    packages=setuptools.find_packages(),
    install_requires=[
        "bs4",
        "lxml",
    ],
    entry_points={"console_scripts": ["logjammer = logjammer.__main__:main"]},
)
