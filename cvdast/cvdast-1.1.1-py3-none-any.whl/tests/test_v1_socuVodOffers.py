import requests
import json
from jinja2 import Template
import pytest
import assertions

HOST_URL = ['shared-vpclink-nlb-latest-tea2-dcd6d62d99a127f5.elb.us-east-1.amazonaws.com']


def _trigger_requests(req_method, url, header, data, proxies=None):
    print("\n\nRegenerating traffic from CloudVector events....")
    return requests.request(method=req_method, url=url, proxies=proxies, headers=header, data=data, verify=False)


def test_v1_socuvodoffers():
    data = {}
    
    req = {
             "data": data,
             "headers": {'Accept': '*/*', 'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'en', 'Authorization': 'khkhkhk', 'Bodyid': 'tsn:A7F000001676839', 'Connection': 'Keep-Alive', 'Content-Type': 'application/json', 'User-Agent': 'Automation-QA', 'X-Amzn-Apigateway-Api-Id': 'x5eycc06si', 'X-Amzn-Trace-Id': 'Root=1-5f0f28c3-cfea1c800ca982e8e635d8a8', 'X-Forwarded-For': '52.86.16.176', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https', 'Apsrequestid': '1@aps-discovery-ts-latest-01.tea2.tivo.com-26574-1594828995603', 'Content-Length': '2', 'Set-Cookie-params': None}
          }
    url = Template("shared-vpclink-nlb-latest-tea2-dcd6d62d99a127f5.elb.us-east-1.amazonaws.comhttp://shared-vpclink-nlb-latest-tea2-dcd6d62d99a127f5.elb.us-east-1.amazonaws.com/v1/socuVodOffers").render(**data)
    resp = _trigger_requests("GET", url,
                      header=req["headers"],
                      data=json.dumps(data))
    print(resp.status_code)
    print(resp.text)
    assertions.assert_for_v1_socuVodOffers(req,resp)


