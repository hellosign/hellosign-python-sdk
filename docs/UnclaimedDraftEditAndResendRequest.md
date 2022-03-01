# UnclaimedDraftEditAndResendRequest



## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `client_id`<sup>*_required_</sup> | ```str``` |  Client id of the app you&#39;re using to create this draft. Visit our [embedded page](https://app.hellosign.com/api/embeddedSigningWalkthrough) to learn more about this parameter.  |  |
| `editor_options` | [```SubEditorOptions```](SubEditorOptions.md) |    |  |
| `is_for_embedded_signing` | ```bool``` |  The request created from this draft will also be signable in embedded mode if set to `true`. Defaults to `false`.  |  [default to False] |
| `requester_email_address` | ```str``` |  The email address of the user that should be designated as the requester of this draft. If not set, original requester&#39;s email address will be used.  |  |
| `requesting_redirect_url` | ```str``` |  The URL you want signers redirected to after they successfully request a signature.  |  |
| `signing_redirect_url` | ```str``` |  The URL you want signers redirected to after they successfully sign.  |  |
| `test_mode` | ```bool``` |  Whether this is a test, the signature request created from this draft will not be legally binding if set to `true`. Defaults to `false`.  |  [default to False] |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


