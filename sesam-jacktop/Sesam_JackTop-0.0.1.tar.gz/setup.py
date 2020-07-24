from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Sesam_JackTop',
    version='0.0.1',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    license='MIT',
    author='abinpulivelil',
    author_email='abinpulivelil@gmail.com',
    description='Sesam Software Jacket and Topside Helper Tools',
    classifiers=classifiers,
    keywords='Sesam GeniE',
    packages=find_packages(),
    install_requires=['']
)