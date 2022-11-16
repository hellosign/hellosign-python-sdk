# SignatureRequestUpdateRequest



## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `signature_id`<sup>*_required_</sup> | ```str``` |  The signature ID for the recipient.  |  |
| `email_address` | ```str``` |  The new email address for the recipient.<br><br>**NOTE**: Optional if `name` is provided.  |  |
| `name` | ```str``` |  The new name for the recipient.<br><br>**NOTE**: Optional if `email_address` is provided.  |  |
| `expires_at` | ```int, none_type``` |  The new time when the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable.  |  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


