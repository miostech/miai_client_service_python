# ValidationPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Phone number | 
**ip** | **str** | IP | 

## Example

```python
from openapi_client.models.validation_post import ValidationPost

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationPost from a JSON string
validation_post_instance = ValidationPost.from_json(json)
# print the JSON string representation of the object
print(ValidationPost.to_json())

# convert the object into a dict
validation_post_dict = validation_post_instance.to_dict()
# create an instance of ValidationPost from a dict
validation_post_from_dict = ValidationPost.from_dict(validation_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


