# hellosign-python-sdk

HelloSign v3 API

## ⚠ This package is not yet ready for production use ⚠

We are working hard on getting this package ready, but it is not there, yet!

You should think twice before using package on anything critical.

The interfaces may change without warning. Backwards compatibility is not yet
guaranteed nor implied!

## Contributing

### Submodule

This repo uses the [hellosign/openapi](https://github.com/hellosign/openapi) repo
as a submodule for its OAS source. When you first clone this repo you must also
instantiate the submodule by running the following:

```shell
git submodule init
git submodule update
```

### Changes to the OAS

You must make OAS changes in the `oas/openapi.yaml` file within the
[hellosign/openapi](https://github.com/hellosign/openapi) submodule.

### Changes to the SDK code

You must make SDK code changes in the mustache file within the `templates`
directory that corresponds to the file you want updated.

We use [OpenAPI Generator](https://openapi-generator.tech/) to automatically
generate this SDK from the OAS, using the template files.

### Building

You must have `docker` (or `podman` linked to `docker`) installed. Highly
recommended to use
[rootless docker](https://docs.docker.com/engine/security/rootless/).

Run the following and everything is done for you:

```shell
./build
```

*Attention*: Any changes you have made to the SDK code that you have not made
to the OAS file and/or the mustache template files _will be lost_ when you run
this command.

## Installation & Usage

### Requirements.

Python 3.7

### easy_install

Install using `easy_install`:

```shell
easy_install hellosign-python-sdk
```

### pip

Install using `pip`:

```shell
pip install hellosign-python-sdk
```

### Repo

Install from code:

```shell
git clone https://github.com/HelloSign/hellosign-python-sdk.git
cd hellosign-python-sdk
python setup.py install --user
```

Then import the package:
```python
import hellosign_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:


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
    api = apis.AccountApi(api_client)

    data = models.AccountCreateRequest(
        email_address="newuser@hellosign.com",
    )

    try:
        response = api.account_create(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


## Documentation for API Endpoints

All URIs are relative to *https://api.hellosign.com/v3*

|Class | Method | HTTP request | Description|
|------------ | ------------- | ------------- | -------------|
|```AccountApi``` | [```account_create```](docs/AccountApi.md#account_create) | ```POST /account/create``` | Signs up for a new HelloSign Account.|
```AccountApi``` | [```account_get```](docs/AccountApi.md#account_get) | ```GET /account``` | Returns your Account settings.|
```AccountApi``` | [```account_update```](docs/AccountApi.md#account_update) | ```PUT /account``` | Updates your Account&#39;s settings.|
```AccountApi``` | [```account_verify```](docs/AccountApi.md#account_verify) | ```POST /account/verify``` | Verify whether a HelloSign Account exists.|
|```ApiAppApi``` | [```api_app_create```](docs/ApiAppApi.md#api_app_create) | ```POST /api_app``` | Creates a new API App.|
```ApiAppApi``` | [```api_app_delete```](docs/ApiAppApi.md#api_app_delete) | ```DELETE /api_app/{client_id}``` | Deletes an API App.|
```ApiAppApi``` | [```api_app_get```](docs/ApiAppApi.md#api_app_get) | ```GET /api_app/{client_id}``` | Gets an API App.|
```ApiAppApi``` | [```api_app_list```](docs/ApiAppApi.md#api_app_list) | ```GET /api_app/list``` | Lists your API Apps.|
```ApiAppApi``` | [```api_app_update```](docs/ApiAppApi.md#api_app_update) | ```PUT /api_app/{client_id}``` | Updates an existing API App.|
|```BulkSendJobApi``` | [```bulk_send_job_get```](docs/BulkSendJobApi.md#bulk_send_job_get) | ```GET /bulk_send_job/{bulk_send_job_id}``` | Gets a BulkSendJob that includes all SignatureRequests it has sent.|
```BulkSendJobApi``` | [```bulk_send_job_list```](docs/BulkSendJobApi.md#bulk_send_job_list) | ```GET /bulk_send_job/list``` | Lists the BulkSendJob that you have access to.|
|```EmbeddedApi``` | [```embedded_edit_url```](docs/EmbeddedApi.md#embedded_edit_url) | ```POST /embedded/edit_url/{template_id}``` | Retrieves an embedded template object.|
```EmbeddedApi``` | [```embedded_sign_url```](docs/EmbeddedApi.md#embedded_sign_url) | ```GET /embedded/sign_url/{signature_id}``` | Retrieves an embedded signing object.|
|```OAuthApi``` | [```oauth_token_generate```](docs/OAuthApi.md#oauth_token_generate) | ```POST /oauth/token``` | OAuth Token Generate|
```OAuthApi``` | [```oauth_token_refresh```](docs/OAuthApi.md#oauth_token_refresh) | ```POST /oauth/token?refresh``` | OAuth Token Refresh|
|```ReportApi``` | [```report_create```](docs/ReportApi.md#report_create) | ```POST /report/create``` | Creates one or more report(s).|
|```SignatureRequestApi``` | [```signature_request_bulk_create_embedded_with_template```](docs/SignatureRequestApi.md#signature_request_bulk_create_embedded_with_template) | ```POST /signature_request/bulk_create_embedded_with_template``` | Creates BulkSendJob which sends SignatureRequests in bulk based off of the provided Template(s) to be signed in an embedded window.|
```SignatureRequestApi``` | [```signature_request_bulk_send_with_template```](docs/SignatureRequestApi.md#signature_request_bulk_send_with_template) | ```POST /signature_request/bulk_send_with_template``` | Creates BulkSendJob which sends SignatureRequests in bulk based off of the provided Template(s).|
```SignatureRequestApi``` | [```signature_request_cancel```](docs/SignatureRequestApi.md#signature_request_cancel) | ```POST /signature_request/cancel/{signature_request_id}``` | Cancels an incomplete SignatureRequest.|
```SignatureRequestApi``` | [```signature_request_create_embedded```](docs/SignatureRequestApi.md#signature_request_create_embedded) | ```POST /signature_request/create_embedded``` | Creates a new SignatureRequest to be signed in an embedded window.|
```SignatureRequestApi``` | [```signature_request_create_embedded_with_template```](docs/SignatureRequestApi.md#signature_request_create_embedded_with_template) | ```POST /signature_request/create_embedded_with_template``` | Creates and sends a new SignatureRequest based off of the provided Template(s).|
```SignatureRequestApi``` | [```signature_request_files```](docs/SignatureRequestApi.md#signature_request_files) | ```GET /signature_request/files/{signature_request_id}``` | Obtain a copy of the current documents.|
```SignatureRequestApi``` | [```signature_request_get```](docs/SignatureRequestApi.md#signature_request_get) | ```GET /signature_request/{signature_request_id}``` | Gets a SignatureRequest that includes the current status for each signer.|
```SignatureRequestApi``` | [```signature_request_list```](docs/SignatureRequestApi.md#signature_request_list) | ```GET /signature_request/list``` | Lists the SignatureRequests (both inbound and outbound) that you have access to.|
```SignatureRequestApi``` | [```signature_request_release_hold```](docs/SignatureRequestApi.md#signature_request_release_hold) | ```POST /signature_request/release_hold/{signature_request_id}``` | Releases a SignatureRequest from hold.|
```SignatureRequestApi``` | [```signature_request_remind```](docs/SignatureRequestApi.md#signature_request_remind) | ```POST /signature_request/remind/{signature_request_id}``` | Sends an email to the signer reminding them to sign the signature request.|
```SignatureRequestApi``` | [```signature_request_remove```](docs/SignatureRequestApi.md#signature_request_remove) | ```POST /signature_request/remove/{signature_request_id}``` | Remove access to a completed SignatureRequest.|
```SignatureRequestApi``` | [```signature_request_send```](docs/SignatureRequestApi.md#signature_request_send) | ```POST /signature_request/send``` | Creates and sends a new SignatureRequest with the submitted documents.|
```SignatureRequestApi``` | [```signature_request_send_with_template```](docs/SignatureRequestApi.md#signature_request_send_with_template) | ```POST /signature_request/send_with_template``` | Creates and sends a new SignatureRequest based off of one or more Templates.|
```SignatureRequestApi``` | [```signature_request_update```](docs/SignatureRequestApi.md#signature_request_update) | ```POST /signature_request/update/{signature_request_id}``` | Update an email address on a signature request.|
|```TeamApi``` | [```team_add_member```](docs/TeamApi.md#team_add_member) | ```PUT /team/add_member``` | Adds or invites a user to your Team.|
```TeamApi``` | [```team_create```](docs/TeamApi.md#team_create) | ```POST /team/create``` | Creates a new Team.|
```TeamApi``` | [```team_delete```](docs/TeamApi.md#team_delete) | ```DELETE /team/destroy``` | Deletes your Team.|
```TeamApi``` | [```team_get```](docs/TeamApi.md#team_get) | ```GET /team``` | Gets your Team and a list of its members.|
```TeamApi``` | [```team_remove_member```](docs/TeamApi.md#team_remove_member) | ```POST /team/remove_member``` | Removes a user from your Team.|
```TeamApi``` | [```team_update```](docs/TeamApi.md#team_update) | ```PUT /team``` | Updates a Team&#39;s name.|
|```TemplateApi``` | [```template_add_user```](docs/TemplateApi.md#template_add_user) | ```POST /template/add_user/{template_id}``` | Gives the specified Account access to the specified Template.|
```TemplateApi``` | [```template_create_embedded_draft```](docs/TemplateApi.md#template_create_embedded_draft) | ```POST /template/create_embedded_draft``` | Creates an embedded template draft for further editing.|
```TemplateApi``` | [```template_delete```](docs/TemplateApi.md#template_delete) | ```POST /template/delete/{template_id}``` | Deletes the specified template.|
```TemplateApi``` | [```template_files```](docs/TemplateApi.md#template_files) | ```GET /template/files/{template_id}``` | Obtain a copy of a template&#39;s original files.|
```TemplateApi``` | [```template_get```](docs/TemplateApi.md#template_get) | ```GET /template/{template_id}``` | Gets a Template which includes a list of Accounts that can access it.|
```TemplateApi``` | [```template_list```](docs/TemplateApi.md#template_list) | ```GET /template/list``` | Lists your Templates.|
```TemplateApi``` | [```template_remove_user```](docs/TemplateApi.md#template_remove_user) | ```POST /template/remove_user/{template_id}``` | Removes the specified Account&#39;s access to the specified Template.|
```TemplateApi``` | [```template_update_files```](docs/TemplateApi.md#template_update_files) | ```POST /template/update_files/{template_id}``` | Overlays a new file with the overlay of an existing template.|
|```UnclaimedDraftApi``` | [```unclaimed_draft_create```](docs/UnclaimedDraftApi.md#unclaimed_draft_create) | ```POST /unclaimed_draft/create``` | Creates a new Draft that can be claimed using the claim URL.|
```UnclaimedDraftApi``` | [```unclaimed_draft_create_embedded```](docs/UnclaimedDraftApi.md#unclaimed_draft_create_embedded) | ```POST /unclaimed_draft/create_embedded``` | Creates a new Draft that will be claimed for use in an embedded iFrame.|
```UnclaimedDraftApi``` | [```unclaimed_draft_create_embedded_with_template```](docs/UnclaimedDraftApi.md#unclaimed_draft_create_embedded_with_template) | ```POST /unclaimed_draft/create_embedded_with_template``` | Creates a new Draft using existing template(s) that will be claimed for use in an embedded iFrame.|
```UnclaimedDraftApi``` | [```unclaimed_draft_edit_and_resend```](docs/UnclaimedDraftApi.md#unclaimed_draft_edit_and_resend) | ```POST /unclaimed_draft/edit_and_resend/{signature_request_id}``` | Creates a new signature request from an embedded request that can be edited prior to being sent.|


## Documentation For Models

 - [AccountCreateRequest](docs/AccountCreateRequest.md)
 - [AccountCreateResponse](docs/AccountCreateResponse.md)
 - [AccountGetResponse](docs/AccountGetResponse.md)
 - [AccountResponse](docs/AccountResponse.md)
 - [AccountResponseQuotas](docs/AccountResponseQuotas.md)
 - [AccountUpdateRequest](docs/AccountUpdateRequest.md)
 - [AccountVerifyRequest](docs/AccountVerifyRequest.md)
 - [AccountVerifyResponse](docs/AccountVerifyResponse.md)
 - [AccountVerifyResponseAccount](docs/AccountVerifyResponseAccount.md)
 - [ApiAppCreateRequest](docs/ApiAppCreateRequest.md)
 - [ApiAppGetResponse](docs/ApiAppGetResponse.md)
 - [ApiAppListResponse](docs/ApiAppListResponse.md)
 - [ApiAppResponse](docs/ApiAppResponse.md)
 - [ApiAppResponseOAuth](docs/ApiAppResponseOAuth.md)
 - [ApiAppResponseOptions](docs/ApiAppResponseOptions.md)
 - [ApiAppResponseOwnerAccount](docs/ApiAppResponseOwnerAccount.md)
 - [ApiAppResponseWhiteLabelingOptions](docs/ApiAppResponseWhiteLabelingOptions.md)
 - [ApiAppUpdateRequest](docs/ApiAppUpdateRequest.md)
 - [BulkSendJobGetResponse](docs/BulkSendJobGetResponse.md)
 - [BulkSendJobGetResponseSignatureRequests](docs/BulkSendJobGetResponseSignatureRequests.md)
 - [BulkSendJobListResponse](docs/BulkSendJobListResponse.md)
 - [BulkSendJobResponse](docs/BulkSendJobResponse.md)
 - [BulkSendJobSendResponse](docs/BulkSendJobSendResponse.md)
 - [EmbeddedEditUrlRequest](docs/EmbeddedEditUrlRequest.md)
 - [EmbeddedEditUrlResponse](docs/EmbeddedEditUrlResponse.md)
 - [EmbeddedEditUrlResponseEmbedded](docs/EmbeddedEditUrlResponseEmbedded.md)
 - [EmbeddedSignUrlResponse](docs/EmbeddedSignUrlResponse.md)
 - [EmbeddedSignUrlResponseEmbedded](docs/EmbeddedSignUrlResponseEmbedded.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [EventCallbackAccountRequest](docs/EventCallbackAccountRequest.md)
 - [EventCallbackAccountRequestPayload](docs/EventCallbackAccountRequestPayload.md)
 - [EventCallbackApiAppRequest](docs/EventCallbackApiAppRequest.md)
 - [EventCallbackApiAppRequestPayload](docs/EventCallbackApiAppRequestPayload.md)
 - [EventCallbackRequestEvent](docs/EventCallbackRequestEvent.md)
 - [EventCallbackRequestEventMetadata](docs/EventCallbackRequestEventMetadata.md)
 - [FileResponse](docs/FileResponse.md)
 - [ListInfoResponse](docs/ListInfoResponse.md)
 - [OAuthTokenGenerateRequest](docs/OAuthTokenGenerateRequest.md)
 - [OAuthTokenRefreshRequest](docs/OAuthTokenRefreshRequest.md)
 - [OAuthTokenResponse](docs/OAuthTokenResponse.md)
 - [ReportCreateRequest](docs/ReportCreateRequest.md)
 - [ReportCreateResponse](docs/ReportCreateResponse.md)
 - [ReportResponse](docs/ReportResponse.md)
 - [SignatureRequestBulkCreateEmbeddedWithTemplateRequest](docs/SignatureRequestBulkCreateEmbeddedWithTemplateRequest.md)
 - [SignatureRequestBulkSendWithTemplateRequest](docs/SignatureRequestBulkSendWithTemplateRequest.md)
 - [SignatureRequestCreateEmbeddedRequest](docs/SignatureRequestCreateEmbeddedRequest.md)
 - [SignatureRequestCreateEmbeddedWithTemplateRequest](docs/SignatureRequestCreateEmbeddedWithTemplateRequest.md)
 - [SignatureRequestGetResponse](docs/SignatureRequestGetResponse.md)
 - [SignatureRequestListResponse](docs/SignatureRequestListResponse.md)
 - [SignatureRequestRemindRequest](docs/SignatureRequestRemindRequest.md)
 - [SignatureRequestResponse](docs/SignatureRequestResponse.md)
 - [SignatureRequestResponseCustomField](docs/SignatureRequestResponseCustomField.md)
 - [SignatureRequestResponseData](docs/SignatureRequestResponseData.md)
 - [SignatureRequestResponseSignatures](docs/SignatureRequestResponseSignatures.md)
 - [SignatureRequestSendRequest](docs/SignatureRequestSendRequest.md)
 - [SignatureRequestSendWithTemplateRequest](docs/SignatureRequestSendWithTemplateRequest.md)
 - [SignatureRequestUpdateRequest](docs/SignatureRequestUpdateRequest.md)
 - [SubAttachment](docs/SubAttachment.md)
 - [SubBulkSignerList](docs/SubBulkSignerList.md)
 - [SubBulkSignerListCustomField](docs/SubBulkSignerListCustomField.md)
 - [SubBulkSignerListSigner](docs/SubBulkSignerListSigner.md)
 - [SubCC](docs/SubCC.md)
 - [SubCustomField](docs/SubCustomField.md)
 - [SubEditorOptions](docs/SubEditorOptions.md)
 - [SubFieldOptions](docs/SubFieldOptions.md)
 - [SubFormFieldGroup](docs/SubFormFieldGroup.md)
 - [SubFormFieldRule](docs/SubFormFieldRule.md)
 - [SubFormFieldRuleAction](docs/SubFormFieldRuleAction.md)
 - [SubFormFieldRuleTrigger](docs/SubFormFieldRuleTrigger.md)
 - [SubFormFieldsPerDocumentBase](docs/SubFormFieldsPerDocumentBase.md)
 - [SubFormFieldsPerDocumentCheckbox](docs/SubFormFieldsPerDocumentCheckbox.md)
 - [SubFormFieldsPerDocumentCheckboxMerge](docs/SubFormFieldsPerDocumentCheckboxMerge.md)
 - [SubFormFieldsPerDocumentDateSigned](docs/SubFormFieldsPerDocumentDateSigned.md)
 - [SubFormFieldsPerDocumentDropdown](docs/SubFormFieldsPerDocumentDropdown.md)
 - [SubFormFieldsPerDocumentHyperlink](docs/SubFormFieldsPerDocumentHyperlink.md)
 - [SubFormFieldsPerDocumentInitials](docs/SubFormFieldsPerDocumentInitials.md)
 - [SubFormFieldsPerDocumentRadio](docs/SubFormFieldsPerDocumentRadio.md)
 - [SubFormFieldsPerDocumentSignature](docs/SubFormFieldsPerDocumentSignature.md)
 - [SubFormFieldsPerDocumentText](docs/SubFormFieldsPerDocumentText.md)
 - [SubFormFieldsPerDocumentTextMerge](docs/SubFormFieldsPerDocumentTextMerge.md)
 - [SubFormFieldsPerDocumentTypeEnum](docs/SubFormFieldsPerDocumentTypeEnum.md)
 - [SubMergeField](docs/SubMergeField.md)
 - [SubOAuth](docs/SubOAuth.md)
 - [SubOptions](docs/SubOptions.md)
 - [SubSignatureRequestEmbeddedSigner](docs/SubSignatureRequestEmbeddedSigner.md)
 - [SubSignatureRequestEmbeddedTemplateSigner](docs/SubSignatureRequestEmbeddedTemplateSigner.md)
 - [SubSignatureRequestSigner](docs/SubSignatureRequestSigner.md)
 - [SubSignatureRequestTemplateSigner](docs/SubSignatureRequestTemplateSigner.md)
 - [SubSigningOptions](docs/SubSigningOptions.md)
 - [SubTemplateRole](docs/SubTemplateRole.md)
 - [SubUnclaimedDraftEmbeddedSigner](docs/SubUnclaimedDraftEmbeddedSigner.md)
 - [SubUnclaimedDraftEmbeddedTemplateSigner](docs/SubUnclaimedDraftEmbeddedTemplateSigner.md)
 - [SubUnclaimedDraftSigner](docs/SubUnclaimedDraftSigner.md)
 - [SubWhiteLabelingOptions](docs/SubWhiteLabelingOptions.md)
 - [TeamAddMemberRequest](docs/TeamAddMemberRequest.md)
 - [TeamCreateRequest](docs/TeamCreateRequest.md)
 - [TeamGetResponse](docs/TeamGetResponse.md)
 - [TeamRemoveMemberRequest](docs/TeamRemoveMemberRequest.md)
 - [TeamResponse](docs/TeamResponse.md)
 - [TeamUpdateRequest](docs/TeamUpdateRequest.md)
 - [TemplateAddUserRequest](docs/TemplateAddUserRequest.md)
 - [TemplateCreateEmbeddedDraftRequest](docs/TemplateCreateEmbeddedDraftRequest.md)
 - [TemplateCreateEmbeddedDraftResponse](docs/TemplateCreateEmbeddedDraftResponse.md)
 - [TemplateCreateEmbeddedDraftResponseTemplate](docs/TemplateCreateEmbeddedDraftResponseTemplate.md)
 - [TemplateEditResponse](docs/TemplateEditResponse.md)
 - [TemplateGetResponse](docs/TemplateGetResponse.md)
 - [TemplateListResponse](docs/TemplateListResponse.md)
 - [TemplateRemoveUserRequest](docs/TemplateRemoveUserRequest.md)
 - [TemplateResponse](docs/TemplateResponse.md)
 - [TemplateResponseAccount](docs/TemplateResponseAccount.md)
 - [TemplateResponseAccountQuota](docs/TemplateResponseAccountQuota.md)
 - [TemplateResponseCCRole](docs/TemplateResponseCCRole.md)
 - [TemplateResponseCustomField](docs/TemplateResponseCustomField.md)
 - [TemplateResponseDocument](docs/TemplateResponseDocument.md)
 - [TemplateResponseDocumentCustomField](docs/TemplateResponseDocumentCustomField.md)
 - [TemplateResponseDocumentCustomFieldAvgTextLength](docs/TemplateResponseDocumentCustomFieldAvgTextLength.md)
 - [TemplateResponseDocumentFieldGroup](docs/TemplateResponseDocumentFieldGroup.md)
 - [TemplateResponseDocumentFormField](docs/TemplateResponseDocumentFormField.md)
 - [TemplateResponseSignerRole](docs/TemplateResponseSignerRole.md)
 - [TemplateUpdateFilesRequest](docs/TemplateUpdateFilesRequest.md)
 - [TemplateUpdateFilesResponse](docs/TemplateUpdateFilesResponse.md)
 - [TemplateUpdateFilesResponseTemplate](docs/TemplateUpdateFilesResponseTemplate.md)
 - [UnclaimedDraftCreateEmbeddedRequest](docs/UnclaimedDraftCreateEmbeddedRequest.md)
 - [UnclaimedDraftCreateEmbeddedWithTemplateRequest](docs/UnclaimedDraftCreateEmbeddedWithTemplateRequest.md)
 - [UnclaimedDraftCreateRequest](docs/UnclaimedDraftCreateRequest.md)
 - [UnclaimedDraftCreateResponse](docs/UnclaimedDraftCreateResponse.md)
 - [UnclaimedDraftEditAndResendRequest](docs/UnclaimedDraftEditAndResendRequest.md)
 - [UnclaimedDraftResponse](docs/UnclaimedDraftResponse.md)
 - [WarningResponse](docs/WarningResponse.md)


## Documentation For Authorization


## api_key

- **Type**: HTTP basic authentication


## oauth2

- **Type**: Bearer authentication (JWT)


## Author

apisupport@hellosign.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in hellosign_sdk.apis and hellosign_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:

- `from hellosign_sdk.api.default_api import DefaultApi`
- `from hellosign_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:

```python
import sys
sys.setrecursionlimit(1500)
import hellosign_sdk
from hellosign_sdk.apis import *
from hellosign_sdk.models import *
```

## About this package

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

