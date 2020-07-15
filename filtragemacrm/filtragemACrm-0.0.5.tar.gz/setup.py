# -*- coding: utf-8 -*-
from setuptools import setup

setup(
  name='filtragemACrm',
  version='0.0.5',
  url='https://github.com/alancaio/filtragemACrm',
  license='MIT License',
  author='Alan Caio Rodrigues Marques',
  author_email='alancaiorm@gmail.com',
  keywords='filtragem imagens duplicadas',
  description=u'Métodos de filtragem de imagem repetida e com blur',
  packages=['filtragemACrm'],
  install_requires=[
      'scikit-image>=0.17.2',
      'opencv-python>=4.1.0'],
)
