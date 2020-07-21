from setuptools import setup, find_packages


setup(
    name='wsgitoolbox',
    author='Hakim Rachidi',
    author_email='hakimrachidi02@gmail.com',
    version='0.0.1',
    description='Toolbox for python web development',
    install_requires=[
        'werkzeug>=0.16.0'
    ],
    packages=find_packages()
)