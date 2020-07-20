# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： Czf陈章辅
# 开发人员 ： 陈章辅(Administrator)
# 开发时间 ： 2020/7/20 13:27
# 文件名称 ： Log.py
# 开发工具 ： PyCharm
import math
import numpy


def divided(d, number):
    """
    除法
    :param d: 被除数
    :param number: 数字
    :return: <tuple> (小数结果, 整除的商, 整除的余数)
    """
    rtn1 = d / number
    rtn2 = d // number
    rtn3 = d % number

    return rtn1, rtn2, rtn3


def many_system(num):
    """
    进制转换
    :param num: 数字
    :return: <tuple> (十六进制, 八进制, 二进制, 十进制)
    """
    num = int(num)
    _HEX = hex(num)
    _OCT = oct(num)
    _BIN = bin(num)
    _DEC = int(num, 16)
    rtn = (_HEX, _OCT, _BIN, _DEC)
    return rtn