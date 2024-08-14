# ProductPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **str** | Message of response | 
**data** | **object** |  | 

## Example

```python
from openapi_client.models.product_post_response import ProductPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductPostResponse from a JSON string
product_post_response_instance = ProductPostResponse.from_json(json)
# print the JSON string representation of the object
print(ProductPostResponse.to_json())

# convert the object into a dict
product_post_response_dict = product_post_response_instance.to_dict()
# create an instance of ProductPostResponse from a dict
product_post_response_from_dict = ProductPostResponse.from_dict(product_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


