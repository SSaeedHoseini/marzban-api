# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from marzban-api.models.node_usage_response import NodeUsageResponse

class TestNodeUsageResponse(unittest.TestCase):
    """NodeUsageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeUsageResponse:
        """Test NodeUsageResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeUsageResponse`
        """
        model = NodeUsageResponse()
        if include_optional:
            return NodeUsageResponse(
                node_id = 56,
                node_name = '',
                uplink = 56,
                downlink = 56
            )
        else:
            return NodeUsageResponse(
                node_name = '',
                uplink = 56,
                downlink = 56,
        )
        """

    def testNodeUsageResponse(self):
        """Test NodeUsageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
