from cloudimage.constants import DEFAULT_DOMAIN
from cloudimage.exceptions import FilterNotGood

import re

class BaseHandler:
    def validate_domain(self, domain):
        import re
        pattern = re.compile("^.+\\..+$")
        if pattern.match(domain):
            return True
        return False

    def _check_values(self, filter, value, filters):
        for _filter in filters:
            if filter in _filter["name_list"]:
                _value_reg = _filter["value_reg"]
                if (_value_reg is None or _value_reg == "") and (value is None or value == ""):
                    return True
                pattern = re.compile("^" + _value_reg + "$")
                if pattern.match(str(value)):
                    return True

        raise FilterNotGood(filter, filters)

    def _reset_works(self):
        self.filters = {}
        self.operators = {}
        self.params = {}

    def __init__(self, token, domain=DEFAULT_DOMAIN, salt="", active_salt="", SCRSET="w"):
        self.token = token
        self.salt = salt
        self.active_salt = active_salt
        self.SCRSET = SCRSET
        self.filters = {}
        self.operators = {}
        self.params = {}

        if self.validate_domain(domain):
            self.domain = domain
        else:
            self.domain = DEFAULT_DOMAIN

    def printinfo(self):
        print(self.token)
        print(self.domain)
        print(self.version)

