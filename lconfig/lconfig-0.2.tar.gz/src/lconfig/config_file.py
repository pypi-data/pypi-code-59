from functools import reduce
import yaml
import operator


class ConfigFile:

    file: str
    config: dict

    def __init__(self, file: str):
        self.file = file
        self.config = self.read(self.file)

    def find(self, element: str) -> dict:
        return reduce(operator.getitem, element.split('.'), self.config)

    @staticmethod
    def read(file: str) -> dict:
        with open(file, 'r') as stream:
            result = yaml.safe_load(stream)
        return result or {}
