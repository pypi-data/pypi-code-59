#!/usr/bin/env python

import re
import setuptools

version = ""


setuptools.setup(
    name="esayRedis",
    version="0.3.4",
    author="q2536807",
    author_email="616566665@qq.com",
    description="esayRedisTest",
    long_description="esayRedisTest",
    url="http://example.com",
    install_requires=['fastapi','aredis','starlette','pydantic','uuid','asyncio'],
    packages=setuptools.find_packages(),
    include_package_data = True,
    platforms = "any"
)