"""
Flask-Query
-------------

通过对象创建sql语句
"""
from setuptools import setup

setup(
    name='Flask-Query',
    version='0.0.1',
    url='https://github.com/huangdingbo/flask-query',
    license='BSD',
    author='Billy J. Hee',
    author_email='378969398@qq.com',
    description='通过对象创建sql语句',
    long_description=__doc__,
    packages=['flask_query'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask', 'pymysql', 'DBUtils'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
