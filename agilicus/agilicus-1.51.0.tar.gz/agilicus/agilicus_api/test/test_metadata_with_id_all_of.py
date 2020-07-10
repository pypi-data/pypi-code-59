# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.07.09
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import agilicus_api
from agilicus_api.models.metadata_with_id_all_of import MetadataWithIdAllOf  # noqa: E501
from agilicus_api.rest import ApiException

class TestMetadataWithIdAllOf(unittest.TestCase):
    """MetadataWithIdAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetadataWithIdAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.metadata_with_id_all_of.MetadataWithIdAllOf()  # noqa: E501
        if include_optional :
            return MetadataWithIdAllOf(
                id = '123'
            )
        else :
            return MetadataWithIdAllOf(
        )

    def testMetadataWithIdAllOf(self):
        """Test MetadataWithIdAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
