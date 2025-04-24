# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `events_list` to Fivetran `event_type`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.94_
- Summary Self-Evaluation: _The mappings generally align well with the target schema, with a high degree of match confidence across the majority of fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | Timestamp of when Fivetran marked a record as deleted | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record | `events_list._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping used.* |
| `autohidden` | Whether event type is hidden | `events_list.autohidden` | 🟢 _0.70_ | *Field likely refers to the same concept as in the source schema.* |
| `deleted` | Whether event type is deleted | `events_list.deleted` | 🟢 _0.70_ | *Field likely refers to the same concept as in the source schema.* |
| `display` | The display name of the event | `events_list.display` | 🟢 _0.90_ | *High-level match of display names of events.* |
| `flow_hidden` | If the event is hidden from Pathfinder/Pathfinder Users or not | `events_list.flow_hidden` | 🟢 _0.70_ | *Field likely refers to similar visibility control.* |
| `hidden` | If the event is hidden or not. | `events_list.hidden` | 🟢 _0.70_ | *There is a high probability these fields mean the same thing across schemas.* |
| `id` | Event type ID | `events_list.id` | 🟢 _0.95_ | *Identifiers across systems are commonly synonymous.* |
| `in_waitroom` | Whether event type is in waitroom | `events_list.in_waitroom` | 🟢 _0.70_ | *Likely describes similar allocation of event type to a waitroom.* |
| `name` | Event name | `events_list.name` | 🟢 _1.00_ | *Perfect match of event names across systems.* |
| `non_active` | If the event is marked inactive or not | `events_list.non_active` | 🟢 _0.70_ | *Refers to the same status of activity level, likely same use.* |
| `project_name` | Project name | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `timeline_hidden` | If the event is hidden or not | `events_list.timeline_hidden` | 🟢 _0.70_ | *Likely the same use in context of event visibility in timelines.* |
| `totals` | The total number of times the event has happened this week | `events_list.totals` | 🟢 _0.80_ | *Refers to aggregate numbers; closely matched concepts.* |
| `totals_delta` | This represents the change in event volume from the previous week. | `events_list.totals_delta` | 🟢 _0.80_ | *Change in event volume is a directly comparable metric.* |
| `value` | Name of the event in the raw data. | `events_list.value` | 🟢 _1.00_ | *Direct match of event descriptions.* |
| `waitroom_approved` | Waitroom approved | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `events` to Fivetran `event`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The fields evaluated generally match well, but some unique Airbyte-specific contexts are absent in the Fivetran target schema, indicating incomplete but highly accurate mapping. The overall table subject matter alignment is strong._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | Timestamp of when Fivetran marked a record as deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `events._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables, matched exactly with _airbyte_extracted_at.* |
| `amplitude_id` | An internal ID used to count unique users. | `events.amplitude_id` | 🟢 _0.80_ | *Direct match found with a high confidence level.* |
| `ad_id` | (Android) Google Play Services advertising ID (AdID). This usually is wiped after ingestion and therefore will be blank  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `amplitude_attribution_ids` | Anonymized hash of the advertising IDs that Amplitude stores for internal purposes; not useful for customers by any means. But this will appear if advertising IDs were sent which proves that adid/idfv existed even though currently wiped  | `events.amplitude_attribution_ids` | 🟢 _0.80_ | *Direct match found with a high confidence level.* |
| `app` | Project ID found in your project's Settings page | `events.app` | 🟢 _0.90_ | *Direct match found, strong relevance to the context* |
