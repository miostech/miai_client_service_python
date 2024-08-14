# SiteSeoPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of product | 
**performance** | **float** | Performance of product | 
**accessibility** | **float** | Accessibility of product | 
**best_practices** | **float** | Best practices of product | 
**seo** | **float** | Seo of product | 
**html_analytics** | **str** | Html analytics of product | 

## Example

```python
from openapi_client.models.site_seo_put import SiteSeoPut

# TODO update the JSON string below
json = "{}"
# create an instance of SiteSeoPut from a JSON string
site_seo_put_instance = SiteSeoPut.from_json(json)
# print the JSON string representation of the object
print(SiteSeoPut.to_json())

# convert the object into a dict
site_seo_put_dict = site_seo_put_instance.to_dict()
# create an instance of SiteSeoPut from a dict
site_seo_put_from_dict = SiteSeoPut.from_dict(site_seo_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


