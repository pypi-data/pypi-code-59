from .stop_words import STOP_WORDS
from ...language import Language
from ...attrs import LANG


class MarathiDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters[LANG] = lambda text: "mr"
    stop_words = STOP_WORDS


class Marathi(Language):
    lang = "mr"
    Defaults = MarathiDefaults


__all__ = ["Marathi"]
