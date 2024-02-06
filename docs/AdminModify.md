# AdminModify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**is_sudo** | **bool** |  | 

## Example

```python
from marzban_api.models.admin_modify import AdminModify

# TODO update the JSON string below
json = "{}"
# create an instance of AdminModify from a JSON string
admin_modify_instance = AdminModify.from_json(json)
# print the JSON string representation of the object
print AdminModify.to_json()

# convert the object into a dict
admin_modify_dict = admin_modify_instance.to_dict()
# create an instance of AdminModify from a dict
admin_modify_form_dict = admin_modify.from_dict(admin_modify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


