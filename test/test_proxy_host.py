# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from marzban-api.models.proxy_host import ProxyHost

class TestProxyHost(unittest.TestCase):
    """ProxyHost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProxyHost:
        """Test ProxyHost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProxyHost`
        """
        model = ProxyHost()
        if include_optional:
            return ProxyHost(
                remark = '',
                address = '',
                port = 56,
                sni = '',
                host = '',
                security = 'inbound_default',
                alpn = '',
                fingerprint = '',
                allowinsecure = True,
                is_disabled = True
            )
        else:
            return ProxyHost(
                remark = '',
                address = '',
        )
        """

    def testProxyHost(self):
        """Test ProxyHost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
