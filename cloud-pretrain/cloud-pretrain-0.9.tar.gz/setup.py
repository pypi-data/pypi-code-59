from setuptools import setup, find_packages
from cloudpretrain import __version__

setup(
    name='cloud-pretrain',
    version=__version__,
    packages=find_packages(exclude=("bert", "cloudpretrain-server")),
    install_requires=[
        'Click==7.0',
        "galaxy-fds-sdk==1.3.9",
        "six>=1.12.0",
        "ansicolors==1.1.8",
        "cloud-ml-sdk>=0.4.4",
        "tabulate==0.8.5",
        "tqdm"
    ],
    entry_points='''
        [console_scripts]
        cloud-pretrain=cloudpretrain.cli:cli
        cptcli=cloudpretrain.cli:cli
    ''',
)