import os
from setuptools import setup, find_packages

from django_richtexteditor import __version__


def read_file(fname):
    try:
        with open(fname) as f:
            return f.read()
    except IOError:
            return ''


setup(
    name='django-richtexteditor',
    version=__version__,
    license='BSD 3-Clause',
    url='https://github.com/cizario/django-richtexteditor/',
    author='Nizar DELLELI',
    author_email='nizar.delleli@gmail.com',
    description='Django Rich Text Editor',
    long_description=read_file('README.rst'),
    long_description_content_type='text/x-rst',
    keywords='django richtext editor ckeditor tinymce markdown reStructruedText wysiwyg',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    project_urls={
        'Documentation': 'https://github.com/cizario/django-richtexteditor/',
        'Release notes': 'https://github.com/cizario/django-richtexteditor/',
        'Funding': 'https://github.com/cizario/django-richtexteditor/',
        'Source': 'https://github.com/cizario/django-richtexteditor/',
        'Tracker': 'https://github.com/cizario/django-richtexteditor/issues',
    },
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    # package_data={},
    # data_files=[],
    # py_modules=[],
    install_requires=[
        # 'Django>=2.0',
    ],
    python_requires='>=3.6',
)
