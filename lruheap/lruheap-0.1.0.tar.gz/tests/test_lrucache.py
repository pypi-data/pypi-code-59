"""Module for unittest."""

import unittest
from nose.tools import raises # noqa
from lru.lrucache import LRUCache

class LRUCacheTest(unittest.TestCase):
    def setUp(self):
        self.capacity = 10
        self.cache = LRUCache(self.capacity)

        for index in range(self.capacity):
            self.cache.set(1, int(index))

    def tearDown(self):
        self.cache = None

    @raises(KeyError)
    def test_set(self):
        self.cache.set(1, int(index))

    def test_get(self):
        self.cache.get(1)