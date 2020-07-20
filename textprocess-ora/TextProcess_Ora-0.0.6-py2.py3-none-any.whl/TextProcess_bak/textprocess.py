#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals, print_function
import re
from copy import deepcopy

try:
    import psyco
    psyco.full()
except:
    pass

try:
    from TextProcess_bak.zh_wiki import zh2Hant, zh2Hans
except ImportError:
    from TextProcess_bak.zh_wiki import zh2Hant, zh2Hans

import sys
py3k = sys.version_info >= (3, 0, 0)

if py3k:
    UEMPTY = ''
else:
    _zh2Hant, _zh2Hans = {}, {}
    for old, new in ((zh2Hant, _zh2Hant), (zh2Hans, _zh2Hans)):
        for k, v in old.items():
            if isinstance(k,unicode) and isinstance(v,unicode):
                new[k] = v
            else:
                new[k.decode('utf8')] = v.decode('utf8')
    zh2Hant = _zh2Hant
    zh2Hans = _zh2Hans
    UEMPTY = ''.decode('utf8')

"""
### 基础正则过滤
1. emotion表情：u'\[[:a-zA-Z\u4e00-\u9fa5]{1,10}\]' 现推荐：emoji.demojize()方法
2. 过滤超链接tag，href
3. 过滤http地址
4. 把长数字都换成一个特殊字符NUM
5. 过滤括号：【xxxxx】/（xxxxxxx）/ [xxxx] 【.*】|（.*）|\[.*\]
6. 过滤非中文字符，连续标点和空格
7. 过滤连续空格

text_regex_preprocessing(text, "OnlinePipe")
"""
class TextProcess():
    def evaluate(self, rawContent, pattern):
        """

        :param rawContent: 待处理的文本
        :param pattern: 正则匹配的模式
        """
        if None in (rawContent, pattern):
            return None
        text = rawContent
        switcher = {
            "Emotion": self.replace_emotion,
            "TagHref": self.remove_ahref,
            "Http": self.remove_http,
            "LongNumber": self.replace_long_num,
            "Brackets": self.replace_brackets,
            "NoChinese": self.remove_not_che,
            "ExtraSpace": self.clean_extra_spaces,
            "ControlCharacter": self.replace_control_character,
            "ChiEngNum": self.keep_chi_eng_num,
            "ChiEng": self.keep_chi_eng,
            "Chi": self.remove_not_che,
            "OnlinePipe": self.preprocessing_all_online,
            "OnlinePipeStrictMore": self.preprocessing_all_online_strict_more,
            "OnlinePipeStrictMost": self.preprocessing_all_online_strict_most,
            "HotlinePipe": self.preprocessing_all_hotline,
        }
        func = switcher.get(pattern, lambda: "nothing")
        return self.clean_extra_spaces(func(text))

    def Tra2Sim(self, text, flag):
        """
        繁体简体互换
        :param text:原始文本
        :param flag:'zh-hant':简体到繁体 ; 'zh-hans':繁体到简体
        """
        # 转换繁体到简体
        if flag=='zh-hans':
            return Converter('zh-hans').convert(text)
        # 转换简体到繁体
        if flag == 'zh-hant':
            return Converter('zh-hant').convert(text)

    def strLower(self, eng_text):
        """
        english A to a
        :param engtext:
        :return:
        """
        if not isinstance(eng_text, unicode):
            return unicode(eng_text)
        return eng_text.lower()

    def strQ2B(self, ustring):
        """
        full width to half width
        :param ustring:
        :return:
        """
        ss = ""
        for s in ustring:
            rstring = ""
            for uchar in s:
                inside_code = ord(uchar)
                if inside_code == 12288:  # 全角空格直接转换
                    inside_code = 32
                elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
                    inside_code -= 65248
                rstring += unichr(inside_code)
            ss += rstring
        return ss

    def preprocessing_all_online(self, text):
        t1 = self.strLower(text)
        t1 = self.Tra2Sim(t1, 'zh-hans')
        t1 = self.strQ2B(t1)
        t1 = self.replace_emotion(t1, "")
        t2 = self.remove_ahref(t1, "")
        t3 = self.remove_http(t2, "")
        t4 = self.replace_time(t3,"TIME")
        t5 = self.replace_long_num(t4, "NUM")
        t6 = self.replace_brackets(t5, "")
        t7 = self.keep_chi_eng_num(t6, "")
        t8 = self.replace_control_character(t7, "")
        return t8

    def preprocessing_all_online_strict_most(self, text):
        t1 = self.strLower(text)
        t1 = self.Tra2Sim(t1, 'zh-hans')
        t1 = self.strQ2B(t1)
        t1 = self.replace_emotion(t1, "")
        t2 = self.remove_ahref(t1, "")
        t3 = self.remove_http(t2, "")
        t4 = self.replace_long_num(t3, "")
        t5 = self.replace_brackets(t4, "")
        t6 = self.remove_not_che(t5)
        t7 = self.replace_control_character(t6, "")
        return t7

    def preprocessing_all_online_strict_more(self, text):
        t1 = self.strLower(text)
        t1 = self.Tra2Sim(t1, 'zh-hans')
        t1 = self.strQ2B(t1)
        t1 = self.replace_emotion(t1, "")
        t2 = self.remove_ahref(t1, "")
        t3 = self.remove_http(t2, "")
        t4 = self.replace_long_num(t3, "")
        t5 = self.replace_brackets(t4, "")
        t6 = self.keep_chi_eng(t5, "")
        t7 = self.replace_control_character(t6, "")
        return t7


    def preprocessing_all_hotline(self, text):
        t1 = self.replace_emotion(text, " ")
        t2 = self.remove_ahref(t1, " ")
        t3 = self.remove_http(t2, " ")
        t4 = self.replace_long_num(t3, " ")
        t5 = self.replace_brackets(t4, " ")
        t6 = self.remove_not_che(t5)
        return t6

    def replace_control_character(self, text, sub_str=""):
        """
        去除控制字符
        :param text: 待处理的文本
        :param sub_str: 用于替换的子串
        """
        re_str = u'[\t\r\n\v\f]'
        return self.replace_pattern(re_str, sub_str, text)

    def keep_chi_eng_num(self, text, sub_str=""):
        """
        保留中文、英文及数字
        :param text:
        :param sub_str:
        """
        res_str = u'[^a-zA-Z 0-9\u4e00-\u9fa5]'
        return self.replace_pattern(res_str, sub_str, text)

    def keep_chi_eng(self, text, sub_str=""):
        """
        保留中文、英文
        :param text:
        :param sub_str:
        """
        res_str = u'[^a-zA-Z\u4e00-\u9fa5]'
        return self.replace_pattern(res_str, sub_str, text)

    def filter_emoji(self, desstr, restr=''):
        # 过滤表情
        try:
            co = re.compile(u'[\U00010000-\U0010ffff]')
        except re.error:
            co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        return co.sub(restr, desstr)

    def replace_emotion(self, text, sub_str=""):
        # re_str = '[\U00010000-\U0010ffff]'

        # re_str = u'\[[:a-zA-Z\u4e00-\u9fa5]{1,10}\]'
        return self.filter_emoji(text, sub_str)

    # def convert_emotion(self, text):
    #     return emoji.demojize(text)

    def remove_ahref(self, text, sub_str=""):
        re_str = u'<[^>]*>'
        return self.replace_pattern(re_str, sub_str, text)

    def remove_http(self, text, sub_str=""):
        re_str = u'https?://[a-zA-Z0-9\.\?/&\=\:\;\-\_]*'
        return self.replace_pattern(re_str, sub_str, text)

    def replace_time(self,text,sub_str=""):
        re_str =u'\d+月|\d+日|\d+天|\d+星期|\d+小时'
        return self.replace_pattern(re_str,sub_str,text)

    def replace_long_num(self, text, sub_str=""):
        re_str = u'-?(0(\.\d*)?|([1-9]\d+\.?\d+)|(\.\d+))([Ee][+-]?\d+)?'
        return self.replace_pattern(re_str, sub_str, text)

    def replace_brackets(self, text, sub_str=""):
        re_str = u'【.*】|（.*）|\[.*\]|「.*」|{.*}'
        return self.replace_pattern(re_str, sub_str, text)

    def remove_not_che(self, text):
        text = self.replace_pattern(u'[^\u4e00-\u9fa5 ]', "", text)
        return text

    def remove_not_che_and_comma(self, text):
        text = self.replace_pattern(u'[^\u4e00-\u9fa5，。？！ ]', " ", text)
        text = self.replace_pattern(u'。{2,}|，{2,}|^，|^。|^？|^！', "", text.strip())
        return text

    def remove_commas(self, text):
        text = self.replace_pattern(u'。{2,}|，{2,}|,{2,}|？{2,}|！{2,}| {2,}', "", text.strip())
        return text

    def clean_extra_spaces(self, text):
        text = self.replace_pattern(u' {2,}', "", text.strip())
        return text

    def replace_pattern(self, re_str, sub_str, text):
        regex_pattern = re.compile(re_str)
        return regex_pattern.sub(sub_str, text)

# states
(START, END, FAIL, WAIT_TAIL) = list(range(4))
# conditions
(TAIL, ERROR, MATCHED_SWITCH, UNMATCHED_SWITCH, CONNECTOR) = list(range(5))

MAPS = {}

class Node(object):
    def __init__(self, from_word, to_word=None, is_tail=True,
            have_child=False):
        self.from_word = from_word
        if to_word is None:
            self.to_word = from_word
            self.data = (is_tail, have_child, from_word)
            self.is_original = True
        else:
            self.to_word = to_word or from_word
            self.data = (is_tail, have_child, to_word)
            self.is_original = False
        self.is_tail = is_tail
        self.have_child = have_child

    def is_original_long_word(self):
        return self.is_original and len(self.from_word)>1

    def is_follow(self, chars):
        return chars != self.from_word[:-1]

    def __str__(self):
        return '<Node, %s, %s, %s, %s>' % (repr(self.from_word),
                repr(self.to_word), self.is_tail, self.have_child)

    __repr__ = __str__

class ConvertMap(object):
    def __init__(self, name, mapping=None):
        self.name = name
        self._map = {}
        if mapping:
            self.set_convert_map(mapping)

    def set_convert_map(self, mapping):
        convert_map = {}
        have_child = {}
        max_key_length = 0
        for key in sorted(mapping.keys()):
            if len(key)>1:
                for i in range(1, len(key)):
                    parent_key = key[:i]
                    have_child[parent_key] = True
            have_child[key] = False
            max_key_length = max(max_key_length, len(key))
        for key in sorted(have_child.keys()):
            convert_map[key] = (key in mapping, have_child[key],
                    mapping.get(key, UEMPTY))
        self._map = convert_map
        self.max_key_length = max_key_length

    def __getitem__(self, k):
        try:
            is_tail, have_child, to_word  = self._map[k]
            return Node(k, to_word, is_tail, have_child)
        except:
            return Node(k)

    def __contains__(self, k):
        return k in self._map

    def __len__(self):
        return len(self._map)

class StatesMachineException(Exception): pass

class StatesMachine(object):
    def __init__(self):
        self.state = START
        self.final = UEMPTY
        self.len = 0
        self.pool = UEMPTY

    def clone(self, pool):
        new = deepcopy(self)
        new.state = WAIT_TAIL
        new.pool = pool
        return new

    def feed(self, char, map):
        node = map[self.pool+char]

        if node.have_child:
            if node.is_tail:
                if node.is_original:
                    cond = UNMATCHED_SWITCH
                else:
                    cond = MATCHED_SWITCH
            else:
                cond = CONNECTOR
        else:
            if node.is_tail:
                cond = TAIL
            else:
                cond = ERROR

        new = None
        if cond == ERROR:
            self.state = FAIL
        elif cond == TAIL:
            if self.state == WAIT_TAIL and node.is_original_long_word():
                self.state = FAIL
            else:
                self.final += node.to_word
                self.len += 1
                self.pool = UEMPTY
                self.state = END
        elif self.state == START or self.state == WAIT_TAIL:
            if cond == MATCHED_SWITCH:
                new = self.clone(node.from_word)
                self.final += node.to_word
                self.len += 1
                self.state = END
                self.pool = UEMPTY
            elif cond == UNMATCHED_SWITCH or cond == CONNECTOR:
                if self.state == START:
                    new = self.clone(node.from_word)
                    self.final += node.to_word
                    self.len += 1
                    self.state = END
                else:
                    if node.is_follow(self.pool):
                        self.state = FAIL
                    else:
                        self.pool = node.from_word
        elif self.state == END:
            # END is a new START
            self.state = START
            new = self.feed(char, map)
        elif self.state == FAIL:
            raise StatesMachineException('Translate States Machine '
                    'have error with input data %s' % node)
        return new

    def __len__(self):
        return self.len + 1

    def __str__(self):
        return '<StatesMachine %s, pool: "%s", state: %s, final: %s>' % (
                id(self), self.pool, self.state, self.final)
    __repr__ = __str__

class Converter(object):
    def __init__(self, to_encoding):
        self.to_encoding = to_encoding
        self.map = MAPS[to_encoding]
        self.start()

    def feed(self, char):
        branches = []
        for fsm in self.machines:
            new = fsm.feed(char, self.map)
            if new:
                branches.append(new)
        if branches:
            self.machines.extend(branches)
        self.machines = [fsm for fsm in self.machines if fsm.state != FAIL]
        all_ok = True
        for fsm in self.machines:
            if fsm.state != END:
                all_ok = False
        if all_ok:
            self._clean()
        return self.get_result()

    def _clean(self):
        if len(self.machines):
            self.machines.sort(key=lambda x: len(x))
            # self.machines.sort(cmp=lambda x,y: cmp(len(x), len(y)))
            self.final += self.machines[0].final
        self.machines = [StatesMachine()]

    def start(self):
        self.machines = [StatesMachine()]
        self.final = UEMPTY

    def end(self):
        self.machines = [fsm for fsm in self.machines
                if fsm.state == FAIL or fsm.state == END]
        self._clean()

    def convert(self, string):
        self.start()
        for char in string:
            self.feed(char)
        self.end()
        return self.get_result()

    def get_result(self):
        return self.final


def registery(name, mapping):
    global MAPS
    MAPS[name] = ConvertMap(name, mapping)

registery('zh-hant', zh2Hant)
registery('zh-hans', zh2Hans)
del zh2Hant, zh2Hans

# def clean_text(text):
#     textprocess = TextProcess_bak()
#     return textprocess.evaluate(text,'OnlinePipeStrictMore')
#
# def main():
#     print(clean_text('我😍愛你中華https://<a></a>,,,,,, Hello Word 121233124234213 [sdfsd]{}【】'))
#
# if __name__ == '__main__':
#     main()