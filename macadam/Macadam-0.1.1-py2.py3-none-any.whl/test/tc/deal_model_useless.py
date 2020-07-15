# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/7/2 0:11
# @author  : Mo
# @function:


import os


def get_all_dirs_files(path_dir):
    """
        递归获取某个目录下的所有文件(所有层, 包括子目录)
    :param path_dir: str, like '/home/data'
    :return: list, like ['2020_01_08.txt']
    """
    path_files = []
    def get_path_files(path_dir):
        """
            递归函数, 获取某个目录下的所有文件
        :param path_dir: str, like '/home/data'
        :return: list, like ['2020_01_08.txt']
        """
        for root, dirs, files in os.walk(path_dir):
            for fi in files: # 递归的终止条件
                path_file = os.path.join(root, fi)
                path_files.append(path_file)
            for di in dirs:  # 语间目录便继续递归
                path_dir = os.path.join(root, di)
                get_path_files(path_dir)
    get_path_files(path_dir)
    return path_files


if __name__ == '__main__':
    path="D:/workspace/pythonMyCode/Macadam/macadam/data/model"
    files = get_all_dirs_files(path)
    for file in files:
        if ".info" in file or ".h5" in file:
            os.remove(file)


