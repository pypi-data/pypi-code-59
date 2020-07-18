import pathlib
import setuptools
from distutils.core import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='pytodd',
    packages=['pytodd'],
    version='0.1.3',
    license='MIT',
    description='Python port of todd project for Google Drive IO.',
    author='Siddhant Kushwaha',
    author_email='k16.siddhant@gmail.com',
    url='https://github.com/siddhantkushwaha/pytodd',
    download_url='https://github.com/siddhantkushwaha/pytodd/archive/0.1.3.tar.gz',
    keywords=['GOOGLE DRIVE', 'STORAGE', 'DOWNLOAD'],
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True
)
