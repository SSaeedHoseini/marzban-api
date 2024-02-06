# marzban-api.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**base_get**](DefaultApi.md#base_get) | **GET** / | Base


# **base_get**
> str base_get()

Base

### Example


```python
import marzban-api
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
    api_instance = marzban-api.DefaultApi(api_client)

    try:
        # Base
        api_response = api_instance.base_get()
        print("The response of DefaultApi->base_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->base_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

