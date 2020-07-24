from distutils.core import setup


setup(
name='lcmSuper', # 对外我们模块的名字
version='1.0', # 版本号
description='这是第一个对外发布的模块，测试哦', #描述
author='liming', # 作者
author_email='141137990@qq.com',
py_modules=['lcmSuper.demo1','lcmSuper.demo2'] # 要发布的模块
)