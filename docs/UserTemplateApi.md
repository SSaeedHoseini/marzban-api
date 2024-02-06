# marzban-api.UserTemplateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_template_api_user_template_post**](UserTemplateApi.md#add_user_template_api_user_template_post) | **POST** /api/user_template | Add User Template
[**get_user_template_api_user_template_id_get**](UserTemplateApi.md#get_user_template_api_user_template_id_get) | **GET** /api/user_template/{id} | Get User Template
[**get_user_templates_api_user_template_get**](UserTemplateApi.md#get_user_templates_api_user_template_get) | **GET** /api/user_template | Get User Templates
[**modify_user_template_api_user_template_id_put**](UserTemplateApi.md#modify_user_template_api_user_template_id_put) | **PUT** /api/user_template/{id} | Modify User Template
[**remove_user_template_api_user_template_id_delete**](UserTemplateApi.md#remove_user_template_api_user_template_id_delete) | **DELETE** /api/user_template/{id} | Remove User Template


# **add_user_template_api_user_template_post**
> UserTemplateResponse add_user_template_api_user_template_post(user_template_create)

Add User Template

Add a new user template  - **name** can be up to 64 characters - **data_limit** must be in bytes and larger or equal to 0 - **expire_duration** must be in seconds and larger or equat to 0 - **inbounds** dictionary of protocol:inbound_tags, empty means all inbounds

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.user_template_create import UserTemplateCreate
from marzban-api.models.user_template_response import UserTemplateResponse
from marzban-api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban-api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban-api.UserTemplateApi(api_client)
    user_template_create = marzban-api.UserTemplateCreate() # UserTemplateCreate | 

    try:
        # Add User Template
        api_response = api_instance.add_user_template_api_user_template_post(user_template_create)
        print("The response of UserTemplateApi->add_user_template_api_user_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTemplateApi->add_user_template_api_user_template_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_template_create** | [**UserTemplateCreate**](UserTemplateCreate.md)|  | 

### Return type

[**UserTemplateResponse**](UserTemplateResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**403** | You&#39;re not allowed |  -  |
**409** | Template by this name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_template_api_user_template_id_get**
> UserTemplateResponse get_user_template_api_user_template_id_get(id)

Get User Template

Get User Template information with id

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.user_template_response import UserTemplateResponse
from marzban-api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban-api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban-api.UserTemplateApi(api_client)
    id = 56 # int | 

    try:
        # Get User Template
        api_response = api_instance.get_user_template_api_user_template_id_get(id)
        print("The response of UserTemplateApi->get_user_template_api_user_template_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTemplateApi->get_user_template_api_user_template_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UserTemplateResponse**](UserTemplateResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**404** | User Template not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_templates_api_user_template_get**
> List[UserTemplateResponse] get_user_templates_api_user_template_get(offset=offset, limit=limit)

Get User Templates

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.user_template_response import UserTemplateResponse
from marzban-api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban-api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban-api.UserTemplateApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # Get User Templates
        api_response = api_instance.get_user_templates_api_user_template_get(offset=offset, limit=limit)
        print("The response of UserTemplateApi->get_user_templates_api_user_template_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTemplateApi->get_user_templates_api_user_template_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**List[UserTemplateResponse]**](UserTemplateResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_user_template_api_user_template_id_put**
> UserTemplateResponse modify_user_template_api_user_template_id_put(id, user_template_modify)

Modify User Template

Modify User Template  - **name** can be up to 64 characters - **data_limit** must be in bytes and larger or equal to 0 - **expire_duration** must be in seconds and larger or equat to 0 - **inbounds** dictionary of protocol:inbound_tags, empty means all inbounds

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.user_template_modify import UserTemplateModify
from marzban-api.models.user_template_response import UserTemplateResponse
from marzban-api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban-api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban-api.UserTemplateApi(api_client)
    id = 56 # int | 
    user_template_modify = marzban-api.UserTemplateModify() # UserTemplateModify | 

    try:
        # Modify User Template
        api_response = api_instance.modify_user_template_api_user_template_id_put(id, user_template_modify)
        print("The response of UserTemplateApi->modify_user_template_api_user_template_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTemplateApi->modify_user_template_api_user_template_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **user_template_modify** | [**UserTemplateModify**](UserTemplateModify.md)|  | 

### Return type

[**UserTemplateResponse**](UserTemplateResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**404** | User Template not found |  -  |
**403** | You&#39;re not allowed |  -  |
**409** | Template by this name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_template_api_user_template_id_delete**
> object remove_user_template_api_user_template_id_delete(id)

Remove User Template

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban-api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban-api.UserTemplateApi(api_client)
    id = 56 # int | 

    try:
        # Remove User Template
        api_response = api_instance.remove_user_template_api_user_template_id_delete(id)
        print("The response of UserTemplateApi->remove_user_template_api_user_template_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTemplateApi->remove_user_template_api_user_template_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**404** | User Template not found |  -  |
**403** | You&#39;re not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

