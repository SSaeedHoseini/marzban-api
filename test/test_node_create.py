# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from marzban_api.models.node_create import NodeCreate

class TestNodeCreate(unittest.TestCase):
    """NodeCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeCreate:
        """Test NodeCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeCreate`
        """
        model = NodeCreate()
        if include_optional:
            return NodeCreate(
                name = '',
                address = '',
                port = 56,
                api_port = 56,
                usage_coefficient = 1.337,
                add_as_new_host = True
            )
        else:
            return NodeCreate(
                name = '',
                address = '',
        )
        """

    def testNodeCreate(self):
        """Test NodeCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
