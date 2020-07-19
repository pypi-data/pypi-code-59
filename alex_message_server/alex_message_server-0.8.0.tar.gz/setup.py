from setuptools import setup, find_packages

setup(name="alex_message_server",
      version="0.8.0",
      description="alex_message_server",
      author="Alexey V. Danilyuk",
      author_email="danilyuk-aleksey@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
