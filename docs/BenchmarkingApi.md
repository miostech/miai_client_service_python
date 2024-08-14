# openapi_client.BenchmarkingApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_benchmarking**](BenchmarkingApi.md#get_benchmarking) | **GET** /benchmarking/get/benchmarking/{list_benchmarking} | Get benchmarking


# **get_benchmarking**
> TemplatePostResponse get_benchmarking(list_benchmarking)

Get benchmarking

Get benchmarking

### Example


```python
import openapi_client
from openapi_client.models.template_post_response import TemplatePostResponse
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
    api_instance = openapi_client.BenchmarkingApi(api_client)
    list_benchmarking = 'list_benchmarking_example' # str | 

    try:
        # Get benchmarking
        api_response = api_instance.get_benchmarking(list_benchmarking)
        print("The response of BenchmarkingApi->get_benchmarking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenchmarkingApi->get_benchmarking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_benchmarking** | **str**|  | 

### Return type

[**TemplatePostResponse**](TemplatePostResponse.md)

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

