from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="Royal-Cashews",
    version="1.0.0",
    description="This is a shop managing package",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/jesvinvijesh/MSJ_Royal_Cashews",
    author="Jesvin Vijesh",
    author_email="msjjesvin@gmail.com",
    license="MIT",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    packages=["Retail_Management","Retail_Management.migrations"],
    include_package_data=True,
)