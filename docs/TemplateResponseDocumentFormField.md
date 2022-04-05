# TemplateResponseDocumentFormField

An array of Form Field objects containing the name and type of each named textbox and checkmark field.

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `api_id` | ```str``` |  A unique id for the form field.  |  |
| `name` | ```str``` |  The name of the form field.  |  |
| `type` | ```str``` |  The type of this form field. See [field types](/api/reference/constants/#field-types).  |  |
| `x` | ```int``` |  The horizontal offset in pixels for this form field.  |  |
| `y` | ```int``` |  The vertical offset in pixels for this form field.  |  |
| `width` | ```int``` |  The width in pixels of this form field.  |  |
| `height` | ```int``` |  The height in pixels of this form field.  |  |
| `required` | ```bool``` |  Boolean showing whether or not this field is required.  |  |
| `group` | ```str, none_type``` |  The name of the group this field is in. If this field is not a group, this defaults to `null`.  |  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


