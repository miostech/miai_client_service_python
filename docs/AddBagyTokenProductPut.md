# AddBagyTokenProductPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_product** | **str** | Id of product | 
**bagy_token** | **str** | Bagy token of product | 

## Example

```python
from openapi_client.models.add_bagy_token_product_put import AddBagyTokenProductPut

# TODO update the JSON string below
json = "{}"
# create an instance of AddBagyTokenProductPut from a JSON string
add_bagy_token_product_put_instance = AddBagyTokenProductPut.from_json(json)
# print the JSON string representation of the object
print(AddBagyTokenProductPut.to_json())

# convert the object into a dict
add_bagy_token_product_put_dict = add_bagy_token_product_put_instance.to_dict()
# create an instance of AddBagyTokenProductPut from a dict
add_bagy_token_product_put_from_dict = AddBagyTokenProductPut.from_dict(add_bagy_token_product_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


