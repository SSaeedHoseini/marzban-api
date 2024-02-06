# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from marzban-api.models.system_stats import SystemStats

class TestSystemStats(unittest.TestCase):
    """SystemStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemStats:
        """Test SystemStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemStats`
        """
        model = SystemStats()
        if include_optional:
            return SystemStats(
                version = '',
                mem_total = 56,
                mem_used = 56,
                cpu_cores = 56,
                cpu_usage = 1.337,
                total_user = 56,
                users_active = 56,
                incoming_bandwidth = 56,
                outgoing_bandwidth = 56,
                incoming_bandwidth_speed = 56,
                outgoing_bandwidth_speed = 56
            )
        else:
            return SystemStats(
                version = '',
                mem_total = 56,
                mem_used = 56,
                cpu_cores = 56,
                cpu_usage = 1.337,
                total_user = 56,
                users_active = 56,
                incoming_bandwidth = 56,
                outgoing_bandwidth = 56,
                incoming_bandwidth_speed = 56,
                outgoing_bandwidth_speed = 56,
        )
        """

    def testSystemStats(self):
        """Test SystemStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
