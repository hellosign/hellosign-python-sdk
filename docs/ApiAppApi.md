# ```hellosign_sdk.ApiAppApi```

All URIs are relative to *https://api.hellosign.com/v3*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[```api_app_create```](ApiAppApi.md#api_app_create) | ```POST /api_app``` | Create API App|
|[```api_app_delete```](ApiAppApi.md#api_app_delete) | ```DELETE /api_app/{client_id}``` | Delete API App|
|[```api_app_get```](ApiAppApi.md#api_app_get) | ```GET /api_app/{client_id}``` | Get API App|
|[```api_app_list```](ApiAppApi.md#api_app_list) | ```GET /api_app/list``` | List API Apps|
|[```api_app_update```](ApiAppApi.md#api_app_update) | ```PUT /api_app/{client_id}``` | Update API App|


# ```api_app_create```
> ```ApiAppGetResponse api_app_create(api_app_create_request)```

Create API App

Creates a new API App.

### Example

* Basic Authentication (api_key):
* Bearer (JWT) Authentication (oauth2):

```python
from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis, models

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.ApiAppApi(api_client)

    oauth = models.SubOAuth(
        callback_url="https://example.com/oauth",
        scopes=["basic_account_info" "request_signature"],
    )

    white_labeling_options = models.SubWhiteLabelingOptions(
        primary_button_color="#00b3e6",
        primary_button_text_color="#ffffff",
    )

    custom_logo_file = open('./CustomLogoFile.png', 'rb')

    data = models.ApiAppCreateRequest(
        name="My Production App",
        domains=["example.com"],
        oauth=oauth,
        white_labeling_options=white_labeling_options,
        custom_logo_file=custom_logo_file,
    )

    try:
        response = api.api_app_create(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `api_app_create_request` | [**ApiAppCreateRequest**](ApiAppCreateRequest.md) |  |  |

### Return type

[**ApiAppGetResponse**](ApiAppGetResponse.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-Ratelimit-Reset -  <br>  |
**4XX** | failed_operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# ```api_app_delete```
> ```api_app_delete(client_id)```

Delete API App

Deletes an API App. Can only be invoked for apps you own.

### Example

* Basic Authentication (api_key):
* Bearer (JWT) Authentication (oauth2):

```python
from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.ApiAppApi(api_client)

    client_id = "0dd3b823a682527788c4e40cb7b6f7e9"

    try:
        response = api.api_app_delete(client_id)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `client_id` | **str** | The client id of the API App to delete. |  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-Ratelimit-Reset -  <br>  |
**4XX** | failed_operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# ```api_app_get```
> ```ApiAppGetResponse api_app_get(client_id)```

Get API App

Returns an object with information about an API App.

### Example

* Basic Authentication (api_key):
* Bearer (JWT) Authentication (oauth2):

```python
from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.ApiAppApi(api_client)

    client_id = "0dd3b823a682527788c4e40cb7b6f7e9"

    try:
        response = api.api_app_get(client_id)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `client_id` | **str** | The client id of the API App to retrieve. |  |

### Return type

[**ApiAppGetResponse**](ApiAppGetResponse.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-Ratelimit-Reset -  <br>  |
**4XX** | failed_operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# ```api_app_list```
> ```ApiAppListResponse api_app_list()```

List API Apps

Returns a list of API Apps that are accessible by you. If you are on a team with an Admin or Developer role, this list will include apps owned by teammates.

### Example

* Basic Authentication (api_key):
* Bearer (JWT) Authentication (oauth2):

```python
from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.ApiAppApi(api_client)

    page = 1
    page_size = 2

    try:
        response = api.api_app_list(
            page=page,
            page_size=page_size,
        )
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `page` | **int** | Which page number of the API App List to return. Defaults to `1`. | [optional][default to 1] |
| `page_size` | **int** | Number of objects to be returned per page. Must be between `1` and `100`. Default is `20`. | [optional][default to 20] |

### Return type

[**ApiAppListResponse**](ApiAppListResponse.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-Ratelimit-Reset -  <br>  |
**4XX** | failed_operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# ```api_app_update```
> ```ApiAppGetResponse api_app_update(client_id, api_app_update_request)```

Update API App

Updates an existing API App. Can only be invoked for apps you own. Only the fields you provide will be updated. If you wish to clear an existing optional field, provide an empty string.

### Example

* Basic Authentication (api_key):
* Bearer (JWT) Authentication (oauth2):

```python
from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis, models

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.ApiAppApi(api_client)

    white_labeling_options = models.SubWhiteLabelingOptions(
        primary_button_color="#00b3e6",
        primary_button_text_color="#ffffff",
    )

    custom_logo_file = open('./CustomLogoFile.png', 'rb')

    data = models.ApiAppUpdateRequest(
        name="New Name",
        callback_url="http://example.com/hellosign",
        white_labeling_options=white_labeling_options,
        custom_logo_file=custom_logo_file,
    )

    client_id = "0dd3b823a682527788c4e40cb7b6f7e9"

    try:
        response = api.api_app_update(client_id, data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `client_id` | **str** | The client id of the API App to update. |  |
| `api_app_update_request` | [**ApiAppUpdateRequest**](ApiAppUpdateRequest.md) |  |  |

### Return type

[**ApiAppGetResponse**](ApiAppGetResponse.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-Ratelimit-Reset -  <br>  |
**4XX** | failed_operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

