from distutils.core import setup

setup(
    name='drweizhang_testpy',
    version='0.1dev',
    packages=['src',],
    license='MIT',
    long_description=open('README.md').read(),
    url='https://github.com/wei-zhang-thz/exp',
    install_requires=[
        'numpy',
    ],
)