import unittest
import random

from word_identifiers import words_to_id, id_to_words
from word_identifiers import wordlist


class TestInverses(unittest.TestCase):
    def number_to_word_to_number_test(self):
        for _ in range(10 ** 4):
            identifier = random.randint(0, 10 ** 100)
            self.assertEqual(words_to_id(id_to_words(identifier)), identifier)
        for _ in range(10 ** 2):
            identifier = random.randint(0, 10 ** 100)
            self.assertEqual(words_to_id(id_to_words(identifier)), identifier)

    def word_to_number_to_word_test(self):
        for _ in range(10 ** 4):
            identifier = [random.choice(wordlist) for _ in range(random.randint(0, 20))]
            if not identifier or identifier[0] == "form":
                continue
            self.assertEqual(id_to_words(words_to_id(identifier)), identifier)
