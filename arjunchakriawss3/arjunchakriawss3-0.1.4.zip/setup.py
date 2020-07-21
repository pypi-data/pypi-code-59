from setuptools import setup

setup(
    name = 'arjunchakriawss3',
    version = '0.1.4',
    packages = ['arjunchakriawss3'],
    entry_points = {
        'console_scripts': [
            'arjunchakriawss3 = arjunchakriawss3.__main__:main'
        ]
    },
    install_requires = [
        'boto3',
        'requests'
    ]
)