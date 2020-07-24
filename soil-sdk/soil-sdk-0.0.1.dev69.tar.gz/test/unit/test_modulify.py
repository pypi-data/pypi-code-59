# pylint: disable=missing-docstring,no-self-use

import unittest


class TestModulify(unittest.TestCase):
    pass

    # def test_modulify_a_function_no_args(self) -> None:
    #     @modulify
    #     def test_no_args() -> List[DataStructure]:
    #         return [DataStructure('1234')]

    #     assert test_no_args()[0].id == '1234'

    # def test_modulify_a_function_mod_args(self) -> None:
    #     @modulify(output_types=[DataStructure])
    #     def test_no_args() -> List[DataStructure]:
    #         return [DataStructure('1234')]

    #     assert test_no_args()[0].id == '1234'

    # def test_modulify_a_function_fn_args(self) -> None:
    #     @modulify
    #     def test_no_args(test: DataStructure) -> List[DataStructure]:
    #         return [test]

    #     assert test_no_args('test') == 'test'

    # def test_modulify_a_function_both_args(self) -> None:
    #     @modulify(output_types=[DataStructure])
    #     def test_no_args(test: DataStructure) -> List[DataStructure]:
    #         return [test]

    #     assert test_no_args('test') == 'test'
