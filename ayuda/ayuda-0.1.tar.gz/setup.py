
import setuptools
from ayuda import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='ayuda',
    version=__version__,
    author="Rodrigo Ramos",
    author_email="rodrigohernan.ramos@gmail.com",
    description="Program for save your notes and share between git",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/rodrigohernan.ramos/ayuda",
    # for new version exec: git tag 0.1 -m "description" | git push --tags origin master
    download_url = 'https://gitlab.com/rodrigohernan.ramos/ayuda/tarball/{}'.format(__version__),
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'urwid',
        'PyYaml',
        'gitpython'
    ],
    entry_points='''
        [console_scripts]
        ayuda=ayuda.main:main
    ''',
    python_requires='>=3.6',
)