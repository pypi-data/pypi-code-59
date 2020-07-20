#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： Czf陈章辅
# 开发人员 ： 陈章辅(Administrator)
# 开发时间 ： 2020/7/20 12:54
# 文件名称 ： Log.py
# 开发工具 ： PyCharm
from . import Office


def log_to(log_file, year, month, day, *content, sep='\n'):
    """
    将内容添加至当前某个.log文件
    :param year: 年份
    :param month: 月份
    :param day: 天
    :param content: 内容
    :param log_file: .log文件
    :param sep: 分隔符
    :return: None
    """
    date = 'Date: {:s}/{:s}/{:s}\n'
    date.format(year, month, day)
    for item in map(str, content):
        Office.write_file(log_file, date, item, '\n', sep=sep)
