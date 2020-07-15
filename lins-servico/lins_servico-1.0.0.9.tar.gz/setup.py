from distutils.core import setup
from setuptools import find_packages

def get_version():
    return open('version.txt', 'r').read().strip()

setup(
    name='lins_servico',
    description='Pacote para gerenciar serviços através de threads',
    version=get_version(),
    packages=find_packages(),
    url='https://bitbucket.org/grupolinsferrao/pypck-servico/',
    author='Gustavo Schaedler',
    author_email='gustavopoa@gmail.com',
    license='MIT',
)