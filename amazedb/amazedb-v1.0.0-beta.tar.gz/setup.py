from distutils.core import setup

setup(
    name='amazedb',
    packages=['amazedb'],
    version='v1.0.0-beta',
    license='MIT',
    description='This is a light-weight, NoSQL, file-based database managemet system',
    long_description='# amazedb\n It is a file based NoSQL database management system written in python.\n \n All the databases are stored in the ```db``` sub-directory of the current directory. This behaviour can be manipulated as we\'ll see later on.\n\n## Using the database\n\n The database can simply be used by cloning the project in a directory you may call ```amazedb``` and then create another directory named ```db``` in your projects root. Then import the main file as:\n\n```python\nfrom amazedb import dbms as db\n```\n\nThis will create the namespace ```db``` in your file.\n\n## Creating and accessing databases\n\n Now that you have imported the dbms, you can access a database with the following code:\n\n```python\nmydb = db.db(\'mydb\')\n```\n\nThis will try to locate the ```./db``` directory relative to the file you are working on. To locate a different directory, you can use:\n\n```python\nmydb = db.db(\'mydb\', dbPath="D:/project")\n```\n\nIn this case, it will look for ```D:/project/db``` directory. \n\nNow, what next? The project will see if the *mydb* databae exists in that directory. If it exists, well and good otherwise it will be created by default. To override this behaviour, simply use:\n\n```python\nmydb = db.db(\'mydb\', safeMode=False)\n```\n\nIn this case, an exception will be raised if the database is not found.\n\n*This page is still incomplete. We\'re working on it*\n',
    long_description_content_type="text/markdown",
    author='Jalaj Kumar',
    author_email='axiom.jalaj.28@gmail.com',
    url='https://github.com/jalaj-k/amazedb',
    download_url='https://github.com/jalaj-k/amazedb/archive/v1.0.0-beta.tar.gz',
    keywords=['database', 'nosql', 'dbms'],
    install_requires=[
        'cryptography',
        'colorama',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)