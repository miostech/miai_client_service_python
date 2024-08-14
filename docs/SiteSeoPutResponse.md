# SiteSeoPutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **str** | Message of response | 
**data** | **object** |  | 

## Example

```python
from openapi_client.models.site_seo_put_response import SiteSeoPutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SiteSeoPutResponse from a JSON string
site_seo_put_response_instance = SiteSeoPutResponse.from_json(json)
# print the JSON string representation of the object
print(SiteSeoPutResponse.to_json())

# convert the object into a dict
site_seo_put_response_dict = site_seo_put_response_instance.to_dict()
# create an instance of SiteSeoPutResponse from a dict
site_seo_put_response_from_dict = SiteSeoPutResponse.from_dict(site_seo_put_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


