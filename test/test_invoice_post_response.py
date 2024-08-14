# coding: utf-8

"""
    API MIOS DIRECT

    API for integration with MIOS DIRECT

    The version of the OpenAPI document: 1.0.30
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.invoice_post_response import InvoicePostResponse

class TestInvoicePostResponse(unittest.TestCase):
    """InvoicePostResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoicePostResponse:
        """Test InvoicePostResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoicePostResponse`
        """
        model = InvoicePostResponse()
        if include_optional:
            return InvoicePostResponse(
                msg = '',
                data = None
            )
        else:
            return InvoicePostResponse(
                msg = '',
                data = None,
        )
        """

    def testInvoicePostResponse(self):
        """Test InvoicePostResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
