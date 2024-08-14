# openapi_client.TemplateApi

All URIs are relative to *https://mios-direct.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](TemplateApi.md#create_template) | **POST** /template/ | Create template
[**return_all_templates**](TemplateApi.md#return_all_templates) | **GET** /template/ | Return all template
[**return_all_templates_by_project**](TemplateApi.md#return_all_templates_by_project) | **GET** /template/{id_project} | Return all template by project
[**return_template_by_name**](TemplateApi.md#return_template_by_name) | **GET** /template/by/name/{template_name} | Return template by name


# **create_template**
> TemplatePostResponse create_template(template_post)

Create template

Create template

### Example

* Bearer Authentication (JwtBearer):

```python
import openapi_client
from openapi_client.models.template_post import TemplatePost
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
    api_instance = openapi_client.TemplateApi(api_client)
    template_post = openapi_client.TemplatePost() # TemplatePost | 

    try:
        # Create template
        api_response = api_instance.create_template(template_post)
        print("The response of TemplateApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_post** | [**TemplatePost**](TemplatePost.md)|  | 

### Return type

[**TemplatePostResponse**](TemplatePostResponse.md)

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

# **return_all_templates**
> TemplatePostResponse return_all_templates()

Return all template

Return all template

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
    api_instance = openapi_client.TemplateApi(api_client)

    try:
        # Return all template
        api_response = api_instance.return_all_templates()
        print("The response of TemplateApi->return_all_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->return_all_templates: %s\n" % e)
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

# **return_all_templates_by_project**
> TemplatePostResponse return_all_templates_by_project(id_project)

Return all template by project

Return all template by project

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
    api_instance = openapi_client.TemplateApi(api_client)
    id_project = 'id_project_example' # str | 

    try:
        # Return all template by project
        api_response = api_instance.return_all_templates_by_project(id_project)
        print("The response of TemplateApi->return_all_templates_by_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->return_all_templates_by_project: %s\n" % e)
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

# **return_template_by_name**
> TemplatePostResponse return_template_by_name(template_name)

Return template by name

Return template by name

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
    api_instance = openapi_client.TemplateApi(api_client)
    template_name = 'template_name_example' # str | 

    try:
        # Return template by name
        api_response = api_instance.return_template_by_name(template_name)
        print("The response of TemplateApi->return_template_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->return_template_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**|  | 

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

