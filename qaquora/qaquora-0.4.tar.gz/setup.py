#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup
import os

with open(os.path.join('C:/Users/HP/qaquora','README.md'),encoding='utf-8') as j:
    long_description = j.read()
setup(name="qaquora",
version="0.4",
description="This is a python package to extra all questions and answers related to any topic on quora",
author="Yugal Jain",
packages=['qaquora'],
long_description = long_description,
long_description_content_type = 'text/markdown',
install_requires=['selenium','pandas','beautifulsoup4'])

