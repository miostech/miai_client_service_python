# AccountPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of account | 
**last_name** | **str** | Last name of account | 
**image_profile** | **str** |  | [optional] 
**email** | **str** | Email of account | 
**country** | **str** | Country of account | 
**password** | **str** | Password of account | 
**phone_number** | **str** | Phone number of account | 
**provider** | **str** | Provider of account | 

## Example

```python
from openapi_client.models.account_post import AccountPost

# TODO update the JSON string below
json = "{}"
# create an instance of AccountPost from a JSON string
account_post_instance = AccountPost.from_json(json)
# print the JSON string representation of the object
print(AccountPost.to_json())

# convert the object into a dict
account_post_dict = account_post_instance.to_dict()
# create an instance of AccountPost from a dict
account_post_from_dict = AccountPost.from_dict(account_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


