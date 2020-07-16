import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='caperea-server',
    version='0.1.0.dev1',
    description='Library management platform.',
    long_description=README,
    long_description_content_type='text/x-rst',
    packages=find_packages(include=['caperea.*']),
    include_package_data=True,
    author='Pascal Pepe',
    author_email='contact@pascalpepe.fr',
    url='https://caperea.pascalpepe.com',
    project_urls={
        'Documentation': 'https://pascalpepe.gitlab.io/caperea-server',
        'Source code': 'https://gitlab.com/pascalpepe/caperea-server',
        'Issue tracker': 'https://gitlab.com/pascalpepe/caperea-server/issues',
    },
    license='AGPL-3.0-only',
    keywords='django caperea',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
