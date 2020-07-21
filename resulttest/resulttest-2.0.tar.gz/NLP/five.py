# @Time : 2020/7/21 10:58 
# @Author : XX
# @File : s.py
# @Software: PyCharm

import logging
import gensim
from gensim.models import word2vec

word2vec.LineSentence("")
model = gensim.models.Word2Vec(sentences, size=200, sg=1, iter=8)
model.wv.save_word2vec_format()
wordVec = gensim.models.KeyedVectors.load_word2vec_format()