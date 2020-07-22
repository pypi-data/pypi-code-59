from typing import List, Optional, Tuple


class StrType:
    def __init__(self, t: str, verbose: Optional[str] = None):
        self.t = t
        self.verbose = verbose

    def __str__(self):
        return self.t

    def __repr__(self):
        return "<StrType: {}>".format(self.t)

    def __eq__(self, o: object):
        return self.t == o


class StrTyped:
    # StrType objects here

    @classmethod
    def all_strtypes(cls) -> List[StrType]:
        return [st for st in cls.__dict__.values() if isinstance(st, StrType)]

    def __str__(self):
        return "StrTyped object"

    def __repr__(self):
        return "<StrTyped: {}>".format(", ".join(st.t for st in self.all_strtypes()))


class DjangoStrTyped(StrTyped):
    @classmethod
    def choices_style(cls) -> List[Tuple[str, str]]:
        return [(st.t, st.verbose or "") for st in cls.all_strtypes()]
