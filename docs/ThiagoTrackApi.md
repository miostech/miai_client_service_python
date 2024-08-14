# openapi_client.ThiagoTrackApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coordinates_by_address**](ThiagoTrackApi.md#get_coordinates_by_address) | **GET** /thiago-track/get/coordinates/address/{street}/{number}/{city}/{state} | Get coordinates by address
[**return_trace_route**](ThiagoTrackApi.md#return_trace_route) | **GET** /thiago-track/{pick_lon}/{pick_lat}/{drop_lon}/{drop_lat} | Return trace route


# **get_coordinates_by_address**
> AccountPostResponseNoToken get_coordinates_by_address(street, number, city, state)

Get coordinates by address

Get coordinates by address

### Example

* Bearer Authentication (JwtBearer):

```python
import openapi_client
from openapi_client.models.account_post_response_no_token import AccountPostResponseNoToken
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
    api_instance = openapi_client.ThiagoTrackApi(api_client)
    street = 'street_example' # str | 
    number = 'number_example' # str | 
    city = 'city_example' # str | 
    state = 'state_example' # str | 

    try:
        # Get coordinates by address
        api_response = api_instance.get_coordinates_by_address(street, number, city, state)
        print("The response of ThiagoTrackApi->get_coordinates_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThiagoTrackApi->get_coordinates_by_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **street** | **str**|  | 
 **number** | **str**|  | 
 **city** | **str**|  | 
 **state** | **str**|  | 

### Return type

[**AccountPostResponseNoToken**](AccountPostResponseNoToken.md)

### Authorization

[JwtBearer](../README.md#JwtBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get coordinates by address |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_trace_route**
> AccountPostResponseNoToken return_trace_route(pick_lon, pick_lat, drop_lon, drop_lat)

Return trace route

Return trace route

### Example

* Bearer Authentication (JwtBearer):

```python
import openapi_client
from openapi_client.models.account_post_response_no_token import AccountPostResponseNoToken
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
    api_instance = openapi_client.ThiagoTrackApi(api_client)
    pick_lon = 'pick_lon_example' # str | 
    pick_lat = 'pick_lat_example' # str | 
    drop_lon = 'drop_lon_example' # str | 
    drop_lat = 'drop_lat_example' # str | 

    try:
        # Return trace route
        api_response = api_instance.return_trace_route(pick_lon, pick_lat, drop_lon, drop_lat)
        print("The response of ThiagoTrackApi->return_trace_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThiagoTrackApi->return_trace_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pick_lon** | **str**|  | 
 **pick_lat** | **str**|  | 
 **drop_lon** | **str**|  | 
 **drop_lat** | **str**|  | 

### Return type

[**AccountPostResponseNoToken**](AccountPostResponseNoToken.md)

### Authorization

[JwtBearer](../README.md#JwtBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return trace route |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

