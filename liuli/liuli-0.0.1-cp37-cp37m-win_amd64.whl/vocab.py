from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from typing import Dict


class Vocab:
    def __init__(self):
        self.vocab_size = 0
        self.total_count = 0
        self.max_token_length = 0

    def add_word(self, word: str, count: int = 1) -> None:
        raise NotImplementedError

    def build(self, word2count: Dict[str, int]) -> None:
        for word, count in word2count.items():
            self.add_word(word, count)

    def search(self, text: str) -> int:
        '''
        查找一个单词或前缀,返回其计数
        返回0表示是一个前缀,返回-1示不存在
        '''
        raise NotImplementedError

    def __contains__(self, text):
        '''
        前缀或单词是否存在词典中
        '''
        return self.search(text) >= 0

    def __len__(self):
        return self.vocab_size

    def __str__(self):
        return f"\nvocab_size: {self.vocab_size}\ntotal_count: {self.total_count}\nmax_token_length: {self.max_token_length}"


class PrefixDictVocab(Vocab):

    def __init__(self):
        super().__init__()
        self.dict = {}

    def add_word(self, word: str, count: int = 1) -> None:
        self.vocab_size += 1
        self.total_count += count
        self.max_token_length = max(self.max_token_length, len(word))
        for i in range(1, len(word)):
            # 加入前缀
            prefix = word[:i]
            if not prefix in self.dict:
                self.dict[prefix] = 0
        self.dict[word] = count

    def search(self, text: str) -> int:
        return self.dict.get(text, -1)


class TrieVocab(Vocab):
    '''
    实现一个Trie(前缀树)
    用于单词的查找和前缀查找
    每个节点是一个哈希表,键为当前字符,值为下一层节点
    >>> trie = TrieVocab()
    >>> user_dict = {token:jieba.get_FREQ(token) for token in 
                        jieba.lcut('南京市长江大桥',cut_all=True)}
    >>> trie.build(user_dict)
    >>> print(trie)
    ROOT
     +- 南
     |   +- 京
     |   |   +- 7228
     |   |   +- 市
     |   |   |   +- 2046
     +- 京
     |   +- 市
     |   |   +- 2
     +- 市
     |   +- 长
     |   |   +- 8782
     +- 长
     |   +- 江
     |   |   +- 18930
     |   |   +- 大
     |   |   |   +- 桥
     |   |   |   |   +- 3858
     +- 大
     |   +- 桥
     |   |   +- 3288
    >>> trie.search('南京市')
    12
    >>> trie.search('南')
    0
    >>> trie.search('南京南站')
    -1
    >>> trie.get_descendants("南")
    [['南京', 7228], ['南京市', 2046]]
    >>> trie.get_descendants("长")
    [['长江', 18930], ['长江大桥', 3858]]
    '''

    def __init__(self, count_flag: str = "#"):
        super().__init__()
        self.root = {}
        self.count_flag = count_flag

    def add_word(self, word: str, count: int = 1) -> None:
        self.vocab_size += 1
        self.total_count += count
        self.max_token_length = max(self.max_token_length, len(word))
        node = self.root
        for c in word:
            if not c in node:
                # 新建节点
                node[c] = {}
            # 向下遍历
            node = node[c]
        # 记录计数值
        node[self.count_flag] = count

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not c in node:
                return -1
            node = node[c]
        if self.count_flag in node:
            return node[self.count_flag]
        return 0

    def get_descendants(self, prefix, depth: int = -1,
                        first: int = -1, topk: int = -1):
        node = self.root
        for c in prefix:
            if not c in node:
                return []
            node = node[c]
        queue = [(prefix, node)]
        descendants = []
        # 层序遍历取子孙节点
        while queue:
            current_prefix, node = queue.pop(0)
            if depth > 0 and len(current_prefix) - len(prefix) > depth:
                break
            for k, v in node.items():
                if k == self.count_flag:
                    descendants.append([current_prefix, v])
                    if first > 0 and len(descendants) >= first:
                        break
                else:
                    # 前缀+当前节点字 = 新前缀
                    queue.append((current_prefix+k, v))
        return descendants if topk < 0 else \
            sorted(descendants, key=lambda x: x[1], reverse=True)[:topk]

    def __str__(self) -> str:
        def dfs(root, buffer, prefix=''):
            for k, v in root.items():
                if k == self.count_flag:
                    buffer.append('%s +- %s' % (prefix, v))
                else:
                    buffer.append('%s +- %s' % (prefix, k))
                    dfs(v, buffer, prefix+' |  ')
        buffer = ['ROOT']
        dfs(self.root, buffer)
        return '\n'.join(buffer)
