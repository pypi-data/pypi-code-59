try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = [
    "atc_uiautomator>=0.7",
]

setup(
    name='auto_runner',
    version='1.6',
    url='',
    license='',
    author='thomas.ning',
    author_email='',
    description='',
    packages=['auto_runner'],
    include_package_data=True,
    zip_safe=False
)