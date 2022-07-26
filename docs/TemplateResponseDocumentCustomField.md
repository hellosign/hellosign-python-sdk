# TemplateResponseDocumentCustomField



## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `name` | ```str``` |  The name of the Custom Field.  |  |
| `type` | ```str``` |  The type of this Custom Field. Only `text` and `checkbox` are currently supported.  |  |
| `signer` | ```str``` |  The signer of the Custom Field.  |  |
| `x` | ```int``` |  The horizontal offset in pixels for this form field.  |  |
| `y` | ```int``` |  The vertical offset in pixels for this form field.  |  |
| `width` | ```int``` |  The width in pixels of this form field.  |  |
| `height` | ```int``` |  The height in pixels of this form field.  |  |
| `required` | ```bool``` |  Boolean showing whether or not this field is required.  |  |
| `api_id` | ```str``` |  The unique ID for this field.  |  |
| `group` | ```str, none_type``` |  The name of the group this field is in. If this field is not a group, this defaults to `null`.  |  |
| `avg_text_length` | [```TemplateResponseFieldAvgTextLength```](TemplateResponseFieldAvgTextLength.md) |    |  |
| `is_multiline` | ```bool, none_type``` |  Whether this form field is multiline text.  |  |
| `original_font_size` | ```int, none_type``` |  Original font size used in this form field&#39;s text.  |  |
| `font_family` | ```str, none_type``` |  Font family used in this form field&#39;s text.  |  |
| `named_form_fields` | [```{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type```](.md) |  Deprecated. Use `form_fields` inside the [documents](https://developers.hellosign.com/api/reference/operation/templateGet/#!c&#x3D;200&amp;path&#x3D;template/documents&amp;t&#x3D;response) array instead.  |  |
| `reusable_form_id` | ```str, none_type``` |    |  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


