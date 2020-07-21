#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup
setup(name="qaquora",
version="0.1",
description="This is a python package to extra all questions and answers related to any topic on quora",
author="Yugal Jain",
packages=['qaquora'],
install_requires=['selenium','pandas','beautifulsoup4'])

