# openapi_client.InvoiceApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**return_invoice_by_email**](InvoiceApi.md#return_invoice_by_email) | **GET** /invoice/{email} | Return invoice by email


# **return_invoice_by_email**
> InvoicePostResponse return_invoice_by_email(email)

Return invoice by email

Return invoice by email

### Example

* Bearer Authentication (JwtBearer):

```python
import openapi_client
from openapi_client.models.invoice_post_response import InvoicePostResponse
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
    api_instance = openapi_client.InvoiceApi(api_client)
    email = 'email_example' # str | 

    try:
        # Return invoice by email
        api_response = api_instance.return_invoice_by_email(email)
        print("The response of InvoiceApi->return_invoice_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->return_invoice_by_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**InvoicePostResponse**](InvoicePostResponse.md)

### Authorization

[JwtBearer](../README.md#JwtBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

