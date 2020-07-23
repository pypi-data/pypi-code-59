#coding=utf-8
from distutils.core import setup

setup(
    name='wengwengSuperMath',    #对外我们模块的名字
    version='1.0',   #版本号
    description='这是第一个对外发布的模块，里面只有加法和乘法，用于测试哦',  #描述
    author='ak',    #作者
    author_email='172577060@qq.com',
    py_modules=['wengwengSuperMath.demo1','wengwengSuperMath.demo2']  #要发布的模块
)