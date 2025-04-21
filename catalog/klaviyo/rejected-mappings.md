# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `metrics` to Fivetran `metric`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: ❌ _0.38_
- Summary Self-Evaluation: _Table mapping has moderate confidence but most field mappings are missing._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `created` | Timestamp of when the metric was created. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | Unique ID of the metric being tracked. | `metrics.id` | 🟢 _1.00_ | *Perfect match with 'metrics.id'* |
| `integration_id` | Foreign key referencing the INTEGRATION that the metric is being pulled from. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | Name of the metric (same as `EVENT.type`) | `metrics.attributes.name` | 🟢 _1.00_ | *Perfect match with 'metrics.attributes.name'* |
| `updated` | Timestamp of when the metric was last updated. | `metrics.updated` | 🟢 _1.00_ | *Perfect match with 'metrics.updated'* |
| `integration_category` | Use-case category of the integrated platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `integration_name` | Name of the integrated platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_deleted` | Boolean that is true if the campaign has been soft-deleted. | `metrics._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match with 'metrics._airbyte_extracted_at'* |

### Mapping: Airbyte `events` to Fivetran `event`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mapping has a high level of confidence as majority of fields are well aligned. However, some fields could not be mapped and are marked as missing which reduces the overall completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_variation` | Unique ID of the attributed flow or campaign variation group.  This does not map onto another table.   | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `campaign_id` | Foreign key referencing the CAMPAIGN that the event is attributed to. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `datetime` | Timestamp of when the event was recorded in Klaviyo. Should be the same/nominally off from `timestamp`. | `events.attributes.datetime` | 🟢 _1.00_ | *Column 'datetime' maps directly to 'events.attributes.datetime'.* |
| `timestamp` | Timestamp of when the event was triggered. Should be the same/nominally off from `datetime`. | `events.attributes.timestamp` | 🟢 _1.00_ | *Column 'timestamp' maps directly to 'events.attributes.timestamp'.* |
| `flow_id` | Foreign key referencing the FLOW that the event is attributed to. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `flow_message_id` | Unique ID of the FLOW_MESSAGE that the event is attributed to.  This does not map onto another table.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | Unique ID of the event. | `events.id` | 🟢 _1.00_ | *Column 'id' maps directly to 'events.id'.* |
| `metric_id` | Foreign key referencing the metric being captured. | `events.relationships.metric.data.id` | 🟢 _1.00_ | *Column 'metric_id' maps directly to 'events.relationships.metric.data.id'.* |
| `person_id` | Foreign key referencing the PERSON who triggered the event. | `events.relationships.profile.data.id` | 🟢 _1.00_ | *Column 'person_id' maps directly to 'events.relationships.profile.data.id'.* |
| `type` | Type of event that was triggered. This is the same as the METRIC name. | `events.type` | 🟢 _1.00_ | *Column 'type' maps directly to 'events.type'.* |
| `uuid` | Universally Unique Identifier of the event. | `events.attributes.uuid` | 🟢 _1.00_ | *Column 'uuid' maps directly to 'events.attributes.uuid'.* |
| `property_value` | Numeric value associated with the event (ie the dollars associated with a purchase). | `events.attributes.event_properties` | 🟢 _1.00_ | *Column 'property_value' maps directly to 'events.attributes.event_properties'.* |
| `_fivetran_deleted` | Boolean that is true if the campaign has been soft-deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `campaigns` to Fivetran `campaign`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: 🟢 _0.78_
- Summary Self-Evaluation: _The table matches perfectly with a score of 1.00. Completion score is based on the ratio of correctly mapped fields to the total fields in the table. There are 7 fields which stood unmatched with 'Missing' expression resulting in the score of 0.78._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | Boolean that is true if the campaign has been soft-deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `campaign_type` | Type of campaign. | `campaigns.type` | 🟢 _1.00_ | *Campaign type is perfectly mapped from 'campaigns.type' with the score of 1.00* |
| `created` | Timestamp of when the campaign was created, in UTC. | `campaigns.attributes.created_at` | 🟢 _1.00_ | *Created is perfectly mapped from 'campaigns.attributes.created_at' with the score of 1.00* |
| `email_template_id` | Foreign key referencing the ID of the `email_template` object that will be the  content of this campaign. Note the Email Template is copied when creating this campaign,  so future changes to that Email Template will not alter the content of this campaign.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `from_email` | The email address your email will be sent from and will be used in the reply-to header. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `from_name` | The name or label associated with the email address you're sending from. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | Unique ID of the campaign. | `campaigns.id` | 🟢 _1.00_ | *Id is perfectly mapped from 'campaigns.id' with the score of 1.00* |
| `name` | A name for this campaign. If not specified, this will default to the subject of the campaign. | `campaigns.attributes.name` | 🟢 _1.00_ | *Name is perfectly mapped from 'campaigns.attributes.name' with the score of 1.00* |
| `send_time` | Timestamp of when the campaign is scheduled to be sent in the future, if  ["smart send time"](https://help.klaviyo.com/hc/en-us/articles/360029794371-Smart-Send-Time-in-Klaviyo#how-to-utilize-smart-send-time3) is used.   | `campaigns.attributes.send_time` | 🟢 _1.00_ | *Send time is perfectly mapped from 'campaigns.attributes.send_time' with the score of 1.00* |
| `sent_at` | Timestamp of when the campaign was first sent out to users. | `campaigns.attributes.scheduled_at` | 🟢 _1.00_ | *Sent at is perfectly mapped from 'campaigns.attributes.scheduled_at' with the score of 1.00* |
| `status` | Current status of the campaign. Either "draft", "scheduled", "sent", or "cancelled". | `campaigns.attributes.status` | 🟢 _1.00_ | *Status is perfectly mapped from 'campaigns.attributes.status' with the score of 1.00* |
| `status_id` | Corresponding ID to the current status. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status_label` | The label of the status as it appears in the UI (should be the same as `status`). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `subject` | The subject line of the campaign's email. | `campaigns.attributes.message` | 🟢 _1.00_ | *Subject is perfectly mapped from 'campaigns.attributes.message' with the score of 1.00* |
| `updated` | Timestamp of when the campaign was last updated. | `campaigns.attributes.updated_at` | 🟢 _1.00_ | *Updated is perfectly mapped from 'campaigns.attributes.updated_at' with the score of 1.00* |
| `archived` | Boolean of whether the campaign has been archived or not | `campaigns.attributes.archived` | 🟢 _1.00_ | *Archived is perfectly mapped from 'campaigns.attributes.archived' with the score of 1.00* |
| `scheduled` | The datetime when the campaign was scheduled for future sending | `campaigns.attributes.scheduled_at` | 🟢 _1.00_ | *Scheduled is perfectly mapped from 'campaigns.attributes.scheduled_at' with the score of 1.00* |
