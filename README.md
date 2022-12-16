# hellosign-python-sdk

Dropbox Sign v3 API

## ⚠ This package is not yet ready for production use ⚠

We are working hard on getting this package ready, but it is not there, yet!

You should think twice before using package on anything critical.

The interfaces may change without warning. Backwards compatibility is not yet
guaranteed nor implied!

## Contributing

This repo is no longer accepting new issues or Pull Requests. All issues or
Pull Requests *must* be opened against the
[hellosign/hellosign-openapi](https://github.com/hellosign/hellosign-openapi) repo!

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
./run-build
```

*Attention*: Any changes you have made to the SDK code that you have not made
to the OAS file and/or the mustache template files _will be lost_ when you run
this command.

## Installation & Usage

### Requirements.

Python >=3.7

### pip

Install using `pip`:

```shell
python3 pipenv install hellosign-python-sdk==6.0.0-beta22.24
```

Alternatively:

```shell
pip install git+https://github.com/hellosign/hellosign-python-sdk.git@openapi
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
|```AccountApi``` | [```account_create```](docs/AccountApi.md#account_create) | ```POST /account/create``` | Create Account|
```AccountApi``` | [```account_get```](docs/AccountApi.md#account_get) | ```GET /account``` | Get Account|
```AccountApi``` | [```account_update```](docs/AccountApi.md#account_update) | ```PUT /account``` | Update Account|
```AccountApi``` | [```account_verify```](docs/AccountApi.md#account_verify) | ```POST /account/verify``` | Verify Account|
|```ApiAppApi``` | [```api_app_create```](docs/ApiAppApi.md#api_app_create) | ```POST /api_app``` | Create API App|
```ApiAppApi``` | [```api_app_delete```](docs/ApiAppApi.md#api_app_delete) | ```DELETE /api_app/{client_id}``` | Delete API App|
```ApiAppApi``` | [```api_app_get```](docs/ApiAppApi.md#api_app_get) | ```GET /api_app/{client_id}``` | Get API App|
```ApiAppApi``` | [```api_app_list```](docs/ApiAppApi.md#api_app_list) | ```GET /api_app/list``` | List API Apps|
```ApiAppApi``` | [```api_app_update```](docs/ApiAppApi.md#api_app_update) | ```PUT /api_app/{client_id}``` | Update API App|
|```BulkSendJobApi``` | [```bulk_send_job_get```](docs/BulkSendJobApi.md#bulk_send_job_get) | ```GET /bulk_send_job/{bulk_send_job_id}``` | Get Bulk Send Job|
```BulkSendJobApi``` | [```bulk_send_job_list```](docs/BulkSendJobApi.md#bulk_send_job_list) | ```GET /bulk_send_job/list``` | List Bulk Send Jobs|
|```EmbeddedApi``` | [```embedded_edit_url```](docs/EmbeddedApi.md#embedded_edit_url) | ```POST /embedded/edit_url/{template_id}``` | Get Embedded Template Edit URL|
```EmbeddedApi``` | [```embedded_sign_url```](docs/EmbeddedApi.md#embedded_sign_url) | ```GET /embedded/sign_url/{signature_id}``` | Get Embedded Sign URL|
|```OAuthApi``` | [```oauth_token_generate```](docs/OAuthApi.md#oauth_token_generate) | ```POST /oauth/token``` | OAuth Token Generate|
```OAuthApi``` | [```oauth_token_refresh```](docs/OAuthApi.md#oauth_token_refresh) | ```POST /oauth/token?refresh``` | OAuth Token Refresh|
|```ReportApi``` | [```report_create```](docs/ReportApi.md#report_create) | ```POST /report/create``` | Create Report|
|```SignatureRequestApi``` | [```signature_request_bulk_create_embedded_with_template```](docs/SignatureRequestApi.md#signature_request_bulk_create_embedded_with_template) | ```POST /signature_request/bulk_create_embedded_with_template``` | Embedded Bulk Send with Template|
```SignatureRequestApi``` | [```signature_request_bulk_send_with_template```](docs/SignatureRequestApi.md#signature_request_bulk_send_with_template) | ```POST /signature_request/bulk_send_with_template``` | Bulk Send with Template|
```SignatureRequestApi``` | [```signature_request_cancel```](docs/SignatureRequestApi.md#signature_request_cancel) | ```POST /signature_request/cancel/{signature_request_id}``` | Cancel Incomplete Signature Request|
```SignatureRequestApi``` | [```signature_request_create_embedded```](docs/SignatureRequestApi.md#signature_request_create_embedded) | ```POST /signature_request/create_embedded``` | Create Embedded Signature Request|
```SignatureRequestApi``` | [```signature_request_create_embedded_with_template```](docs/SignatureRequestApi.md#signature_request_create_embedded_with_template) | ```POST /signature_request/create_embedded_with_template``` | Create Embedded Signature Request with Template|
```SignatureRequestApi``` | [```signature_request_files```](docs/SignatureRequestApi.md#signature_request_files) | ```GET /signature_request/files/{signature_request_id}``` | Download Files|
```SignatureRequestApi``` | [```signature_request_files_as_data_uri```](docs/SignatureRequestApi.md#signature_request_files_as_data_uri) | ```GET /signature_request/files_as_data_uri/{signature_request_id}``` | Download Files as Data Uri|
```SignatureRequestApi``` | [```signature_request_files_as_file_url```](docs/SignatureRequestApi.md#signature_request_files_as_file_url) | ```GET /signature_request/files_as_file_url/{signature_request_id}``` | Download Files as File Url|
```SignatureRequestApi``` | [```signature_request_get```](docs/SignatureRequestApi.md#signature_request_get) | ```GET /signature_request/{signature_request_id}``` | Get Signature Request|
```SignatureRequestApi``` | [```signature_request_list```](docs/SignatureRequestApi.md#signature_request_list) | ```GET /signature_request/list``` | List Signature Requests|
```SignatureRequestApi``` | [```signature_request_release_hold```](docs/SignatureRequestApi.md#signature_request_release_hold) | ```POST /signature_request/release_hold/{signature_request_id}``` | Release On-Hold Signature Request|
```SignatureRequestApi``` | [```signature_request_remind```](docs/SignatureRequestApi.md#signature_request_remind) | ```POST /signature_request/remind/{signature_request_id}``` | Send Request Reminder|
```SignatureRequestApi``` | [```signature_request_remove```](docs/SignatureRequestApi.md#signature_request_remove) | ```POST /signature_request/remove/{signature_request_id}``` | Remove Signature Request Access|
```SignatureRequestApi``` | [```signature_request_send```](docs/SignatureRequestApi.md#signature_request_send) | ```POST /signature_request/send``` | Send Signature Request|
```SignatureRequestApi``` | [```signature_request_send_with_template```](docs/SignatureRequestApi.md#signature_request_send_with_template) | ```POST /signature_request/send_with_template``` | Send with Template|
```SignatureRequestApi``` | [```signature_request_update```](docs/SignatureRequestApi.md#signature_request_update) | ```POST /signature_request/update/{signature_request_id}``` | Update Signature Request|
|```TeamApi``` | [```team_add_member```](docs/TeamApi.md#team_add_member) | ```PUT /team/add_member``` | Add User to Team|
```TeamApi``` | [```team_create```](docs/TeamApi.md#team_create) | ```POST /team/create``` | Create Team|
```TeamApi``` | [```team_delete```](docs/TeamApi.md#team_delete) | ```DELETE /team/destroy``` | Delete Team|
```TeamApi``` | [```team_get```](docs/TeamApi.md#team_get) | ```GET /team``` | Get Team|
```TeamApi``` | [```team_info```](docs/TeamApi.md#team_info) | ```GET /team/info``` | Get Team Info|
```TeamApi``` | [```team_invites```](docs/TeamApi.md#team_invites) | ```GET /team/invites``` | List Team Invites|
```TeamApi``` | [```team_members```](docs/TeamApi.md#team_members) | ```GET /team/members/{team_id}``` | List Team Members|
```TeamApi``` | [```team_remove_member```](docs/TeamApi.md#team_remove_member) | ```POST /team/remove_member``` | Remove User from Team|
```TeamApi``` | [```team_sub_teams```](docs/TeamApi.md#team_sub_teams) | ```GET /team/sub_teams/{team_id}``` | List Sub Teams|
```TeamApi``` | [```team_update```](docs/TeamApi.md#team_update) | ```PUT /team``` | Update Team|
|```TemplateApi``` | [```template_add_user```](docs/TemplateApi.md#template_add_user) | ```POST /template/add_user/{template_id}``` | Add User to Template|
```TemplateApi``` | [```template_create_embedded_draft```](docs/TemplateApi.md#template_create_embedded_draft) | ```POST /template/create_embedded_draft``` | Create Embedded Template Draft|
```TemplateApi``` | [```template_delete```](docs/TemplateApi.md#template_delete) | ```POST /template/delete/{template_id}``` | Delete Template|
```TemplateApi``` | [```template_files```](docs/TemplateApi.md#template_files) | ```GET /template/files/{template_id}``` | Get Template Files|
```TemplateApi``` | [```template_files_as_data_uri```](docs/TemplateApi.md#template_files_as_data_uri) | ```GET /template/files_as_data_uri/{template_id}``` | Get Template Files as Data Uri|
```TemplateApi``` | [```template_files_as_file_url```](docs/TemplateApi.md#template_files_as_file_url) | ```GET /template/files_as_file_url/{template_id}``` | Get Template Files as File Url|
```TemplateApi``` | [```template_get```](docs/TemplateApi.md#template_get) | ```GET /template/{template_id}``` | Get Template|
```TemplateApi``` | [```template_list```](docs/TemplateApi.md#template_list) | ```GET /template/list``` | List Templates|
```TemplateApi``` | [```template_remove_user```](docs/TemplateApi.md#template_remove_user) | ```POST /template/remove_user/{template_id}``` | Remove User from Template|
```TemplateApi``` | [```template_update_files```](docs/TemplateApi.md#template_update_files) | ```POST /template/update_files/{template_id}``` | Update Template Files|
|```UnclaimedDraftApi``` | [```unclaimed_draft_create```](docs/UnclaimedDraftApi.md#unclaimed_draft_create) | ```POST /unclaimed_draft/create``` | Create Unclaimed Draft|
```UnclaimedDraftApi``` | [```unclaimed_draft_create_embedded```](docs/UnclaimedDraftApi.md#unclaimed_draft_create_embedded) | ```POST /unclaimed_draft/create_embedded``` | Create Embedded Unclaimed Draft|
```UnclaimedDraftApi``` | [```unclaimed_draft_create_embedded_with_template```](docs/UnclaimedDraftApi.md#unclaimed_draft_create_embedded_with_template) | ```POST /unclaimed_draft/create_embedded_with_template``` | Create Embedded Unclaimed Draft with Template|
```UnclaimedDraftApi``` | [```unclaimed_draft_edit_and_resend```](docs/UnclaimedDraftApi.md#unclaimed_draft_edit_and_resend) | ```POST /unclaimed_draft/edit_and_resend/{signature_request_id}``` | Edit and Resend Unclaimed Draft|


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
 - [ErrorResponseError](docs/ErrorResponseError.md)
 - [EventCallbackRequest](docs/EventCallbackRequest.md)
 - [EventCallbackRequestEvent](docs/EventCallbackRequestEvent.md)
 - [EventCallbackRequestEventMetadata](docs/EventCallbackRequestEventMetadata.md)
 - [FileResponse](docs/FileResponse.md)
 - [FileResponseDataUri](docs/FileResponseDataUri.md)
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
 - [SignatureRequestResponseAttachment](docs/SignatureRequestResponseAttachment.md)
 - [SignatureRequestResponseCustomFieldBase](docs/SignatureRequestResponseCustomFieldBase.md)
 - [SignatureRequestResponseCustomFieldCheckbox](docs/SignatureRequestResponseCustomFieldCheckbox.md)
 - [SignatureRequestResponseCustomFieldText](docs/SignatureRequestResponseCustomFieldText.md)
 - [SignatureRequestResponseCustomFieldTypeEnum](docs/SignatureRequestResponseCustomFieldTypeEnum.md)
 - [SignatureRequestResponseDataBase](docs/SignatureRequestResponseDataBase.md)
 - [SignatureRequestResponseDataTypeEnum](docs/SignatureRequestResponseDataTypeEnum.md)
 - [SignatureRequestResponseDataValueCheckbox](docs/SignatureRequestResponseDataValueCheckbox.md)
 - [SignatureRequestResponseDataValueCheckboxMerge](docs/SignatureRequestResponseDataValueCheckboxMerge.md)
 - [SignatureRequestResponseDataValueDateSigned](docs/SignatureRequestResponseDataValueDateSigned.md)
 - [SignatureRequestResponseDataValueDropdown](docs/SignatureRequestResponseDataValueDropdown.md)
 - [SignatureRequestResponseDataValueInitials](docs/SignatureRequestResponseDataValueInitials.md)
 - [SignatureRequestResponseDataValueRadio](docs/SignatureRequestResponseDataValueRadio.md)
 - [SignatureRequestResponseDataValueSignature](docs/SignatureRequestResponseDataValueSignature.md)
 - [SignatureRequestResponseDataValueText](docs/SignatureRequestResponseDataValueText.md)
 - [SignatureRequestResponseDataValueTextMerge](docs/SignatureRequestResponseDataValueTextMerge.md)
 - [SignatureRequestResponseSignatures](docs/SignatureRequestResponseSignatures.md)
 - [SignatureRequestSendRequest](docs/SignatureRequestSendRequest.md)
 - [SignatureRequestSendWithTemplateRequest](docs/SignatureRequestSendWithTemplateRequest.md)
 - [SignatureRequestUpdateRequest](docs/SignatureRequestUpdateRequest.md)
 - [SubAttachment](docs/SubAttachment.md)
 - [SubBulkSignerList](docs/SubBulkSignerList.md)
 - [SubBulkSignerListCustomField](docs/SubBulkSignerListCustomField.md)
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
 - [SubSignatureRequestSigner](docs/SubSignatureRequestSigner.md)
 - [SubSignatureRequestTemplateSigner](docs/SubSignatureRequestTemplateSigner.md)
 - [SubSigningOptions](docs/SubSigningOptions.md)
 - [SubTeamResponse](docs/SubTeamResponse.md)
 - [SubTemplateRole](docs/SubTemplateRole.md)
 - [SubUnclaimedDraftSigner](docs/SubUnclaimedDraftSigner.md)
 - [SubUnclaimedDraftTemplateSigner](docs/SubUnclaimedDraftTemplateSigner.md)
 - [SubWhiteLabelingOptions](docs/SubWhiteLabelingOptions.md)
 - [TeamAddMemberRequest](docs/TeamAddMemberRequest.md)
 - [TeamCreateRequest](docs/TeamCreateRequest.md)
 - [TeamGetInfoResponse](docs/TeamGetInfoResponse.md)
 - [TeamGetResponse](docs/TeamGetResponse.md)
 - [TeamInfoResponse](docs/TeamInfoResponse.md)
 - [TeamInviteResponse](docs/TeamInviteResponse.md)
 - [TeamInvitesResponse](docs/TeamInvitesResponse.md)
 - [TeamMemberResponse](docs/TeamMemberResponse.md)
 - [TeamMembersResponse](docs/TeamMembersResponse.md)
 - [TeamParentResponse](docs/TeamParentResponse.md)
 - [TeamRemoveMemberRequest](docs/TeamRemoveMemberRequest.md)
 - [TeamResponse](docs/TeamResponse.md)
 - [TeamSubTeamsResponse](docs/TeamSubTeamsResponse.md)
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
 - [TemplateResponseDocumentFieldGroup](docs/TemplateResponseDocumentFieldGroup.md)
 - [TemplateResponseDocumentFormField](docs/TemplateResponseDocumentFormField.md)
 - [TemplateResponseDocumentStaticField](docs/TemplateResponseDocumentStaticField.md)
 - [TemplateResponseFieldAvgTextLength](docs/TemplateResponseFieldAvgTextLength.md)
 - [TemplateResponseNamedFormField](docs/TemplateResponseNamedFormField.md)
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
- Package version: 6.0.0-beta22.24
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

