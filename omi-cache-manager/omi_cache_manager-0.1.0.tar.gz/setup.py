#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "omi_cache_manager",
    version = "0.1.0",
    keywords = ("ache_manager","redis","async"),
    description = "an async cache manage implemention with aio backend",
    long_description = "an cache manage implemention with aio backend",
    license = "Apache License",

    url = "",
    author = "limc",
    author_email = "limc@ohs-sys.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["pydantic","asyncio","aioredis"]
)