# openapi_client.HotmartApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_hotmart_post**](HotmartApi.md#service_hotmart_post) | **POST** /hotmart | Service
[**service_hotmart_whats_get**](HotmartApi.md#service_hotmart_whats_get) | **GET** /hotmart/whats | Service
[**service_hotmart_whats_post**](HotmartApi.md#service_hotmart_whats_post) | **POST** /hotmart/whats | Service


# **service_hotmart_post**
> object service_hotmart_post()

Service

### Example


```python
import openapi_client
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
    api_instance = openapi_client.HotmartApi(api_client)

    try:
        # Service
        api_response = api_instance.service_hotmart_post()
        print("The response of HotmartApi->service_hotmart_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotmartApi->service_hotmart_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **service_hotmart_whats_get**
> object service_hotmart_whats_get()

Service

### Example


```python
import openapi_client
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
    api_instance = openapi_client.HotmartApi(api_client)

    try:
        # Service
        api_response = api_instance.service_hotmart_whats_get()
        print("The response of HotmartApi->service_hotmart_whats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotmartApi->service_hotmart_whats_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **service_hotmart_whats_post**
> object service_hotmart_whats_post()

Service

### Example


```python
import openapi_client
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
    api_instance = openapi_client.HotmartApi(api_client)

    try:
        # Service
        api_response = api_instance.service_hotmart_whats_post()
        print("The response of HotmartApi->service_hotmart_whats_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotmartApi->service_hotmart_whats_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

