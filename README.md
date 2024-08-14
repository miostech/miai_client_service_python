# openapi-client
API for integration with MIAI To get started, you need a token where you can get it by do a post request to 'Get account by email and password' and use the token in the header (Authorization: Bearer token) to access the other endpoints 

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.31
- Package version: 1.0.0
- Generator version: 7.7.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://miosdirect.com/](https://miosdirect.com/)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mios-direct.azurewebsites.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mios-direct.azurewebsites.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtBearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountApi(api_client)
    email = 'email_example' # str | 
    id_product = 'id_product_example' # str | 
    rule = 'rule_example' # str | 

    try:
        # Add user in product
        api_response = api_instance.add_user_in_product(email, id_product, rule)
        print("The response of AccountApi->add_user_in_product:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->add_user_in_product: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://mios-direct.azurewebsites.net*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**add_user_in_product**](docs/AccountApi.md#add_user_in_product) | **POST** /account/add/user/in/product/{email}/{id_product}/{rule} | Add user in product
*AccountApi* | [**create_account**](docs/AccountApi.md#create_account) | **POST** /account/ | Create account
*AccountApi* | [**delete_user_in_product**](docs/AccountApi.md#delete_user_in_product) | **DELETE** /account/delete/user/in/product/{email}/{id_product} | Delete user in product
*AccountApi* | [**get_account_by_email_and_password**](docs/AccountApi.md#get_account_by_email_and_password) | **GET** /account/{email}/{password} | Get account by email and password
*AccountApi* | [**get_account_by_token**](docs/AccountApi.md#get_account_by_token) | **GET** /account/me | Get account by token
*AccountApi* | [**get_user_from_product**](docs/AccountApi.md#get_user_from_product) | **GET** /account/user/from/product/{id_product} | Get user from product
*AccountApi* | [**link_payment**](docs/AccountApi.md#link_payment) | **GET** /account/link/payment/{plan}/{email} | Link payment
*AccountApi* | [**service_account_test_thiago_get**](docs/AccountApi.md#service_account_test_thiago_get) | **GET** /account/test-thiago | Service
*BagyApi* | [**return_all_analytics_products_from_bagy**](docs/BagyApi.md#return_all_analytics_products_from_bagy) | **GET** /bagy/get/analytics/products/{id_project} | Return all analytics products from bagy
*BagyApi* | [**return_all_clients_from_bagy**](docs/BagyApi.md#return_all_clients_from_bagy) | **GET** /bagy/{id_project} | Return all clients from bagy
*BagyApi* | [**return_all_data_from_analytic**](docs/BagyApi.md#return_all_data_from_analytic) | **GET** /bagy/get-data-from/analytic | Return all data from analytic
*BagyApi* | [**return_all_products_from_bagy**](docs/BagyApi.md#return_all_products_from_bagy) | **GET** /bagy/get/products/{id_project} | Return all products from bagy
*BenchmarkingApi* | [**get_benchmarking**](docs/BenchmarkingApi.md#get_benchmarking) | **GET** /benchmarking/get/benchmarking/{list_benchmarking} | Get benchmarking
*EnterpriseApi* | [**add_bagy_token_enterprise**](docs/EnterpriseApi.md#add_bagy_token_enterprise) | **PUT** /enterprise/add-bagy-token | Add bagy token to enterprise
*EnterpriseApi* | [**add_business_id_account_enterprise**](docs/EnterpriseApi.md#add_business_id_account_enterprise) | **PUT** /enterprise/add-business-id-account/meta | Add business id account to enterprise
*EnterpriseApi* | [**add_phone_number_enterprise**](docs/EnterpriseApi.md#add_phone_number_enterprise) | **PUT** /enterprise/phone-number/meta | Add phone number to enterprise
*EnterpriseApi* | [**add_token_meta_enterprise**](docs/EnterpriseApi.md#add_token_meta_enterprise) | **PUT** /enterprise/add-token/meta | Add token meta to enterprise
*EnterpriseApi* | [**create_enterprise**](docs/EnterpriseApi.md#create_enterprise) | **POST** /enterprise/ | Create enterprise
*EnterpriseApi* | [**return_all_enterprise**](docs/EnterpriseApi.md#return_all_enterprise) | **GET** /enterprise/all | Return all enterprise
*EnterpriseApi* | [**return_analytics_enterprise**](docs/EnterpriseApi.md#return_analytics_enterprise) | **GET** /enterprise/return/analytics/{enterprise} | Return analytics enterprise
*InvoiceApi* | [**return_invoice_by_email**](docs/InvoiceApi.md#return_invoice_by_email) | **GET** /invoice/{email} | Return invoice by email
*ProductApi* | [**add_bagy_token_product**](docs/ProductApi.md#add_bagy_token_product) | **PUT** /product/add-bagy-token | Add bagy token to product
*ProductApi* | [**add_business_id_account_product**](docs/ProductApi.md#add_business_id_account_product) | **PUT** /product/add-business-id-account/meta | Add business id account to product
*ProductApi* | [**add_phone_number_to_product**](docs/ProductApi.md#add_phone_number_to_product) | **PUT** /product/ | Add phone number to product
*ProductApi* | [**add_token_meta_product**](docs/ProductApi.md#add_token_meta_product) | **PUT** /product/add-token/meta | Add token meta to product
*ProductApi* | [**create_product**](docs/ProductApi.md#create_product) | **POST** /product/ | Create product
*ProductApi* | [**return_all_products**](docs/ProductApi.md#return_all_products) | **GET** /product/all | Return all products
*ProductApi* | [**return_analytics**](docs/ProductApi.md#return_analytics) | **GET** /product/return/analytics/{id_product} | Return analytics
*SiteSeoApi* | [**create_site_seo**](docs/SiteSeoApi.md#create_site_seo) | **POST** /site-seo/ | Create site seo
*SiteSeoApi* | [**return_all_site_seo_to_process**](docs/SiteSeoApi.md#return_all_site_seo_to_process) | **GET** /site-seo/all/to/process | Return all site seo to process
*SiteSeoApi* | [**return_site_seo_by_base64_url**](docs/SiteSeoApi.md#return_site_seo_by_base64_url) | **GET** /site-seo/{base_64_url}/{id_product} | Return site seo by base 64 url
*SiteSeoApi* | [**update_site_seo_score**](docs/SiteSeoApi.md#update_site_seo_score) | **PUT** /site-seo/score | Update site seo score
*TemplateApi* | [**create_template**](docs/TemplateApi.md#create_template) | **POST** /template/ | Create template
*TemplateApi* | [**return_all_templates**](docs/TemplateApi.md#return_all_templates) | **GET** /template/ | Return all template
*TemplateApi* | [**return_all_templates_by_project**](docs/TemplateApi.md#return_all_templates_by_project) | **GET** /template/{id_project} | Return all template by project
*TemplateApi* | [**return_template_by_name**](docs/TemplateApi.md#return_template_by_name) | **GET** /template/by/name/{template_name} | Return template by name
*ThiagoTrackApi* | [**get_coordinates_by_address**](docs/ThiagoTrackApi.md#get_coordinates_by_address) | **GET** /thiago-track/get/coordinates/address/{street}/{number}/{city}/{state} | Get coordinates by address
*ThiagoTrackApi* | [**return_trace_route**](docs/ThiagoTrackApi.md#return_trace_route) | **GET** /thiago-track/{pick_lon}/{pick_lat}/{drop_lon}/{drop_lat} | Return trace route
*ValidationApi* | [**create_validation**](docs/ValidationApi.md#create_validation) | **POST** /validation/ | Create validation
*ValidationApi* | [**get_validation**](docs/ValidationApi.md#get_validation) | **GET** /validation/{code} | Get validation
*WhatsappMessageApi* | [**add_whatsapp_message**](docs/WhatsappMessageApi.md#add_whatsapp_message) | **POST** /whatsapp-message | Add whatsapp message
*WhatsappMessageApi* | [**return_all_messages_by_phone_number_id**](docs/WhatsappMessageApi.md#return_all_messages_by_phone_number_id) | **GET** /whatsapp-message/return/messages/by/phone-number-id/{phone_number_id} | Return all messages by phone number id
*WhatsappMessageApi* | [**return_all_messages_by_wa_id**](docs/WhatsappMessageApi.md#return_all_messages_by_wa_id) | **GET** /whatsapp-message/return/messages/by/wa-id/{wa_id} | Return all messages by wa id
*WhatsappMessageApi* | [**return_all_whatsapp_messages**](docs/WhatsappMessageApi.md#return_all_whatsapp_messages) | **GET** /whatsapp-message/all-whatsapp-messages | Return all whatsapp messages
*WhatsappMessageApi* | [**return_messages_by_wa_id**](docs/WhatsappMessageApi.md#return_messages_by_wa_id) | **GET** /whatsapp-message/grouped/messages/by/wa-id | Return messages by wa id
*WhatsappMessageApi* | [**return_messages_by_wa_id_filtered**](docs/WhatsappMessageApi.md#return_messages_by_wa_id_filtered) | **GET** /whatsapp-message/grouped/messages/by/wa-id/filtered/{wa_id} | Return messages by wa id filtered
*WhatsappMessageApi* | [**send_message**](docs/WhatsappMessageApi.md#send_message) | **POST** /whatsapp-message/sent-message | Send message
*WhatsappMessageApi* | [**send_message_template**](docs/WhatsappMessageApi.md#send_message_template) | **POST** /whatsapp-message/send-message-template | Send message template
*WhatsappMessageClickedApi* | [**create_whatsapp_message_clicked**](docs/WhatsappMessageClickedApi.md#create_whatsapp_message_clicked) | **POST** /whatsapp-message-clicked/ | Create whatsapp_message_clicked


## Documentation For Models

 - [AccountPost](docs/AccountPost.md)
 - [AccountPostResponse](docs/AccountPostResponse.md)
 - [AccountPostResponseNoToken](docs/AccountPostResponseNoToken.md)
 - [AddBagyTokenProductPut](docs/AddBagyTokenProductPut.md)
 - [AddTokenMetaProductPut](docs/AddTokenMetaProductPut.md)
 - [ContactProductPut](docs/ContactProductPut.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [InvoicePostResponse](docs/InvoicePostResponse.md)
 - [ProductPost](docs/ProductPost.md)
 - [ProductPostResponse](docs/ProductPostResponse.md)
 - [ProductPutResponse](docs/ProductPutResponse.md)
 - [SiteSeoPost](docs/SiteSeoPost.md)
 - [SiteSeoPostResponse](docs/SiteSeoPostResponse.md)
 - [SiteSeoPut](docs/SiteSeoPut.md)
 - [SiteSeoPutResponse](docs/SiteSeoPutResponse.md)
 - [TemplateComponent](docs/TemplateComponent.md)
 - [TemplatePost](docs/TemplatePost.md)
 - [TemplatePostResponse](docs/TemplatePostResponse.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [ValidationPost](docs/ValidationPost.md)
 - [ValidationResponse](docs/ValidationResponse.md)
 - [WhatsappMessageClickedPost](docs/WhatsappMessageClickedPost.md)
 - [WhatsappMessageClickedPostResponse](docs/WhatsappMessageClickedPostResponse.md)
 - [WhatsappMessagePost](docs/WhatsappMessagePost.md)
 - [WhatsappMessagePostResponse](docs/WhatsappMessagePostResponse.md)
 - [WhatsappMessageTemplatePost](docs/WhatsappMessageTemplatePost.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="JwtBearer"></a>
### JwtBearer

- **Type**: Bearer authentication


## Author

oscarsilva@mios.pt


