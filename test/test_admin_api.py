# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from marzban_api.api.admin_api import AdminApi


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AdminApi()

    def tearDown(self) -> None:
        pass

    def test_create_admin_api_admin_post(self) -> None:
        """Test case for create_admin_api_admin_post

        Create Admin
        """
        pass

    def test_get_admins_api_admins_get(self) -> None:
        """Test case for get_admins_api_admins_get

        Get Admins
        """
        pass

    def test_get_current_admin_api_admin_get(self) -> None:
        """Test case for get_current_admin_api_admin_get

        Get Current Admin
        """
        pass

    def test_login_for_access_token_api_admin_token_post(self) -> None:
        """Test case for login_for_access_token_api_admin_token_post

        Login For Access Token
        """
        pass

    def test_modify_admin_api_admin_username_put(self) -> None:
        """Test case for modify_admin_api_admin_username_put

        Modify Admin
        """
        pass

    def test_remove_admin_api_admin_username_delete(self) -> None:
        """Test case for remove_admin_api_admin_username_delete

        Remove Admin
        """
        pass


if __name__ == '__main__':
    unittest.main()
