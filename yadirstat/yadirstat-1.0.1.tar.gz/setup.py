import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='yadirstat',
      version='1.0.1',
      description='Получение статистики из Яндекс Директ',
      long_description=long_description,
      packages=['yadirstat'],
      author="Lubiviy Alexander",
      author_email='lybiviyalexandr@gmail.com',
      url="https://github.com/Lubiviy/yadirstat",
                 )