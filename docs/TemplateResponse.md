# TemplateResponse



## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `template_id` | ```str``` |  The id of the Template.  |  |
| `title` | ```str``` |  The title of the Template. This will also be the default subject of the message sent to signers when using this Template to send a SignatureRequest. This can be overridden when sending the SignatureRequest.  |  |
| `message` | ```str``` |  The default message that will be sent to signers when using this Template to send a SignatureRequest. This can be overridden when sending the SignatureRequest.  |  |
| `updated_at` | ```int``` |  Time the template was last updated.  |  |
| `is_embedded` | ```bool, none_type``` |  `true` if this template was created using an embedded flow, `false` if it was created on our website.  |  |
| `is_creator` | ```bool, none_type``` |  `true` if you are the owner of this template, `false` if it&#39;s been shared with you by a team member.  |  |
| `can_edit` | ```bool, none_type``` |  Indicates whether edit rights have been granted to you by the owner (always `true` if that&#39;s you).  |  |
| `is_locked` | ```bool, none_type``` |  `true` if you exceed Template quota; these can only be used in test mode. `false` if the template is included with the Template quota; these can be used at any time.  |  |
| `metadata` | [```{str: (bool, date, datetime, dict, float, int, list, str, none_type)}```](.md) |  The metadata attached to the template.  |  |
| `signer_roles` | [```[TemplateResponseSignerRole]```](TemplateResponseSignerRole.md) |    |  |
| `cc_roles` | [```[TemplateResponseCCRole]```](TemplateResponseCCRole.md) |    |  |
| `documents` | [```[TemplateResponseDocument]```](TemplateResponseDocument.md) |    |  |
| `custom_fields` | [```[TemplateResponseCustomField], none_type```](TemplateResponseCustomField.md) |    |  |
| `accounts` | [```[TemplateResponseAccount], none_type```](TemplateResponseAccount.md) |    |  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


