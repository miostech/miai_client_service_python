# openapi_client.AccountApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_in_product**](AccountApi.md#add_user_in_product) | **POST** /account/add/user/in/product/{email}/{id_product}/{rule} | Add user in product
[**create_account**](AccountApi.md#create_account) | **POST** /account/ | Create account
[**delete_user_in_product**](AccountApi.md#delete_user_in_product) | **DELETE** /account/delete/user/in/product/{email}/{id_product} | Delete user in product
[**get_account_by_email_and_password**](AccountApi.md#get_account_by_email_and_password) | **GET** /account/{email}/{password} | Get account by email and password
[**get_account_by_token**](AccountApi.md#get_account_by_token) | **GET** /account/me | Get account by token
[**get_user_from_product**](AccountApi.md#get_user_from_product) | **GET** /account/user/from/product/{id_product} | Get user from product
[**link_payment**](AccountApi.md#link_payment) | **GET** /account/link/payment/{plan}/{email} | Link payment


# **add_user_in_product**
> AccountPostResponseNoToken add_user_in_product(email, id_product, rule)

Add user in product

Add user in product

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountApi(api_client)
    email = 'email_example' # str | 
    id_product = 'id_product_example' # str | 
    rule = 'rule_example' # str | 

    try:
        # Add user in product
        api_response = api_instance.add_user_in_product(email, id_product, rule)
        print("The response of AccountApi->add_user_in_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->add_user_in_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **id_product** | **str**|  | 
 **rule** | **str**|  | 

### Return type

[**AccountPostResponseNoToken**](AccountPostResponseNoToken.md)

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

# **create_account**
> AccountPostResponse create_account(account_post)

Create account

Create account

### Example


```python
import openapi_client
from openapi_client.models.account_post import AccountPost
from openapi_client.models.account_post_response import AccountPostResponse
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
    api_instance = openapi_client.AccountApi(api_client)
    account_post = openapi_client.AccountPost() # AccountPost | 

    try:
        # Create account
        api_response = api_instance.create_account(account_post)
        print("The response of AccountApi->create_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->create_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_post** | [**AccountPost**](AccountPost.md)|  | 

### Return type

[**AccountPostResponse**](AccountPostResponse.md)

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

# **delete_user_in_product**
> AccountPostResponseNoToken delete_user_in_product(email, id_product)

Delete user in product

Delete user in product

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountApi(api_client)
    email = 'email_example' # str | 
    id_product = 'id_product_example' # str | 

    try:
        # Delete user in product
        api_response = api_instance.delete_user_in_product(email, id_product)
        print("The response of AccountApi->delete_user_in_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->delete_user_in_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **id_product** | **str**|  | 

### Return type

[**AccountPostResponseNoToken**](AccountPostResponseNoToken.md)

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

# **get_account_by_email_and_password**
> AccountPostResponse get_account_by_email_and_password(email, password)

Get account by email and password

Get account by email and password

### Example


```python
import openapi_client
from openapi_client.models.account_post_response import AccountPostResponse
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
    api_instance = openapi_client.AccountApi(api_client)
    email = 'email_example' # str | 
    password = 'password_example' # str | 

    try:
        # Get account by email and password
        api_response = api_instance.get_account_by_email_and_password(email, password)
        print("The response of AccountApi->get_account_by_email_and_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_by_email_and_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **password** | **str**|  | 

### Return type

[**AccountPostResponse**](AccountPostResponse.md)

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

# **get_account_by_token**
> AccountPostResponse get_account_by_token()

Get account by token

Get account by token

### Example


```python
import openapi_client
from openapi_client.models.account_post_response import AccountPostResponse
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
    api_instance = openapi_client.AccountApi(api_client)

    try:
        # Get account by token
        api_response = api_instance.get_account_by_token()
        print("The response of AccountApi->get_account_by_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_by_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountPostResponse**](AccountPostResponse.md)

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

# **get_user_from_product**
> AccountPostResponseNoToken get_user_from_product(id_product)

Get user from product

Get user from product

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountApi(api_client)
    id_product = 'id_product_example' # str | 

    try:
        # Get user from product
        api_response = api_instance.get_user_from_product(id_product)
        print("The response of AccountApi->get_user_from_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_user_from_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_product** | **str**|  | 

### Return type

[**AccountPostResponseNoToken**](AccountPostResponseNoToken.md)

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

# **link_payment**
> AccountPostResponseNoToken link_payment(plan, email)

Link payment

Link payment

### Example


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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountApi(api_client)
    plan = 'plan_example' # str | 
    email = 'email_example' # str | 

    try:
        # Link payment
        api_response = api_instance.link_payment(plan, email)
        print("The response of AccountApi->link_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->link_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | **str**|  | 
 **email** | **str**|  | 

### Return type

[**AccountPostResponseNoToken**](AccountPostResponseNoToken.md)

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

