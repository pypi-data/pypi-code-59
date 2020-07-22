from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import re
from math import log
from typing import Dict, Generator, List

from liuli.vocab import Vocab

re_split = re.compile(r"([,;:.?!\s\r\n])")
re_zh = re.compile(r"[\u4E00-\u9FD5]")


class Tokenizer:
    '''
    规则：依赖先验词典及其计数信息
    1. 局部贪心: 前/后/双向/最少词数 最大匹配
    2. 全局动规: 倾向于最大匹配 p(长江)*p(大桥) < p(长江大桥)
    TODO: 3. 统计学习: HMM/CRF
    >>> vocab = TrieVocab()
    >>> user_dict = {token:jieba.get_FREQ(token) for token in jieba.lcut('南京市长江大桥',cut_all=True)}
    >>> vocab.build(user_dict)
    >>> tokenizer = Tokenizer(vocab)
    >>> tokenizer.max_forward_cut('南京市长江大桥')
    ['南京市', '长江大桥']
    >>> tokenizer._get_DAG('武汉市长江大桥')
    {0: [0], 1: [1], 2: [2, 3], 3: [3, 4, 6], 4: [4], 5: [5, 6], 6: [6]}
    >>> tokenizer.max_forward_cut('武汉市长江大桥')
    ['武', '汉', '市长', '江', '大桥']
    >>> vocab.add_word("武汉")
    >>> tokenizer._get_DAG('武汉市长江大桥')
    {0: [0, 1], 1: [1], 2: [2, 3], 3: [3, 4, 6], 4: [4], 5: [5, 6], 6: [6]}
    >>> tokenizer.max_forward_cut('武汉市长江大桥')
    ['武汉', '市长', '江', '大桥']
    >>> tokenizer.max_forward_cut('武汉市长江大桥',reverse=True)
    ['武汉', '市', '长江大桥']
    >>> tokenizer.max_bi_direction_cut('武汉市长江大桥')
    ['武汉', '市', '长江大桥']
    >>> list(tokenizer.cut('武汉市长江大桥','max'))
    ['武汉', '市', '长江大桥']
    '''

    def __init__(self, vocab: Vocab) -> None:
        self.vocab = vocab

    def max_forward_cut(self, text: str, reverse=False) -> List[str]:
        '''
        最大匹配算法
        每次匹配窗口 [l, l+max_token_length]
        '''
        text = text[::-1 if reverse else 1]
        L = len(text)
        window_size = self.vocab.max_token_length
        res = []
        if reverse:
            # 窗口递减 没有用到前缀结构，每次从可能的最长开始
            # 前后向均可实现
            # 此后向不依赖于后缀结构
            l, r = 0, min(window_size, L-1)
            while l < L and r >= l:
                tmp_word = text[l:r+1][::-1]
                # 单字或找到一个单词
                if l == r or self.vocab.search(tmp_word) > 0:
                    l = r + 1
                    r = min(l+window_size, L-1)
                    res.append(tmp_word)
                else:
                    r -= 1
        else:
            # 窗口递增 使用前缀结构，只用于前向
            l = r = 0
            # 没有匹配结果时使用单字
            hit_word = text[l]
            hit_ix = l+1
            while l < L:
                tmp_word = text[l:r+1]
                if r <= l+window_size and r < L and tmp_word in self.vocab:
                    r += 1
                    if self.vocab.search(tmp_word) > 0:
                        hit_word = tmp_word
                        hit_ix = r
                else:
                    res.append(hit_word)
                    l = r = hit_ix
                    if hit_ix == L:
                        break
                    hit_word = text[l]
                    hit_ix = l+1

        return res[::-1 if reverse else 1]

    def max_bi_direction_cut(self, text: str):
        f = self.max_forward_cut(text)
        b = self.max_forward_cut(text, reverse=True)
        len_f = len(f)
        len_b = len(b)
        if len_f != len_b:
            # 最小词数原则
            return b if len_b < len_f else f
        else:
            # 词数相同时，返回单字数最少的结果
            len_f_s = len([1 for t in f if len(t) == 1])
            len_b_s = len([1 for t in b if len(t) == 1])
            # 单字数也相同时，优先返回逆向
            return b if len_b_s <= len_f_s else f

    def _get_DAG(self, text):
        '''
        切词有向无环图的邻接矩阵
        {start: [end1, end2]}
        start == end 单字
        '''
        ADJ = {}  # Adjoint Matrix
        for start in range(len(text)):
            # 不与其他字成词的情况
            ADJ[start] = [start]
            end = start+1
            tmp_word = text[start:end+1]
            # 前缀匹配
            while end < len(text) and tmp_word in self.vocab:
                # 连边
                if self.vocab.search(tmp_word) > 0:
                    ADJ[start].append(end)
                end += 1
                tmp_word = text[start:end+1]
        return ADJ

    def _max_prob_cut(self, text: str, DAG: Dict) -> Generator:
        # 最大切分概率，对应尾节点索引，最大切分词
        # {start: (max_path_prob, end, token)}
        path = {len(text): (0, 0, '')}  # dummy_path
        log_total = log(self.vocab.total_count)
        for start in range(len(text) - 1, -1, -1):
            # max() [tuple] sort by key=tuple[0]
            path[start] = max(
                (
                    # P(text[start:end+1]) = log(count/total_count) = log_token - log_total
                    # P_cut(text[end+1:]) = path[end + 1][0] #被多次依赖，冗余计算在前
                    # P_cut(text[start:]) = P(text[start:end+1]) + P_cut(text[end+1:])
                    log(max(1, self.vocab.search(text[start:end + 1]))) \
                    - log_total + path[end + 1][0],
                    end,
                    text[start:end + 1]
                ) for end in DAG[start]
            )
        start = 0
        while start < len(text):
            yield path[start][2]
            # 对应尾节点的下一个开始
            start = path[start][1]+1

    def cut(self, text, mode: str = ['max', 'all', 'search'][0]) -> Generator:
        '''
        区分不同切分模式
        '''
        for block in re_split.split(text):
            if re_zh.findall(block):
                DAG = self._get_DAG(block)
                if mode == 'max':
                    # 最大概率模式
                    for token in self._max_prob_cut(block, DAG):
                        yield token
                elif mode == 'all':
                    # 全模式 取切词有向无环图所有连边
                    for start, ends in DAG.items():
                        for end in ends:
                            if end >= start:
                                tmp_word = block[start:end+1]
                                if self.vocab.search(tmp_word) > 0:
                                    yield tmp_word
                elif mode == 'search':
                    # 搜索模式 对最大概率切分结果的每个token使用全模式
                    for token in self._max_prob_cut(block, DAG):
                        for sub_token in self.cut(token, 'all'):
                            yield sub_token
                else:
                    raise ValueError("no support for cut mode: %s", mode)
            else:
                if block.strip():
                    yield block
