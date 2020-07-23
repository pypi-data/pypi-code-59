from setuptools import setup, find_packages

def read_file(fname):
    try:
        with open(fname) as f:
            return f.read()
    except IOError:
            return ''


setup(
    name='sphinx-django-theme',
    version='0.0.1.dev0',
    license='BSD 3-Clause',
    description='sphinx theme for django projects',
    long_description=read_file('README.rst'),
    long_description_content_type='text/x-rst',
    author='Nizar DELLELI',
    author_email='nizar.delleli@gmail.com',
    # maintainer='',
    # maintainer_email='',
    keywords='sphinx django theme',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
    ],
    url='https://github.com/cizario/sphinx-django-theme/',
    download_url='https://github.com/cizario/sphinx-django-theme/',
    project_urls={
        'Tracker': 'https://github.com/cizario/sphinx-django-theme/issues',
        'Source': 'https://github.com/cizario/sphinx-django-theme/',
        # 'Funding': 'https://patreon.com/cizario',
        # 'Say Thanks!': 'http://saythanks.io/to/cizario',
        'Release notes': 'https://github.com/cizario/sphinx-django-theme/releases',
        'Documentation': 'https://sphinx-django-theme.readthedocs.io/en/latest/',
    },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=[],
)
