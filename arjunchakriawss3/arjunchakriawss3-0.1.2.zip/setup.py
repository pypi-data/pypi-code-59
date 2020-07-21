from setuptools import setup


try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

setup(
    name = 'arjunchakriawss3',
    version = '0.1.2',
    packages = ['arjunchakriawss3'],
    entry_points = {
        'console_scripts': [
            'arjunchakriawss3 = arjunchakriawss3.__main__:main'
        ]
    },
    install_requires=load_requirements("requirements.txt")
)