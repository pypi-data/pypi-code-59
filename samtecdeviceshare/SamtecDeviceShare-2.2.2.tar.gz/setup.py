import sys
import io
import re
from setuptools import setup

with io.open("samtecdeviceshare/__init__.py", "rt", encoding="utf8") as fp:
    version = re.search(r'__version__ = "(.*?)"', fp.read()).group(1)
    (major_version, minor_version, revision) = version.split('.')

requirements = ['aiohttp', 'fastapi', 'lockfile', 'pydantic', 'pyhumps', 'uvicorn']

if 'linux' in sys.platform:
    requirements += ['python-networkmanager', 'dbus-python']

short_description = 'Handles a variety of common routines for SDC-based applications.'

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name='SamtecDeviceShare',
    version=version,
    install_requires=requirements,
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer='Samtec - ASH',
    maintainer_email='samtec-ash@samtec.com',
    packages=['samtecdeviceshare'],
    license='MIT',
    platforms="Linux"
)
