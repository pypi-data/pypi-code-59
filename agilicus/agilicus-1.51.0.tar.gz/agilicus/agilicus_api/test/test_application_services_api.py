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

import agilicus_api
from agilicus_api.api.application_services_api import ApplicationServicesApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestApplicationServicesApi(unittest.TestCase):
    """ApplicationServicesApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.application_services_api.ApplicationServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_application_service(self):
        """Test case for create_application_service

        Create an ApplicationService  # noqa: E501
        """
        pass

    def test_delete_application_service(self):
        """Test case for delete_application_service

        Remove an ApplicationService  # noqa: E501
        """
        pass

    def test_get_application_service(self):
        """Test case for get_application_service

        Get a single ApplicationService  # noqa: E501
        """
        pass

    def test_list_application_services(self):
        """Test case for list_application_services

        Get a subset of the ApplicationServices  # noqa: E501
        """
        pass

    def test_replace_application_service(self):
        """Test case for replace_application_service

        Create or update an Application Service.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
