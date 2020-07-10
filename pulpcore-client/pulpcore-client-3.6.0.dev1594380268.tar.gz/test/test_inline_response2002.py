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

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.inline_response2002 import InlineResponse2002  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestInlineResponse2002(unittest.TestCase):
    """InlineResponse2002 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2002
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.inline_response2002.InlineResponse2002()  # noqa: E501
        if include_optional :
            return InlineResponse2002(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    pulpcore.client.pulpcore.models.pulp_export.PulpExport(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        task = '0', 
                        exported_resources = [
                            pulpcore.client.pulpcore.models.exported_resources.ExportedResources()
                            ], 
                        params = pulpcore.client.pulpcore.models.params.Params(), 
                        output_file_info = pulpcore.client.pulpcore.models.output_file_info.Output file info(), )
                    ]
            )
        else :
            return InlineResponse2002(
                count = 56,
                results = [
                    pulpcore.client.pulpcore.models.pulp_export.PulpExport(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        task = '0', 
                        exported_resources = [
                            pulpcore.client.pulpcore.models.exported_resources.ExportedResources()
                            ], 
                        params = pulpcore.client.pulpcore.models.params.Params(), 
                        output_file_info = pulpcore.client.pulpcore.models.output_file_info.Output file info(), )
                    ],
        )

    def testInlineResponse2002(self):
        """Test InlineResponse2002"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
