# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping: Airbyte `flows` to Fivetran `flow`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.88_
- Summary Self-Evaluation: _The given field mappings align quite well with the target schema allowing a lot of the data to be preserved. However, there is one field ('_fivetran_deleted') that could not be appropriately matched causing a slightly lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `created` | Timestamp of when the flow was first created. | `flows.attributes.created` | 🟢 _1.00_ | *Perfect match.* |
| `id` | Unique ID of the flow. | `flows.id` | 🟢 _1.00_ | *Perfect match.* |
| `name` | Name of the flow. | `flows.attributes.name` | 🟢 _1.00_ | *Perfect match.* |
| `status` | Current status of the flow. Either 'manual', 'live', or 'draft'. Read more [here](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-Started-with-Flows#the-flow-action-status9). | `flows.attributes.status` | 🟢 _1.00_ | *Perfect match.* |
| `updated` | Timestamp of when the flow was last updated. | `flows.attributes.updated` | 🟢 _1.00_ | *Perfect match.* |
| `archived` | Boolean of whether this record has been archived | `flows.attributes.archived` | 🟢 _1.00_ | *Perfect match.* |
| `trigger_type` | Corresponds to the object which triggered the flow. | `flows.attributes.trigger_type` | 🟢 _1.00_ | *Perfect match.* |
| `_fivetran_deleted` | Boolean that is true if the campaign has been soft-deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `profiles` to Fivetran `person`


- Table Match Confidence Score: 🟢 _0.95_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _High confidence in overall table and field mapping. All field names match closely to their source counterparts, with only one field (_fivetran_deleted) set to MISSING. Some fields could have different meanings but based on the provided context, assumptions have been made._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the user if you use your own unique identifier. Otherwise, Klaviyo  recommends using the email as the primary key.   | `profiles.id` | 🟢 _1.00_ | *Perfect match found for 'id'.* |
| `address_1` | First line of the person's address. | `profiles.attributes.location.address1` | 🟢 _1.00_ | *Perfect match found for 'address_1'.* |
| `address_2` | Second line of the person's address. | `profiles.attributes.location.address2` | 🟢 _1.00_ | *Perfect match found for 'address_2'.* |
| `city` | City they live in. | `profiles.attributes.location.city` | 🟢 _1.00_ | *Perfect match found for 'city'.* |
| `country` | Country they live in. | `profiles.attributes.location.country` | 🟢 _1.00_ | *Perfect match found for 'country'.* |
| `zip` | Postal code where they live. | `profiles.attributes.location.zip` | 🟢 _1.00_ | *Perfect match found for 'zip'.* |
| `created` | Timestamp of when the person's profile was created. | `profiles.attributes.created` | 🟢 _1.00_ | *Perfect match found for 'created'.* |
| `email` | The email address and the unique identifier for a profile. | `profiles.attributes.email` | 🟢 _1.00_ | *Perfect match found for 'email'.* |
| `first_name` | Person's first name. | `profiles.attributes.first_name` | 🟢 _1.00_ | *Perfect match found for 'first_name'.* |
| `last_name` | Person's surname. | `profiles.attributes.last_name` | 🟢 _1.00_ | *Perfect match found for 'last_name'.* |
| `latitude` | Latitude of the person's location. | `profiles.attributes.location.latitude` | 🟢 _1.00_ | *Perfect match found for 'latitude'.* |
| `longitude` | Longitude of the person's location. | `profiles.attributes.location.longitude` | 🟢 _1.00_ | *Perfect match found for 'longitude'.* |
| `organization` | Business organization they belong to. | `profiles.attributes.organization` | 🟢 _1.00_ | *Perfect match found for 'organization'.* |
| `phone_number` | Associated phone number. | `profiles.attributes.phone_number` | 🟢 _1.00_ | *Perfect match found for 'phone_number'.* |
| `region` | Region or state they live in. | `profiles.attributes.location.region` | 🟢 _0.70_ | *Good match found for 'region', but the term could have multiple contexts.* |
| `timezone` | Timezone they are situated in. | `profiles.attributes.location.timezone` | 🟢 _1.00_ | *Perfect match found for 'timezone'.* |
| `title` | Title at their business or organization. | `profiles.attributes.title` | 🟢 _1.00_ | *Perfect match found for 'title'.* |
| `updated` | Timestamp of when the person profile was last updated. | `profiles.attributes.updated` | 🟢 _1.00_ | *Perfect match found for 'updated'.* |
| `last_event_date` | Date and time of the most recent event the triggered an update to the profile, in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm) | `profiles.attributes.last_event_date` | 🟢 _1.00_ | *Perfect match found for 'last_event_date'.* |
| `_fivetran_deleted` | Boolean that is true if the campaign has been soft-deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
