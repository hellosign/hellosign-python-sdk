# SignatureRequestResponseCustomFieldBase

An array of Custom Field objects containing the name and type of each custom field.

* Text Field uses `SignatureRequestResponseCustomFieldText`
* Checkbox Field uses `SignatureRequestResponseCustomFieldCheckbox`

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `type`<sup>*_required_</sup> | ```str``` |  The type of this Custom Field. Only &#39;text&#39; and &#39;checkbox&#39; are currently supported.  |  |
| `name`<sup>*_required_</sup> | ```str``` |  The name of the Custom Field.  |  |
| `required` | ```bool``` |  A boolean value denoting if this field is required.  |  |
| `api_id` | ```str``` |  The unique ID for this field.  |  |
| `editor` | ```str``` |  The name of the Role that is able to edit this field.  |  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


