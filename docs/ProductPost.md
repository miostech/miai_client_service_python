# ProductPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_account_creator** | **str** | Id of account creator | 
**email_account_creator** | **str** | Email of account creator | 
**name** | **str** | Name of product | 
**description** | **str** | Description of product | 
**image** | **str** | Image of product | 
**services** | **List[str]** | Services of product | 
**site** | **str** | Site of product | 
**id_account** | **str** | Id of account | 

## Example

```python
from openapi_client.models.product_post import ProductPost

# TODO update the JSON string below
json = "{}"
# create an instance of ProductPost from a JSON string
product_post_instance = ProductPost.from_json(json)
# print the JSON string representation of the object
print(ProductPost.to_json())

# convert the object into a dict
product_post_dict = product_post_instance.to_dict()
# create an instance of ProductPost from a dict
product_post_from_dict = ProductPost.from_dict(product_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


