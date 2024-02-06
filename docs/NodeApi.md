# marzban_api.NodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_node_api_node_post**](NodeApi.md#add_node_api_node_post) | **POST** /api/node | Add Node
[**get_node_api_node_node_id_get**](NodeApi.md#get_node_api_node_node_id_get) | **GET** /api/node/{node_id} | Get Node
[**get_node_api_node_settings_get**](NodeApi.md#get_node_api_node_settings_get) | **GET** /api/node/settings | Get Node
[**get_nodes_api_nodes_get**](NodeApi.md#get_nodes_api_nodes_get) | **GET** /api/nodes | Get Nodes
[**get_usage_api_nodes_usage_get**](NodeApi.md#get_usage_api_nodes_usage_get) | **GET** /api/nodes/usage | Get Usage
[**modify_node_api_node_node_id_put**](NodeApi.md#modify_node_api_node_node_id_put) | **PUT** /api/node/{node_id} | Modify Node
[**reconnect_node_api_node_node_id_reconnect_post**](NodeApi.md#reconnect_node_api_node_node_id_reconnect_post) | **POST** /api/node/{node_id}/reconnect | Reconnect Node
[**remove_node_api_node_node_id_delete**](NodeApi.md#remove_node_api_node_node_id_delete) | **DELETE** /api/node/{node_id} | Remove Node


# **add_node_api_node_post**
> NodeResponse add_node_api_node_post(node_create)

Add Node

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.node_create import NodeCreate
from marzban_api.models.node_response import NodeResponse
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
    api_instance = marzban_api.NodeApi(api_client)
    node_create = marzban_api.NodeCreate() # NodeCreate | 

    try:
        # Add Node
        api_response = api_instance.add_node_api_node_post(node_create)
        print("The response of NodeApi->add_node_api_node_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->add_node_api_node_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_create** | [**NodeCreate**](NodeCreate.md)|  | 

### Return type

[**NodeResponse**](NodeResponse.md)

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

# **get_node_api_node_node_id_get**
> NodeResponse get_node_api_node_node_id_get(node_id)

Get Node

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.node_response import NodeResponse
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
    api_instance = marzban_api.NodeApi(api_client)
    node_id = 56 # int | 

    try:
        # Get Node
        api_response = api_instance.get_node_api_node_node_id_get(node_id)
        print("The response of NodeApi->get_node_api_node_node_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->get_node_api_node_node_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 

### Return type

[**NodeResponse**](NodeResponse.md)

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
**404** | Node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_api_node_settings_get**
> NodeSettings get_node_api_node_settings_get()

Get Node

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.node_settings import NodeSettings
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
    api_instance = marzban_api.NodeApi(api_client)

    try:
        # Get Node
        api_response = api_instance.get_node_api_node_settings_get()
        print("The response of NodeApi->get_node_api_node_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->get_node_api_node_settings_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NodeSettings**](NodeSettings.md)

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
**404** | Node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes_api_nodes_get**
> List[NodeResponse] get_nodes_api_nodes_get()

Get Nodes

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.node_response import NodeResponse
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
    api_instance = marzban_api.NodeApi(api_client)

    try:
        # Get Nodes
        api_response = api_instance.get_nodes_api_nodes_get()
        print("The response of NodeApi->get_nodes_api_nodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->get_nodes_api_nodes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[NodeResponse]**](NodeResponse.md)

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

# **get_usage_api_nodes_usage_get**
> NodesUsageResponse get_usage_api_nodes_usage_get(start=start, end=end)

Get Usage

Get nodes usage

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.nodes_usage_response import NodesUsageResponse
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
    api_instance = marzban_api.NodeApi(api_client)
    start = 'start_example' # str |  (optional)
    end = 'end_example' # str |  (optional)

    try:
        # Get Usage
        api_response = api_instance.get_usage_api_nodes_usage_get(start=start, end=end)
        print("The response of NodeApi->get_usage_api_nodes_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->get_usage_api_nodes_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**|  | [optional] 
 **end** | **str**|  | [optional] 

### Return type

[**NodesUsageResponse**](NodesUsageResponse.md)

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

# **modify_node_api_node_node_id_put**
> NodeResponse modify_node_api_node_node_id_put(node_id, node_modify)

Modify Node

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import marzban_api
from marzban_api.models.node_modify import NodeModify
from marzban_api.models.node_response import NodeResponse
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
    api_instance = marzban_api.NodeApi(api_client)
    node_id = 56 # int | 
    node_modify = marzban_api.NodeModify() # NodeModify | 

    try:
        # Modify Node
        api_response = api_instance.modify_node_api_node_node_id_put(node_id, node_modify)
        print("The response of NodeApi->modify_node_api_node_node_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->modify_node_api_node_node_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 
 **node_modify** | [**NodeModify**](NodeModify.md)|  | 

### Return type

[**NodeResponse**](NodeResponse.md)

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
**404** | Node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconnect_node_api_node_node_id_reconnect_post**
> object reconnect_node_api_node_node_id_reconnect_post(node_id)

Reconnect Node

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
    api_instance = marzban_api.NodeApi(api_client)
    node_id = 56 # int | 

    try:
        # Reconnect Node
        api_response = api_instance.reconnect_node_api_node_node_id_reconnect_post(node_id)
        print("The response of NodeApi->reconnect_node_api_node_node_id_reconnect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->reconnect_node_api_node_node_id_reconnect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 

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
**404** | Node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_node_api_node_node_id_delete**
> object remove_node_api_node_node_id_delete(node_id)

Remove Node

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
    api_instance = marzban_api.NodeApi(api_client)
    node_id = 56 # int | 

    try:
        # Remove Node
        api_response = api_instance.remove_node_api_node_node_id_delete(node_id)
        print("The response of NodeApi->remove_node_api_node_node_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeApi->remove_node_api_node_node_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 

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
**404** | Node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

