# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.inline_response20012 import InlineResponse20012  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestInlineResponse20012(unittest.TestCase):
    """InlineResponse20012 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20012
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.inline_response20012.InlineResponse20012()  # noqa: E501
        if include_optional :
            return InlineResponse20012(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    pulpcore.client.pulp_rpm.models.rpm/rpm_remote.rpm.RpmRemote(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        url = '0', 
                        ca_cert = '0', 
                        client_cert = '0', 
                        client_key = '0', 
                        tls_validation = True, 
                        proxy_url = '0', 
                        username = '0', 
                        password = '0', 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        download_concurrency = 1, 
                        policy = 'immediate', 
                        sles_auth_token = '0', )
                    ]
            )
        else :
            return InlineResponse20012(
                count = 56,
                results = [
                    pulpcore.client.pulp_rpm.models.rpm/rpm_remote.rpm.RpmRemote(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        url = '0', 
                        ca_cert = '0', 
                        client_cert = '0', 
                        client_key = '0', 
                        tls_validation = True, 
                        proxy_url = '0', 
                        username = '0', 
                        password = '0', 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        download_concurrency = 1, 
                        policy = 'immediate', 
                        sles_auth_token = '0', )
                    ],
        )

    def testInlineResponse20012(self):
        """Test InlineResponse20012"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
