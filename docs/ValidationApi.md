# openapi_client.ValidationApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_validation**](ValidationApi.md#create_validation) | **POST** /validation/ | Create validation
[**get_validation**](ValidationApi.md#get_validation) | **GET** /validation/{code} | Get validation


# **create_validation**
> ValidationResponse create_validation(validation_post)

Create validation

Create validation

### Example


```python
import openapi_client
from openapi_client.models.validation_post import ValidationPost
from openapi_client.models.validation_response import ValidationResponse
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
    api_instance = openapi_client.ValidationApi(api_client)
    validation_post = openapi_client.ValidationPost() # ValidationPost | 

    try:
        # Create validation
        api_response = api_instance.create_validation(validation_post)
        print("The response of ValidationApi->create_validation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationApi->create_validation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_post** | [**ValidationPost**](ValidationPost.md)|  | 

### Return type

[**ValidationResponse**](ValidationResponse.md)

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

# **get_validation**
> ValidationResponse get_validation(code)

Get validation

Get validation

### Example


```python
import openapi_client
from openapi_client.models.validation_response import ValidationResponse
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
    api_instance = openapi_client.ValidationApi(api_client)
    code = 'code_example' # str | 

    try:
        # Get validation
        api_response = api_instance.get_validation(code)
        print("The response of ValidationApi->get_validation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationApi->get_validation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**ValidationResponse**](ValidationResponse.md)

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

