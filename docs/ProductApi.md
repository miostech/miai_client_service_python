# openapi_client.ProductApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bagy_token_product**](ProductApi.md#add_bagy_token_product) | **PUT** /product/add-bagy-token | Add bagy token to product
[**add_business_id_account_product**](ProductApi.md#add_business_id_account_product) | **PUT** /product/add-business-id-account/meta | Add business id account to product
[**add_phone_number_to_product**](ProductApi.md#add_phone_number_to_product) | **PUT** /product/ | Add phone number to product
[**add_token_meta_product**](ProductApi.md#add_token_meta_product) | **PUT** /product/add-token/meta | Add token meta to product
[**create_product**](ProductApi.md#create_product) | **POST** /product/ | Create product
[**return_all_products**](ProductApi.md#return_all_products) | **GET** /product/all | Return all products
[**return_analytics**](ProductApi.md#return_analytics) | **GET** /product/return/analytics/{id_product} | Return analytics


# **add_bagy_token_product**
> ProductPostResponse add_bagy_token_product(add_bagy_token_product_put)

Add bagy token to product

Add bagy token to product

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
    api_instance = openapi_client.ProductApi(api_client)
    add_bagy_token_product_put = openapi_client.AddBagyTokenProductPut() # AddBagyTokenProductPut | 

    try:
        # Add bagy token to product
        api_response = api_instance.add_bagy_token_product(add_bagy_token_product_put)
        print("The response of ProductApi->add_bagy_token_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->add_bagy_token_product: %s\n" % e)
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

# **add_business_id_account_product**
> ProductPutResponse add_business_id_account_product(add_token_meta_product_put)

Add business id account to product

Add business id account to product

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
    api_instance = openapi_client.ProductApi(api_client)
    add_token_meta_product_put = openapi_client.AddTokenMetaProductPut() # AddTokenMetaProductPut | 

    try:
        # Add business id account to product
        api_response = api_instance.add_business_id_account_product(add_token_meta_product_put)
        print("The response of ProductApi->add_business_id_account_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->add_business_id_account_product: %s\n" % e)
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

# **add_phone_number_to_product**
> ProductPostResponse add_phone_number_to_product(contact_product_put)

Add phone number to product

Add phone number to product

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
    api_instance = openapi_client.ProductApi(api_client)
    contact_product_put = openapi_client.ContactProductPut() # ContactProductPut | 

    try:
        # Add phone number to product
        api_response = api_instance.add_phone_number_to_product(contact_product_put)
        print("The response of ProductApi->add_phone_number_to_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->add_phone_number_to_product: %s\n" % e)
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

# **add_token_meta_product**
> ProductPutResponse add_token_meta_product(add_token_meta_product_put)

Add token meta to product

Add token meta to product

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
    api_instance = openapi_client.ProductApi(api_client)
    add_token_meta_product_put = openapi_client.AddTokenMetaProductPut() # AddTokenMetaProductPut | 

    try:
        # Add token meta to product
        api_response = api_instance.add_token_meta_product(add_token_meta_product_put)
        print("The response of ProductApi->add_token_meta_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->add_token_meta_product: %s\n" % e)
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

# **create_product**
> ProductPostResponse create_product(product_post)

Create product

Create product

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
    api_instance = openapi_client.ProductApi(api_client)
    product_post = openapi_client.ProductPost() # ProductPost | 

    try:
        # Create product
        api_response = api_instance.create_product(product_post)
        print("The response of ProductApi->create_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->create_product: %s\n" % e)
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

# **return_all_products**
> ProductPostResponse return_all_products()

Return all products

Return all products

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
    api_instance = openapi_client.ProductApi(api_client)

    try:
        # Return all products
        api_response = api_instance.return_all_products()
        print("The response of ProductApi->return_all_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->return_all_products: %s\n" % e)
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

# **return_analytics**
> ProductPostResponse return_analytics(id_product)

Return analytics

Return analytics

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
    api_instance = openapi_client.ProductApi(api_client)
    id_product = 'id_product_example' # str | 

    try:
        # Return analytics
        api_response = api_instance.return_analytics(id_product)
        print("The response of ProductApi->return_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->return_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_product** | **str**|  | 

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

