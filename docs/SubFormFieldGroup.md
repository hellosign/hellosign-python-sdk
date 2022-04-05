# SubFormFieldGroup



## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `group_id`<sup>*_required_</sup> | ```str``` |  ID of group. Use this to reference a specific group from the `group` value in `form_fields_per_document`.  |  |
| `group_label`<sup>*_required_</sup> | ```str``` |  Name of the group  |  |
| `requirement`<sup>*_required_</sup> | ```str``` |  Examples: `require_0-1` `require_1` `require_1-ormore`<br><br>- Check out the list of [acceptable `requirement` checkbox type values](/api/reference/constants/#checkbox-field-grouping). - Check out the list of [acceptable `requirement` radio type fields](/api/reference/constants/#radio-field-grouping). - Radio groups require **at least** two fields per group.  |  |


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


