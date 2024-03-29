# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from marzban_api.models.admin_modify import AdminModify

class TestAdminModify(unittest.TestCase):
    """AdminModify unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdminModify:
        """Test AdminModify
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdminModify`
        """
        model = AdminModify()
        if include_optional:
            return AdminModify(
                password = '',
                is_sudo = True
            )
        else:
            return AdminModify(
                password = '',
                is_sudo = True,
        )
        """

    def testAdminModify(self):
        """Test AdminModify"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
