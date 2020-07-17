# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： Czf陈章辅
# 开发人员 ： 陈章辅(Administrator)
# 开发时间 ： 2020/7/5 15:53
# 文件名称 ： Cmd.py
# 开发工具 ： PyCharm
import hashlib
import hmac
from xpinyin import Pinyin


def inv_str(s):
    """
    颠倒字符串
    :param s: 需要颠倒的字符串
    :return: <str> "颠倒后的字符串"
    """
    rtn = ''.join(s[::-1])
    return rtn


def inv_list(s):
    """
    颠倒字符串
    :param s: 需要颠倒的字符串
    :return: <str> "颠倒后的字符串"
    """
    rtn = s[::-1]
    return rtn


def inv_num(n):
    """
    颠倒数字
    :param n: 需要颠倒的字符串
    :return: <float/int> 颠倒后的数字
    """
    rtn = None
    if isinstance(n, int):
        rtn = int(str(n)[::-1])
    elif isinstance(n, float):
        rtn = float(str(n)[::-1])

    return rtn


def encryption(string,  lib='md5', is_hmac=True, encoding='utf-8', hmacer='hmac'):
    """
    加密字符串
    :param string: 需要加密的字符串
    :param lib: 加密模式
    :param is_hmac: 是否使用 hmac
    :param encoding: 编码方式
    :return: <str> "加密后的字符串"
    """
    libs = ['md5', 'sha1', 'sha256', 'sha512']
    if is_hmac:
        if not lib in libs:
            raise ValueError('无此模式')
        else:
            if lib == libs[0]:
                s = string.encode(encoding)
                key = hmacer.encode(encoding)
                h = hmac.new(key, s, digestmod='MD5')
                return h.hexdigest()

            if lib == libs[1]:
                s = string.encode(encoding)
                key = hmacer.encode(encoding)
                h = hmac.new(key, s, digestmod='SHA1')
                return h.hexdigest()

            if lib == libs[2]:
                s = string.encode(encoding)
                key = hmacer.encode(encoding)
                h = hmac.new(key, s, digestmod='SHA256')
                return h.hexdigest()

            if lib == libs[3]:
                s = string.encode(encoding)
                key = hmacer.encode(encoding)
                h = hmac.new(key, s, digestmod='SHA512')
                return h.hexdigest()
    else:
        if not lib in libs:
            raise ValueError('无此模式')
        else:
            if lib == libs[0]:
                md5 = hashlib.md5()
                md5.update(string.encode(encoding))
                return md5.hexdigest()

            if lib == libs[1]:
                sha1 = hashlib.sha1()
                sha1.update(string.encode(encoding))
                return sha1.hexdigest()

            if lib == libs[2]:
                sha256 = hashlib.sha256()
                sha256.update(string.encode(encoding))
                return sha256.hexdigest()

            if lib == libs[3]:
                sha512 = hashlib.sha512()
                sha512.update(string.encode(encoding))
                return sha512.hexdigest()


def sort_chinese_list(words, reverse=False):
    """
    对汉字列表排序（音序法）
    :param words: 需要排序的汉字列表
    :param reverse: 正序赋值False，倒序赋值True
    :return: <list> [排序后的列表]
    """
    pinyin = Pinyin()

    temp = []
    for item in words:
        temp.append((pinyin.get_pinyin(item), item))
    temp.sort(reverse=reverse)

    rtn = []
    for i in range(len(temp)):
        rtn.append(temp[i][1])
    return rtn


def sort_chinese_str(words, reverse=False, sep=' '):
    """
    对汉字列表排序（音序法）
    :param words: 需要排序的汉字列表
    :param reverse: 正序赋值False，倒序赋值True
    :param sep: 分隔符
    :return: <str> "排序后的字符串"
    """
    pinyin = Pinyin()

    temp = []
    for item in words:
        temp.append((pinyin.get_pinyin(item), item))
    temp.sort(reverse=reverse)

    rtn = []
    for i in range(len(temp)):
        rtn.append(temp[i][1])
    rtn = sep.join(rtn)
    return rtn


def get_location_code(words, sep=' '):
    """
    获取汉字的区位码
    :param words: 需要获取区位码的汉字字符串
    :param sep: 分隔符
    :return: <str> 区位码
    """
    tmp = []

    for w in words:
        gbk = w.encode('gbk')
        code = '{0:02d}'.format((gbk[0] - 160)) + '{0:02d}'.format((gbk[1] - 160))
        tmp.append(code)

    rtn = sep.join(tmp)
    return rtn


def get_pinyin(words):
    """
    获取汉字字符串每个汉字的拼音
    :param words: 汉字字符串
    :return: <dict> ""
    """
    pinyin = Pinyin()
    p = pinyin.get_pinyin(words)
    p = p.split('-')
    rtn = dict(zip(words, p))
    return rtn