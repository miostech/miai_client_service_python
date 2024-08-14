# openapi_client.BagyApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**return_all_analytics_products_from_bagy**](BagyApi.md#return_all_analytics_products_from_bagy) | **GET** /bagy/get/analytics/products/{id_project} | Return all analytics products from bagy
[**return_all_clients_from_bagy**](BagyApi.md#return_all_clients_from_bagy) | **GET** /bagy/{id_project} | Return all clients from bagy
[**return_all_data_from_analytic**](BagyApi.md#return_all_data_from_analytic) | **GET** /bagy/get-data-from/analytic | Return all data from analytic
[**return_all_products_from_bagy**](BagyApi.md#return_all_products_from_bagy) | **GET** /bagy/get/products/{id_project} | Return all products from bagy


# **return_all_analytics_products_from_bagy**
> TemplatePostResponse return_all_analytics_products_from_bagy(id_project)

Return all analytics products from bagy

Return all analytics products from bagy

### Example

* Bearer Authentication (JwtBearer):

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
    api_instance = openapi_client.BagyApi(api_client)
    id_project = 'id_project_example' # str | 

    try:
        # Return all analytics products from bagy
        api_response = api_instance.return_all_analytics_products_from_bagy(id_project)
        print("The response of BagyApi->return_all_analytics_products_from_bagy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BagyApi->return_all_analytics_products_from_bagy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**|  | 

### Return type

[**TemplatePostResponse**](TemplatePostResponse.md)

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

# **return_all_clients_from_bagy**
> TemplatePostResponse return_all_clients_from_bagy(id_project)

Return all clients from bagy

Return all clients from bagy

### Example

* Bearer Authentication (JwtBearer):

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
    api_instance = openapi_client.BagyApi(api_client)
    id_project = 'id_project_example' # str | 

    try:
        # Return all clients from bagy
        api_response = api_instance.return_all_clients_from_bagy(id_project)
        print("The response of BagyApi->return_all_clients_from_bagy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BagyApi->return_all_clients_from_bagy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**|  | 

### Return type

[**TemplatePostResponse**](TemplatePostResponse.md)

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

# **return_all_data_from_analytic**
> TemplatePostResponse return_all_data_from_analytic()

Return all data from analytic

Return all data from analytic

### Example

* Bearer Authentication (JwtBearer):

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
    api_instance = openapi_client.BagyApi(api_client)

    try:
        # Return all data from analytic
        api_response = api_instance.return_all_data_from_analytic()
        print("The response of BagyApi->return_all_data_from_analytic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BagyApi->return_all_data_from_analytic: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TemplatePostResponse**](TemplatePostResponse.md)

### Authorization

[JwtBearer](../README.md#JwtBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_all_products_from_bagy**
> TemplatePostResponse return_all_products_from_bagy(id_project)

Return all products from bagy

Return all products from bagy

### Example

* Bearer Authentication (JwtBearer):

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
    api_instance = openapi_client.BagyApi(api_client)
    id_project = 'id_project_example' # str | 

    try:
        # Return all products from bagy
        api_response = api_instance.return_all_products_from_bagy(id_project)
        print("The response of BagyApi->return_all_products_from_bagy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BagyApi->return_all_products_from_bagy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**|  | 

### Return type

[**TemplatePostResponse**](TemplatePostResponse.md)

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

