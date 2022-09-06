# ```hellosign_sdk.EmbeddedApi```

All URIs are relative to *https://api.hellosign.com/v3*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[```embedded_edit_url```](EmbeddedApi.md#embedded_edit_url) | ```POST /embedded/edit_url/{template_id}``` | Get Embedded Template Edit URL|
|[```embedded_sign_url```](EmbeddedApi.md#embedded_sign_url) | ```GET /embedded/sign_url/{signature_id}``` | Get Embedded Sign URL|


# ```embedded_edit_url```
> ```EmbeddedEditUrlResponse embedded_edit_url(template_id, embedded_edit_url_request)```

Get Embedded Template Edit URL

Retrieves an embedded object containing a template url that can be opened in an iFrame. Note that only templates created via the embedded template process are available to be edited with this endpoint.

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
    api = apis.EmbeddedApi(api_client)

    data = models.EmbeddedEditUrlRequest(
        cc_roles=[""],
        merge_fields=[],
    )

    template_id = "5de8179668f2033afac48da1868d0093bf133266"

    try:
        response = api.embedded_edit_url(template_id, data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `template_id` | **str** | The id of the template to edit. |  |
| `embedded_edit_url_request` | [**EmbeddedEditUrlRequest**](EmbeddedEditUrlRequest.md) |  |  |

### Return type

[**EmbeddedEditUrlResponse**](EmbeddedEditUrlResponse.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-Ratelimit-Reset -  <br>  |
**4XX** | failed_operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# ```embedded_sign_url```
> ```EmbeddedSignUrlResponse embedded_sign_url(signature_id)```

Get Embedded Sign URL

Retrieves an embedded object containing a signature url that can be opened in an iFrame. Note that templates created via the embedded template process will only be accessible through the API.

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
    api = apis.EmbeddedApi(api_client)

    signature_id = "50e3542f738adfa7ddd4cbd4c00d2a8ab6e4194b"

    try:
        response = api.embedded_sign_url(signature_id)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `signature_id` | **str** | The id of the signature to get a signature url for. |  |

### Return type

[**EmbeddedSignUrlResponse**](EmbeddedSignUrlResponse.md)

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

