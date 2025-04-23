# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `metrics` to Fivetran `metric`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.86_
- Summary Self-Evaluation: _The table match score indicates a high confidence that the source and target tables describe the same domain. The completion score is decent but not perfect due to `MISSING` mappings for some fields, decreasing the overall confidence._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `created` | Timestamp of when the metric was created. | `metrics.attributes.created` | 🟢 _0.95_ | *Direct match found, high confidence.* |
| `id` | Unique ID of the metric being tracked. | `metrics.id` | 🟢 _0.95_ | *Direct match found, high confidence.* |
| `integration_id` | Foreign key referencing the INTEGRATION that the metric is being pulled from. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | Name of the metric (same as `EVENT.type`) | `metrics.attributes.name` | 🟢 _0.95_ | *Direct match found within the same domain, high confidence.* |
| `updated` | Timestamp of when the metric was last updated. | `metrics.updated` | 🟢 _0.95_ | *Direct match found, high confidence.* |
| `integration_category` | Use-case category of the integrated platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `integration_name` | Name of the integrated platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_deleted` | Boolean that is true if the campaign has been soft-deleted. | `metrics._airbyte_extracted_at` | 🟢 _0.90_ | *Mapped to `_airbyte_extracted_at` which is a recommended mapping, but different semantics.* |

### Mapping: Airbyte `events` to Fivetran `event`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: ❌ _0.35_
- Summary Self-Evaluation: _Partial matches for field mappings with a considerable amount of missing matches suggest a moderate table match but low completion. Fields that have direct mappings show a high confidence, while several missing mappings drastically lower the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_variation` | Unique ID of the attributed flow or campaign variation group.  This does not map onto another table.   | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `campaign_id` | Foreign key referencing the CAMPAIGN that the event is attributed to. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `datetime` | Timestamp of when the event was recorded in Klaviyo. Should be the same/nominally off from `timestamp`. | `events.datetime` | 🟢 _0.90_ | *Direct mapping with minor discrepancies in attribute names.* |
| `timestamp` | Timestamp of when the event was triggered. Should be the same/nominally off from `datetime`. | `events.attributes.timestamp` | 🟢 _0.90_ | *Direct mapping with minor discrepancies in attribute names.* |
| `flow_id` | Foreign key referencing the FLOW that the event is attributed to. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `flow_message_id` | Unique ID of the FLOW_MESSAGE that the event is attributed to.  This does not map onto another table.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | Unique ID of the event. | `events.id` | 🟢 _1.00_ | *Perfect mapping.* |
| `metric_id` | Foreign key referencing the metric being captured. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `person_id` | Foreign key referencing the PERSON who triggered the event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `type` | Type of event that was triggered. This is the same as the METRIC name. | `events.type` | 🟢 _1.00_ | *Perfect mapping.* |
| `uuid` | Universally Unique Identifier of the event. | `events.attributes.uuid` | 🟢 _1.00_ | *Perfect mapping.* |
| `property_value` | Numeric value associated with the event (ie the dollars associated with a purchase). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_deleted` | Boolean that is true if the campaign has been soft-deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `campaigns` to Fivetran `campaign`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _Several fields have direct mappings, but the presence of many 'MISSING' expression mappings and differences across similar but not identical fields impacts both the table match and completion scores._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | Boolean that is true if the campaign has been soft-deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `campaign_type` | Type of campaign. | `campaigns.type` | 🟢 _1.00_ | *Direct mapping available.* |
| `created` | Timestamp of when the campaign was created, in UTC. | `campaigns.attributes.created_at` | 🟢 _1.00_ | *Direct mapping available.* |
| `email_template_id` | Foreign key referencing the ID of the `email_template` object that will be the  content of this campaign. Note the Email Template is copied when creating this campaign,  so future changes to that Email Template will not alter the content of this campaign.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `from_email` | The email address your email will be sent from and will be used in the reply-to header. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `from_name` | The name or label associated with the email address you're sending from. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | Unique ID of the campaign. | `campaigns.id` | 🟢 _1.00_ | *Direct mapping available.* |
| `name` | A name for this campaign. If not specified, this will default to the subject of the campaign. | `campaigns.attributes.name` | 🟢 _1.00_ | *Direct mapping available.* |
| `send_time` | Timestamp of when the campaign is scheduled to be sent in the future, if  ["smart send time"](https://help.klaviyo.com/hc/en-us/articles/360029794371-Smart-Send-Time-in-Klaviyo#how-to-utilize-smart-send-time3) is used.   | `campaigns.attributes.send_time` | 🟢 _0.70_ | *Partial match, consider a similarity in usage but not a perfect one.* |
| `sent_at` | Timestamp of when the campaign was first sent out to users. | `campaigns.attributes.scheduled_at` | 🟢 _1.00_ | *Direct mapping available.* |
| `status` | Current status of the campaign. Either "draft", "scheduled", "sent", or "cancelled". | `campaigns.attributes.status` | 🟢 _0.70_ | *Partial match, consider a similarity in usage but not a perfect one.* |
| `status_id` | Corresponding ID to the current status. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status_label` | The label of the status as it appears in the UI (should be the same as `status`). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `subject` | The subject line of the campaign's email. | `campaigns.attributes.message` | 🟢 _1.00_ | *Direct mapping available.* |
| `updated` | Timestamp of when the campaign was last updated. | `campaigns.attributes.updated_at` | 🟢 _1.00_ | *Direct mapping available.* |
| `archived` | Boolean of whether the campaign has been archived or not | `campaigns.attributes.archived` | 🟢 _0.70_ | *Partial match, ambiguity in the nature of 'archived' status between implementations.* |
| `scheduled` | The datetime when the campaign was scheduled for future sending | `campaigns.attributes.scheduled_at` | 🟢 _1.00_ | *Direct mapping available.* |
