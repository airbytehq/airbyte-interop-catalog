# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping: Airbyte `flows` to Fivetran `flow`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.78_
- Summary Self-Evaluation: _Most field mappings have been accurately paired with high confidence scores. The table match score indicates a strong correlation between the source and target schemas, reflecting a well-aligned table mapping configuration. The completion score signifies a high but not full population of the field mappings, aligning well with the project criteria which is acceptable given the scenarios where some source fields might not be serialized as fully as the target._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `created` | Timestamp of when the flow was first created. | `flows.attributes.created` | 🟢 _0.90_ | *Strong match for the timestamp field indicating the creation time matching perfectly.* |
| `id` | Unique ID of the flow. | `flows.id` | 🟢 _0.95_ | *Perfect match with unique ID fields in both source and target.* |
| `name` | Name of the flow. | `flows.attributes.name` | 🟢 _0.88_ | *Field name matches directly, indicating a strong representation of the same attribute.* |
| `status` | Current status of the flow. Either 'manual', 'live', or 'draft'. Read more [here](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-Started-with-Flows#the-flow-action-status9). | `flows.attributes.status` | 🟢 _0.83_ | *Good match between status descriptions, slightly less confident due to textual variations in descriptions.* |
| `updated` | Timestamp of when the flow was last updated. | `flows.attributes.updated` | 🟢 _0.90_ | *Strong match for the timestamp field indicating the update time matching perfectly.* |
| `archived` | Boolean of whether this record has been archived | `flows.attributes.archived` | 🟢 _0.80_ | *Good match, boolean fields align well but minor uncertainties exist.* |
| `trigger_type` | Corresponds to the object which triggered the flow. | `flows.attributes.trigger_type` | 🟢 _0.85_ | *Strong correlation between trigger types hinted by descriptions.* |
| `_fivetran_deleted` | Boolean that is true if the campaign has been soft-deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `profiles` to Fivetran `person`


- Table Match Confidence Score: 🟢 _0.88_
- Table Completion Score: 🟢 _0.73_
- Summary Self-Evaluation: _The table mapping is likely representing the same subject matter, with most fields having strong and relevant matches. However, some fields had to be set to 'MISSING' due to lack of an apparent counterpart in the source, lowering the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the user if you use your own unique identifier. Otherwise, Klaviyo  recommends using the email as the primary key.   | `profiles.id` | 🟢 _1.00_ | *Direct and exact match found.* |
| `address_1` | First line of the person's address. | `profiles.attributes.location.address1` | 🟢 _0.95_ | *Direct match at nested level.* |
| `address_2` | Second line of the person's address. | `profiles.attributes.location.address2` | 🟢 _0.95_ | *Direct match at nested level.* |
| `city` | City they live in. | `profiles.attributes.location.city` | 🟢 _0.90_ | *Relevant match found at nested level.* |
| `country` | Country they live in. | `profiles.attributes.location.country` | 🟢 _0.90_ | *Relevant and direct match.* |
| `zip` | Postal code where they live. | `profiles.attributes.location.zip` | 🟢 _0.90_ | *Direct match for postal code identified.* |
| `created` | Timestamp of when the person's profile was created. | `profiles.attributes.created` | 🟢 _0.90_ | *Timestamp fields perfectly align.* |
| `email` | The email address and the unique identifier for a profile. | `profiles.attributes.email` | 🟢 _1.00_ | *Exact match with primary key relevance.* |
| `first_name` | Person's first name. | `profiles.attributes.first_name` | 🟢 _0.95_ | *Direct and exact match found.* |
| `last_name` | Person's surname. | `profiles.attributes.last_name` | 🟢 _0.95_ | *Direct and exact match found.* |
| `latitude` | Latitude of the person's location. | `profiles.attributes.location.latitude` | 🟢 _0.85_ | *Exact match for latitude.* |
| `longitude` | Longitude of the person's location. | `profiles.attributes.location.longitude` | 🟢 _0.85_ | *Exact match for longitude.* |
| `organization` | Business organization they belong to. | `profiles.attributes.organization` | 🟢 _0.90_ | *Directly matches business organization field.* |
| `phone_number` | Associated phone number. | `profiles.attributes.phone_number` | 🟢 _0.90_ | *Direct match found.* |
| `region` | Region or state they live in. | `profiles.attributes.location.region` | 🟢 _0.70_ | *Possible match considering regional data, but ambiguity remains.* |
| `timezone` | Timezone they are situated in. | `profiles.attributes.location.timezone` | 🟢 _0.70_ | *Relevant match found, although some variations may exist due to different timezone formats.* |
| `title` | Title at their business or organization. | `profiles.attributes.title` | 🟢 _0.90_ | *Direct match on job title.* |
| `updated` | Timestamp of when the person profile was last updated. | `profiles.attributes.updated` | 🟢 _0.90_ | *Timestamp fields align well.* |
| `last_event_date` | Date and time of the most recent event the triggered an update to the profile, in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm) | `profiles.attributes.last_event_date` | 🟢 _0.90_ | *Exact match for event timestamp.* |
| `_fivetran_deleted` | Boolean that is true if the campaign has been soft-deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
