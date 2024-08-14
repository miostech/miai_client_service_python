# openapi_client.EnterpriseApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bagy_token_enterprise**](EnterpriseApi.md#add_bagy_token_enterprise) | **PUT** /enterprise/add-bagy-token | Add bagy token to enterprise
[**add_business_id_account_enterprise**](EnterpriseApi.md#add_business_id_account_enterprise) | **PUT** /enterprise/add-business-id-account/meta | Add business id account to enterprise
[**add_phone_number_enterprise**](EnterpriseApi.md#add_phone_number_enterprise) | **PUT** /enterprise/phone-number/meta | Add phone number to enterprise
[**add_token_meta_enterprise**](EnterpriseApi.md#add_token_meta_enterprise) | **PUT** /enterprise/add-token/meta | Add token meta to enterprise
[**create_enterprise**](EnterpriseApi.md#create_enterprise) | **POST** /enterprise/ | Create enterprise
[**return_all_enterprise**](EnterpriseApi.md#return_all_enterprise) | **GET** /enterprise/all | Return all enterprise
[**return_analytics_enterprise**](EnterpriseApi.md#return_analytics_enterprise) | **GET** /enterprise/return/analytics/{id_product} | Return analytics enterprise


# **add_bagy_token_enterprise**
> ProductPostResponse add_bagy_token_enterprise(add_bagy_token_product_put)

Add bagy token to enterprise

Add bagy token to enterprise

### Example

* Bearer Authentication (JwtBearer):

```python
import openapi_client
from openapi_client.models.add_bagy_token_product_put import AddBagyTokenProductPut
from openapi_client.models.product_post_response import ProductPostResponse
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
    api_instance = openapi_client.EnterpriseApi(api_client)
    add_bagy_token_product_put = openapi_client.AddBagyTokenProductPut() # AddBagyTokenProductPut | 

    try:
        # Add bagy token to enterprise
        api_response = api_instance.add_bagy_token_enterprise(add_bagy_token_product_put)
        print("The response of EnterpriseApi->add_bagy_token_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->add_bagy_token_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_bagy_token_product_put** | [**AddBagyTokenProductPut**](AddBagyTokenProductPut.md)|  | 

### Return type

[**ProductPostResponse**](ProductPostResponse.md)

### Authorization

[JwtBearer](../README.md#JwtBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_business_id_account_enterprise**
> ProductPutResponse add_business_id_account_enterprise(add_token_meta_product_put)

Add business id account to enterprise

This endpoint is used to add business id account to enterprise.

### Example

* Bearer Authentication (JwtBearer):

```python
import openapi_client
from openapi_client.models.add_token_meta_product_put import AddTokenMetaProductPut
from openapi_client.models.product_put_response import ProductPutResponse
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
    api_instance = openapi_client.EnterpriseApi(api_client)
    add_token_meta_product_put = openapi_client.AddTokenMetaProductPut() # AddTokenMetaProductPut | 

    try:
        # Add business id account to enterprise
        api_response = api_instance.add_business_id_account_enterprise(add_token_meta_product_put)
        print("The response of EnterpriseApi->add_business_id_account_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->add_business_id_account_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_token_meta_product_put** | [**AddTokenMetaProductPut**](AddTokenMetaProductPut.md)|  | 

### Return type

[**ProductPutResponse**](ProductPutResponse.md)

### Authorization

[JwtBearer](../README.md#JwtBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_phone_number_enterprise**
> ProductPostResponse add_phone_number_enterprise(contact_product_put)

Add phone number to enterprise

This endpoint is used to add a phone number to an enterprise.

### Example

* Bearer Authentication (JwtBearer):

```python
import openapi_client
from openapi_client.models.contact_product_put import ContactProductPut
from openapi_client.models.product_post_response import ProductPostResponse
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
    api_instance = openapi_client.EnterpriseApi(api_client)
    contact_product_put = openapi_client.ContactProductPut() # ContactProductPut | 

    try:
        # Add phone number to enterprise
        api_response = api_instance.add_phone_number_enterprise(contact_product_put)
        print("The response of EnterpriseApi->add_phone_number_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->add_phone_number_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_product_put** | [**ContactProductPut**](ContactProductPut.md)|  | 

### Return type

[**ProductPostResponse**](ProductPostResponse.md)

### Authorization

[JwtBearer](../README.md#JwtBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_token_meta_enterprise**
> ProductPutResponse add_token_meta_enterprise(add_token_meta_product_put)

Add token meta to enterprise

This endpoint is used to add token meta to enterprise.

### Example

* Bearer Authentication (JwtBearer):

```python
import openapi_client
from openapi_client.models.add_token_meta_product_put import AddTokenMetaProductPut
from openapi_client.models.product_put_response import ProductPutResponse
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
    api_instance = openapi_client.EnterpriseApi(api_client)
    add_token_meta_product_put = openapi_client.AddTokenMetaProductPut() # AddTokenMetaProductPut | 

    try:
        # Add token meta to enterprise
        api_response = api_instance.add_token_meta_enterprise(add_token_meta_product_put)
        print("The response of EnterpriseApi->add_token_meta_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->add_token_meta_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_token_meta_product_put** | [**AddTokenMetaProductPut**](AddTokenMetaProductPut.md)|  | 

### Return type

[**ProductPutResponse**](ProductPutResponse.md)

### Authorization

[JwtBearer](../README.md#JwtBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_enterprise**
> ProductPostResponse create_enterprise(product_post)

Create enterprise

This endpoint is used to create an enterprise.

### Example

* Bearer Authentication (JwtBearer):

```python
import openapi_client
from openapi_client.models.product_post import ProductPost
from openapi_client.models.product_post_response import ProductPostResponse
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
    api_instance = openapi_client.EnterpriseApi(api_client)
    product_post = openapi_client.ProductPost() # ProductPost | 

    try:
        # Create enterprise
        api_response = api_instance.create_enterprise(product_post)
        print("The response of EnterpriseApi->create_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->create_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_post** | [**ProductPost**](ProductPost.md)|  | 

### Return type

[**ProductPostResponse**](ProductPostResponse.md)

### Authorization

[JwtBearer](../README.md#JwtBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_all_enterprise**
> ProductPostResponse return_all_enterprise()

Return all enterprise

This endpoint is used to return all enterprise.

### Example

* Bearer Authentication (JwtBearer):

```python
import openapi_client
from openapi_client.models.product_post_response import ProductPostResponse
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
    api_instance = openapi_client.EnterpriseApi(api_client)

    try:
        # Return all enterprise
        api_response = api_instance.return_all_enterprise()
        print("The response of EnterpriseApi->return_all_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->return_all_enterprise: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProductPostResponse**](ProductPostResponse.md)

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

# **return_analytics_enterprise**
> ProductPostResponse return_analytics_enterprise(enterprise)

Return analytics enterprise

This endpoint is used to return analytics enterprise.

### Example

* Bearer Authentication (JwtBearer):

```python
import openapi_client
from openapi_client.models.product_post_response import ProductPostResponse
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
    api_instance = openapi_client.EnterpriseApi(api_client)
    enterprise = 'enterprise_example' # str | 

    try:
        # Return analytics enterprise
        api_response = api_instance.return_analytics_enterprise(enterprise)
        print("The response of EnterpriseApi->return_analytics_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->return_analytics_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**|  | 

### Return type

[**ProductPostResponse**](ProductPostResponse.md)

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

