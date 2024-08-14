# ProductPutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **str** | Message of response | 
**data** | **object** |  | 

## Example

```python
from openapi_client.models.product_put_response import ProductPutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductPutResponse from a JSON string
product_put_response_instance = ProductPutResponse.from_json(json)
# print the JSON string representation of the object
print(ProductPutResponse.to_json())

# convert the object into a dict
product_put_response_dict = product_put_response_instance.to_dict()
# create an instance of ProductPutResponse from a dict
product_put_response_from_dict = ProductPutResponse.from_dict(product_put_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


