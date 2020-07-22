from unittest import TestCase
from platform import system

from canaries.canaries import *

class Test_canaries(TestCase):
    def test_probe(self):
        lib = canary(
            system(), 
            './test/target/test.error.none.l',
            probe=True
        )
        self.assertIsNotNone(lib)
        self.assertTrue(canaries._probe(lib))

    def test_isolated(self):
        self.assertTrue(canaries._isolated('./test/target/test.error.none.l'))

    def test_canary(self):
        lib = canary(
            system(),
            './test/target/test.error.none.l',
            probe=True
        )
        self.assertIsNotNone(lib)

    def test_load_input_type_error(self):
        with self.assertRaises(TypeError):
            lib = load(123, probe=True)

    def test_load_paths_type_error(self):
        with self.assertRaises(TypeError):
            lib = load({'Linux': 123}, probe=True)

    def test_load_error_invalid(self):
        lib = load('./test/target/test.error.invalid.l', probe=True)
        self.assertIsNone(lib)

    def test_load_error_logic(self):
        lib = load('./test/target/test.error.logic.l', probe=True)
        self.assertIsNone(lib)

    def test_load_error_runtime(self):
        lib = load('./test/target/test.error.runtime.l', probe=True)
        self.assertIsNone(lib)

    def test_load_str(self):
        lib = load('./test/target/test.error.none.l', probe=True)
        self.assertIsNotNone(lib)

    def test_load_no_probe_str(self):
        lib = load('./test/target/test.error.none.l')
        self.assertIsNotNone(lib)

    def test_load_list(self):
        lib = load(
            [
                './test/target/test.error.logic.l',
                './test/target/test.error.none.l'
            ],
            probe=True
        )
        self.assertIsNotNone(lib)

    def test_load_dict(self):
        lib = load(
            {
                'Linux': ['./test/target/test.error.none.l'],
                'Darwin': ['./test/target/test.error.none.l'],
                'Windows': ['./test/target/test.error.none.l']
            },
            probe=True
        )
        self.assertIsNotNone(lib)
