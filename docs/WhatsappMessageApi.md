# openapi_client.WhatsappMessageApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_whatsapp_message**](WhatsappMessageApi.md#add_whatsapp_message) | **POST** /whatsapp-message | Add whatsapp message
[**return_all_messages_by_phone_number_id**](WhatsappMessageApi.md#return_all_messages_by_phone_number_id) | **GET** /whatsapp-message/return/messages/by/phone-number-id/{phone_number_id} | Return all messages by phone number id
[**return_all_messages_by_wa_id**](WhatsappMessageApi.md#return_all_messages_by_wa_id) | **GET** /whatsapp-message/return/messages/by/wa-id/{wa_id} | Return all messages by wa id
[**return_all_whatsapp_messages**](WhatsappMessageApi.md#return_all_whatsapp_messages) | **GET** /whatsapp-message/all-whatsapp-messages | Return all whatsapp messages
[**return_messages_by_wa_id**](WhatsappMessageApi.md#return_messages_by_wa_id) | **GET** /whatsapp-message/grouped/messages/by/wa-id | Return messages by wa id
[**return_messages_by_wa_id_filtered**](WhatsappMessageApi.md#return_messages_by_wa_id_filtered) | **GET** /whatsapp-message/grouped/messages/by/wa-id/filtered/{wa_id} | Return messages by wa id filtered
[**send_message**](WhatsappMessageApi.md#send_message) | **POST** /whatsapp-message/sent-message | Send message
[**send_message_template**](WhatsappMessageApi.md#send_message_template) | **POST** /whatsapp-message/send-message-template | Send message template


# **add_whatsapp_message**
> WhatsappMessagePostResponse add_whatsapp_message(whatsapp_message_post)

Add whatsapp message

Add whatsapp message

### Example


```python
import openapi_client
from openapi_client.models.whatsapp_message_post import WhatsappMessagePost
from openapi_client.models.whatsapp_message_post_response import WhatsappMessagePostResponse
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
    api_instance = openapi_client.WhatsappMessageApi(api_client)
    whatsapp_message_post = openapi_client.WhatsappMessagePost() # WhatsappMessagePost | 

    try:
        # Add whatsapp message
        api_response = api_instance.add_whatsapp_message(whatsapp_message_post)
        print("The response of WhatsappMessageApi->add_whatsapp_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappMessageApi->add_whatsapp_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whatsapp_message_post** | [**WhatsappMessagePost**](WhatsappMessagePost.md)|  | 

### Return type

[**WhatsappMessagePostResponse**](WhatsappMessagePostResponse.md)

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

# **return_all_messages_by_phone_number_id**
> WhatsappMessagePostResponse return_all_messages_by_phone_number_id(phone_number_id)

Return all messages by phone number id

Return all messages by phone number id

### Example


```python
import openapi_client
from openapi_client.models.whatsapp_message_post_response import WhatsappMessagePostResponse
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
    api_instance = openapi_client.WhatsappMessageApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Return all messages by phone number id
        api_response = api_instance.return_all_messages_by_phone_number_id(phone_number_id)
        print("The response of WhatsappMessageApi->return_all_messages_by_phone_number_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappMessageApi->return_all_messages_by_phone_number_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

### Return type

[**WhatsappMessagePostResponse**](WhatsappMessagePostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_all_messages_by_wa_id**
> WhatsappMessagePostResponse return_all_messages_by_wa_id(wa_id)

Return all messages by wa id

Return all messages by wa id

### Example


```python
import openapi_client
from openapi_client.models.whatsapp_message_post_response import WhatsappMessagePostResponse
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
    api_instance = openapi_client.WhatsappMessageApi(api_client)
    wa_id = 'wa_id_example' # str | 

    try:
        # Return all messages by wa id
        api_response = api_instance.return_all_messages_by_wa_id(wa_id)
        print("The response of WhatsappMessageApi->return_all_messages_by_wa_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappMessageApi->return_all_messages_by_wa_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wa_id** | **str**|  | 

### Return type

[**WhatsappMessagePostResponse**](WhatsappMessagePostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_all_whatsapp_messages**
> WhatsappMessagePostResponse return_all_whatsapp_messages()

Return all whatsapp messages

Return all whatsapp messages

### Example


```python
import openapi_client
from openapi_client.models.whatsapp_message_post_response import WhatsappMessagePostResponse
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
    api_instance = openapi_client.WhatsappMessageApi(api_client)

    try:
        # Return all whatsapp messages
        api_response = api_instance.return_all_whatsapp_messages()
        print("The response of WhatsappMessageApi->return_all_whatsapp_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappMessageApi->return_all_whatsapp_messages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WhatsappMessagePostResponse**](WhatsappMessagePostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_messages_by_wa_id**
> WhatsappMessagePostResponse return_messages_by_wa_id()

Return messages by wa id

Return messages by wa id

### Example


```python
import openapi_client
from openapi_client.models.whatsapp_message_post_response import WhatsappMessagePostResponse
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
    api_instance = openapi_client.WhatsappMessageApi(api_client)

    try:
        # Return messages by wa id
        api_response = api_instance.return_messages_by_wa_id()
        print("The response of WhatsappMessageApi->return_messages_by_wa_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappMessageApi->return_messages_by_wa_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WhatsappMessagePostResponse**](WhatsappMessagePostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_messages_by_wa_id_filtered**
> WhatsappMessagePostResponse return_messages_by_wa_id_filtered(wa_id)

Return messages by wa id filtered

Return messages by wa id filtered

### Example


```python
import openapi_client
from openapi_client.models.whatsapp_message_post_response import WhatsappMessagePostResponse
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
    api_instance = openapi_client.WhatsappMessageApi(api_client)
    wa_id = 'wa_id_example' # str | 

    try:
        # Return messages by wa id filtered
        api_response = api_instance.return_messages_by_wa_id_filtered(wa_id)
        print("The response of WhatsappMessageApi->return_messages_by_wa_id_filtered:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappMessageApi->return_messages_by_wa_id_filtered: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wa_id** | **str**|  | 

### Return type

[**WhatsappMessagePostResponse**](WhatsappMessagePostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> WhatsappMessagePostResponse send_message(whatsapp_message_post)

Send message

Send message

### Example


```python
import openapi_client
from openapi_client.models.whatsapp_message_post import WhatsappMessagePost
from openapi_client.models.whatsapp_message_post_response import WhatsappMessagePostResponse
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
    api_instance = openapi_client.WhatsappMessageApi(api_client)
    whatsapp_message_post = openapi_client.WhatsappMessagePost() # WhatsappMessagePost | 

    try:
        # Send message
        api_response = api_instance.send_message(whatsapp_message_post)
        print("The response of WhatsappMessageApi->send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappMessageApi->send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whatsapp_message_post** | [**WhatsappMessagePost**](WhatsappMessagePost.md)|  | 

### Return type

[**WhatsappMessagePostResponse**](WhatsappMessagePostResponse.md)

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

# **send_message_template**
> WhatsappMessagePostResponse send_message_template(whatsapp_message_template_post)

Send message template

Send message template

### Example


```python
import openapi_client
from openapi_client.models.whatsapp_message_post_response import WhatsappMessagePostResponse
from openapi_client.models.whatsapp_message_template_post import WhatsappMessageTemplatePost
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
    api_instance = openapi_client.WhatsappMessageApi(api_client)
    whatsapp_message_template_post = openapi_client.WhatsappMessageTemplatePost() # WhatsappMessageTemplatePost | 

    try:
        # Send message template
        api_response = api_instance.send_message_template(whatsapp_message_template_post)
        print("The response of WhatsappMessageApi->send_message_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappMessageApi->send_message_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whatsapp_message_template_post** | [**WhatsappMessageTemplatePost**](WhatsappMessageTemplatePost.md)|  | 

### Return type

[**WhatsappMessagePostResponse**](WhatsappMessagePostResponse.md)

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

