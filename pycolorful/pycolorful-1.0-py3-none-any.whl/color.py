# -*- coding:utf-8 -*-
__author__ = 'Ankele'
__date__ = '2020/7/15 0015'

import six


class Color:
    def __init__(self):
        pass

    @staticmethod
    def print_colorful(content, mode=0, front=30, backend=47, end=''):
        """
        Print string with colors
        :param content: string content
        :param mode: 0默认值 1高亮 22非粗体 4下划线 24非下划线 5闪烁 25非闪烁 7反显 27非反显
        :param front: 30黑色 31红色 32绿色 33黄色 34蓝色 35洋红 36青色 37白色
        :param end: 40黑色 41红色 42绿色 43黄色 44蓝色 45洋红 46青色 47白色
        :return: None
        """
        six.print_('\033[' + str(mode) + ';' + str(front) + ';' + str(backend) + 'm', end=end)
        six.print_(content, end=end)
        six.print_('\033[0m')
