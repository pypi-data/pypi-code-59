#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： Czf陈章辅
# 开发人员 ： 陈章辅(Administrator)
# 开发时间 ： 2020/7/10 19:59
# 文件名称 ： Office.py
# 开发工具 ： PyCharm
import os
import re
import sys
import codecs
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileMerger


def create_file(file_path, file_name):
    """
    新建文件
    :param file_path: 新文件路径
    :param file_name: 新文件名称(含后缀)
    :return: None
    """
    f = open(os.path.join(file_path, file_name), 'w+')
    f.close()


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


def write_file(file_path, *content, mode='w', coding='utf-8', sep=' '):
    """
    写入文件
    :param file_path: 文件路径 包含文件名(含后缀)
    :param content: 需要写入的内容
    :param mode: 模式
    :param coding: 编码模式
    :param sep: 分隔符
    :return: None
    """
    with open(file_path, mode=mode, encoding=coding) as f:
        for item in map(str, content):
            f.write(item + sep)


def get_extend_files(file_path='', file_ext='all'):
    """
    遍历目录，并返回后缀名为需要的后缀名的文件的列表
    :param file_path: 路径
    :param file_ext: 需要的后缀名
    :return: <list> [后缀名为需要的后缀名的文件]
    """
    file_list_rtn = []
    for root, dirs, files in os.walk(file_path):
        for one_file in files:
            file_dir = os.path.join(root, one_file)
            if file_ext == 'all':
                file_list_rtn.append(re.sub(r'\\', '/', file_dir))
            elif os.path.splitext(file_dir)[1] == file_ext:
                file_list_rtn.append(re.sub(r'\\', '/', file_dir))
    file_list_rtn.sort()
    return file_list_rtn


def merging_pdf(path, output_path, import_bookmarks=False):
    """
    合并 PDF
    :param path: 源PDF路径
    :param output_path: 合并后的的PDF文件存放路径(含文件名)
    :param import_bookmarks: 导入书签
    :return: None
    """
    merger = PdfFileMerger()
    file_list = get_extend_files(path, '.pdf')
    if len(file_list) == 0:
        raise FileNotFoundError('PDF files do not exist in this directory and its subdirectories')
    for file_name in file_list:
        f = codecs.open(file_name, 'rb')
        file_read = PdfFileReader(f)
        file_name_not_ext = os.path.basename(os.path.splitext(file_name)[0])

        if file_read.isEncrypted is True:
            print('不支持的加密文件 %s' % file_name)
            continue
        merger.append(file_read, bookmark=file_name_not_ext, import_bookmarks=import_bookmarks)
        f.close()
    merger.write(output_path)
    merger.close()


def get_pdf_page_num(path):
    """
    获取PDF总页数
    :param path: PDF路径
    :return: <int> 页码数
    """
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page_num = pdf.getNumPages()
    return page_num


def get_pdf_outline(pdf_path, list_path, is_page=True):
    """
    获取PDF大纲
    :param pdf_path: PDF路径
    :param list_path: 保存大纲的文件的路径
    :param is_page: 是否含页码
    :return: None
    """
    def get_outline(obj, isPage):
        rtn = []
        for o in obj:
            if type(o).__name__ == 'Destination':
                if isPage:
                    rtn.append(o.get('/Title') + '\t\t' + str(o.get('/Page') + 1) + '\n')
                else:
                    rtn.append(o.get('/Title') + '\n')
            elif type(o).__name__ == 'list':
                get_outline(o, isPage)
        return rtn

    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        outlines = pdf.getOutlines()
        mylist = get_outline(outlines, is_page)
        with open(list_path, 'w') as fl:
            for item in mylist:
                fl.write(str(item))
