from setuptools import setup, find_packages
from mdocspoofer import __version__

setup(
    name='mdocspoofer',
    version=f'{__version__}',
    license='BSD 3-Clause License',
    description='Spoof SerialEM mdoc files from a directory of multi-frame micrographs created in Tomo5',
    author='Alister Burt',
    author_email='alisterburt@gmail.com',
    url='https://github.com/alisterburt/mdocspoofer',
    download_url=f'https://github.com/alisterburt/mdocspoofer/archive/v{__version__}.tar.gz',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click~=7.1.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points="""
    [console_scripts]
    mdocspoofer=mdocspoofer.mdoc:cli
    """
)
