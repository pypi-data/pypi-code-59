# coding=utf-8
from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = '1.0.1'
description = '简单异步任务队列'
update = '又是造轮子系列咯，Python上有很多成熟完善的异步任务队列框架可以用，比如Celery，或者RQ，不过这些都不自带消息队列服务，都需要使用Redis、RabbitMQ之类的消息队列才行，我用到小项目中又不需要附带这么多东西，于是自己动手来实现咯。'
description = f'{description}。版本[{version}] 更新内容：{update}'

setup(
    name='onecat_task_queue',
    version=version,
    packages=setuptools.find_packages(),
    install_requires=[],
    url='https://gitee.com/deali/OneCat-TaskQueue',
    # license='GPLv3',
    author='DealiAxy',
    author_email='dealiaxy@gmail.com',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
