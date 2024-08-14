# openapi_client.SiteSeoApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_site_seo**](SiteSeoApi.md#create_site_seo) | **POST** /site-seo/ | Create site seo
[**return_all_site_seo_to_process**](SiteSeoApi.md#return_all_site_seo_to_process) | **GET** /site-seo/all/to/process | Return all site seo to process
[**return_site_seo_by_base64_url**](SiteSeoApi.md#return_site_seo_by_base64_url) | **GET** /site-seo/{base_64_url}/{id_product} | Return site seo by base 64 url
[**update_site_seo_score**](SiteSeoApi.md#update_site_seo_score) | **PUT** /site-seo/score | Update site seo score


# **create_site_seo**
> SiteSeoPostResponse create_site_seo(site_seo_post)

Create site seo

Create site seo

### Example


```python
import openapi_client
from openapi_client.models.site_seo_post import SiteSeoPost
from openapi_client.models.site_seo_post_response import SiteSeoPostResponse
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
    api_instance = openapi_client.SiteSeoApi(api_client)
    site_seo_post = [openapi_client.SiteSeoPost()] # List[SiteSeoPost] | 

    try:
        # Create site seo
        api_response = api_instance.create_site_seo(site_seo_post)
        print("The response of SiteSeoApi->create_site_seo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteSeoApi->create_site_seo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_seo_post** | [**List[SiteSeoPost]**](SiteSeoPost.md)|  | 

### Return type

[**SiteSeoPostResponse**](SiteSeoPostResponse.md)

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

# **return_all_site_seo_to_process**
> SiteSeoPostResponse return_all_site_seo_to_process()

Return all site seo to process

Return all site seo to process

### Example


```python
import openapi_client
from openapi_client.models.site_seo_post_response import SiteSeoPostResponse
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
    api_instance = openapi_client.SiteSeoApi(api_client)

    try:
        # Return all site seo to process
        api_response = api_instance.return_all_site_seo_to_process()
        print("The response of SiteSeoApi->return_all_site_seo_to_process:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteSeoApi->return_all_site_seo_to_process: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SiteSeoPostResponse**](SiteSeoPostResponse.md)

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

# **return_site_seo_by_base64_url**
> SiteSeoPostResponse return_site_seo_by_base64_url(base_64_url, id_product)

Return site seo by base 64 url

Return site seo by base 64 url

### Example


```python
import openapi_client
from openapi_client.models.site_seo_post_response import SiteSeoPostResponse
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
    api_instance = openapi_client.SiteSeoApi(api_client)
    base_64_url = 'base_64_url_example' # str | 
    id_product = 'id_product_example' # str | 

    try:
        # Return site seo by base 64 url
        api_response = api_instance.return_site_seo_by_base64_url(base_64_url, id_product)
        print("The response of SiteSeoApi->return_site_seo_by_base64_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteSeoApi->return_site_seo_by_base64_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_64_url** | **str**|  | 
 **id_product** | **str**|  | 

### Return type

[**SiteSeoPostResponse**](SiteSeoPostResponse.md)

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

# **update_site_seo_score**
> SiteSeoPutResponse update_site_seo_score(site_seo_put)

Update site seo score

Update site seo score

### Example


```python
import openapi_client
from openapi_client.models.site_seo_put import SiteSeoPut
from openapi_client.models.site_seo_put_response import SiteSeoPutResponse
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
    api_instance = openapi_client.SiteSeoApi(api_client)
    site_seo_put = openapi_client.SiteSeoPut() # SiteSeoPut | 

    try:
        # Update site seo score
        api_response = api_instance.update_site_seo_score(site_seo_put)
        print("The response of SiteSeoApi->update_site_seo_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteSeoApi->update_site_seo_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_seo_put** | [**SiteSeoPut**](SiteSeoPut.md)|  | 

### Return type

[**SiteSeoPutResponse**](SiteSeoPutResponse.md)

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

