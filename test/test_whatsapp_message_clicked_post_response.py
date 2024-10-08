# coding: utf-8

"""
    API MIOS DIRECT

    API for integration with MIOS DIRECT

    The version of the OpenAPI document: 1.0.30
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.whatsapp_message_clicked_post_response import WhatsappMessageClickedPostResponse

class TestWhatsappMessageClickedPostResponse(unittest.TestCase):
    """WhatsappMessageClickedPostResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WhatsappMessageClickedPostResponse:
        """Test WhatsappMessageClickedPostResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WhatsappMessageClickedPostResponse`
        """
        model = WhatsappMessageClickedPostResponse()
        if include_optional:
            return WhatsappMessageClickedPostResponse(
                msg = '',
                data = None
            )
        else:
            return WhatsappMessageClickedPostResponse(
                msg = '',
                data = None,
        )
        """

    def testWhatsappMessageClickedPostResponse(self):
        """Test WhatsappMessageClickedPostResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
