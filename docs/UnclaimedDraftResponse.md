# UnclaimedDraftResponse

A group of documents that a user can take ownership of via the claim URL.

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `signature_request_id` | ```str, none_type``` |  The ID of the signature request that is represented by this UnclaimedDraft.  |  |
| `claim_url` | ```str``` |  The URL to be used to claim this UnclaimedDraft.  |  |
| `signing_redirect_url` | ```str, none_type``` |  The URL you want signers redirected to after they successfully sign.  |  |
| `requesting_redirect_url` | ```str, none_type``` |  The URL you want signers redirected to after they successfully request a signature (Will only be returned in the response if it is applicable to the request.).  |  |
| `expires_at` | ```int, none_type``` |  When the link expires.  |  |
| `test_mode` | ```bool``` |  Whether this is a test draft. Signature requests made from test drafts have no legal value.  |  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


