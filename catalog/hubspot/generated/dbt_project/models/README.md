# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping from Airbyte `email_events` to Fivetran `email_event`

- Table Match Confidence Score: 🟢 0.90

- Table Completion Score: 🟢 0.95

### Evaluation

The table match score is high because the field mappings consistently relate similar data across both schemas. The completion score is also high, reflecting that each field has been thoughtfully mapped with minimal missing data.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 1.00 | Standard mapping of _fivetran_synced to _airbyte_extracted_at. |
| `app_id` | The ID of the app that sent the email. | `email_events.appId` | 🟢 0.90 | app_id maps directly to email_events.appId with high confidence due to exact naming and expected context. |
| `caused_by_created` | The timestamp of the event that caused this event. | `email_events.causedBy.created` | 🟢 0.90 | Field matches email_events.causedBy.created based on context and similar naming structure. |
| `caused_by_id` | The event ID which uniquely identifies the event which directly caused this event. If not applicable, this property is omitted. | `email_events.causedBy.id` | 🟢 0.85 | Mapping to email_events.causedBy.id, given the context of event causality and ID purpose. |
| `created` | The created timestamp of the event. | `email_events.created` | 🟢 0.90 | Created timestamp exactly matches email_events.created field. |
| `email_campaign_id` | The ID of the related email campaign. | `email_events.emailCampaignId` | 🟢 0.90 | Direct match to email_events.emailCampaignId, likely identical due to naming and purpose. |
| `filtered_event` | A boolean representing whether the event has been filtered out of reporting based on customer reports settings or not. | `email_events.filteredEvent` | 🟢 0.80 | Somewhat clear mapping to email_events.filteredEvent, representing the same filter logic. |
| `id` | The ID of the event. | `email_events.id` | 🟢 0.90 | Matching event IDs with email_events.id is direct and accurate. |
| `obsoleted_by_created` | The timestamp of the event that made the current event obsolete. | `email_events.obsoletedBy.created` | 🟢 0.80 | Logically aligns with email_events.obsoletedBy.created; naming suggests a correct match. |
| `obsoleted_by_id` | The event ID which uniquely identifies the follow-on event which makes this current event obsolete. If not applicable, this property is omitted. | `email_events.obsoletedBy.id` | 🟢 0.80 | Seems to correctly match with email_events.obsoletedBy.id as per the purpose of the field. |
| `portal_id` | {{ doc("portal_id") }} | `email_events.portalId` | 🟢 0.85 | Likely matches as portal_id is a common field shared across systems, direct naming helps. |
| `recipient` | The email address of the contact related to the event. | `email_events.recipient` | 🟢 0.90 | Email recipient logically and directly relates to email_events.recipient. |
| `sent_by_created` | The timestamp of the SENT event related to this event. | `email_events.sentBy.created` | 🟢 0.85 | Sensible mapping with email_events.sentBy.created based on timestamp semantics. |
| `sent_by_id` | The event ID which uniquely identifies the email message's SENT event. If not applicable, this property is omitted. | `email_events.sentBy.id` | 🟢 0.85 | SentBy ID maps well to email_events.sentBy.id given similar roles in event tracking. |
| `type` | The type of event. | `email_events.type` | 🟢 0.90 | Event type accurately maps to email_events.type, supported by consistent terminology. |


### Mapping from Airbyte `deal_pipelines` to Fivetran `deal_pipeline`

- Table Match Confidence Score: 🟢 1.00

- Table Completion Score: 🟢 0.88

### Evaluation

All fields were matched with high confidence, except for _fivetran_deleted which was missing a corresponding match.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deal_pipelines._airbyte_extracted_at` | 🟢 1.00 | _fivetran_synced is always mapped to _airbyte_extracted_at. |
| `active` | Whether the stage is currently in use. | `deal_pipelines.active` | 🟢 1.00 | Active state has a direct mapping match in target schema. |
| `display_order` | Used to determine the order in which the pipelines appear when viewed in HubSpot. | `deal_pipelines.displayOrder` | 🟢 1.00 | Display order is mapped correctly to the target field. |
| `label` | The human-readable label for the pipeline. The label is used when showing the pipeline in HubSpot. | `deal_pipelines.label` | 🟢 1.00 | Label field matches correctly to target schema. |
| `pipeline_id` | The ID of the pipeline. | `deal_pipelines.pipelineId` | 🟢 1.00 | Pipeline ID field is correctly matched. |
| `created_at` | A timestamp representing when the record was created. | `deal_pipelines.createdAt` | 🟢 1.00 | Created at timestamp field is well mapped. |
| `updated_at` | A timestamp representing when the record was updated. | `deal_pipelines.updatedAt` | 🟢 1.00 | Updated at timestamp field is correctly matched. |


### Mapping from Airbyte `email_events` to Fivetran `email_event_print`

- Table Match Confidence Score: 🟢 0.75

- Table Completion Score: 🟢 0.80

### Evaluation

The table mapping suggests a strong correlation with email events, commonly found in both source and target schemas. Most fields have been appropriately matched to their equivalents.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 1.00 | Standard mapping from _fivetran_synced to _airbyte_extracted_at. |
| `browser` | {{ doc("email_event_browser") }} | `email_events.browser` | 🟢 0.70 | 'browser' matched directly from 'email_events.browser', which is likely a direct mapping of user browsing data. |
| `id` | The ID of the event. | `email_events.id` | ⚠️ 0.65 | 'id' matched to 'email_events.id', typically an identifier field directly shared between schemas. |
| `ip_address` | {{ doc("email_event_ip_address") }} | `email_events.ipAddress` | 🟢 0.70 | Direct match of 'ip_address' to 'email_events.ipAddress', common mapping for IP recording. |
| `location` | {{ doc("email_event_location") }} | `email_events.location` | 🟢 0.70 | Matched 'location' to 'email_events.location', generally indicating the same concept. |
| `user_agent` | {{ doc("email_event_user_agent") }} | `email_events.userAgent` | ⚠️ 0.65 | Directly mapped 'user_agent' to 'email_events.userAgent', reflecting similar user metadata tracking. |


### Mapping from Airbyte `engagements_emails` to Fivetran `engagement_email`

- Table Match Confidence Score: 🟢 0.80

- Table Completion Score: 🟢 0.70

### Evaluation

The table mapping is evaluated with a relatively high confidence due to the presence of standard mappings like `_fivetran_synced` to `_airbyte_extracted_at` and typical fields seen in similar schemas. However, there are fields that exhibit uncertainty, lowering the completion score.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_emails._airbyte_extracted_at` | 🟢 1.00 | Standard mapping of `_fivetran_synced` to `_airbyte_extracted_at`. |
| `engagement_id` | The ID of the engagement. | `engagements_emails.id` | 🟢 0.80 | Direct mapping with high confidence, common field name indicating unique identifier. |
| `property_hs_createdate` | This field marks the email's time of creation and determines where the email sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_emails.properties.hs_createdate` | ⚠️ 0.65 | Field corresponds to a timestamp, but specific conditions in the description suggest slight differences in data presence. |
| `timestamp` | This field marks the email's time of occurrence and determines where the email sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_emails.properties_hs_timestamp` | ⚠️ 0.65 | Another timestamp field, similar explanation as property_hs_createdate. |
| `property_hubspot_owner_id` | The ID of the owner associated with the email. This field determines the user listed as the email creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_emails.properties.hubspot_owner_id` | 🟢 0.70 | Likely mapping for owner ID, but conditional existence in description affects confidence. |
| `property_hubspot_team_id` | The ID of the team associated with the email. This field determines the team listed as the email creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.
 | `engagements_emails.properties.hubspot_team_id` | 🟢 0.70 | Likely mapping for team ID, but conditional existence in description affects confidence. |


### Mapping from Airbyte `engagements_notes` to Fivetran `engagement_note`

- Table Match Confidence Score: 🟢 0.85

- Table Completion Score: ⚠️ 0.57

### Evaluation

The table mapping reflects the same conceptual entity between the source and target. However, one of the field mappings is missing, impacting the completion score. The table map aligns well with data source structures typically shared via similar APIs, thereby achieving a high table match score.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_notes._airbyte_extracted_at` | 🟢 1.00 | This is a standard mapping for all tables and is always mapped to '_airbyte_extracted_at'. |
| `body` | The body of the note. The body has a limit of 65536 characters. | `engagements_notes.properties.hs_note_body` | 🟢 0.80 | The field 'body' maps well to 'hs_note_body' indicating a similar content purpose, thus achieving a high confidence score. |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ 0.00 | No good match found. |
| `property_hs_createdate` | This field marks the note's time of creation and determines where the note sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_notes.properties.hs_createdate` | 🟢 0.70 | This field marks the note's time of creation; mapped to 'hs_createdate' reflecting likely indiscernible temporal data. Meeting specified criteria. |
| `timestamp` | This field marks the note's time of occurrence and determines where the note sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_notes.properties.hs_timestamp` | 🟢 0.70 | This field marks the note's time of occurrence; mapped to 'hs_timestamp', aligns contextually similar to creation date. |
| `property_hubspot_owner_id` | The ID of the owner associated with the note. This field determines the user listed as the note creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_notes.properties.hubspot_owner_id` | 🟢 0.70 | Reflects ownership of the note, aligning contextually with 'hubspot_owner_id', maintaining entity tracking consistency. |
| `property_hubspot_team_id` | The ID of the team associated with the note. This field determines the team listed as the note creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.
 | `engagements_notes.properties.hubspot_team_id` | 🟢 0.70 | Reflects team ownership of the note, aligning consistently with 'hubspot_team_id', reinforcing entity clarity. |


### Mapping from Airbyte `email_events` to Fivetran `email_event_delivered`

- Table Match Confidence Score: 🟢 0.90

- Table Completion Score: 🟢 0.90

### Evaluation

The table mappings are likely to be very similar due to shared API origins. However, the completion score reflects the slight differences in implementations.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 1.00 | Standard mapping to _airbyte_extracted_at, which is always a perfect match. |
| `id` | The ID of the event. | `email_events.id` | 🟢 0.80 | The ID field is likely to be similar, but due to potential differing usages across systems, a score of 0.8 is appropriate. |
| `response` | The full response from the recipient's email server. | `email_events.response` | 🟢 0.70 | The response field is matched based on the content expected; however, different systems might use different levels of detail or format. |
| `smtp_id` | An ID attached to the message by HubSpot. | `email_events.smtpId` | 🟢 0.75 | This ID corresponds to a message-specific identifier used in email systems, and matches are likely but not guaranteed to be identical. |


### Mapping from Airbyte `companies` to Fivetran `company`

- Table Match Confidence Score: 🟢 0.70

- Table Completion Score: 🟢 0.86

### Evaluation

Table match confidence is reasonably high, considering the target schema's table fields are closely matched with source fields.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `companies._airbyte_extracted_at` | 🟢 1.00 | Standard mapping for all tables. |
| `id` | The ID of the company. | `companies.id` | 🟢 1.00 | Exact match found with the corresponding source field. |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `is_deleted` | {{ doc("is_deleted") }} | `companies.archived` | 🟢 0.70 | Matches a logical field in the source schema. |
| `property_name` | The name of the company. | `companies.properties.name` | 🟢 1.00 | Exact match found with the source field. |
| `property_description` | A short statement about the company's mission and goals. | `companies.properties.description` | 🟢 1.00 | Exact match found based on description. |
| `property_createdate` | The date the company was added to your account. | `companies.properties.createdate` | 🟢 1.00 | Exact match found based on purpose. |
| `property_industry` | The type of business the company performs. | `companies.properties.industry` | 🟢 1.00 | Exact match found for describing business type. |
| `property_address` | The street address of the company. | `companies.properties.address` | 🟢 1.00 | Exact match found for street address. |
| `property_address_2` | Additional address information for the company. | `companies.properties.address2` | 🟢 1.00 | Matches additional address information. |
| `property_city` | The city where the company is located. | `companies.properties.city` | 🟢 1.00 | Exact match found for city location. |
| `property_state` | The state where the company is located. | `MISSING` | ❌ 0.00 | No good match found. |
| `property_country` | The country where the company is located. | `companies.properties.country` | 🟢 1.00 | Exact match found for country location. |
| `property_annualrevenue` | The actual or estimated annual revenue of the company. | `companies.properties.annualrevenue` | 🟢 1.00 | Exact match found for annual revenue. |


### Mapping from Airbyte `contacts_list_memberships` to Fivetran `contact_list_member`

- Table Match Confidence Score: 🟢 0.70

- Table Completion Score: ⚠️ 0.60

### Evaluation

The table mappings suggest a moderate confidence that the source and target tables describe similar subjects. The completion score indicates that some fields are well-mapped, but others are missing mappings.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_list_memberships._airbyte_extracted_at` | 🟢 1.00 | Standard mapping for all tables. |
| `added_at` | The timestamp a contact was added to a list. | `MISSING` | ❌ 0.00 | No good match found. |
| `contact_id` | The ID of the related contact. | `contacts_list_memberships.vid` | 🟢 0.70 | Good match with 'contacts_list_memberships.vid'. |
| `contact_list_id` | The ID of the related contact list. | `contacts_list_memberships.static_list_id` | 🟢 0.70 | Good match with 'contacts_list_memberships.static_list_id'. |


### Mapping from Airbyte `engagements_meetings` to Fivetran `engagement_meeting`

- Table Match Confidence Score: 🟢 0.80

- Table Completion Score: 🟢 0.67

### Evaluation

The table mapping is of high quality due to the good alignment between source and target tables. However, the completion score is lower due to one missing field mapping and some field-level uncertainty.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_meetings._airbyte_extracted_at` | 🟢 1.00 | Standard mapping for all tables. Mapped '_fivetran_synced' to source stream's '_airbyte_extracted_at' column. |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ 0.00 | No good match found. |
| `property_hs_createdate` | This field marks the meeting's time of creation and determines where the meeting sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_meetings.properties_hs_createdate` | 🟢 0.70 | The expression shows a direct alignment although with slight contextual uncertainties. |
| `timestamp` | This field marks the meeting's time of occurrence and determines where the meeting sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_meetings.properties_hs_timestamp` | 🟢 0.70 | The expression shows a direct alignment although with slight contextual uncertainties. |
| `property_hubspot_owner_id` | The ID of the owner associated with the meeting. This field determines the user listed as the meeting creator on the record timeline.
 PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_meetings.properties_hubspot_owner_id` | 🟢 0.70 | The expression shows a direct alignment although with slight contextual uncertainties. |
| `property_hubspot_team_id` | The ID of the team associated with the meeting. This field determines the team listed as the meeting creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.
 | `engagements_meetings.properties_hubspot_team_id` | 🟢 0.70 | The expression shows a direct alignment although with slight contextual uncertainties. |


### Mapping from Airbyte `engagements_tasks` to Fivetran `engagement_task`

- Table Match Confidence Score: 🟢 0.70

- Table Completion Score: 🟢 0.83

### Evaluation

The table mapping uses similar source and target models with high confidence. However, one field expression is missing, reducing the overall completion.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_tasks._airbyte_extracted_at` | 🟢 1.00 | Standard mapping for '_fivetran_synced' to '_airbyte_extracted_at' with perfect confidence. |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ 0.00 | No good match found. |
| `property_hs_createdate` | This field marks the task's time of creation and determines where the task sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_tasks.properties_hs_createdate` | 🟢 0.70 | Mapping is likely correct based on similar meaning of creation date fields. |
| `timestamp` | This field marks the task's time of occurrence and determines where the task sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_tasks.properties_hs_timestamp` | 🟢 0.70 | Mapping matches timestamp meaning, considering API version context. |
| `property_hubspot_owner_id` | The ID of the owner associated with the task. This field determines the user listed as the task creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_tasks.properties_hubspot_owner_id` | 🟢 0.70 | Mapping likely correct for owner linkage based on API versioning details. |
| `property_hubspot_team_id` | The ID of the team associated with the task. This field determines the team listed as the task creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.
 | `engagements_tasks.properties_hubspot_team_id` | 🟢 0.70 | Mapping likely correct for team linkage given API versioning restrictions. |


### Mapping from Airbyte `tickets` to Fivetran `ticket`

- Table Match Confidence Score: 🟢 0.70

- Table Completion Score: 🟢 0.93

### Evaluation

The table mapping was evaluated with a high level of confidence due to significant field coverage and strong matching logic between the two systems, despite minor imperfect mappings.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `tickets._airbyte_extracted_at` | 🟢 1.00 | Standard mapping directly from the source's `_airbyte_extracted_at` column. |
| `id` | ID of the ticket. | `tickets.id` | 🟢 0.80 | Direct match with `tickets.id`, indicating strong correspondence between source and target hierarchy. |
| `is_deleted` | Whether the record was deleted (v2 endpoint). | `tickets.archived` | 🟢 0.70 | Mapped to `tickets.archived`, which likely indicates a similar field purpose. |
| `_fivetran_deleted` | Whether the record was deleted (v3 endpoint). | `tickets.archived` | 🟢 0.70 | Also mapped to `tickets.archived`, showing another potential logical mapping. |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `property_closed_date` | The date the ticket was closed. | `tickets.properties.closed_date` | 🟢 0.90 | Mapped to `tickets.properties.closed_date`, indicating direct mapping with proper context. |
| `property_createdate` | The date the ticket was created. | `tickets.properties_createdate` | 🟢 0.90 | Mapped to `tickets.properties_createdate` with apparent logical equivalence and context correctness. |
| `property_first_agent_reply_date` | the date for the first agent reply on the ticket. | `tickets.properties_first_agent_reply_date` | 🟢 0.90 | Mapped to `tickets.properties_first_agent_reply_date`, indicating a clear logical match. |
| `property_hs_pipeline` | The ID of the ticket's pipeline. | `tickets.properties.hs_pipeline` | 🟢 0.90 | Mapped to `tickets.properties.hs_pipeline`, a logical match confirming field integrity. |
| `property_hs_pipeline_stage` | The ID of the ticket's pipeline stage. | `tickets.properties.hs_pipeline_stage` | 🟢 0.90 | Corresponds directly to `tickets.properties.hs_pipeline_stage`, with strong contextual alignment. |
| `property_hs_ticket_priority` | The priority of the ticket. | `tickets.properties.hs_ticket_priority` | 🟢 0.90 | Aligned with `tickets.properties.hs_ticket_priority`, serving an identical purpose. |
| `property_hs_ticket_category` | The category of the ticket. | `tickets.properties.hs_ticket_category` | 🟢 0.90 | Mapped identically to `tickets.properties.hs_ticket_category` with contextual accuracy. |
| `property_hubspot_owner_id` | The ID of the deal's owner. | `tickets.properties_hubspot_owner_id` | 🟢 0.90 | Mapped to `tickets.properties_hubspot_owner_id`, reflecting identical field usage. |
| `property_subject` | Short summary of ticket. | `tickets.properties.subject` | 🟢 0.90 | Mapped to `tickets.properties.subject`, demonstrating a strong match. |
| `property_content` | Text in body of the ticket. | `tickets.properties.content` | 🟢 0.90 | Mapped correctly to `tickets.properties.content`, supporting the mapping's validity. |


### Mapping from Airbyte `email_subscriptions` to Fivetran `email_subscription`

- Table Match Confidence Score: 🟢 0.70

- Table Completion Score: 🟢 1.00

### Evaluation

Table mapping between the source and target is a strong match due to alignment of fields and standardized mappings. Completion score is perfect as all required fields are mapped.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_subscriptions._airbyte_extracted_at` | 🟢 1.00 | Standard mapping to '_airbyte_extracted_at' with full confidence. |
| `active` | Whether the subscription is active. | `email_subscriptions.active` | 🟢 0.70 | Mapped to a field with a closely matching name and plausible function. |
| `description` | The description of the subscription. | `email_subscriptions.description` | 🟢 0.70 | Mapped to a field with a closely matching name and plausible function. |
| `id` | The ID of the email subscription. | `email_subscriptions.id` | 🟢 0.70 | Mapped to a field with a closely matching name and plausible function. |
| `name` | The name of the email subscription. | `email_subscriptions.name` | 🟢 0.70 | Mapped to a field with a closely matching name and plausible function. |
| `portal_id` | {{ doc("portal_id") }} | `email_subscriptions.portalId` | 🟢 0.70 | Mapped to a field with a closely matching name and plausible function. |


### Mapping from Airbyte `contacts` to Fivetran `contact`

- Table Match Confidence Score: 🟢 0.85

- Table Completion Score: 🟢 0.91

### Evaluation

The mapping is generally strong, showing a high level of confidence that the target schema fields align with the source fields. The completion is high, indicating most source fields have corresponding target fields.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts._airbyte_extracted_at` | 🟢 1.00 | _fivetran_synced perfectly maps to contacts._airbyte_extracted_at. |
| `id` | The ID of the contact. | `contacts.id` | 🟢 1.00 | The 'id' field perfectly matches the target schema. |
| `property_email_1` | The email address of the contact. | `contacts.properties_email` | 🟢 0.70 | Partial match with some uncertainty due to potential overlapping with similar fields. |
| `property_company` | The name of the contact's company. | `contacts.properties_company` | 🟢 1.00 | The 'company' field is clearly matched. |
| `property_firstname` | The contact's first name. | `contacts.properties_firstname` | 🟢 1.00 | The 'first name' field is correctly aligned. |
| `property_lastname` | The contact's last name. | `contacts.properties_lastname` | 🟢 1.00 | The 'last name' field is correctly aligned. |
| `property_email` | The contact's email. | `contacts.properties_email` | 🟢 0.70 | Partial match with some uncertainty due to potential duplicate mappings. |
| `property_createdate` | The date that the contact was created in your HubSpot account. | `contacts.properties_createdate` | 🟢 1.00 | Creation date field matches perfectly. |
| `property_jobtitle` | The contact's job title. | `contacts.properties_jobtitle` | 🟢 1.00 | The 'job title' field is well matched. |
| `property_annualrevenue` | The contact's annual company revenue. | `contacts.properties_annualrevenue` | 🟢 1.00 | Annual revenue field is an exact match. |
| `property_hs_calculated_merged_vids` | List of mappings representing contact IDs that have been merged into the contact at hand. Format: <merged_contact_id>:<merged_at_in_epoch_time>;<second_merged_contact_id>:<merged_at_in_epoch_time> This field has replaced the `CONTACT_MERGE_AUDIT` table, which was deprecated by the Hubspot v3 CRM API.
 | `contacts.properties_hs_calculated_merged_vids` | ⚠️ 0.65 | Field partially matched with high confidence for underlying meaning, but lacking precise mapping. |


### Mapping from Airbyte `contacts_merged_audit` to Fivetran `contact_merge_audit`

- Table Match Confidence Score: 🟢 0.85

- Table Completion Score: 🟢 0.90

### Evaluation

The source and target tables are highly likely describing the same subject matter since the fields have meaningful mappings. However, there's a missing match affecting the completion score slightly.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_merged_audit._airbyte_extracted_at` | 🟢 1.00 | _fivetran_synced is perfectly mapped to _airbyte_extracted_at as per standard convention. |
| `canonical_vid` | The contact ID of the contact which the vid_to_merge contact was merged into. | `contacts_merged_audit.canonical_vid` | 🟢 0.90 | The contact ID canonical_vid matches strongly to a similar ID field, indicating a high confidence. |
| `contact_id` | The ID of the contact. | `MISSING` | ❌ 0.00 | No good match found. |
| `entity_id` | The ID of the related entity. | `contacts_merged_audit.entity_id` | 🟢 0.80 | entity_id has a reasonable match with fields in the target schema that relate to entities. |
| `first_name` | The contact's first name. | `contacts_merged_audit.first_name` | 🟢 0.80 | The first name field aligns well with a similarly purposed field in the target schema. |
| `last_name` | The contact's last name. | `contacts_merged_audit.last_name` | 🟢 0.80 | The last name field aligns well with a similarly purposed field in the target schema. |
| `num_properties_moved` | The number of properties which were removed from the merged contact. | `contacts_merged_audit.num_properties_moved` | 🟢 0.70 | The field num_properties_moved relates closely to a count of properties, suggesting reasonable confidence. |
| `timestamp` | Timestamp of when the contacts were merged. | `contacts_merged_audit.timestamp` | 🟢 0.85 | The timestamp field is a direct match with a similarly intended field in the target. |
| `user_id` | The ID of the user. | `contacts_merged_audit.user_id` | 🟢 0.70 | user_id matches a user-related field sufficiently, though not perfectly. |
| `vid_to_merge` | The ID of the contact which was merged. | `contacts_merged_audit.vid_to_merge` | 🟢 0.90 | The field vid_to_merge has a strong correlation with a similar structure in the target. |


### Mapping from Airbyte `owners` to Fivetran `owner`

- Table Match Confidence Score: 🟢 0.90

- Table Completion Score: 🟢 0.70

### Evaluation

The mappings are largely appropriate for the given context with `_fivetran_synced` mapping perfectly, but there are unknown fields marked as 'MISSING'.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `owners._airbyte_extracted_at` | 🟢 1.00 | Standard mapping for '_fivetran_synced' to '_airbyte_extracted_at'. |
| `created_at` | A timestamp for when the owner was created. | `owners.createdAt` | 🟢 0.90 | High confidence match with 'owners.createdAt' given the context. |
| `email` | The email address of the owner. | `owners.email` | 🟢 0.90 | High confidence match with 'owners.email' based on field name and context. |
| `first_name` | The first name of the owner. | `owners.firstName` | 🟢 0.90 | High confidence match with 'owners.firstName' due to similar naming and context. |
| `last_name` | The last name of the owner. | `owners.lastName` | 🟢 0.90 | High confidence match with 'owners.lastName' based on context similarity. |
| `owner_id` | The ID of the owner. | `owners.userId` | 🟢 0.90 | High confidence that 'owner_id' and 'owners.userId' refer to the same entity. |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `type` | The type of owner. | `MISSING` | ❌ 0.00 | No good match found. |
| `updated_at` |  | `owners.updatedAt` | 🟢 0.90 | High confidence in matching 'owners.updatedAt' with 'updated_at'. |


### Mapping from Airbyte `contacts_form_submissions` to Fivetran `contact_form_submission`

- Table Match Confidence Score: 🟢 0.80

- Table Completion Score: 🟢 0.88

### Evaluation

The table match confidence is high due to the presence of common fields in the source and target tables, such as conversion_id and form_id, which are indicative of form submissions. However, the completion is partly reduced as a result of a 'MISSING' field and some other mapped fields having a close match score instead of perfect.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_form_submissions._airbyte_extracted_at` | 🟢 1.00 | The field '_fivetran_synced' is correctly mapped to '_airbyte_extracted_at' as per standard mapping rules. |
| `contact_id` | The ID of the related contact. | `MISSING` | ❌ 0.00 | No good match found. |
| `conversion_id` | A Unique ID for the specific form conversion. | `contacts_form_submissions.conversion_id` | 🟢 0.70 | Close confidence since 'conversion_id' appears to match correctly with the source. |
| `form_id` | The GUID of the form that the submission belongs to. | `contacts_form_submissions.form_id` | 🟢 0.70 | Reasonable confidence as 'form_id' corresponds within the submission context. |
| `page_url` | The URL that the form was submitted on, if applicable. | `contacts_form_submissions.canonical_url` | 🟢 0.70 | Matches with 'canonical_url' reasonably well for a form submission context. |
| `portal_id` | {{ doc("portal_id") }} | `contacts_form_submissions.portal_id` | 🟢 0.70 | Field 'portal_id' mapped with standard naming conventions. |
| `timestamp` | A Unix timestamp in milliseconds of the time the submission occurred. | `contacts_form_submissions.timestamp` | 🟢 0.70 | Field 'timestamp' appears to match the context of form submission times. |
| `title` | The title of the page that the form was submitted on. This will default to the name of the form if no title is provided. | `contacts_form_submissions.page_title` | 🟢 0.70 | Field 'title' matches the common context in form submission metadata. |


### Mapping from Airbyte `deals_property_history` to Fivetran `deal_property_history`

- Table Match Confidence Score: 🟢 0.72

- Table Completion Score: 🟢 0.86

### Evaluation

The table match score is relatively high, indicating a good match between source and target tables based on similar schema elements. However, one field has an expression marked as 'MISSING', lowering the completion score due to incomplete mapping.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deals_property_history._airbyte_extracted_at` | 🟢 1.00 | Standard mapping for _fivetran_synced to _airbyte_extracted_at. |
| `deal_id` | The ID of the related deal record. | `deals_property_history.dealId` | 🟢 0.70 | dealId from deals_property_history is likely to match deal_id based on naming and context. |
| `name` | {{ doc("history_name") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `source` | {{ doc("history_source") }} | `deals_property_history.sourceType` | 🟢 0.70 | sourceType from deals_property_history matches source based on name and typical usage. |
| `source_id` | {{ doc("history_source_id") }} | `deals_property_history.sourceId` | 🟢 0.70 | sourceId from deals_property_history matches source_id based on naming similarities. |
| `timestamp` | {{ doc("history_timestamp") }} | `deals_property_history.timestamp` | 🟢 0.70 | timestamp from deals_property_history matches timestamp based on naming conventions. |
| `value` | {{ doc("history_value") }} | `deals_property_history.value` | 🟢 0.70 | value from deals_property_history matches value, typical mapping based on name. |


### Mapping from Airbyte `engagements` to Fivetran `engagement`

- Table Match Confidence Score: 🟢 0.85

- Table Completion Score: 🟢 0.75

### Evaluation

The table mapping shows high match quality with a strong correspondence between most fields. However, some fields from the source schema could not be mapped to the target schema.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements._airbyte_extracted_at` | 🟢 1.00 | Standard mapping from '_fivetran_synced' to '_airbyte_extracted_at'. |
| `active` | Whether the engagement is currently being shown in the UI.
 PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.
 | `engagements.active` | ⚠️ 0.60 | Mapped to 'engagements.active' with moderate confidence. |
| `created_at` | A timestamp representing when the engagement was created.
 PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.
 | `engagements.createdAt` | ⚠️ 0.60 | Mapped to 'engagements.createdAt' with moderate confidence. |
| `id` | The ID of the engagement. | `engagements.id` | 🟢 0.70 | Mapped to 'engagements.id', high confidence due to clear correspondence. |
| `owner_id` | The ID of the engagement's owner.
PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.
 | `engagements.ownerId` | ⚠️ 0.60 | Mapped to 'engagements.ownerId' with moderate confidence. |
| `portal_id` | {{ doc("portal_id") }} | `engagements.portalId` | ⚠️ 0.60 | Mapped to 'engagements.portalId' with moderate confidence. |
| `timestamp` | A timestamp in representing the time that the engagement should appear in the timeline.
PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.
 | `engagements.timestamp` | ⚠️ 0.60 | Mapped to 'engagements.timestamp' with moderate confidence. |
| `type` | One of NOTE, EMAIL, TASK, MEETING, or CALL, the type of the engagement. | `engagements.type` | 🟢 0.70 | Mapped to 'engagements.type', high confidence due to distinct field type categories. |


### Mapping from Airbyte `companies_property_history` to Fivetran `company_property_history`

- Table Match Confidence Score: 🟢 0.80

- Table Completion Score: 🟢 0.85

### Evaluation

The table match is strong due to the consistent naming and field availability between the source and target. All fields have been mapped with high confidence except for any potential 'MISSING' fields, which slightly lowers the completion score.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `companies_property_history._airbyte_extracted_at` | 🟢 1.00 | Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at'. |
| `company_id` | The ID of the related company record. | `companies_property_history.companyId` | 🟢 0.95 | High confidence mapping based on consistent naming and usage. |
| `name` | {{ doc("history_name") }} | `companies_property_history.properties.name` | 🟢 0.70 | Reasonable match based on naming convention and context. |
| `source` | {{ doc("history_source") }} | `companies_property_history.sourceType` | 🟢 0.70 | Reasonable match based on naming convention and context. |
| `source_id` | {{ doc("history_source_id") }} | `companies_property_history.sourceId` | 🟢 0.70 | Reasonable match based on naming convention and context. |
| `timestamp` | {{ doc("history_timestamp") }} | `companies_property_history.timestamp` | 🟢 0.95 | High confidence due to common timestamp usage across schemas. |
| `value` | {{ doc("history_value") }} | `companies_property_history.value` | 🟢 0.85 | Strong match supported by consistent usage across data sources. |


## Workshop Models

These models are in the workshop directory and are not yet approved.

### Mapping from Airbyte `contacts_property_history` to Fivetran `contact_property_history`

- Table Match Confidence Score: ⚠️ 0.60

- Table Completion Score: ❌ 0.43

### Evaluation

The mapping involves 7 fields, out of which 4 had direct matches. However, 3 fields are marked as 'MISSING', significantly reducing the completion score.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_property_history._airbyte_extracted_at` | 🟢 1.00 | Standard mapping for '_fivetran_synced' to source stream's '_airbyte_extracted_at'. |
| `contact_id` | The ID of the related contact record. | `MISSING` | ❌ 0.00 | No good match found. |
| `name` | {{ doc("history_name") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `source` | {{ doc("history_source") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `source_id` | {{ doc("history_source_id") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `timestamp` | {{ doc("history_timestamp") }} | `contacts_property_history.timestamp` | 🟢 0.70 | Reasonable confidence that 'contacts_property_history.timestamp' is the correct mapping. |
| `value` | {{ doc("history_value") }} | `contacts_property_history.value` | 🟢 0.70 | Reasonable confidence that 'contacts_property_history.value' is the correct mapping. |


### Mapping from Airbyte `forms` to Fivetran `form`

- Table Match Confidence Score: 🟢 0.90

- Table Completion Score: 🟢 0.69

### Evaluation

The table mapping score is high because the tables share many common fields, indicating they likely describe similar subjects. However, the completion score is lower due to several fields mapped as 'MISSING'.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `forms._airbyte_extracted_at` | 🟢 1.00 | Consistently maps to '_airbyte_extracted_at'. |
| `created_at` | A timestamp for when the form was created. | `forms.createdAt` | 🟢 0.80 | Mapped to a corresponding timestamp for creation within forms. |
| `css_class` | The CSS classes assigned to the form. | `forms.displayOptions.cssClass` | 🟢 0.70 | Assigned CSS classes are mapped to a similarly structured path. |
| `follow_up_id` | This field is no longer used. | `MISSING` | ❌ 0.00 | No good match found. |
| `guid` | The internal ID of the form. | `MISSING` | ❌ 0.00 | No good match found. |
| `lead_nurturing_campaign_id` | TBD | `forms.properties.hs_marketing_campaign_guid` | ⚠️ 0.60 | Mapping to a marketing campaign GUID is a possible but uncertain match. |
| `method` | This field is no longer used. | `MISSING` | ❌ 0.00 | No good match found. |
| `name` | The name of the form. | `forms.name` | 🟢 0.90 | Mapped directly to the form's name, indicating a strong match. |
| `notify_recipients` | A comma-separated list of user IDs that should receive submission notifications.
Email addresses will be returned for individuals who aren't users.
 | `forms.configuration.notifyRecipients` | 🟢 0.80 | Correctly identifies a list of user IDs for notifications within the forms. |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `redirect` | The URL that the visitor will be redirected to after filling out the form. | `forms.configuration.postSubmitAction.value` | 🟢 0.80 | Mapped to a post-submit URL, reflecting the described functionality. |
| `submit_text` | The text used for the submit button. | `forms.displayOptions.submitButtonText` | 🟢 0.70 | Submit button text mapping aligns with function. |
| `updated_at` | A timestamp for when the form was last updated. | `forms.updatedAt` | 🟢 0.80 | Mapped to a corresponding timestamp for updates within forms. |


### Mapping from Airbyte `contact_lists` to Fivetran `contact_list`

- Table Match Confidence Score: 🟢 0.70

- Table Completion Score: ⚠️ 0.60

### Evaluation

The table match is relatively strong due to shared data origin (API), but not all fields are present in the source.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contact_lists._airbyte_extracted_at` | 🟢 1.00 | Standard mapping to source stream's '_airbyte_extracted_at' column. |
| `created_at` | A timestamp of the time the list was created. | `contact_lists.createdAt` | 🟢 0.90 | Timestamps align well between 'createdAt' and 'created_at'. |
| `id` | The ID of the contact list. | `contact_lists.listId` | 🟢 0.90 | IDs align well between 'listId' and 'id'. |
| `name` | The name of the contact list. | `contact_lists.name` | 🟢 0.90 | Names align between 'name' and 'name'. |
| `updated_at` | A timestamp of the time that the list was last modified. | `contact_lists.updatedAt` | 🟢 0.90 | Timestamps align well between 'updatedAt' and 'updated_at'. |
| `created_by_id` | The unique identifier of the user who created the contact list. | `contact_lists.authorId` | 🟢 0.80 | Good match between 'authorId' and 'created_by_id'. |
| `object_type_id` | The ID that corresponds to the type of object stored by the list. | `MISSING` | ❌ 0.00 | No good match found. |
| `processing_status` | Indicates the current status of the list's processing, such as 'COMPLETE', 'PROCESSING', 'DONE', or 'FAILED'. | `MISSING` | ❌ 0.00 | No good match found. |
| `processing_type` | Specifies the type of processing applied to the list, for example, 'STATIC' for static lists or 'DYNAMIC' for dynamic lists. | `MISSING` | ❌ 0.00 | No good match found. |
| `list_version` | Represents the version number of the list, incrementing with each modification. | `MISSING` | ❌ 0.00 | No good match found. |
| `filters_updated_at` | The timestamp indicating when the list's filters were last updated. | `MISSING` | ❌ 0.00 | No good match found. |
| `metadata_error` | Any errors that happened the last time the list was processed.
 NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 | `contact_lists.metaData_error` | 🟢 0.70 | Deprecation notice: field may not be populated in future. |
| `metadata_last_processing_state_change_at` | A timestamp of the last time that the processing state changed.
 NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 | `contact_lists.metaData_lastProcessingStateChangeAt` | 🟢 0.70 | Deprecation notice: field may not be populated in future. |
| `metadata_last_size_change_at` | A timestamp of the last time that the size of the list changed.
 NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 | `contact_lists.metaData_lastSizeChangeAt` | 🟢 0.70 | Deprecation notice: field may not be populated in future. |
| `metadata_processing` | One of DONE, REFRESHING, INITIALIZING, or PROCESSING. DONE indicates the list has finished processing, any other value indicates that list membership is being evaluated.
NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 | `contact_lists.metaData_processing` | 🟢 0.70 | Deprecation notice: field may not be populated in future. |
| `metadata_size` | The approximate number of contacts in the list.
NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 | `contact_lists.metaData_size` | 🟢 0.70 | Deprecation notice: field may not be populated in future. |
| `portal_id` | '{{ doc("portal_id") }}'
NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 | `contact_lists.portalId` | 🟢 0.70 | Deprecation notice: field may not be populated in future. |
| `deleteable` | If this is false, this is a system list and cannot be deleted.
 NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 | `contact_lists.deleteable` | 🟢 0.70 | Deprecation notice: field may not be populated in future. |
| `dynamic` | Whether the contact list is dynamic.
NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 | `contact_lists.dynamic` | 🟢 0.70 | Deprecation notice: field may not be populated in future. |


### Mapping from Airbyte `ticket_pipelines` to Fivetran `ticket_pipeline`

- Table Match Confidence Score: ⚠️ 0.65

- Table Completion Score: ⚠️ 0.50

### Evaluation

The table and field mappings include several 'MISSING' entries, indicating incomplete mapping. However, certain fields like '_fivetran_synced' have confident mappings based on standard conventions. Moreover, fields like 'display_order', 'label', 'created_at', and 'updated_at' have plausible mappings, albeit with less confidence due to lack of complete corroboration across source and target schemas.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `ticket_pipelines._airbyte_extracted_at` | 🟢 1.00 | Standard mapping to '_airbyte_extracted_at' column. |
| `active` | Boolean indicating whether the pipeline is active. | `MISSING` | ❌ 0.00 | No good match found. |
| `display_order` | Used to determine the order in which the stages appear when viewed in HubSpot. | `ticket_pipelines.displayOrder` | ⚠️ 0.65 | Mapped to 'ticket_pipelines.displayOrder', indicating similar intents. |
| `label` | The human-readable label for the stage. The label is used when showing the stage in HubSpot. | `ticket_pipelines.label` | ⚠️ 0.65 | Mapped to 'ticket_pipelines.label', indicating similar intents. |
| `object_type_id` | Reference to the object type. | `MISSING` | ❌ 0.00 | No good match found. |
| `pipeline_id` | Reference to the pipeline. | `MISSING` | ❌ 0.00 | No good match found. |
| `created_at` | A timestamp representing when the record was created. | `ticket_pipelines.createdAt` | ⚠️ 0.65 | Timestamp mapped to 'ticket_pipelines.createdAt', consistent with documentation. |
| `updated_at` | A timestamp representing when the record was updated. | `ticket_pipelines.updatedAt` | ⚠️ 0.65 | Timestamp mapped to 'ticket_pipelines.updatedAt', consistent with documentation. |


### Mapping from Airbyte `engagements_calls` to Fivetran `engagement_call`

- Table Match Confidence Score: 🟢 0.80

- Table Completion Score: ❌ 0.43

### Evaluation

The table match score is relatively high due to the commonality in the API usage and consistent field naming conventions between source and target schemas. However, the completion score is low due to missing expressions in key fields, which significantly impacts the ability to map data comprehensively.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_calls._airbyte_extracted_at` | 🟢 1.00 | _fivetran_synced is mapped to a source stream's _airbyte_extracted_at column, which is a standard mapping. |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ 0.00 | No good match found. |
| `_fivetran_deleted` | Boolean to mark rows that were deleted in the source database. | `MISSING` | ❌ 0.00 | No good match found. |
| `property_hs_createdate` | This field marks the call's time of creation and determines where the call sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_calls.properties.hs_createdate` | 🟢 0.70 | This field has a fairly direct matching in the source properties. |
| `timestamp` | This field marks the call's time of occurrence and determines where the call sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `MISSING` | ❌ 0.00 | No good match found. |
| `property_hubspot_owner_id` | The ID of the owner associated with the call. This field determines the user listed as the call creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 | `engagements_calls.properties.hubspot_owner_id` | 🟢 0.70 | This field has a moderate confidence match based on the HubSpot API version context. |
| `property_hubspot_team_id` | The ID of the team associated with the call. This field determines the team listed as the call creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.
 | `engagements_calls.properties.hubspot_team_id` | 🟢 0.70 | This field has a moderate confidence match based on the HubSpot API version context. |


### Mapping from Airbyte `deals` to Fivetran `deal`

- Table Match Confidence Score: 🟢 0.75

- Table Completion Score: 🟢 0.70

### Evaluation

The table mapping reflects a generally good match between source and target tables, as most fields are correctly mapped. However, there are a few fields that could not be matched and are marked as 'MISSING', which affects completion.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `deal_id` | The ID of the deal. | `deals.properties.hs_object_id` | 🟢 0.90 | Matched field 'deal_id' confidently. |
| `is_deleted` | Whether the record was deleted. | `MISSING` | ❌ 0.00 | No good match found. |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ 0.00 | No good match found. |
| `deal_pipeline_id` | The ID of the deal's pipeline. | `MISSING` | ❌ 0.00 | No good match found. |
| `deal_pipeline_stage_id` | The ID of the deal's pipeline stage. | `deals.properties.dealstage` | 🟢 0.85 | Matched field 'deal_pipeline_stage_id' confidently. |
| `owner_id` | The ID of the deal's owner. | `deals.properties_hubspot_owner_id` | 🟢 0.85 | Matched field 'owner_id' confidently. |
| `property_dealname` | The name you have given this deal. | `deals.properties.dealname` | 🟢 0.90 | Matched field 'property_dealname' confidently. |
| `property_description` | A brief description of the deal. | `deals.properties.description` | 🟢 0.90 | Matched field 'property_description' confidently. |
| `property_amount` | The total value of the deal in the deal's currency. | `deals.properties.amount` | 🟢 0.90 | Matched field 'property_amount' confidently. |
| `property_closedate` | The day the deal is expected to close, or was closed. | `deals.properties.closedate` | 🟢 0.90 | Matched field 'property_closedate' confidently. |
| `property_createdate` | The date the deal was created. This property is set automatically by HubSpot. | `deals.properties.createdate` | 🟢 0.90 | Matched field 'property_createdate' confidently. |


### Mapping from Airbyte `subscription_changes` to Fivetran `email_subscription_change`

- Table Match Confidence Score: ⚠️ 0.65

- Table Completion Score: ❌ 0.25

### Evaluation

The table match score indicates a moderate level of confidence that the source and target tables describe similar subject matter. The completion score is low due to multiple 'MISSING' expressions for field mappings, which suggests incomplete mappings.


### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `subscription_changes._airbyte_extracted_at` | 🟢 1.00 | Standard mapping rule applied: '_fivetran_synced' is always mapped to '_airbyte_extracted_at'. No penalty or reward. |
| `caused_by_event_id` | The ID of the event that caused the subscription change. | `MISSING` | ❌ 0.00 | No good match found. |
| `change` | The change which occurred. This enumeration is specific to the 'changeType'; see below for the possible values. | `MISSING` | ❌ 0.00 | No good match found. |
| `change_type` | The type of change which occurred. | `MISSING` | ❌ 0.00 | No good match found. |
| `email_subscription_id` | The ID of the related email subscription. | `MISSING` | ❌ 0.00 | No good match found. |
| `portal_id` | {{ doc("portal_id") }} | `subscription_changes.portalId` | ⚠️ 0.65 | Mapping is considered likely since 'portal_id' matches 'subscription_changes.portalId'. |
| `recipient` | The email address of the related contact. | `subscription_changes.recipient` | ⚠️ 0.65 | Mapping is considered likely since 'recipient' matches 'subscription_changes.recipient'. |
| `source` | The source of the subscription change. | `MISSING` | ❌ 0.00 | No good match found. |
| `timestamp` | The timestamp when this change occurred. If 'causedByEvent' is present, this will be absent. | `subscription_changes.timestamp` | ⚠️ 0.65 | Mapping is considered likely since 'timestamp' matches 'subscription_changes.timestamp'. |

