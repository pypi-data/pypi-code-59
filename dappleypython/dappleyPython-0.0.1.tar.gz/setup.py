#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: enjoyass
# Mail: enjoyass@outlook.com
# Created Time:  2020-7-21 10:17:34
#############################################


from setuptools import setup, find_packages

setup(
    name = "dappleyPython",
    version = "0.0.1",
    keywords = ("pip", "sdk","dappley","dappworks","dappleyPython"),
    description = "dappley sdk is implemented by python",
    long_description = "dappley sdk is implemented by python ,you can send transaction to dappley blockchain by this sdk",
    license = "LGPL v3 Licence",

    url = "https://github.com/dappley/dappley-sdk-python",
    author = "enjoyass",
    author_email = "enjoyass@outlook.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [
        'grpcio==1.28.1',
        'google==2.0.3',
        'protobuf==3.11.3',
        'base58==1.0.3',
        'grpc~=0.3.post19',
        'secp256k1~=0.13.2',
        'pysha3==1.0.2'
    ]
)