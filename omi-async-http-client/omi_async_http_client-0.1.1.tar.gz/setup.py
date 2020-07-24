#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "omi_async_http_client",
    version = "0.1.1",
    keywords = ("http_client","aio","async"),
    description = "an async http client implemention with aio backend",
    long_description = "an async http client implemention with aio backend",
    license = "Apache License",

    url = "https://github.com/limccn/omi_async_http_client",
    author = "limc",
    author_email = "limc@ohs-sys.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["pydantic","aiohttp"]
)

