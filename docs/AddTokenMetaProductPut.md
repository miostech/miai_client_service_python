# AddTokenMetaProductPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_product** | **str** | Id of product | 
**token_meta** | **str** | Token meta of product | 
**wa_business_id** | **str** | Id of business id | 

## Example

```python
from openapi_client.models.add_token_meta_product_put import AddTokenMetaProductPut

# TODO update the JSON string below
json = "{}"
# create an instance of AddTokenMetaProductPut from a JSON string
add_token_meta_product_put_instance = AddTokenMetaProductPut.from_json(json)
# print the JSON string representation of the object
print(AddTokenMetaProductPut.to_json())

# convert the object into a dict
add_token_meta_product_put_dict = add_token_meta_product_put_instance.to_dict()
# create an instance of AddTokenMetaProductPut from a dict
add_token_meta_product_put_from_dict = AddTokenMetaProductPut.from_dict(add_token_meta_product_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


