# UnclaimedDraftEditAndResendRequest



## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `client_id`<sup>*_required_</sup> | ```str``` |  Client id of the app used to create the draft. Used to apply the branding and callback url defined for the app.  |  |
| `editor_options` | [```SubEditorOptions```](SubEditorOptions.md) |    |  |
| `is_for_embedded_signing` | ```bool``` |  The request created from this draft will also be signable in embedded mode if set to `true`.  |  |
| `requester_email_address` | ```str``` |  The email address of the user that should be designated as the requester of this draft. If not set, original requester&#39;s email address will be used.  |  |
| `requesting_redirect_url` | ```str``` |  The URL you want signers redirected to after they successfully request a signature.  |  |
| `show_progress_stepper` | ```bool``` |  When only one step remains in the signature request process and this parameter is set to `false` then the progress stepper will be hidden.  |  [default to True] |
| `signing_redirect_url` | ```str``` |  The URL you want signers redirected to after they successfully sign.  |  |
| `test_mode` | ```bool``` |  Whether this is a test, the signature request created from this draft will not be legally binding if set to `true`. Defaults to `false`.  |  [default to False] |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


