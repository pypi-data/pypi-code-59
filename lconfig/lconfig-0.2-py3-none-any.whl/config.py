from typing import Optional


class Config:

    values: dict

    def __init__(self, values: dict):
        self.values = values

    def get(self, key: str) -> Optional[str]:
        try:
            result = self.values[key]
        except KeyError:
            result = None
        return result
