#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： Czf陈章辅
# 开发人员 ： 陈章辅(Administrator)
# 开发时间 ： 2020/7/5 15:54
# 文件名称 ： File.py
# 开发工具 ： PyCharm
import os


# DONE
def create_file(file_path, file_name):
    """
    新建文件
    :param file_path: 新文件路径
    :param file_name: 新文件名称(含后缀)
    :return: None
    """
    f = open(os.path.join(file_path, file_name), 'w+')
    f.close()


# DONE
def delete_file(file_path, is_all=False):
    """
    删除文件
    :param file_path: 路径。如果is_all=False，则有路径有文件名(含后缀)。如果is_all=True，则只有路径无文件名。
    :param is_all: 是否删除目录下的全部文件
    :return: None
    """
    if not is_all:
        os.remove(file_path)
    elif is_all:
        for root, dirs, files in os.walk(file_path):
            for file in files:
                os.remove(os.path.join(root, file))


# DONE
def read_file(file_path, size=0, mode='r', coding='utf-8'):
    """
    读取文件
    :param file_path: 路径 包含文件名(含后缀)
    :param size: 读取多少个字符(从第一个到最后一个)。汉字、字母、数字、符号都按1个。如果要读取全部，则赋值0
    :param mode: 模式
    :param coding: 编码模式
    :return: <str> "文件内容"
    """
    if size != 0:
        with open(file_path, mode=mode, encoding=coding) as f:
            return f.read(size)
    else:
        with open(file_path, mode=mode, encoding=coding) as f:
            return f.read()


# DONE
def write_file(file_path, content, mode='w', coding='utf-8'):
    """
    写入文件
    :param file_path: 文件路径 包含文件名(含后缀)
    :param content: 需要写入的内容
    :param mode: 模式
    :param coding: 编码模式
    :return: None
    """
    with open(file_path, mode=mode, encoding=coding) as f:
        f.write(content)
