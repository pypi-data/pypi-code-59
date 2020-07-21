from setuptools import setup
def readme():
    with open('README.md','r') as f:
        README=f.read()
    return README
setup(
    name='English to Hindi',
    version='0.0.1',
    description='This module helps in converting English sentences to Hindi',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Anuj kumar',
    author_email='kumaranuj01596@gmail.com',
    license='MIT',
    packages=['eng_hindi'],
    include_package_data=True,
    install_requires=['requests'],
)










