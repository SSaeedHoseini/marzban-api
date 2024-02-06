# marzban-api.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hosts_api_hosts_get**](SystemApi.md#get_hosts_api_hosts_get) | **GET** /api/hosts | Get Hosts
[**get_inbounds_api_inbounds_get**](SystemApi.md#get_inbounds_api_inbounds_get) | **GET** /api/inbounds | Get Inbounds
[**get_system_stats_api_system_get**](SystemApi.md#get_system_stats_api_system_get) | **GET** /api/system | Get System Stats
[**modify_hosts_api_hosts_put**](SystemApi.md#modify_hosts_api_hosts_put) | **PUT** /api/hosts | Modify Hosts


# **get_hosts_api_hosts_get**
> Dict[str, List[ProxyHost]] get_hosts_api_hosts_get()

Get Hosts

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.proxy_host import ProxyHost
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
    api_instance = marzban-api.SystemApi(api_client)

    try:
        # Get Hosts
        api_response = api_instance.get_hosts_api_hosts_get()
        print("The response of SystemApi->get_hosts_api_hosts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_hosts_api_hosts_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, List[ProxyHost]]**

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

# **get_inbounds_api_inbounds_get**
> Dict[str, List[ProxyInbound]] get_inbounds_api_inbounds_get()

Get Inbounds

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.proxy_inbound import ProxyInbound
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
    api_instance = marzban-api.SystemApi(api_client)

    try:
        # Get Inbounds
        api_response = api_instance.get_inbounds_api_inbounds_get()
        print("The response of SystemApi->get_inbounds_api_inbounds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_inbounds_api_inbounds_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, List[ProxyInbound]]**

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

# **get_system_stats_api_system_get**
> SystemStats get_system_stats_api_system_get()

Get System Stats

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.system_stats import SystemStats
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
    api_instance = marzban-api.SystemApi(api_client)

    try:
        # Get System Stats
        api_response = api_instance.get_system_stats_api_system_get()
        print("The response of SystemApi->get_system_stats_api_system_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_system_stats_api_system_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemStats**](SystemStats.md)

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

# **modify_hosts_api_hosts_put**
> Dict[str, List[ProxyHost]] modify_hosts_api_hosts_put(request_body)

Modify Hosts

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban-api
from marzban-api.models.proxy_host import ProxyHost
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
    api_instance = marzban-api.SystemApi(api_client)
    request_body = None # Dict[str, List[ProxyHost]] | 

    try:
        # Modify Hosts
        api_response = api_instance.modify_hosts_api_hosts_put(request_body)
        print("The response of SystemApi->modify_hosts_api_hosts_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->modify_hosts_api_hosts_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, List[ProxyHost]]**](List.md)|  | 

### Return type

**Dict[str, List[ProxyHost]]**

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

