from setuptools import setup, find_packages

setup(name="mess_srv",
      version="0.0.2",
      description="mess_srv",
      author="Sergey Semenov",
      author_email="evlx@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
