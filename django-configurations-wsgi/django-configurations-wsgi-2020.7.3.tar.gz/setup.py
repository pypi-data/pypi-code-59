import setuptools

setuptools.setup(
    name='django-configurations-wsgi',
    version='2020.7.3',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
