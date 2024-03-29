# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from marzban_api.models.user_create import UserCreate

class TestUserCreate(unittest.TestCase):
    """UserCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserCreate:
        """Test UserCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserCreate`
        """
        model = UserCreate()
        if include_optional:
            return UserCreate(
                proxies = {
                    'key' : marzban_api.models.proxy_settings.ProxySettings()
                    },
                expire = 56,
                data_limit = 0.0,
                data_limit_reset_strategy = 'no_reset',
                inbounds = {
                    'key' : [
                        ''
                        ]
                    },
                note = '',
                sub_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sub_last_user_agent = '',
                online_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                on_hold_expire_duration = 56,
                on_hold_timeout = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                username = '',
                status = 'active'
            )
        else:
            return UserCreate(
                username = '',
        )
        """

    def testUserCreate(self):
        """Test UserCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
