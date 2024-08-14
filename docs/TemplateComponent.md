# TemplateComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of component | 
**format** | **str** | Format of component | 
**title_if_button** | **str** |  | [optional] 
**example** | **str** | Example of component | 
**link_redirect_if_button** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.template_component import TemplateComponent

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateComponent from a JSON string
template_component_instance = TemplateComponent.from_json(json)
# print the JSON string representation of the object
print(TemplateComponent.to_json())

# convert the object into a dict
template_component_dict = template_component_instance.to_dict()
# create an instance of TemplateComponent from a dict
template_component_from_dict = TemplateComponent.from_dict(template_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


