# -*- coding: utf-8 -*-
"""
client for EKCA service -- JSON API requests
"""

import json
import urllib.request

# MIME-type sent in requests and expected in responses
JSON_MEDIA_TYPE = 'application/json'


__all__ = [
    'EKCARequest',
    'EKCAUserCertRequest',
]


class EKCARequest(object):
    """
    base class for request sent to EKCA service
    """
    url_format = '{baseurl}/{ca_name}'
    method = 'POST'
    http_headers = {
        'Accept': JSON_MEDIA_TYPE,
        'Content-type': JSON_MEDIA_TYPE,
    }

    def __init__(self, base_url, ca_name, **payload):
        # strip trailing slash from base URL
        if base_url.endswith('/'):
            base_url = base_url[:-1]
        if ca_name:
            base_url = '{base_url}/{ca_name}'.format(base_url=base_url, ca_name=ca_name)
        # strip trailing slash from request URL
        if base_url.endswith('/'):
            base_url = base_url[:-1]
        self._base_url = base_url
        self._payload = payload

    @property
    def _req_url(self):
        return self.url_format.format(baseurl=self._base_url)

    def req(self, cafile=None):
        """
        actually send the request
        """
        http_req = urllib.request.Request(
            self._req_url,
            data=json.dumps(self._payload).encode('utf-8'),
            headers=self.http_headers,
            origin_req_host=None,
            unverifiable=False,
            method=self.method,
        )
        return urllib.request.urlopen(http_req, cafile=cafile)


class EKCAUserCertRequest(EKCARequest):
    """
    class for user certificate request sent to EKCA service
    """
    url_format = '{baseurl}/usercert'
