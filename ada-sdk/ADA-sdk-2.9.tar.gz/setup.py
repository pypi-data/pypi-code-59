from setuptools import setup, find_packages

setup(
    name='ADA-sdk',
    version='2.9',
    packages=find_packages(),
    description='Python SDK for Automation data analytics API',
    include_package_data=True,
    install_requires=[
        'requests',
    ]
)
