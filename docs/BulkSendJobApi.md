# ```hellosign_sdk.BulkSendJobApi```

All URIs are relative to *https://api.hellosign.com/v3*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[```bulk_send_job_get```](BulkSendJobApi.md#bulk_send_job_get) | ```GET /bulk_send_job/{bulk_send_job_id}``` | Get Bulk Send Job|
|[```bulk_send_job_list```](BulkSendJobApi.md#bulk_send_job_list) | ```GET /bulk_send_job/list``` | List Bulk Send Jobs|


# ```bulk_send_job_get```
> ```BulkSendJobGetResponse bulk_send_job_get(bulk_send_job_id)```

Get Bulk Send Job

Returns the status of the BulkSendJob and its SignatureRequests specified by the `bulk_send_job_id` parameter.

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
    api = apis.BulkSendJobApi(api_client)

    bulk_send_job_id = "6e683bc0369ba3d5b6f43c2c22a8031dbf6bd174"

    try:
        response = api.bulk_send_job_get(bulk_send_job_id)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `bulk_send_job_id` | **str** | The id of the BulkSendJob to retrieve. |  |

### Return type

[**BulkSendJobGetResponse**](BulkSendJobGetResponse.md)

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

# ```bulk_send_job_list```
> ```BulkSendJobListResponse bulk_send_job_list()```

List Bulk Send Jobs

Returns a list of BulkSendJob that you can access.

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
    api = apis.BulkSendJobApi(api_client)

    page = 1
    page_size = 20

    try:
        response = api.bulk_send_job_list(
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
| `page` | **int** | Which page number of the BulkSendJob List to return. Defaults to `1`. | [optional][default to 1] |
| `page_size` | **int** | Number of objects to be returned per page. Must be between `1` and `100`. Default is 20. | [optional][default to 20] |

### Return type

[**BulkSendJobListResponse**](BulkSendJobListResponse.md)

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

