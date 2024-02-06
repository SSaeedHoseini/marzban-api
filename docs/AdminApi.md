# marzban-api.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_admin_api_admin_post**](AdminApi.md#create_admin_api_admin_post) | **POST** /api/admin | Create Admin
[**get_admins_api_admins_get**](AdminApi.md#get_admins_api_admins_get) | **GET** /api/admins | Get Admins
[**get_current_admin_api_admin_get**](AdminApi.md#get_current_admin_api_admin_get) | **GET** /api/admin | Get Current Admin
[**login_for_access_token_api_admin_token_post**](AdminApi.md#login_for_access_token_api_admin_token_post) | **POST** /api/admin/token | Login For Access Token
[**modify_admin_api_admin_username_put**](AdminApi.md#modify_admin_api_admin_username_put) | **PUT** /api/admin/{username} | Modify Admin
[**remove_admin_api_admin_username_delete**](AdminApi.md#remove_admin_api_admin_username_delete) | **DELETE** /api/admin/{username} | Remove Admin


# **create_admin_api_admin_post**
> Admin create_admin_api_admin_post(admin_create)

Create Admin

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.admin import Admin
from marzban-api.models.admin_create import AdminCreate
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
    api_instance = marzban-api.AdminApi(api_client)
    admin_create = marzban-api.AdminCreate() # AdminCreate | 

    try:
        # Create Admin
        api_response = api_instance.create_admin_api_admin_post(admin_create)
        print("The response of AdminApi->create_admin_api_admin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_admin_api_admin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_create** | [**AdminCreate**](AdminCreate.md)|  | 

### Return type

[**Admin**](Admin.md)

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
**409** | Admin already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admins_api_admins_get**
> List[Admin] get_admins_api_admins_get(offset=offset, limit=limit, username=username)

Get Admins

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.admin import Admin
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
    api_instance = marzban-api.AdminApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    username = 'username_example' # str |  (optional)

    try:
        # Get Admins
        api_response = api_instance.get_admins_api_admins_get(offset=offset, limit=limit, username=username)
        print("The response of AdminApi->get_admins_api_admins_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_admins_api_admins_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**List[Admin]**](Admin.md)

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
**403** | You&#39;re not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_admin_api_admin_get**
> Admin get_current_admin_api_admin_get()

Get Current Admin

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.admin import Admin
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
    api_instance = marzban-api.AdminApi(api_client)

    try:
        # Get Current Admin
        api_response = api_instance.get_current_admin_api_admin_get()
        print("The response of AdminApi->get_current_admin_api_admin_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_current_admin_api_admin_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Admin**](Admin.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_for_access_token_api_admin_token_post**
> Token login_for_access_token_api_admin_token_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Login For Access Token

### Example


```python
import marzban-api
from marzban-api.models.token import Token
from marzban-api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban-api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with marzban-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban-api.AdminApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Login For Access Token
        api_response = api_instance.login_for_access_token_api_admin_token_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AdminApi->login_for_access_token_api_admin_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->login_for_access_token_api_admin_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_admin_api_admin_username_put**
> Admin modify_admin_api_admin_username_put(username, admin_modify)

Modify Admin

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.admin import Admin
from marzban-api.models.admin_modify import AdminModify
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
    api_instance = marzban-api.AdminApi(api_client)
    username = 'username_example' # str | 
    admin_modify = marzban-api.AdminModify() # AdminModify | 

    try:
        # Modify Admin
        api_response = api_instance.modify_admin_api_admin_username_put(username, admin_modify)
        print("The response of AdminApi->modify_admin_api_admin_username_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->modify_admin_api_admin_username_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **admin_modify** | [**AdminModify**](AdminModify.md)|  | 

### Return type

[**Admin**](Admin.md)

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
**404** | Admin not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_admin_api_admin_username_delete**
> object remove_admin_api_admin_username_delete(username)

Remove Admin

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
    api_instance = marzban-api.AdminApi(api_client)
    username = 'username_example' # str | 

    try:
        # Remove Admin
        api_response = api_instance.remove_admin_api_admin_username_delete(username)
        print("The response of AdminApi->remove_admin_api_admin_username_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_admin_api_admin_username_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

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
**403** | You&#39;re not allowed |  -  |
**404** | Admin not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

