# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from marzban_api.api.system_api import SystemApi


class TestSystemApi(unittest.TestCase):
    """SystemApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SystemApi()

    def tearDown(self) -> None:
        pass

    def test_get_hosts_api_hosts_get(self) -> None:
        """Test case for get_hosts_api_hosts_get

        Get Hosts
        """
        pass

    def test_get_inbounds_api_inbounds_get(self) -> None:
        """Test case for get_inbounds_api_inbounds_get

        Get Inbounds
        """
        pass

    def test_get_system_stats_api_system_get(self) -> None:
        """Test case for get_system_stats_api_system_get

        Get System Stats
        """
        pass

    def test_modify_hosts_api_hosts_put(self) -> None:
        """Test case for modify_hosts_api_hosts_put

        Modify Hosts
        """
        pass


if __name__ == '__main__':
    unittest.main()
