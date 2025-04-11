# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping: Airbyte `campaigns` to Fivetran `campaign`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table match score suggests that the source and target tables describe the same subject matter with reasonable confidence. However, not all fields could be confidently mapped, resulting in a lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | Boolean that is true if the campaign has been soft-deleted. | `campaigns.attributes.archived` | 🟢 _0.70_ | *The expression 'campaigns.attributes.archived' seems to indicate whether a campaign is deleted, similar to '_fivetran_deleted'.* |
| `campaign_type` | Type of campaign. | `campaigns.attributes.channel` | 🟢 _0.70_ | *The expression 'campaigns.attributes.channel' likely maps well to 'campaign_type', denoting the type of campaign.* |
| `created` | Timestamp of when the campaign was created, in UTC. | `campaigns.attributes.created_at` | 🟢 _0.70_ | *The expression 'campaigns.attributes.created_at' appears to indicate the creation timestamp, mapping well to 'created'.* |
| `email_template_id` | Foreign key referencing the ID of the email_template object that will be the content of this campaign. | `campaigns.attributes.template_id` | 🟢 _0.70_ | *Given it's a foreign key, 'campaigns.attributes.template_id' likely maps to 'email_template_id'.* |
| `from_email` | The email address your email will be sent from and will be used in the reply-to header. | `campaigns.attributes.from_email` | 🟢 _0.70_ | *The email expressions map well together, as 'campaigns.attributes.from_email' indicates the sender email.* |
| `from_name` | The name or label associated with the email address you're sending from. | `campaigns.attributes.from_name` | 🟢 _0.70_ | *The expression 'campaigns.attributes.from_name' maps well to identify the sender name.* |
| `id` | Unique ID of the campaign. | `campaigns.id` | 🟢 _1.00_ | *Exact match as 'campaigns.id' clearly maps to 'id'.* |
| `name` | A name for this campaign. If not specified, this will default to the subject of the campaign. | `campaigns.attributes.name` | 🟢 _0.70_ | *'campaigns.attributes.name' captures the essence of 'name' for a campaign.* |
| `send_time` | Timestamp of when the campaign is scheduled to be sent in the future. | `campaigns.attributes.send_time` | 🟢 _0.70_ | *The mapping to 'campaigns.attributes.send_time' indicates scheduling information.* |
| `sent_at` | Timestamp of when the campaign was first sent out to users. | `campaigns.attributes.sent_at` | 🟢 _0.70_ | *The expression 'campaigns.attributes.sent_at' indicates the time sent, mapping well to 'sent_at'.* |
| `status` | Current status of the campaign. Either "draft", "scheduled", "sent", or "cancelled". | `campaigns.attributes.status` | 🟢 _0.70_ | *'campaigns.attributes.status' for campaign state aligns well with 'status'.* |
| `_fivetran_synced` | Timestamp when this record was last synced. | `campaigns._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at' with full confidence.* |

### Mapping: Airbyte `metrics` to Fivetran `metric`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The table mapping is highly confident, as most fields align well between the source and target schemas. The completion score is high because almost all fields are matched, including the special handling of '_fivetran_synced'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the metric. | `metrics.id` | 🟢 _1.00_ | *Perfect match for the unique identifier of the metric.* |
| `name` | Name of the metric. | `metrics.attributes.name` | 🟢 _1.00_ | *Name of the metric matches perfectly between source and target.* |
| `created` | Timestamp when the metric was created. | `metrics.attributes.created` | 🟢 _1.00_ | *Timestamp for creation matches perfectly.* |
| `updated` | Timestamp when the metric was last updated. | `metrics.attributes.updated` | 🟢 _1.00_ | *Timestamp for update matches perfectly.* |
| `integration` | Integration associated with this metric. | `metrics.attributes.integration` | 🟢 _1.00_ | *The associated integration is correctly mapped.* |
| `_fivetran_synced` | Timestamp when this record was last synced. | `metrics._airbyte_extracted_at` | 🟢 _1.00_ | *Mapped '_fivetran_synced' to '_airbyte_extracted_at' as required by standard mapping.* |

### Mapping: Airbyte `events` to Fivetran `event`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _Field mappings are evaluated with high confidence. Most of the fields have clear matches, and the mapping for '_fivetran_synced' to '_airbyte_extracted_at' is a standard 1.00 score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the event. | `events.id` | 🟢 _0.95_ | *The field 'id' maps directly to 'events.id' with strong confidence.* |
| `type` | Type of event that was triggered. This is the same as the METRIC name. | `events.relationships.metric.data.id` | 🟢 _0.70_ | *The field 'type' maps to 'events.relationships.metric.data.id' which is related to METRIC name. The mapping is somewhat confident but requires contextual understanding.* |
| `timestamp` | Timestamp when the event was triggered. | `events.attributes.datetime` | 🟢 _0.85_ | *The field 'timestamp' maps to 'events.attributes.datetime' indicating a high confidence match.* |
| `datetime` | Timestamp when the event was recorded in Klaviyo. | `events.attributes.datetime` | 🟢 _0.85_ | *The field 'datetime' also maps to 'events.attributes.datetime'. These timestamps appear to reflect different event timings but have similar sources.* |
| `event_properties` | JSON object containing properties of the event. | `events.attributes.event_properties` | 🟢 _0.80_ | *The field 'event_properties' appropriately maps to 'events.attributes.event_properties' with good confidence.* |
| `person_id` | Foreign key referencing the PERSON who triggered the event. | `events.relationships.profile.data.id` | 🟢 _0.80_ | *The 'person_id' maps to 'events.relationships.profile.data.id', indicating a foreign key relationship and holding strong confidence in context.* |
| `_fivetran_synced` | Timestamp when this record was last synced. | `events._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at'.* |

### Mapping: Airbyte `profiles` to Fivetran `person`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The table mappings are highly confident due to the strong contextual alignment between fields, except for a few low-confidence mappings or missing mappings where no suitable match was found._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the person. | `profiles.id` | 🟢 _1.00_ | *Perfect match with profiles.id.* |
| `email` | The email address and the unique identifier for a profile. | `profiles.attributes.email` | 🟢 _1.00_ | *Perfect match with profiles.attributes.email.* |
| `first_name` | Person's first name. | `profiles.attributes.first_name` | 🟢 _1.00_ | *Perfect match with profiles.attributes.first_name.* |
| `last_name` | Person's surname. | `profiles.attributes.last_name` | 🟢 _1.00_ | *Perfect match with profiles.attributes.last_name.* |
| `address_1` | First line of the person's address. | `profiles.attributes.location.address1` | 🟢 _0.75_ | *Good match with profiles.attributes.location.address1.* |
| `address_2` | Second line of the person's address. | `profiles.attributes.location.address2` | 🟢 _0.75_ | *Good match with profiles.attributes.location.address2.* |
| `city` | City they live in. | `profiles.attributes.location.city` | 🟢 _0.75_ | *Good match with profiles.attributes.location.city.* |
| `country` | Country they live in. | `profiles.attributes.location.country` | 🟢 _0.75_ | *Good match with profiles.attributes.location.country.* |
| `zip` | Postal code where they live. | `profiles.attributes.location.zip` | ⚠️ _0.60_ | *Matches profiles.attributes.location.zip but with some uncertainty on its usage.* |
| `created` | Timestamp of when the person's profile was created. | `profiles.attributes.created` | 🟢 _1.00_ | *Perfect match with profiles.attributes.created.* |
| `phone_number` | Associated phone number. | `profiles.attributes.phone_number` | 🟢 _0.70_ | *Match with profiles.attributes.phone_number with some uncertainty.* |
| `region` | Region or state they live in. | `profiles.attributes.location.region` | ⚠️ _0.50_ | *Potential match with a similar regional field, but context is unclear.* |
| `timezone` | Timezone they are situated in. | `profiles.attributes.location.timezone` | 🟢 _0.70_ | *Matches profiles.attributes.location.timezone with minor discrepancies.* |
| `organization` | Business organization they belong to. | `profiles.attributes.organization` | 🟢 _0.80_ | *Likely match with profiles.attributes.organization.* |
| `title` | Title at their business or organization. | `profiles.attributes.title` | 🟢 _0.80_ | *Likely match with profiles.attributes.title.* |
| `updated` | Timestamp of when the person profile was last updated. | `profiles.attributes.updated` | 🟢 _1.00_ | *Perfect match with profiles.attributes.updated.* |
| `_fivetran_synced` | Timestamp when this record was last synced. | `profiles._airbyte_extracted_at` | 🟢 _1.00_ | *Direct match to profiles._airbyte_extracted_at as a standard practice.* |

### Mapping: Airbyte `flows` to Fivetran `flow`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _The table matching score reflects a strong correlation between the source and target schemas, as they both derive from a similar API. The completion score is perfect as all required field mappings are present, with the standard sync field mapping receiving a high confidence score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the flow. | `flows.id` | 🟢 _0.95_ | *Mapping is straightforward as 'id' aligns well with the typical unique identifier.* |
| `name` | Name of the flow. | `flows.attributes.name` | 🟢 _0.95_ | *The 'name' mapping aligns well, representing the flow's name accurately.* |
| `created` | Timestamp when the flow was created. | `flows.attributes.created` | 🟢 _0.90_ | *The 'created' mapping accurately captures the timestamp for when the flow was created.* |
| `updated` | Timestamp when the flow was last updated. | `flows.attributes.updated` | 🟢 _0.90_ | *The 'updated' mapping accurately reflects the last updated timestamp for the flow.* |
| `status` | Current status of the flow. | `flows.attributes.status` | 🟢 _0.80_ | *The 'status' mapping is acceptable, representing the current status of the flow.* |
| `trigger_type` | Type of trigger that initiates this flow. | `flows.attributes.trigger_type` | 🟢 _0.80_ | *The 'trigger_type' mapping aligns well as it captures the initiation type for the flow.* |
| `_fivetran_synced` | Timestamp when this record was last synced. | `flows._airbyte_extracted_at` | 🟢 _1.00_ | *Standard sync mapping from '_fivetran_synced' to '_airbyte_extracted_at', always scoring maximally.* |

## Workshop Models

These models are in the workshop directory and are not yet approved.
