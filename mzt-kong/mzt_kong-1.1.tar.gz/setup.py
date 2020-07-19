from setuptools import setup, find_packages

setup(
    name='mzt_kong',
    version="1.1",
    packages=find_packages(),
    install_requires=[
        'mzt_http_utils'
    ]
)
