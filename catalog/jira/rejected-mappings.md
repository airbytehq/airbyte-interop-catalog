# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `issue_custom_field_options` to Fivetran `field_option`


- Table Match Confidence Score: ⚠️ _0.65_
- Table Completion Score: 🟢 _0.67_
- Summary Self-Evaluation: _The table has a moderate match score due to partial mapping completion and a mix of precise and absent field matches._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of the custom field. | `issue_custom_field_options.id` | 🟢 _1.00_ | *Direct mapping to source field 'issue_custom_field_options.id'.* |
| `parent_id` | The ID of the parent custom field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | Name of the field option. | `issue_custom_field_options.name` | 🟢 _1.00_ | *Direct mapping to source field 'issue_custom_field_options.name'.* |

### Mapping: Airbyte `issue_fields` to Fivetran `field`


- Table Match Confidence Score: ⚠️ _0.65_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table match score reflects a moderate level of confidence that the source and target tables are describing the same subject matter, with most fields properly mapped but some missing critical mappings. The completion score indicates a reasonable but not full coverage of field mappings between source and target schemas._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the field. Default fields will have descriptive IDs, whereas custom field IDs will be `'customfield_#####'`.  | `issue_fields.id` | 🟢 _0.95_ | *The field 'id' maps directly and specifically to an identical field in the target schema, ensuring a high confidence score.* |
| `is_array` | Boolean that is true if a field can have multiple values (is mulitselect). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_custom` | Boolean that is true if the field is custom to this organization, and false if  it is default to Jira.  | `issue_fields.custom` | 🟢 _0.70_ | *Although 'is_custom' maps to 'issue_fields.custom', the semantic alignment is not perfect, reflecting a good but cautious confidence score.* |
| `name` | Name of the field as it appears on issue cards. | `issue_fields.name` | 🟢 _0.85_ | *The field 'name' directly correlates with 'issue_fields.name', aligning well semantically and structurally.* |
