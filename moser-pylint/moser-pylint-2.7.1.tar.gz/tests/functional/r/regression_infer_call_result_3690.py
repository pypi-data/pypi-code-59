# pylint: disable-msg=missing-docstring,too-few-public-methods,using-constant-test

class Class:
    @property
    @classmethod
    def func(cls):
        pass


if Class.func:
    pass
