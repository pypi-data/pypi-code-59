from setuptools import setup, find_packages

setup(
    name='accubits',
    version='0.1',
    package=find_packages(),
    include_package_data=True,
    license='MIT',
    download_url='https://github.com/accubits-tech/accubits-cli/archive/0.1.tar.gz',
    author = 'Nithi',
    author_email = 'bearnithi@gmail.com',
    keywords = ['Accubits Cli', 'Front end boilerplates', 'angular boilerplate'],
    install_requires=[
        'Click',
        'gitpython'
    ],
    entry_points='''
        [console_scripts]
        accubits=accubitscli.scripts.accubits:cli
    ''',
)