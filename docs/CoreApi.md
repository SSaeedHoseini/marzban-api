# marzban_api.CoreApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_core_config_api_core_config_get**](CoreApi.md#get_core_config_api_core_config_get) | **GET** /api/core/config | Get Core Config
[**get_core_stats_api_core_get**](CoreApi.md#get_core_stats_api_core_get) | **GET** /api/core | Get Core Stats
[**modify_core_config_api_core_config_put**](CoreApi.md#modify_core_config_api_core_config_put) | **PUT** /api/core/config | Modify Core Config
[**restart_core_api_core_restart_post**](CoreApi.md#restart_core_api_core_restart_post) | **POST** /api/core/restart | Restart Core


# **get_core_config_api_core_config_get**
> object get_core_config_api_core_config_get()

Get Core Config

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
    api_instance = marzban_api.CoreApi(api_client)

    try:
        # Get Core Config
        api_response = api_instance.get_core_config_api_core_config_get()
        print("The response of CoreApi->get_core_config_api_core_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_core_config_api_core_config_get: %s\n" % e)
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

# **get_core_stats_api_core_get**
> CoreStats get_core_stats_api_core_get()

Get Core Stats

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.core_stats import CoreStats
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
    api_instance = marzban_api.CoreApi(api_client)

    try:
        # Get Core Stats
        api_response = api_instance.get_core_stats_api_core_get()
        print("The response of CoreApi->get_core_stats_api_core_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->get_core_stats_api_core_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CoreStats**](CoreStats.md)

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

# **modify_core_config_api_core_config_put**
> object modify_core_config_api_core_config_put(body)

Modify Core Config

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
    api_instance = marzban_api.CoreApi(api_client)
    body = None # object | 

    try:
        # Modify Core Config
        api_response = api_instance.modify_core_config_api_core_config_put(body)
        print("The response of CoreApi->modify_core_config_api_core_config_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->modify_core_config_api_core_config_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_core_api_core_restart_post**
> object restart_core_api_core_restart_post()

Restart Core

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
    api_instance = marzban_api.CoreApi(api_client)

    try:
        # Restart Core
        api_response = api_instance.restart_core_api_core_restart_post()
        print("The response of CoreApi->restart_core_api_core_restart_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->restart_core_api_core_restart_post: %s\n" % e)
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

