# AdminCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**is_sudo** | **bool** |  | 
**password** | **str** |  | 

## Example

```python
from marzban-api.models.admin_create import AdminCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCreate from a JSON string
admin_create_instance = AdminCreate.from_json(json)
# print the JSON string representation of the object
print AdminCreate.to_json()

# convert the object into a dict
admin_create_dict = admin_create_instance.to_dict()
# create an instance of AdminCreate from a dict
admin_create_form_dict = admin_create.from_dict(admin_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


