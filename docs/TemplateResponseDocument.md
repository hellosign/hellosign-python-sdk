# TemplateResponseDocument



## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `name` | ```str``` |  Name of the associated file.  |  |
| `index` | ```int``` |  Document ordering, the lowest index is displayed first and the highest last (0-based indexing).  |  |
| `field_groups` | [```[TemplateResponseDocumentFieldGroup]```](TemplateResponseDocumentFieldGroup.md) |  An array of Form Field Group objects.  |  |
| `form_fields` | [```[TemplateResponseDocumentFormField]```](TemplateResponseDocumentFormField.md) |  An array of Form Field objects containing the name and type of each named textbox and checkmark field.  |  |
| `custom_fields` | [```[TemplateResponseDocumentCustomField]```](TemplateResponseDocumentCustomField.md) |  An array of Document Custom Field objects.  |  |
| `static_fields` | [```[TemplateResponseDocumentStaticField], none_type```](TemplateResponseDocumentStaticField.md) |  An array describing static overlay fields. &lt;b&gt;Note&lt;/b&gt; only available for certain subscriptions.  |  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


