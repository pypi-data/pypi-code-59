from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import logging
from typing import Generator, List

import jieba

from liuli.tokenizer import Tokenizer
from liuli.vocab import PrefixDictVocab, TrieVocab, Vocab

logger = logging.getLogger(__name__)


class Liuli:
    def __init__(self, vocab_type: str = "prefix_dict"):
        self.vocab_type = vocab_type
        self.tokenizer = None

    def check_initialize(self):
        '''
        lazy loading
        惰性加载，使得可以独立使用vocab和tokenizer
        '''
        if self.tokenizer is None:
            jieba_dict_file = jieba.dt.get_dict_file().name
            logger.info("loading dict file from: %s", jieba_dict_file)
            self.load_userdict(jieba_dict_file)
            logger.info("vocab type: %s", self.vocab.__class__)
            logger.info("vocab info: %s", str(self.vocab))
            self.tokenizer = Tokenizer(self.vocab)

    def load_userdict(self, fp: str) -> None:
        '''
        用于更新vocab
        '''
        self.vocab = PrefixDictVocab() if \
            self.vocab_type == "prefix_dict" else TrieVocab()
        user_dict = {}
        with open(fp, 'r', encoding='utf-8') as fr:
            for line in fr:
                line = line.strip().split(' ')
                user_dict[line[0]] = int(line[1])
        self.vocab.build(user_dict)

    def cut(self, text: str, cut_all: bool = False) -> Generator:
        self.check_initialize()
        return self.tokenizer.cut(text, 'all' if cut_all else 'max')

    def lcut(self, text: str, cut_all: bool = False) -> List:
        return list(self.cut(text, cut_all=cut_all))

    def cut_for_search(self, text: str) -> Generator:
        self.check_initialize()
        return self.tokenizer.cut(text, 'search')

    def lcut_for_search(self, text: str) -> List:
        return list(self.cut_for_search(text))
