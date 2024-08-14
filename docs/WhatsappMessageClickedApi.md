# openapi_client.WhatsappMessageClickedApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_whatsapp_message_clicked**](WhatsappMessageClickedApi.md#create_whatsapp_message_clicked) | **POST** /whatsapp-message-clicked/ | Create whatsapp_message_clicked


# **create_whatsapp_message_clicked**
> WhatsappMessageClickedPostResponse create_whatsapp_message_clicked(whatsapp_message_clicked_post)

Create whatsapp_message_clicked

Create whatsapp_message_clicked

### Example


```python
import openapi_client
from openapi_client.models.whatsapp_message_clicked_post import WhatsappMessageClickedPost
from openapi_client.models.whatsapp_message_clicked_post_response import WhatsappMessageClickedPostResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mios-direct.azurewebsites.net
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mios-direct.azurewebsites.net"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WhatsappMessageClickedApi(api_client)
    whatsapp_message_clicked_post = openapi_client.WhatsappMessageClickedPost() # WhatsappMessageClickedPost | 

    try:
        # Create whatsapp_message_clicked
        api_response = api_instance.create_whatsapp_message_clicked(whatsapp_message_clicked_post)
        print("The response of WhatsappMessageClickedApi->create_whatsapp_message_clicked:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappMessageClickedApi->create_whatsapp_message_clicked: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whatsapp_message_clicked_post** | [**WhatsappMessageClickedPost**](WhatsappMessageClickedPost.md)|  | 

### Return type

[**WhatsappMessageClickedPostResponse**](WhatsappMessageClickedPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

