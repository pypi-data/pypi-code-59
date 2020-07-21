from adapay_merchant.api import request_tools
from adapay_merchant.api.request_tools import request_post, request_get


class Application(object):

    @classmethod
    def create(cls, **kwargs):
        """
        商户入驻
        """
        return request_post(request_tools.app, kwargs)

    @classmethod
    def query(cls, **kwargs):
        """
         商户入驻查询
        """
        return request_get(request_tools.app, kwargs)


