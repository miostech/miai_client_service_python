# ContactProductPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_product** | **str** | Id of product | 
**phone_number_id** | **str** | Id of phone number | 
**wa_business_id** | **str** | Id of business id | 
**display_name** | **str** | Display name of product | 
**time_zone** | **str** | Time zone of product | 
**category** | **str** | Category of product | 
**business_description** | **str** | Business description of product | 
**image** | **str** | Image of product | 
**phone_number** | **str** | Phone number of product | 
**active** | **bool** | Number activated | 

## Example

```python
from openapi_client.models.contact_product_put import ContactProductPut

# TODO update the JSON string below
json = "{}"
# create an instance of ContactProductPut from a JSON string
contact_product_put_instance = ContactProductPut.from_json(json)
# print the JSON string representation of the object
print(ContactProductPut.to_json())

# convert the object into a dict
contact_product_put_dict = contact_product_put_instance.to_dict()
# create an instance of ContactProductPut from a dict
contact_product_put_from_dict = ContactProductPut.from_dict(contact_product_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


