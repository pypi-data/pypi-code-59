from cloudimage.constants import DEFAULT_DOMAIN
from cloudimage.lib.base import BaseHandler
from cloudimage.constants import v6_operators, v6_filters, v6_params

class URLHandler(BaseHandler):
    def __init__(self, token, domain=DEFAULT_DOMAIN, salt="", active_salt="", SCRSET="w"):
        super(URLHandler, self).__init__(token, domain=DEFAULT_DOMAIN, salt="", active_salt="", SCRSET="w")
        self.version = "v6"

    def _setFilter(self, filter, value=None):
        if self._check_values(filter, value, v6_filters):
            if not value is None:
                self.filters[filter] = str(value)
            else:
                self.filters[filter] = None
    def _setOperator(self, operator, value=None):
        if self._check_values(operator, value, v6_operators):
            if not value is None:
                self.operators[operator] = str(value)
            else:
                self.operators[operator] = None
    def _setParam(self, param, value=None):
        if self._check_values(param, value, v6_params):
            if not value is None:
                self.params[param] = str(value)
            else:
                self.params[param] = None

    def createURL(self, path, operators={}, filters={}, params={}):
        self._reset_works()
        for operator, value in operators.items():
            self._setOperator(operator, value)
            break
        for filter, value in filters.items():
            self._setFilter(filter, value)
        if len(self.operators) == 0 and len(self.filters) == 0:
            self._setOperator("cdn")
        elif len(self.operators) == 0:
            self._setOperator("cdno")
        for param, value in params.items():
            self._setParam(param, value)

        operator_path = '.'.join(["%s/%s" % (op, va) if ((not va is None) and (not va == "")) else "%s/n" % op for op, va in self.operators.items()])
        filter_path = '.'.join(["%s%s" % item for item in self.filters.items()])
        if filter_path is None or filter_path == "":
            filter_path = "n"
        param_path = '&'.join(["%s=%s" % item for item in self.params.items()])
        return self.token + "." + self.domain + "/" + operator_path + "/" + filter_path + "/" + path + ("?" + param_path if param_path != "" else "")