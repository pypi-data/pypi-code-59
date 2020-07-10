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
from agilicus_api.models.totp_enrollment_status import TOTPEnrollmentStatus  # noqa: E501
from agilicus_api.rest import ApiException

class TestTOTPEnrollmentStatus(unittest.TestCase):
    """TOTPEnrollmentStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TOTPEnrollmentStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.totp_enrollment_status.TOTPEnrollmentStatus()  # noqa: E501
        if include_optional :
            return TOTPEnrollmentStatus(
                state = 'pending', 
                key = 'asdas43ADlaksda8739asfoafsalkasjd'
            )
        else :
            return TOTPEnrollmentStatus(
        )

    def testTOTPEnrollmentStatus(self):
        """Test TOTPEnrollmentStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
