# ```hellosign_sdk.UnclaimedDraftApi```

All URIs are relative to *https://api.hellosign.com/v3*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[```unclaimed_draft_create```](UnclaimedDraftApi.md#unclaimed_draft_create) | ```POST /unclaimed_draft/create``` | Create Unclaimed Draft|
|[```unclaimed_draft_create_embedded```](UnclaimedDraftApi.md#unclaimed_draft_create_embedded) | ```POST /unclaimed_draft/create_embedded``` | Create Embedded Unclaimed Draft|
|[```unclaimed_draft_create_embedded_with_template```](UnclaimedDraftApi.md#unclaimed_draft_create_embedded_with_template) | ```POST /unclaimed_draft/create_embedded_with_template``` | Create Embedded Unclaimed Draft with Template|
|[```unclaimed_draft_edit_and_resend```](UnclaimedDraftApi.md#unclaimed_draft_edit_and_resend) | ```POST /unclaimed_draft/edit_and_resend/{signature_request_id}``` | Edit and Resend Unclaimed Draft|


# ```unclaimed_draft_create```
> ```UnclaimedDraftCreateResponse unclaimed_draft_create(unclaimed_draft_create_request)```

Create Unclaimed Draft

Creates a new Draft that can be claimed using the claim URL. The first authenticated user to access the URL will claim the Draft and will be shown either the \"Sign and send\" or the \"Request signature\" page with the Draft loaded. Subsequent access to the claim URL will result in a 404.

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
    api = apis.UnclaimedDraftApi(api_client)

    signer_1 = models.SubUnclaimedDraftSigner(
        email_address="jack@example.com",
        name="Jack",
        order=0,
    )

    signer_2 = models.SubUnclaimedDraftSigner(
        email_address="jill@example.com",
        name="Jill",
        order=1,
    )

    signing_options = models.SubSigningOptions(
        draw=True,
        type=True,
        upload=True,
        phone=False,
        default_type="draw",
    )

    field_options = models.SubFieldOptions(
        date_format="DD - MM - YYYY",
    )

    data = models.UnclaimedDraftCreateRequest(
        subject="The NDA we talked about",
        type="request_signature",
        message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.",
        signers=[signer_1, signer_2],
        cc_email_addresses=[
            "lawyer@hellosign.com",
            "lawyer@example.com",
        ],
        file=[open("example_signature_request.pdf", "rb")],
        metadata={
            "custom_id": 1234,
            "custom_text": "NDA #9",
        },
        signing_options=signing_options,
        field_options=field_options,
        test_mode=True,
    )

    try:
        response = api.unclaimed_draft_create(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `unclaimed_draft_create_request` | [**UnclaimedDraftCreateRequest**](UnclaimedDraftCreateRequest.md) |  |  |

### Return type

[**UnclaimedDraftCreateResponse**](UnclaimedDraftCreateResponse.md)

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

# ```unclaimed_draft_create_embedded```
> ```UnclaimedDraftCreateResponse unclaimed_draft_create_embedded(unclaimed_draft_create_embedded_request)```

Create Embedded Unclaimed Draft

Creates a new Draft that can be claimed and used in an embedded iFrame. The first authenticated user to access the URL will claim the Draft and will be shown the \"Request signature\" page with the Draft loaded. Subsequent access to the claim URL will result in a `404`. For this embedded endpoint the `requester_email_address` parameter is required.  **NOTE**: Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used and accessed on Dropbox Sign.

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
    api = apis.UnclaimedDraftApi(api_client)

    data = models.UnclaimedDraftCreateEmbeddedRequest(
        client_id="ec64a202072370a737edf4a0eb7f4437",
        file=[open("example_signature_request.pdf", "rb")],
        requester_email_address="jack@hellosign.com",
        test_mode=True,
    )

    try:
        response = api.unclaimed_draft_create_embedded(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `unclaimed_draft_create_embedded_request` | [**UnclaimedDraftCreateEmbeddedRequest**](UnclaimedDraftCreateEmbeddedRequest.md) |  |  |

### Return type

[**UnclaimedDraftCreateResponse**](UnclaimedDraftCreateResponse.md)

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

# ```unclaimed_draft_create_embedded_with_template```
> ```UnclaimedDraftCreateResponse unclaimed_draft_create_embedded_with_template(unclaimed_draft_create_embedded_with_template_request)```

Create Embedded Unclaimed Draft with Template

Creates a new Draft with a previously saved template(s) that can be claimed and used in an embedded iFrame. The first authenticated user to access the URL will claim the Draft and will be shown the \"Request signature\" page with the Draft loaded. Subsequent access to the claim URL will result in a `404`. For this embedded endpoint the `requester_email_address` parameter is required.  **NOTE**: Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used and accessed on Dropbox Sign.

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
    api = apis.UnclaimedDraftApi(api_client)

    signer_1 = models.SubUnclaimedDraftTemplateSigner(
        role="Client",
        name="George",
        email_address="george@example.com",
    )

    cc_1 = models.SubCC(
        role="Accounting",
        email_address="accounting@example.com",
    )

    data = models.UnclaimedDraftCreateEmbeddedWithTemplateRequest(
        client_id="ec64a202072370a737edf4a0eb7f4437",
        template_ids=["61a832ff0d8423f91d503e76bfbcc750f7417c78"],
        requester_email_address="jack@hellosign.com",
        signers=[signer_1],
        ccs=[cc_1],
        test_mode=True,
    )

    try:
        response = api.unclaimed_draft_create_embedded_with_template(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `unclaimed_draft_create_embedded_with_template_request` | [**UnclaimedDraftCreateEmbeddedWithTemplateRequest**](UnclaimedDraftCreateEmbeddedWithTemplateRequest.md) |  |  |

### Return type

[**UnclaimedDraftCreateResponse**](UnclaimedDraftCreateResponse.md)

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

# ```unclaimed_draft_edit_and_resend```
> ```UnclaimedDraftCreateResponse unclaimed_draft_edit_and_resend(signature_request_id, unclaimed_draft_edit_and_resend_request)```

Edit and Resend Unclaimed Draft

Creates a new signature request from an embedded request that can be edited prior to being sent to the recipients. Parameter `test_mode` can be edited prior to request. Signers can be edited in embedded editor. Requester's email address will remain unchanged if `requester_email_address` parameter is not set.  **NOTE**: Embedded unclaimed drafts can only be accessed in embedded iFrames whereas normal drafts can be used and accessed on Dropbox Sign.

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
    api = apis.UnclaimedDraftApi(api_client)

    data = models.UnclaimedDraftEditAndResendRequest(
        client_id="ec64a202072370a737edf4a0eb7f4437",
        test_mode=True,
    )

    signature_request_id = "2f9781e1a83jdja934d808c153c2e1d3df6f8f2f"

    try:
        response = api.unclaimed_draft_edit_and_resend(signature_request_id, data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `signature_request_id` | **str** | The ID of the signature request to edit and resend. |  |
| `unclaimed_draft_edit_and_resend_request` | [**UnclaimedDraftEditAndResendRequest**](UnclaimedDraftEditAndResendRequest.md) |  |  |

### Return type

[**UnclaimedDraftCreateResponse**](UnclaimedDraftCreateResponse.md)

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

