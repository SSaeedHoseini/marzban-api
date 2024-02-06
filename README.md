# marzban-api
Unified GUI Censorship Resistant Solution Powered by Xray

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.4.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import marzban-api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import marzban-api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    admin_create = marzban-api.AdminCreate() # AdminCreate | 

    try:
        # Create Admin
        api_response = api_instance.create_admin_api_admin_post(admin_create)
        print("The response of AdminApi->create_admin_api_admin_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->create_admin_api_admin_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**create_admin_api_admin_post**](docs/AdminApi.md#create_admin_api_admin_post) | **POST** /api/admin | Create Admin
*AdminApi* | [**get_admins_api_admins_get**](docs/AdminApi.md#get_admins_api_admins_get) | **GET** /api/admins | Get Admins
*AdminApi* | [**get_current_admin_api_admin_get**](docs/AdminApi.md#get_current_admin_api_admin_get) | **GET** /api/admin | Get Current Admin
*AdminApi* | [**login_for_access_token_api_admin_token_post**](docs/AdminApi.md#login_for_access_token_api_admin_token_post) | **POST** /api/admin/token | Login For Access Token
*AdminApi* | [**modify_admin_api_admin_username_put**](docs/AdminApi.md#modify_admin_api_admin_username_put) | **PUT** /api/admin/{username} | Modify Admin
*AdminApi* | [**remove_admin_api_admin_username_delete**](docs/AdminApi.md#remove_admin_api_admin_username_delete) | **DELETE** /api/admin/{username} | Remove Admin
*CoreApi* | [**get_core_config_api_core_config_get**](docs/CoreApi.md#get_core_config_api_core_config_get) | **GET** /api/core/config | Get Core Config
*CoreApi* | [**get_core_stats_api_core_get**](docs/CoreApi.md#get_core_stats_api_core_get) | **GET** /api/core | Get Core Stats
*CoreApi* | [**modify_core_config_api_core_config_put**](docs/CoreApi.md#modify_core_config_api_core_config_put) | **PUT** /api/core/config | Modify Core Config
*CoreApi* | [**restart_core_api_core_restart_post**](docs/CoreApi.md#restart_core_api_core_restart_post) | **POST** /api/core/restart | Restart Core
*NodeApi* | [**add_node_api_node_post**](docs/NodeApi.md#add_node_api_node_post) | **POST** /api/node | Add Node
*NodeApi* | [**get_node_api_node_node_id_get**](docs/NodeApi.md#get_node_api_node_node_id_get) | **GET** /api/node/{node_id} | Get Node
*NodeApi* | [**get_node_api_node_settings_get**](docs/NodeApi.md#get_node_api_node_settings_get) | **GET** /api/node/settings | Get Node
*NodeApi* | [**get_nodes_api_nodes_get**](docs/NodeApi.md#get_nodes_api_nodes_get) | **GET** /api/nodes | Get Nodes
*NodeApi* | [**get_usage_api_nodes_usage_get**](docs/NodeApi.md#get_usage_api_nodes_usage_get) | **GET** /api/nodes/usage | Get Usage
*NodeApi* | [**modify_node_api_node_node_id_put**](docs/NodeApi.md#modify_node_api_node_node_id_put) | **PUT** /api/node/{node_id} | Modify Node
*NodeApi* | [**reconnect_node_api_node_node_id_reconnect_post**](docs/NodeApi.md#reconnect_node_api_node_node_id_reconnect_post) | **POST** /api/node/{node_id}/reconnect | Reconnect Node
*NodeApi* | [**remove_node_api_node_node_id_delete**](docs/NodeApi.md#remove_node_api_node_node_id_delete) | **DELETE** /api/node/{node_id} | Remove Node
*SubscriptionApi* | [**user_subscription_info_sub_token_info_get**](docs/SubscriptionApi.md#user_subscription_info_sub_token_info_get) | **GET** /sub/{token}/info | User Subscription Info
*SubscriptionApi* | [**user_subscription_sub_token_get**](docs/SubscriptionApi.md#user_subscription_sub_token_get) | **GET** /sub/{token}/ | User Subscription
*SubscriptionApi* | [**user_subscription_with_client_type_sub_token_client_type_get**](docs/SubscriptionApi.md#user_subscription_with_client_type_sub_token_client_type_get) | **GET** /sub/{token}/{client_type} | User Subscription With Client Type
*SystemApi* | [**get_hosts_api_hosts_get**](docs/SystemApi.md#get_hosts_api_hosts_get) | **GET** /api/hosts | Get Hosts
*SystemApi* | [**get_inbounds_api_inbounds_get**](docs/SystemApi.md#get_inbounds_api_inbounds_get) | **GET** /api/inbounds | Get Inbounds
*SystemApi* | [**get_system_stats_api_system_get**](docs/SystemApi.md#get_system_stats_api_system_get) | **GET** /api/system | Get System Stats
*SystemApi* | [**modify_hosts_api_hosts_put**](docs/SystemApi.md#modify_hosts_api_hosts_put) | **PUT** /api/hosts | Modify Hosts
*UserApi* | [**add_user_api_user_post**](docs/UserApi.md#add_user_api_user_post) | **POST** /api/user | Add User
*UserApi* | [**delete_expired_api_users_expired_delete**](docs/UserApi.md#delete_expired_api_users_expired_delete) | **DELETE** /api/users/expired | Delete Expired
*UserApi* | [**get_user_api_user_username_get**](docs/UserApi.md#get_user_api_user_username_get) | **GET** /api/user/{username} | Get User
*UserApi* | [**get_user_usage_api_user_username_usage_get**](docs/UserApi.md#get_user_usage_api_user_username_usage_get) | **GET** /api/user/{username}/usage | Get User Usage
*UserApi* | [**get_users_api_users_get**](docs/UserApi.md#get_users_api_users_get) | **GET** /api/users | Get Users
*UserApi* | [**modify_user_api_user_username_put**](docs/UserApi.md#modify_user_api_user_username_put) | **PUT** /api/user/{username} | Modify User
*UserApi* | [**remove_user_api_user_username_delete**](docs/UserApi.md#remove_user_api_user_username_delete) | **DELETE** /api/user/{username} | Remove User
*UserApi* | [**reset_user_data_usage_api_user_username_reset_post**](docs/UserApi.md#reset_user_data_usage_api_user_username_reset_post) | **POST** /api/user/{username}/reset | Reset User Data Usage
*UserApi* | [**reset_users_data_usage_api_users_reset_post**](docs/UserApi.md#reset_users_data_usage_api_users_reset_post) | **POST** /api/users/reset | Reset Users Data Usage
*UserApi* | [**revoke_user_subscription_api_user_username_revoke_sub_post**](docs/UserApi.md#revoke_user_subscription_api_user_username_revoke_sub_post) | **POST** /api/user/{username}/revoke_sub | Revoke User Subscription
*UserApi* | [**set_owner_api_user_username_set_owner_put**](docs/UserApi.md#set_owner_api_user_username_set_owner_put) | **PUT** /api/user/{username}/set-owner | Set Owner
*UserTemplateApi* | [**add_user_template_api_user_template_post**](docs/UserTemplateApi.md#add_user_template_api_user_template_post) | **POST** /api/user_template | Add User Template
*UserTemplateApi* | [**get_user_template_api_user_template_id_get**](docs/UserTemplateApi.md#get_user_template_api_user_template_id_get) | **GET** /api/user_template/{id} | Get User Template
*UserTemplateApi* | [**get_user_templates_api_user_template_get**](docs/UserTemplateApi.md#get_user_templates_api_user_template_get) | **GET** /api/user_template | Get User Templates
*UserTemplateApi* | [**modify_user_template_api_user_template_id_put**](docs/UserTemplateApi.md#modify_user_template_api_user_template_id_put) | **PUT** /api/user_template/{id} | Modify User Template
*UserTemplateApi* | [**remove_user_template_api_user_template_id_delete**](docs/UserTemplateApi.md#remove_user_template_api_user_template_id_delete) | **DELETE** /api/user_template/{id} | Remove User Template
*DefaultApi* | [**base_get**](docs/DefaultApi.md#base_get) | **GET** / | Base


## Documentation For Models

 - [Admin](docs/Admin.md)
 - [AdminCreate](docs/AdminCreate.md)
 - [AdminModify](docs/AdminModify.md)
 - [CoreStats](docs/CoreStats.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [LocationInner](docs/LocationInner.md)
 - [NodeCreate](docs/NodeCreate.md)
 - [NodeModify](docs/NodeModify.md)
 - [NodeResponse](docs/NodeResponse.md)
 - [NodeSettings](docs/NodeSettings.md)
 - [NodeStatus](docs/NodeStatus.md)
 - [NodeUsageResponse](docs/NodeUsageResponse.md)
 - [NodesUsageResponse](docs/NodesUsageResponse.md)
 - [Port](docs/Port.md)
 - [ProxyHost](docs/ProxyHost.md)
 - [ProxyHostALPN](docs/ProxyHostALPN.md)
 - [ProxyHostFingerprint](docs/ProxyHostFingerprint.md)
 - [ProxyHostSecurity](docs/ProxyHostSecurity.md)
 - [ProxyInbound](docs/ProxyInbound.md)
 - [ProxyTypes](docs/ProxyTypes.md)
 - [SystemStats](docs/SystemStats.md)
 - [Token](docs/Token.md)
 - [UserCreate](docs/UserCreate.md)
 - [UserDataLimitResetStrategy](docs/UserDataLimitResetStrategy.md)
 - [UserModify](docs/UserModify.md)
 - [UserResponse](docs/UserResponse.md)
 - [UserStatus](docs/UserStatus.md)
 - [UserStatusCreate](docs/UserStatusCreate.md)
 - [UserStatusModify](docs/UserStatusModify.md)
 - [UserTemplateCreate](docs/UserTemplateCreate.md)
 - [UserTemplateModify](docs/UserTemplateModify.md)
 - [UserTemplateResponse](docs/UserTemplateResponse.md)
 - [UserUsageResponse](docs/UserUsageResponse.md)
 - [UserUsagesResponse](docs/UserUsagesResponse.md)
 - [UsersResponse](docs/UsersResponse.md)
 - [ValidationError](docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="OAuth2PasswordBearer"></a>
### OAuth2PasswordBearer

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A


## Author



