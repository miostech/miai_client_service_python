# coding: utf-8

# flake8: noqa
"""
    API MIAI

    API for integration with MIAI To get started, you need a token where you can get it by do a post request to 'Get account by email and password' and use the token in the header (Authorization: Bearer token) to access the other endpoints 

    The version of the OpenAPI document: 1.0.31
    Contact: oscarsilva@mios.pt
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openapi_client.models.account_post import AccountPost
from openapi_client.models.account_post_response import AccountPostResponse
from openapi_client.models.account_post_response_no_token import AccountPostResponseNoToken
from openapi_client.models.add_bagy_token_product_put import AddBagyTokenProductPut
from openapi_client.models.add_token_meta_product_put import AddTokenMetaProductPut
from openapi_client.models.contact_product_put import ContactProductPut
from openapi_client.models.http_validation_error import HTTPValidationError
from openapi_client.models.invoice_post_response import InvoicePostResponse
from openapi_client.models.product_post import ProductPost
from openapi_client.models.product_post_response import ProductPostResponse
from openapi_client.models.product_put_response import ProductPutResponse
from openapi_client.models.site_seo_post import SiteSeoPost
from openapi_client.models.site_seo_post_response import SiteSeoPostResponse
from openapi_client.models.site_seo_put import SiteSeoPut
from openapi_client.models.site_seo_put_response import SiteSeoPutResponse
from openapi_client.models.template_component import TemplateComponent
from openapi_client.models.template_post import TemplatePost
from openapi_client.models.template_post_response import TemplatePostResponse
from openapi_client.models.validation_error import ValidationError
from openapi_client.models.validation_error_loc_inner import ValidationErrorLocInner
from openapi_client.models.validation_post import ValidationPost
from openapi_client.models.validation_response import ValidationResponse
from openapi_client.models.whatsapp_message_clicked_post import WhatsappMessageClickedPost
from openapi_client.models.whatsapp_message_clicked_post_response import WhatsappMessageClickedPostResponse
from openapi_client.models.whatsapp_message_post import WhatsappMessagePost
from openapi_client.models.whatsapp_message_post_response import WhatsappMessagePostResponse
from openapi_client.models.whatsapp_message_template_post import WhatsappMessageTemplatePost
