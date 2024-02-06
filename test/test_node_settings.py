# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from marzban_api.models.node_settings import NodeSettings

class TestNodeSettings(unittest.TestCase):
    """NodeSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeSettings:
        """Test NodeSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeSettings`
        """
        model = NodeSettings()
        if include_optional:
            return NodeSettings(
                min_node_version = 'v0.2.0',
                certificate = ''
            )
        else:
            return NodeSettings(
                certificate = '',
        )
        """

    def testNodeSettings(self):
        """Test NodeSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
