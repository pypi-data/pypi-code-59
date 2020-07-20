from setuptools import setup, find_packages

setup(name="chat_serverside",
      version="0.0.2",
      description="chat_serverside",
      author="Dmitriy",
      author_email="",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )