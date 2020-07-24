from distutils.core import setup

setup(
    name='django-auditlog-py3',
    version='1.0.1',
    packages=['auditlog', 'auditlog.migrations', 'auditlog.management', 'auditlog.management.commands'],
    package_dir={'': 'src'},
    url='https://github.com/crgross10/django-auditlog-py3',
    license='MIT',
    author='cristiano-gross',
    description='Audit log app for Django',
    install_requires=[
        'django-jsonfield>=1.0.0',
        'python-dateutil==2.6.0'
    ],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],        
)
