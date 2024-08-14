# InvoicePostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **str** | Message of response | 
**data** | **object** |  | 

## Example

```python
from openapi_client.models.invoice_post_response import InvoicePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePostResponse from a JSON string
invoice_post_response_instance = InvoicePostResponse.from_json(json)
# print the JSON string representation of the object
print(InvoicePostResponse.to_json())

# convert the object into a dict
invoice_post_response_dict = invoice_post_response_instance.to_dict()
# create an instance of InvoicePostResponse from a dict
invoice_post_response_from_dict = InvoicePostResponse.from_dict(invoice_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


