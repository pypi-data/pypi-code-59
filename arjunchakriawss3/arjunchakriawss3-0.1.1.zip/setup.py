from setuptools import setup
setup(
    name = 'arjunchakriawss3',
    version = '0.1.1',
    packages = ['arjunchakriawss3'],
    entry_points = {
        'console_scripts': [
            'arjunchakriawss3 = arjunchakriawss3.__main__:main'
        ]
    }
)