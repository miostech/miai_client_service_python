# TemplatePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_project** | **str** | Id of current project | 
**name** | **str** | Name of template | 
**category** | **str** | Category of template | 
**allow_category_change** | **bool** | Allow category change of template | 
**language** | **str** | Language of template | 
**components** | [**List[TemplateComponent]**](TemplateComponent.md) | Components of template | 

## Example

```python
from openapi_client.models.template_post import TemplatePost

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePost from a JSON string
template_post_instance = TemplatePost.from_json(json)
# print the JSON string representation of the object
print(TemplatePost.to_json())

# convert the object into a dict
template_post_dict = template_post_instance.to_dict()
# create an instance of TemplatePost from a dict
template_post_from_dict = TemplatePost.from_dict(template_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


