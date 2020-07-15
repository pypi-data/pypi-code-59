import requests
import json
from jinja2 import Template
import pytest
import assertions

HOST_URL = ['shared-vpclink-nlb-latest-tea2-dcd6d62d99a127f5.elb.us-east-1.amazonaws.com']


def _trigger_requests(req_method, url, header, data, proxies=None):
    print("\n\nRegenerating traffic from CloudVector events....")
    return requests.request(method=req_method, url=url, proxies=proxies, headers=header, data=data, verify=False)


def test_series_seriespreview_seriesid(seriesId):
    data = {}
    data["seriesId"] = seriesId
    
    req = {
             "data": data,
             "headers": {'Authorization': 'khkhkhk', 'BodyId': 123, 'Origin-RequestId': ''}
          }
    url = Template("/v1/series/seriesPreview/{{seriesId}}").render(**data)
    resp = _trigger_requests("get", url,
                      header=req["headers"],
                      data=json.dumps(data))
    print(resp.status_code)
    print(resp.text)
    assertions.assert_for_series_seriesPreview_seriesId(req,resp)


