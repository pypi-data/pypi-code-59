# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
import json


ERROR_MESSAGES = {
    "en": {0: "OK", 1: "Error"},
    "zh-hans": {0: "OK", 1: "Error"},
}
LANGUAGE = "zh-hans"


def set_language(language):
    global LANGUAGE
    language = language.lower()
    LANGUAGE = language

def set_error_message(language, code, message):
    language = language.lower()
    if not language in ERROR_MESSAGES:
        ERROR_MESSAGES[language] = {0: "OK", 1: "Error"}
    ERROR_MESSAGES[language][code] = message

def get_error_message(code, language=None):
    language = language or LANGUAGE
    language = language.lower()
    return ERROR_MESSAGES.get(language, {}).get(code, "No error message...")


class classproperty(property):
    """Subclass property to make classmethod properties possible"""
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()


class BizErrorBase(RuntimeError):
    """Base class of all errors.
    """
    CODE = None

    @classproperty
    @classmethod
    def MESSAGE(cls):
        return get_error_message(cls.CODE)

    def __init__(self, message=None, **kwargs):
        if isinstance(message, self.__class__):
            super().__init__(message.code, message.message)
        else:
            message = message or self.MESSAGE
            if not isinstance(message, str):
                message = str(message)
            if kwargs:
                message = message.format(**kwargs)
            super().__init__(self.CODE, message)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return json.dumps({
            "code": self.args[0],
            "message": self.args[1]
        }, ensure_ascii=False)

    @property
    def code(self):
        return self.args[0]

    @property
    def message(self):
        return self.args[1]

    @property
    def json(self):
        return {
            "code": self.code,
            "message": self.message,
        }


class OK(BizErrorBase):
    CODE = 0

class BizError(BizErrorBase):
    CODE = 1

