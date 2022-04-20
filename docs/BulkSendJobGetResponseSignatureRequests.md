# BulkSendJobGetResponseSignatureRequests



## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `test_mode` | ```bool, none_type``` |  Whether this is a test signature request. Test requests have no legal value. Defaults to `false`.  |  [default to False] |
| `signature_request_id` | ```str``` |  The id of the SignatureRequest.  |  |
| `requester_email_address` | ```str``` |  The email address of the initiator of the SignatureRequest.  |  |
| `title` | ```str``` |  The title the specified Account uses for the SignatureRequest.  |  |
| `original_title` | ```str``` |  Default Label for account.  |  |
| `subject` | ```str``` |  The subject in the email that was initially sent to the signers.  |  |
| `message` | ```str, none_type``` |  The custom message in the email that was initially sent to the signers.  |  |
| `metadata` | [```{str: (bool, date, datetime, dict, float, int, list, str, none_type)}```](.md) |  The metadata attached to the signature request.  |  |
| `created_at` | ```int``` |  Time the signature request was created.  |  |
| `is_complete` | ```bool``` |  Whether or not the SignatureRequest has been fully executed by all signers.  |  |
| `is_declined` | ```bool``` |  Whether or not the SignatureRequest has been declined by a signer.  |  |
| `has_error` | ```bool``` |  Whether or not an error occurred (either during the creation of the SignatureRequest or during one of the signings).  |  |
| `final_copy_uri` | ```str``` |  (Deprecated) The relative URI where the PDF copy of the finalized documents can be downloaded. Only present when `is_complete &#x3D; true`. This will be removed at some point; use the files_url instead.  |  |
| `files_url` | ```str``` |  The URL where a copy of the request&#39;s documents can be downloaded.  |  |
| `signing_url` | ```str, none_type``` |  The URL where a signer, after authenticating, can sign the documents. This should only be used by users with existing HelloSign accounts as they will be required to log in before signing.  |  |
| `details_url` | ```str``` |  The URL where the requester and the signers can view the current status of the SignatureRequest.  |  |
| `cc_email_addresses` | ```[str]``` |  A list of email addresses that were CCed on the SignatureRequest. They will receive a copy of the final PDF once all the signers have signed.  |  |
| `signing_redirect_url` | ```str, none_type``` |  The URL you want the signer redirected to after they successfully sign.  |  |
| `template_ids` | ```[str], none_type``` |  Templates IDs used in this SignatureRequest (if any).  |  |
| `custom_fields` | [```[SignatureRequestResponseCustomField], none_type```](SignatureRequestResponseCustomField.md) |    |  |
| `attachments` | [```[SignatureRequestResponseAttachment], none_type```](SignatureRequestResponseAttachment.md) |    |  |
| `response_data` | [```[SignatureRequestResponseData], none_type```](SignatureRequestResponseData.md) |    |  |
| `signatures` | [```[SignatureRequestResponseSignatures]```](SignatureRequestResponseSignatures.md) |    |  |
| `bulk_send_job_id` | ```str``` |  The id of the BulkSendJob.  |  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


