# marzban_api.SubscriptionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_subscription_info_sub_token_info_get**](SubscriptionApi.md#user_subscription_info_sub_token_info_get) | **GET** /sub/{token}/info | User Subscription Info
[**user_subscription_sub_token_get**](SubscriptionApi.md#user_subscription_sub_token_get) | **GET** /sub/{token}/ | User Subscription
[**user_subscription_with_client_type_sub_token_client_type_get**](SubscriptionApi.md#user_subscription_with_client_type_sub_token_client_type_get) | **GET** /sub/{token}/{client_type} | User Subscription With Client Type


# **user_subscription_info_sub_token_info_get**
> UserResponse user_subscription_info_sub_token_info_get(token)

User Subscription Info

### Example


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


# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.SubscriptionApi(api_client)
    token = 'token_example' # str | 

    try:
        # User Subscription Info
        api_response = api_instance.user_subscription_info_sub_token_info_get(token)
        print("The response of SubscriptionApi->user_subscription_info_sub_token_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->user_subscription_info_sub_token_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_subscription_sub_token_get**
> object user_subscription_sub_token_get(token, user_agent=user_agent)

User Subscription

Subscription link, V2ray and Clash supported

### Example


```python
import marzban_api
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.SubscriptionApi(api_client)
    token = 'token_example' # str | 
    user_agent = '' # str |  (optional) (default to '')

    try:
        # User Subscription
        api_response = api_instance.user_subscription_sub_token_get(token, user_agent=user_agent)
        print("The response of SubscriptionApi->user_subscription_sub_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->user_subscription_sub_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **user_agent** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_subscription_with_client_type_sub_token_client_type_get**
> object user_subscription_with_client_type_sub_token_client_type_get(token, client_type)

User Subscription With Client Type

Subscription link, v2ray, clash, sing-box, outline and clash-meta supported

### Example


```python
import marzban_api
from marzban_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = marzban_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with marzban_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = marzban_api.SubscriptionApi(api_client)
    token = 'token_example' # str | 
    client_type = 'client_type_example' # str | 

    try:
        # User Subscription With Client Type
        api_response = api_instance.user_subscription_with_client_type_sub_token_client_type_get(token, client_type)
        print("The response of SubscriptionApi->user_subscription_with_client_type_sub_token_client_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->user_subscription_with_client_type_sub_token_client_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **client_type** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**400** | Invalid subscription type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

