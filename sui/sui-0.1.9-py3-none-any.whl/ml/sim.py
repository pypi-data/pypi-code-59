"""Module tackling the similarity between vectors
Date: 15/Jul/2020
Author: Li Tang
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import nmslib
from gensim.models import word2vec

__author__ = ['Li Tang']
__copyright__ = 'Li Tang'
__credits__ = ['Li Tang']
__license__ = 'MIT'
__version__ = '0.1.9'
__maintainer__ = ['Li Tang']
__email__ = 'litang1025@gmail.com'
__status__ = 'Production'


class SuiMlSimError(Exception):
    pass


class SimiCalculator:
    def __init__(self, method='hnsw', space='cosinesimil'):
        self.method = method
        self.space = space
        self.calculator = nmslib.init(method=self.method, space=self.space)

    def load(self, data):
        self.calculator.addDataPointBatch(data)
        self.calculator.createIndex({'post': 2}, print_progress=False)

    def get(self, vector, k=1):
        """

        :param vector:
        :param k:
        :return: [idx0, idx1, ..., idxk], [dist0, dist1, ..., distk]
        """
        return self.calculator.knnQuery(vector, k)

    def get_batch(self, data, k=1, num_threads=4):
        """

        :param data:
        :param k:
        :param num_threads:
        :return: [([idx0_for_data[0], idx1_for_data[0], ..., idxk_for_data[0]], [dist0, dist1, ..., distk]),
                  ([idx0_for_data[1], idx1_for_data[1], ..., idxk_for_data[1]], [dist0, dist1, ..., distk]),
                  ...
                 ]
        """
        return self.calculator.knnQueryBatch(data, k=k, num_threads=num_threads)


class Item_CF_Embedding:
    def __init__(self, model):
        self.__model = model

    def train(self, input_list=None, input_file=None):
        self.__model.train(input_list, epochs=epochs, total_words=total_words, total_examples=total_examples)

    def predict(self, item_id):
        return self.__model.wv(item_id)

    def dump(self):
        pass

    def restore(self):
        pass