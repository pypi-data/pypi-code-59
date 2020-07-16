import unittest
import json
import os
from jpconfig.jpconfig import Config

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.file = os.getcwd() + os.path.sep +'test.json'
        self.config = Config(file=self.file)
        self.config.name = 'test'

    def test_add(self):
        self.config + {"age": 30}
        assert(self.config.age == 30)
        assert(self.config.name == 'test')

    def test_create_file(self):
        assert(os.path.exists(self.file) == True)
    
    def test_insert_item(self):
        self.config.age = 33
        self.config._update({"age": 34})
        assert(self.config.age == 34)

    def test_get_item(self):
        assert(self.config.name == 'test')

    def test_loading_from_file(self):
        test_config = Config(file=self.file)
        assert(test_config.name == 'test')

    def test_save(self):
        with open(self.file, 'r') as f:
            saved = f.read()
        assert(saved == self.config.__repr__())

    def test_remove_item(self):
        del self.config["name"]
        assert(self.config.name == None)

    def test_remove_attr(self):
        del self.config.name
        assert(self.config.name == None)

    def test_list(self):
        assert(self.config.keys() == ['name'])

    def test_file_path(self):
        assert(self.config.file_path == self.file)

    def test_file_path_not_set(self):
        with self.assertRaises(SystemExit):
            Config()

    def tearDown(self):
        os.remove(self.file)
