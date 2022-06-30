# ApiAppResponse

Contains information about an API App.

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `callback_url` | ```str, none_type``` |  The app&#39;s callback URL (for events)  |  |
| `client_id` | ```str``` |  The app&#39;s client id  |  |
| `created_at` | ```int``` |  The time that the app was created  |  |
| `domains` | ```[str]``` |  The domain name(s) associated with the app  |  |
| `name` | ```str``` |  The name of the app  |  |
| `is_approved` | ```bool``` |  Boolean to indicate if the app has been approved  |  |
| `oauth` | [```ApiAppResponseOAuth```](ApiAppResponseOAuth.md) |    |  |
| `options` | [```ApiAppResponseOptions```](ApiAppResponseOptions.md) |    |  |
| `owner_account` | [```ApiAppResponseOwnerAccount```](ApiAppResponseOwnerAccount.md) |    |  |
| `white_labeling_options` | [```ApiAppResponseWhiteLabelingOptions```](ApiAppResponseWhiteLabelingOptions.md) |    |  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


