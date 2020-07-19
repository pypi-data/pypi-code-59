import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='syzygy-docs-themes',
    version='0.1.0.dev1',
    description='Sphinx themes for the documentation of Kogia, Caperea and Stenella.',
    long_description=README,
    long_description_content_type='text/x-rst',
    entry_points = {
        'sphinx.html_themes': [
            'caperea = syzygy_docs_themes.caperea',
            'kogia = syzygy_docs_themes.kogia',
            'stenella = syzygy_docs_themes.stenella',
            'syzygy = syzygy_docs_themes.syzygy',
        ]
    },
    packages=find_packages(include=['syzygy_docs_themes']),
    include_package_data=True,
    author='Pascal Pepe',
    author_email='contact@pascalpepe.fr',
    url='https://pascalpepe.gitlab.io/syzygy-docs-themes',
    project_urls={
        'Documentation': 'https://pascalpepe.gitlab.io/syzygy-docs-themes',
        'Source code': 'https://gitlab.com/pascalpepe/syzygy-docs-themes',
        'Issue tracker': 'https://gitlab.com/pascalpepe/syzygy-docs-themes/issues',
    },
    license='Apache-2.0',
    keywords='sphinx docs theme kogia caperea stenella',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development',
        'Topic :: Software Development :: Documentation',
    ]
)
