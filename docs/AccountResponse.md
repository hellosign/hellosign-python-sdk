# AccountResponse



## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `account_id` | ```str``` |  The ID of the Account  |  |
| `email_address` | ```str``` |  The email address associated with the Account.  |  |
| `is_locked` | ```bool``` |  Returns `true` if the user has been locked out of their account by a team admin.  |  |
| `is_paid_hs` | ```bool``` |  Returns `true` if the user has a paid Dropbox Sign account.  |  |
| `is_paid_hf` | ```bool``` |  Returns `true` if the user has a paid HelloFax account.  |  |
| `quotas` | [```AccountResponseQuotas```](AccountResponseQuotas.md) |    |  |
| `callback_url` | ```str, none_type``` |  The URL that Dropbox Sign events will `POST` to.  |  |
| `role_code` | ```str, none_type``` |  The membership role for the team.  |  |
| `team_id` | ```str, none_type``` |  The id of the team account belongs to.  |  |
| `locale` | ```str, none_type``` |  The locale used in this Account. Check out the list of [supported locales](/api/reference/constants/#supported-locales) to learn more about the possible values.  |  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


