# WhatsappMessageTemplatePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_message** | **str** | Id of message | 
**wa_id** | **str** | Id of whatsapp | 
**wam_id** | **str** | Id of whatsapp message | 
**wa_profile_name** | **str** | Profile name of whatsapp | 
**phone_number_id** | **str** | Id of phone number | 
**message_product** | **str** | Message of product | 
**display_phone_number** | **str** | Display phone number | 
**profile_name** | **str** | Profile name | 
**from_phone_number** | **str** | From phone number | 
**date_message** | **str** | Date of message | 
**type_message** | **str** | Type of message | 
**body_message** | **str** | Body of message | 
**video_message** | **str** | Video of message | 
**image_message** | **str** | Image of message | 
**document_message** | **str** | Document of message | 
**audio_message** | **str** | Audio of message | 
**caption_message** | **str** | Caption of message | 
**status_message** | **str** | Status of message | 
**template_name** | **str** | Template name | 
**template_type** | **str** | Template type | 
**marketing_campaign** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.whatsapp_message_template_post import WhatsappMessageTemplatePost

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappMessageTemplatePost from a JSON string
whatsapp_message_template_post_instance = WhatsappMessageTemplatePost.from_json(json)
# print the JSON string representation of the object
print(WhatsappMessageTemplatePost.to_json())

# convert the object into a dict
whatsapp_message_template_post_dict = whatsapp_message_template_post_instance.to_dict()
# create an instance of WhatsappMessageTemplatePost from a dict
whatsapp_message_template_post_from_dict = WhatsappMessageTemplatePost.from_dict(whatsapp_message_template_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


