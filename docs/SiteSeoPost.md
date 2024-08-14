# SiteSeoPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_product** | **str** | Id of product | 
**base_64_url** | **str** | Base 64 url of product | 
**performance** | **int** | Performance of product | 
**accessibility** | **int** | Accessibility of product | 
**best_practices** | **int** | Best practices of product | 
**seo** | **int** | Seo of product | 
**html_analytics** | **str** | Html analytics of product | 

## Example

```python
from openapi_client.models.site_seo_post import SiteSeoPost

# TODO update the JSON string below
json = "{}"
# create an instance of SiteSeoPost from a JSON string
site_seo_post_instance = SiteSeoPost.from_json(json)
# print the JSON string representation of the object
print(SiteSeoPost.to_json())

# convert the object into a dict
site_seo_post_dict = site_seo_post_instance.to_dict()
# create an instance of SiteSeoPost from a dict
site_seo_post_from_dict = SiteSeoPost.from_dict(site_seo_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


