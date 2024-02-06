# marzban_api.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_api_user_post**](UserApi.md#add_user_api_user_post) | **POST** /api/user | Add User
[**delete_expired_api_users_expired_delete**](UserApi.md#delete_expired_api_users_expired_delete) | **DELETE** /api/users/expired | Delete Expired
[**get_user_api_user_username_get**](UserApi.md#get_user_api_user_username_get) | **GET** /api/user/{username} | Get User
[**get_user_usage_api_user_username_usage_get**](UserApi.md#get_user_usage_api_user_username_usage_get) | **GET** /api/user/{username}/usage | Get User Usage
[**get_users_api_users_get**](UserApi.md#get_users_api_users_get) | **GET** /api/users | Get Users
[**modify_user_api_user_username_put**](UserApi.md#modify_user_api_user_username_put) | **PUT** /api/user/{username} | Modify User
[**remove_user_api_user_username_delete**](UserApi.md#remove_user_api_user_username_delete) | **DELETE** /api/user/{username} | Remove User
[**reset_user_data_usage_api_user_username_reset_post**](UserApi.md#reset_user_data_usage_api_user_username_reset_post) | **POST** /api/user/{username}/reset | Reset User Data Usage
[**reset_users_data_usage_api_users_reset_post**](UserApi.md#reset_users_data_usage_api_users_reset_post) | **POST** /api/users/reset | Reset Users Data Usage
[**revoke_user_subscription_api_user_username_revoke_sub_post**](UserApi.md#revoke_user_subscription_api_user_username_revoke_sub_post) | **POST** /api/user/{username}/revoke_sub | Revoke User Subscription
[**set_owner_api_user_username_set_owner_put**](UserApi.md#set_owner_api_user_username_set_owner_put) | **PUT** /api/user/{username}/set-owner | Set Owner


# **add_user_api_user_post**
> UserResponse add_user_api_user_post(user_create)

Add User

Add a new user  - **username** must have 3 to 32 characters and is allowed to contain a-z, 0-9, and underscores in between - **expire** must be an UTC timestamp - **data_limit** must be in Bytes, e.g. 1073741824B = 1GB - **proxies** dictionary of protocol:settings - **inbounds** dictionary of protocol:inbound_tags, empty means all inbounds

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.user_create import UserCreate
from marzban_api.models.user_response import UserResponse
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.UserApi(api_client)
    user_create = marzban_api.UserCreate() # UserCreate | 

    try:
        # Add User
        api_response = api_instance.add_user_api_user_post(user_create)
        print("The response of UserApi->add_user_api_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->add_user_api_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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
**409** | User already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_expired_api_users_expired_delete**
> object delete_expired_api_users_expired_delete(passed_time)

Delete Expired

Delete expired users - **passed_time** must be a timestamp - This function will delete all expired users that meet the specified number of days passed and can't be undone.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.UserApi(api_client)
    passed_time = 56 # int | 

    try:
        # Delete Expired
        api_response = api_instance.delete_expired_api_users_expired_delete(passed_time)
        print("The response of UserApi->delete_expired_api_users_expired_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_expired_api_users_expired_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **passed_time** | **int**|  | 

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
**404** | No expired user found. |  -  |
**403** | You&#39;re not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_api_user_username_get**
> UserResponse get_user_api_user_username_get(username)

Get User

Get users information

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.user_response import UserResponse
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.UserApi(api_client)
    username = 'username_example' # str | 

    try:
        # Get User
        api_response = api_instance.get_user_api_user_username_get(username)
        print("The response of UserApi->get_user_api_user_username_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_api_user_username_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

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
**404** | User not found |  -  |
**403** | You&#39;re not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage_api_user_username_usage_get**
> UserUsagesResponse get_user_usage_api_user_username_usage_get(username, start=start, end=end)

Get User Usage

Get users usage

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.user_usages_response import UserUsagesResponse
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.UserApi(api_client)
    username = 'username_example' # str | 
    start = 'start_example' # str |  (optional)
    end = 'end_example' # str |  (optional)

    try:
        # Get User Usage
        api_response = api_instance.get_user_usage_api_user_username_usage_get(username, start=start, end=end)
        print("The response of UserApi->get_user_usage_api_user_username_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_usage_api_user_username_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **start** | **str**|  | [optional] 
 **end** | **str**|  | [optional] 

### Return type

[**UserUsagesResponse**](UserUsagesResponse.md)

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
**404** | User not found |  -  |
**403** | You&#39;re not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_api_users_get**
> UsersResponse get_users_api_users_get(offset=offset, limit=limit, username=username, status=status, sort=sort)

Get Users

Get all users

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.user_status import UserStatus
from marzban_api.models.users_response import UsersResponse
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.UserApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    username = 'username_example' # str |  (optional)
    status = marzban_api.UserStatus() # UserStatus |  (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # Get Users
        api_response = api_instance.get_users_api_users_get(offset=offset, limit=limit, username=username, status=status, sort=sort)
        print("The response of UserApi->get_users_api_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_users_api_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **username** | **str**|  | [optional] 
 **status** | [**UserStatus**](.md)|  | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

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

# **modify_user_api_user_username_put**
> UserResponse modify_user_api_user_username_put(username, user_modify)

Modify User

Modify a user  - set **expire** to 0 to make the user unlimited in time, null to no change - set **data_limit** to 0 to make the user unlimited in data, null to no change - **proxies** dictionary of protocol:settings, empty means no change - **inbounds** dictionary of protocol:inbound_tags, empty means no change

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.user_modify import UserModify
from marzban_api.models.user_response import UserResponse
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.UserApi(api_client)
    username = 'username_example' # str | 
    user_modify = marzban_api.UserModify() # UserModify | 

    try:
        # Modify User
        api_response = api_instance.modify_user_api_user_username_put(username, user_modify)
        print("The response of UserApi->modify_user_api_user_username_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->modify_user_api_user_username_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **user_modify** | [**UserModify**](UserModify.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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
**404** | User not found |  -  |
**403** | You&#39;re not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_api_user_username_delete**
> object remove_user_api_user_username_delete(username)

Remove User

Remove a user

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.UserApi(api_client)
    username = 'username_example' # str | 

    try:
        # Remove User
        api_response = api_instance.remove_user_api_user_username_delete(username)
        print("The response of UserApi->remove_user_api_user_username_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->remove_user_api_user_username_delete: %s\n" % e)
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
**404** | User not found |  -  |
**403** | You&#39;re not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_user_data_usage_api_user_username_reset_post**
> UserResponse reset_user_data_usage_api_user_username_reset_post(username)

Reset User Data Usage

Reset user data usage

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.user_response import UserResponse
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.UserApi(api_client)
    username = 'username_example' # str | 

    try:
        # Reset User Data Usage
        api_response = api_instance.reset_user_data_usage_api_user_username_reset_post(username)
        print("The response of UserApi->reset_user_data_usage_api_user_username_reset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->reset_user_data_usage_api_user_username_reset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

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
**404** | User not found |  -  |
**403** | You&#39;re not allowed |  -  |
**409** | User already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_users_data_usage_api_users_reset_post**
> object reset_users_data_usage_api_users_reset_post()

Reset Users Data Usage

Reset all users data usage

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.UserApi(api_client)

    try:
        # Reset Users Data Usage
        api_response = api_instance.reset_users_data_usage_api_users_reset_post()
        print("The response of UserApi->reset_users_data_usage_api_users_reset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->reset_users_data_usage_api_users_reset_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**403** | You&#39;re not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_user_subscription_api_user_username_revoke_sub_post**
> UserResponse revoke_user_subscription_api_user_username_revoke_sub_post(username)

Revoke User Subscription

Revoke users subscription (Subscription link and proxies)

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.user_response import UserResponse
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.UserApi(api_client)
    username = 'username_example' # str | 

    try:
        # Revoke User Subscription
        api_response = api_instance.revoke_user_subscription_api_user_username_revoke_sub_post(username)
        print("The response of UserApi->revoke_user_subscription_api_user_username_revoke_sub_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->revoke_user_subscription_api_user_username_revoke_sub_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

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
**404** | User not found |  -  |
**403** | You&#39;re not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_owner_api_user_username_set_owner_put**
> UserResponse set_owner_api_user_username_set_owner_put(username, admin_username)

Set Owner

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.user_response import UserResponse
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.UserApi(api_client)
    username = 'username_example' # str | 
    admin_username = 'admin_username_example' # str | 

    try:
        # Set Owner
        api_response = api_instance.set_owner_api_user_username_set_owner_put(username, admin_username)
        print("The response of UserApi->set_owner_api_user_username_set_owner_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->set_owner_api_user_username_set_owner_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **admin_username** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

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
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

