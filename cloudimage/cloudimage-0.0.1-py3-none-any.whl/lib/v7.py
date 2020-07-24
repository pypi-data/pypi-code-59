from cloudimage.constants import DEFAULT_DOMAIN
from cloudimage.lib.base import BaseHandler
from cloudimage.constants import v7_operators, v7_filters

class URLHandler(BaseHandler):
    def __init__(self, token, domain=DEFAULT_DOMAIN, salt="", active_salt="", SCRSET="w"):
        super(URLHandler, self).__init__(token, domain=DEFAULT_DOMAIN, salt="", active_salt="", SCRSET="w")
        self.version = "v7"

    def _setFilter(self, filter, value=None):
        if self._check_values(filter, value, v7_filters):
            self.filters[filter] = str(value)

    def _setOperator(self, operator, value=None):
        if self._check_values(operator, value, v7_operators):
            self.operators[operator] = str(value)

    def createURL(self, path, operators={}, filters={}):
        self._reset_works()
        for operator, value in operators.items():
            self._setOperator(operator, value)
        for filter, value in filters.items():
            self._setFilter(filter, value)

        operator_path = '&'.join(["%s=%s" % item for item in self.operators.items()])
        filter_path = '&'.join(["%s=%s" % item for item in self.filters.items()])
        query_path = '&'.join([operator_path, filter_path])
        return self.token + "." + self.domain + "/" + self.version + "/" + path + "?" + query_path