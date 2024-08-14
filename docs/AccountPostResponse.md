# AccountPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **str** | Message of response | 
**data** | **object** |  | 
**token** | [**AnyOf**](AnyOf.md) | Access token | 

## Example

```python
from openapi_client.models.account_post_response import AccountPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountPostResponse from a JSON string
account_post_response_instance = AccountPostResponse.from_json(json)
# print the JSON string representation of the object
print(AccountPostResponse.to_json())

# convert the object into a dict
account_post_response_dict = account_post_response_instance.to_dict()
# create an instance of AccountPostResponse from a dict
account_post_response_from_dict = AccountPostResponse.from_dict(account_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


