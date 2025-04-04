# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping: Airbyte `email_events` to Fivetran `email_event`


- Table Match Confidence Score: 🟢 _0.90__
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The table match score is high because the field mappings consistently relate similar data across both schemas. The completion score is also high, reflecting that each field has been thoughtfully mapped with minimal missing data._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping of _fivetran_synced to _airbyte_extracted_at._ |
| `app_id` | The ID of the app that sent the email. | `email_events.appId` | 🟢 _0.90_ | _app_id maps directly to email_events.appId with high confidence due to exact naming and expected context._ |
| `caused_by_created` | The timestamp of the event that caused this event. | `email_events.causedBy.created` | 🟢 _0.90_ | _Field matches email_events.causedBy.created based on context and similar naming structure._ |
| `caused_by_id` | The event ID which uniquely identifies the event which directly caused this event. If not applicable, this property is omitted. | `email_events.causedBy.id` | 🟢 _0.85_ | _Mapping to email_events.causedBy.id, given the context of event causality and ID purpose._ |
| `created` | The created timestamp of the event. | `email_events.created` | 🟢 _0.90_ | _Created timestamp exactly matches email_events.created field._ |
| `email_campaign_id` | The ID of the related email campaign. | `email_events.emailCampaignId` | 🟢 _0.90_ | _Direct match to email_events.emailCampaignId, likely identical due to naming and purpose._ |
| `filtered_event` | A boolean representing whether the event has been filtered out of reporting based on customer reports settings or not. | `email_events.filteredEvent` | 🟢 _0.80_ | _Somewhat clear mapping to email_events.filteredEvent, representing the same filter logic._ |
| `id` | The ID of the event. | `email_events.id` | 🟢 _0.90_ | _Matching event IDs with email_events.id is direct and accurate._ |
| `obsoleted_by_created` | The timestamp of the event that made the current event obsolete. | `email_events.obsoletedBy.created` | 🟢 _0.80_ | _Logically aligns with email_events.obsoletedBy.created; naming suggests a correct match._ |
| `obsoleted_by_id` | The event ID which uniquely identifies the follow-on event which makes this current event obsolete. If not applicable, this property is omitted. | `email_events.obsoletedBy.id` | 🟢 _0.80_ | _Seems to correctly match with email_events.obsoletedBy.id as per the purpose of the field._ |
| `portal_id` | {{ doc("portal_id") }} | `email_events.portalId` | 🟢 _0.85_ | _Likely matches as portal_id is a common field shared across systems, direct naming helps._ |
| `recipient` | The email address of the contact related to the event. | `email_events.recipient` | 🟢 _0.90_ | _Email recipient logically and directly relates to email_events.recipient._ |
| `sent_by_created` | The timestamp of the SENT event related to this event. | `email_events.sentBy.created` | 🟢 _0.85_ | _Sensible mapping with email_events.sentBy.created based on timestamp semantics._ |
| `sent_by_id` | The event ID which uniquely identifies the email message's SENT event. If not applicable, this property is omitted. | `email_events.sentBy.id` | 🟢 _0.85_ | _SentBy ID maps well to email_events.sentBy.id given similar roles in event tracking._ |
| `type` | The type of event. | `email_events.type` | 🟢 _0.90_ | _Event type accurately maps to email_events.type, supported by consistent terminology._ |

### Mapping: Airbyte `deal_pipelines` to Fivetran `deal_pipeline`


- Table Match Confidence Score: 🟢 _1.00__
- Table Completion Score: 🟢 _0.88_
- Summary Self-Evaluation: _All fields were matched with high confidence, except for _fivetran_deleted which was missing a corresponding match._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deal_pipelines._airbyte_extracted_at` | 🟢 _1.00_ | __fivetran_synced is always mapped to _airbyte_extracted_at._ |
| `active` | Whether the stage is currently in use. | `deal_pipelines.active` | 🟢 _1.00_ | _Active state has a direct mapping match in target schema._ |
| `display_order` | Used to determine the order in which the pipelines appear when viewed in HubSpot. | `deal_pipelines.displayOrder` | 🟢 _1.00_ | _Display order is mapped correctly to the target field._ |
| `label` | The human-readable label for the pipeline. The label is used when showing the pipeline in HubSpot. | `deal_pipelines.label` | 🟢 _1.00_ | _Label field matches correctly to target schema._ |
| `pipeline_id` | The ID of the pipeline. | `deal_pipelines.pipelineId` | 🟢 _1.00_ | _Pipeline ID field is correctly matched._ |
| `created_at` | A timestamp representing when the record was created. | `deal_pipelines.createdAt` | 🟢 _1.00_ | _Created at timestamp field is well mapped._ |
| `updated_at` | A timestamp representing when the record was updated. | `deal_pipelines.updatedAt` | 🟢 _1.00_ | _Updated at timestamp field is correctly matched._ |

### Mapping: Airbyte `email_events` to Fivetran `email_event_print`


- Table Match Confidence Score: 🟢 _0.75__
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mapping suggests a strong correlation with email events, commonly found in both source and target schemas. Most fields have been appropriately matched to their equivalents._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping from _fivetran_synced to _airbyte_extracted_at._ |
| `browser` | {{ doc("email_event_browser") }} | `email_events.browser` | 🟢 _0.70_ | _'browser' matched directly from 'email_events.browser', which is likely a direct mapping of user browsing data._ |
| `id` | The ID of the event. | `email_events.id` | ⚠️ _0.65_ | _'id' matched to 'email_events.id', typically an identifier field directly shared between schemas._ |
| `ip_address` | {{ doc("email_event_ip_address") }} | `email_events.ipAddress` | 🟢 _0.70_ | _Direct match of 'ip_address' to 'email_events.ipAddress', common mapping for IP recording._ |
| `location` | {{ doc("email_event_location") }} | `email_events.location` | 🟢 _0.70_ | _Matched 'location' to 'email_events.location', generally indicating the same concept._ |
| `user_agent` | {{ doc("email_event_user_agent") }} | `email_events.userAgent` | ⚠️ _0.65_ | _Directly mapped 'user_agent' to 'email_events.userAgent', reflecting similar user metadata tracking._ |

### Mapping: Airbyte `engagements_emails` to Fivetran `engagement_email`


- Table Match Confidence Score: 🟢 _0.80__
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The table mapping is evaluated with a relatively high confidence due to the presence of standard mappings like `_fivetran_synced` to `_airbyte_extracted_at` and typical fields seen in similar schemas. However, there are fields that exhibit uncertainty, lowering the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_emails._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping of `_fivetran_synced` to `_airbyte_extracted_at`._ |
| `engagement_id` | The ID of the engagement. | `engagements_emails.id` | 🟢 _0.80_ | _Direct mapping with high confidence, common field name indicating unique identifier._ |
| `property_hs_createdate` | This field marks the email's time of creation and determines where the email sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_emails.properties.hs_createdate` | ⚠️ _0.65_ | _Field corresponds to a timestamp, but specific conditions in the description suggest slight differences in data presence._ |
| `timestamp` | This field marks the email's time of occurrence and determines where the email sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_emails.properties_hs_timestamp` | ⚠️ _0.65_ | _Another timestamp field, similar explanation as property_hs_createdate._ |
| `property_hubspot_owner_id` | The ID of the owner associated with the email. This field determines the user listed as the email creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_emails.properties.hubspot_owner_id` | 🟢 _0.70_ | _Likely mapping for owner ID, but conditional existence in description affects confidence._ |
| `property_hubspot_team_id` | The ID of the team associated with the email. This field determines the team listed as the email creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_emails.properties.hubspot_team_id` | 🟢 _0.70_ | _Likely mapping for team ID, but conditional existence in description affects confidence._ |

### Mapping: Airbyte `engagements_notes` to Fivetran `engagement_note`


- Table Match Confidence Score: 🟢 _0.85__
- Table Completion Score: ⚠️ _0.57_
- Summary Self-Evaluation: _The table mapping reflects the same conceptual entity between the source and target. However, one of the field mappings is missing, impacting the completion score. The table map aligns well with data source structures typically shared via similar APIs, thereby achieving a high table match score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_notes._airbyte_extracted_at` | 🟢 _1.00_ | _This is a standard mapping for all tables and is always mapped to '_airbyte_extracted_at'._ |
| `body` | The body of the note. The body has a limit of 65536 characters. | `engagements_notes.properties.hs_note_body` | 🟢 _0.80_ | _The field 'body' maps well to 'hs_note_body' indicating a similar content purpose, thus achieving a high confidence score._ |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `property_hs_createdate` | This field marks the note's time of creation and determines where the note sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_notes.properties.hs_createdate` | 🟢 _0.70_ | _This field marks the note's time of creation; mapped to 'hs_createdate' reflecting likely indiscernible temporal data. Meeting specified criteria._ |
| `timestamp` | This field marks the note's time of occurrence and determines where the note sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_notes.properties.hs_timestamp` | 🟢 _0.70_ | _This field marks the note's time of occurrence; mapped to 'hs_timestamp', aligns contextually similar to creation date._ |
| `property_hubspot_owner_id` | The ID of the owner associated with the note. This field determines the user listed as the note creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_notes.properties.hubspot_owner_id` | 🟢 _0.70_ | _Reflects ownership of the note, aligning contextually with 'hubspot_owner_id', maintaining entity tracking consistency._ |
| `property_hubspot_team_id` | The ID of the team associated with the note. This field determines the team listed as the note creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_notes.properties.hubspot_team_id` | 🟢 _0.70_ | _Reflects team ownership of the note, aligning consistently with 'hubspot_team_id', reinforcing entity clarity._ |

### Mapping: Airbyte `email_events` to Fivetran `email_event_delivered`


- Table Match Confidence Score: 🟢 _0.90__
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mappings are likely to be very similar due to shared API origins. However, the completion score reflects the slight differences in implementations._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping to _airbyte_extracted_at, which is always a perfect match._ |
| `id` | The ID of the event. | `email_events.id` | 🟢 _0.80_ | _The ID field is likely to be similar, but due to potential differing usages across systems, a score of 0.8 is appropriate._ |
| `response` | The full response from the recipient's email server. | `email_events.response` | 🟢 _0.70_ | _The response field is matched based on the content expected; however, different systems might use different levels of detail or format._ |
| `smtp_id` | An ID attached to the message by HubSpot. | `email_events.smtpId` | 🟢 _0.75_ | _This ID corresponds to a message-specific identifier used in email systems, and matches are likely but not guaranteed to be identical._ |

### Mapping: Airbyte `companies` to Fivetran `company`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: 🟢 _0.86_
- Summary Self-Evaluation: _Table match confidence is reasonably high, considering the target schema's table fields are closely matched with source fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `companies._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping for all tables._ |
| `id` | The ID of the company. | `companies.id` | 🟢 _1.00_ | _Exact match found with the corresponding source field._ |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `is_deleted` | {{ doc("is_deleted") }} | `companies.archived` | 🟢 _0.70_ | _Matches a logical field in the source schema._ |
| `property_name` | The name of the company. | `companies.properties.name` | 🟢 _1.00_ | _Exact match found with the source field._ |
| `property_description` | A short statement about the company's mission and goals. | `companies.properties.description` | 🟢 _1.00_ | _Exact match found based on description._ |
| `property_createdate` | The date the company was added to your account. | `companies.properties.createdate` | 🟢 _1.00_ | _Exact match found based on purpose._ |
| `property_industry` | The type of business the company performs. | `companies.properties.industry` | 🟢 _1.00_ | _Exact match found for describing business type._ |
| `property_address` | The street address of the company. | `companies.properties.address` | 🟢 _1.00_ | _Exact match found for street address._ |
| `property_address_2` | Additional address information for the company. | `companies.properties.address2` | 🟢 _1.00_ | _Matches additional address information._ |
| `property_city` | The city where the company is located. | `companies.properties.city` | 🟢 _1.00_ | _Exact match found for city location._ |
| `property_state` | The state where the company is located. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `property_country` | The country where the company is located. | `companies.properties.country` | 🟢 _1.00_ | _Exact match found for country location._ |
| `property_annualrevenue` | The actual or estimated annual revenue of the company. | `companies.properties.annualrevenue` | 🟢 _1.00_ | _Exact match found for annual revenue._ |

### Mapping: Airbyte `contacts_list_memberships` to Fivetran `contact_list_member`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table mappings suggest a moderate confidence that the source and target tables describe similar subjects. The completion score indicates that some fields are well-mapped, but others are missing mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_list_memberships._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping for all tables._ |
| `added_at` | The timestamp a contact was added to a list. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `contact_id` | The ID of the related contact. | `contacts_list_memberships.vid` | 🟢 _0.70_ | _Good match with 'contacts_list_memberships.vid'._ |
| `contact_list_id` | The ID of the related contact list. | `contacts_list_memberships.static_list_id` | 🟢 _0.70_ | _Good match with 'contacts_list_memberships.static_list_id'._ |

### Mapping: Airbyte `engagements_meetings` to Fivetran `engagement_meeting`


- Table Match Confidence Score: 🟢 _0.80__
- Table Completion Score: 🟢 _0.67_
- Summary Self-Evaluation: _The table mapping is of high quality due to the good alignment between source and target tables. However, the completion score is lower due to one missing field mapping and some field-level uncertainty._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_meetings._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping for all tables. Mapped '_fivetran_synced' to source stream's '_airbyte_extracted_at' column._ |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `property_hs_createdate` | This field marks the meeting's time of creation and determines where the meeting sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_meetings.properties_hs_createdate` | 🟢 _0.70_ | _The expression shows a direct alignment although with slight contextual uncertainties._ |
| `timestamp` | This field marks the meeting's time of occurrence and determines where the meeting sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_meetings.properties_hs_timestamp` | 🟢 _0.70_ | _The expression shows a direct alignment although with slight contextual uncertainties._ |
| `property_hubspot_owner_id` | The ID of the owner associated with the meeting. This field determines the user listed as the meeting creator on the record timeline.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_meetings.properties_hubspot_owner_id` | 🟢 _0.70_ | _The expression shows a direct alignment although with slight contextual uncertainties._ |
| `property_hubspot_team_id` | The ID of the team associated with the meeting. This field determines the team listed as the meeting creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_meetings.properties_hubspot_team_id` | 🟢 _0.70_ | _The expression shows a direct alignment although with slight contextual uncertainties._ |

### Mapping: Airbyte `engagements_tasks` to Fivetran `engagement_task`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: 🟢 _0.83_
- Summary Self-Evaluation: _The table mapping uses similar source and target models with high confidence. However, one field expression is missing, reducing the overall completion._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_tasks._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping for '_fivetran_synced' to '_airbyte_extracted_at' with perfect confidence._ |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `property_hs_createdate` | This field marks the task's time of creation and determines where the task sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_tasks.properties_hs_createdate` | 🟢 _0.70_ | _Mapping is likely correct based on similar meaning of creation date fields._ |
| `timestamp` | This field marks the task's time of occurrence and determines where the task sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_tasks.properties_hs_timestamp` | 🟢 _0.70_ | _Mapping matches timestamp meaning, considering API version context._ |
| `property_hubspot_owner_id` | The ID of the owner associated with the task. This field determines the user listed as the task creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_tasks.properties_hubspot_owner_id` | 🟢 _0.70_ | _Mapping likely correct for owner linkage based on API versioning details._ |
| `property_hubspot_team_id` | The ID of the team associated with the task. This field determines the team listed as the task creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_tasks.properties_hubspot_team_id` | 🟢 _0.70_ | _Mapping likely correct for team linkage given API versioning restrictions._ |

### Mapping: Airbyte `tickets` to Fivetran `ticket`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: 🟢 _0.93_
- Summary Self-Evaluation: _The table mapping was evaluated with a high level of confidence due to significant field coverage and strong matching logic between the two systems, despite minor imperfect mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `tickets._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping directly from the source's `_airbyte_extracted_at` column._ |
| `id` | ID of the ticket. | `tickets.id` | 🟢 _0.80_ | _Direct match with `tickets.id`, indicating strong correspondence between source and target hierarchy._ |
| `is_deleted` | Whether the record was deleted (v2 endpoint). | `tickets.archived` | 🟢 _0.70_ | _Mapped to `tickets.archived`, which likely indicates a similar field purpose._ |
| `_fivetran_deleted` | Whether the record was deleted (v3 endpoint). | `tickets.archived` | 🟢 _0.70_ | _Also mapped to `tickets.archived`, showing another potential logical mapping._ |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `property_closed_date` | The date the ticket was closed. | `tickets.properties.closed_date` | 🟢 _0.90_ | _Mapped to `tickets.properties.closed_date`, indicating direct mapping with proper context._ |
| `property_createdate` | The date the ticket was created. | `tickets.properties_createdate` | 🟢 _0.90_ | _Mapped to `tickets.properties_createdate` with apparent logical equivalence and context correctness._ |
| `property_first_agent_reply_date` | the date for the first agent reply on the ticket. | `tickets.properties_first_agent_reply_date` | 🟢 _0.90_ | _Mapped to `tickets.properties_first_agent_reply_date`, indicating a clear logical match._ |
| `property_hs_pipeline` | The ID of the ticket's pipeline. | `tickets.properties.hs_pipeline` | 🟢 _0.90_ | _Mapped to `tickets.properties.hs_pipeline`, a logical match confirming field integrity._ |
| `property_hs_pipeline_stage` | The ID of the ticket's pipeline stage. | `tickets.properties.hs_pipeline_stage` | 🟢 _0.90_ | _Corresponds directly to `tickets.properties.hs_pipeline_stage`, with strong contextual alignment._ |
| `property_hs_ticket_priority` | The priority of the ticket. | `tickets.properties.hs_ticket_priority` | 🟢 _0.90_ | _Aligned with `tickets.properties.hs_ticket_priority`, serving an identical purpose._ |
| `property_hs_ticket_category` | The category of the ticket. | `tickets.properties.hs_ticket_category` | 🟢 _0.90_ | _Mapped identically to `tickets.properties.hs_ticket_category` with contextual accuracy._ |
| `property_hubspot_owner_id` | The ID of the deal's owner. | `tickets.properties_hubspot_owner_id` | 🟢 _0.90_ | _Mapped to `tickets.properties_hubspot_owner_id`, reflecting identical field usage._ |
| `property_subject` | Short summary of ticket. | `tickets.properties.subject` | 🟢 _0.90_ | _Mapped to `tickets.properties.subject`, demonstrating a strong match._ |
| `property_content` | Text in body of the ticket. | `tickets.properties.content` | 🟢 _0.90_ | _Mapped correctly to `tickets.properties.content`, supporting the mapping's validity._ |

### Mapping: Airbyte `email_subscriptions` to Fivetran `email_subscription`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _Table mapping between the source and target is a strong match due to alignment of fields and standardized mappings. Completion score is perfect as all required fields are mapped._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_subscriptions._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping to '_airbyte_extracted_at' with full confidence._ |
| `active` | Whether the subscription is active. | `email_subscriptions.active` | 🟢 _0.70_ | _Mapped to a field with a closely matching name and plausible function._ |
| `description` | The description of the subscription. | `email_subscriptions.description` | 🟢 _0.70_ | _Mapped to a field with a closely matching name and plausible function._ |
| `id` | The ID of the email subscription. | `email_subscriptions.id` | 🟢 _0.70_ | _Mapped to a field with a closely matching name and plausible function._ |
| `name` | The name of the email subscription. | `email_subscriptions.name` | 🟢 _0.70_ | _Mapped to a field with a closely matching name and plausible function._ |
| `portal_id` | {{ doc("portal_id") }} | `email_subscriptions.portalId` | 🟢 _0.70_ | _Mapped to a field with a closely matching name and plausible function._ |

### Mapping: Airbyte `contacts` to Fivetran `contact`


- Table Match Confidence Score: 🟢 _0.85__
- Table Completion Score: 🟢 _0.91_
- Summary Self-Evaluation: _The mapping is generally strong, showing a high level of confidence that the target schema fields align with the source fields. The completion is high, indicating most source fields have corresponding target fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts._airbyte_extracted_at` | 🟢 _1.00_ | __fivetran_synced perfectly maps to contacts._airbyte_extracted_at._ |
| `id` | The ID of the contact. | `contacts.id` | 🟢 _1.00_ | _The 'id' field perfectly matches the target schema._ |
| `property_email_1` | The email address of the contact. | `contacts.properties_email` | 🟢 _0.70_ | _Partial match with some uncertainty due to potential overlapping with similar fields._ |
| `property_company` | The name of the contact's company. | `contacts.properties_company` | 🟢 _1.00_ | _The 'company' field is clearly matched._ |
| `property_firstname` | The contact's first name. | `contacts.properties_firstname` | 🟢 _1.00_ | _The 'first name' field is correctly aligned._ |
| `property_lastname` | The contact's last name. | `contacts.properties_lastname` | 🟢 _1.00_ | _The 'last name' field is correctly aligned._ |
| `property_email` | The contact's email. | `contacts.properties_email` | 🟢 _0.70_ | _Partial match with some uncertainty due to potential duplicate mappings._ |
| `property_createdate` | The date that the contact was created in your HubSpot account. | `contacts.properties_createdate` | 🟢 _1.00_ | _Creation date field matches perfectly._ |
| `property_jobtitle` | The contact's job title. | `contacts.properties_jobtitle` | 🟢 _1.00_ | _The 'job title' field is well matched._ |
| `property_annualrevenue` | The contact's annual company revenue. | `contacts.properties_annualrevenue` | 🟢 _1.00_ | _Annual revenue field is an exact match._ |
| `property_hs_calculated_merged_vids` | List of mappings representing contact IDs that have been merged into the contact at hand. Format: <merged_contact_id>:<merged_at_in_epoch_time>;<second_merged_contact_id>:<merged_at_in_epoch_time> This field has replaced the `CONTACT_MERGE_AUDIT` table, which was deprecated by the Hubspot v3 CRM API.  | `contacts.properties_hs_calculated_merged_vids` | ⚠️ _0.65_ | _Field partially matched with high confidence for underlying meaning, but lacking precise mapping._ |

### Mapping: Airbyte `contacts_merged_audit` to Fivetran `contact_merge_audit`


- Table Match Confidence Score: 🟢 _0.85__
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The source and target tables are highly likely describing the same subject matter since the fields have meaningful mappings. However, there's a missing match affecting the completion score slightly._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_merged_audit._airbyte_extracted_at` | 🟢 _1.00_ | __fivetran_synced is perfectly mapped to _airbyte_extracted_at as per standard convention._ |
| `canonical_vid` | The contact ID of the contact which the vid_to_merge contact was merged into. | `contacts_merged_audit.canonical_vid` | 🟢 _0.90_ | _The contact ID canonical_vid matches strongly to a similar ID field, indicating a high confidence._ |
| `contact_id` | The ID of the contact. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `entity_id` | The ID of the related entity. | `contacts_merged_audit.entity_id` | 🟢 _0.80_ | _entity_id has a reasonable match with fields in the target schema that relate to entities._ |
| `first_name` | The contact's first name. | `contacts_merged_audit.first_name` | 🟢 _0.80_ | _The first name field aligns well with a similarly purposed field in the target schema._ |
| `last_name` | The contact's last name. | `contacts_merged_audit.last_name` | 🟢 _0.80_ | _The last name field aligns well with a similarly purposed field in the target schema._ |
| `num_properties_moved` | The number of properties which were removed from the merged contact. | `contacts_merged_audit.num_properties_moved` | 🟢 _0.70_ | _The field num_properties_moved relates closely to a count of properties, suggesting reasonable confidence._ |
| `timestamp` | Timestamp of when the contacts were merged. | `contacts_merged_audit.timestamp` | 🟢 _0.85_ | _The timestamp field is a direct match with a similarly intended field in the target._ |
| `user_id` | The ID of the user. | `contacts_merged_audit.user_id` | 🟢 _0.70_ | _user_id matches a user-related field sufficiently, though not perfectly._ |
| `vid_to_merge` | The ID of the contact which was merged. | `contacts_merged_audit.vid_to_merge` | 🟢 _0.90_ | _The field vid_to_merge has a strong correlation with a similar structure in the target._ |

### Mapping: Airbyte `owners` to Fivetran `owner`


- Table Match Confidence Score: 🟢 _0.90__
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The mappings are largely appropriate for the given context with `_fivetran_synced` mapping perfectly, but there are unknown fields marked as 'MISSING'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `owners._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping for '_fivetran_synced' to '_airbyte_extracted_at'._ |
| `created_at` | A timestamp for when the owner was created. | `owners.createdAt` | 🟢 _0.90_ | _High confidence match with 'owners.createdAt' given the context._ |
| `email` | The email address of the owner. | `owners.email` | 🟢 _0.90_ | _High confidence match with 'owners.email' based on field name and context._ |
| `first_name` | The first name of the owner. | `owners.firstName` | 🟢 _0.90_ | _High confidence match with 'owners.firstName' due to similar naming and context._ |
| `last_name` | The last name of the owner. | `owners.lastName` | 🟢 _0.90_ | _High confidence match with 'owners.lastName' based on context similarity._ |
| `owner_id` | The ID of the owner. | `owners.userId` | 🟢 _0.90_ | _High confidence that 'owner_id' and 'owners.userId' refer to the same entity._ |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `type` | The type of owner. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `updated_at` |  | `owners.updatedAt` | 🟢 _0.90_ | _High confidence in matching 'owners.updatedAt' with 'updated_at'._ |

### Mapping: Airbyte `contacts_form_submissions` to Fivetran `contact_form_submission`


- Table Match Confidence Score: 🟢 _0.80__
- Table Completion Score: 🟢 _0.88_
- Summary Self-Evaluation: _The table match confidence is high due to the presence of common fields in the source and target tables, such as conversion_id and form_id, which are indicative of form submissions. However, the completion is partly reduced as a result of a 'MISSING' field and some other mapped fields having a close match score instead of perfect._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_form_submissions._airbyte_extracted_at` | 🟢 _1.00_ | _The field '_fivetran_synced' is correctly mapped to '_airbyte_extracted_at' as per standard mapping rules._ |
| `contact_id` | The ID of the related contact. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `conversion_id` | A Unique ID for the specific form conversion. | `contacts_form_submissions.conversion_id` | 🟢 _0.70_ | _Close confidence since 'conversion_id' appears to match correctly with the source._ |
| `form_id` | The GUID of the form that the submission belongs to. | `contacts_form_submissions.form_id` | 🟢 _0.70_ | _Reasonable confidence as 'form_id' corresponds within the submission context._ |
| `page_url` | The URL that the form was submitted on, if applicable. | `contacts_form_submissions.canonical_url` | 🟢 _0.70_ | _Matches with 'canonical_url' reasonably well for a form submission context._ |
| `portal_id` | {{ doc("portal_id") }} | `contacts_form_submissions.portal_id` | 🟢 _0.70_ | _Field 'portal_id' mapped with standard naming conventions._ |
| `timestamp` | A Unix timestamp in milliseconds of the time the submission occurred. | `contacts_form_submissions.timestamp` | 🟢 _0.70_ | _Field 'timestamp' appears to match the context of form submission times._ |
| `title` | The title of the page that the form was submitted on. This will default to the name of the form if no title is provided. | `contacts_form_submissions.page_title` | 🟢 _0.70_ | _Field 'title' matches the common context in form submission metadata._ |

### Mapping: Airbyte `deals_property_history` to Fivetran `deal_property_history`


- Table Match Confidence Score: 🟢 _0.72__
- Table Completion Score: 🟢 _0.86_
- Summary Self-Evaluation: _The table match score is relatively high, indicating a good match between source and target tables based on similar schema elements. However, one field has an expression marked as 'MISSING', lowering the completion score due to incomplete mapping._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deals_property_history._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping for _fivetran_synced to _airbyte_extracted_at._ |
| `deal_id` | The ID of the related deal record. | `deals_property_history.dealId` | 🟢 _0.70_ | _dealId from deals_property_history is likely to match deal_id based on naming and context._ |
| `name` | {{ doc("history_name") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `source` | {{ doc("history_source") }} | `deals_property_history.sourceType` | 🟢 _0.70_ | _sourceType from deals_property_history matches source based on name and typical usage._ |
| `source_id` | {{ doc("history_source_id") }} | `deals_property_history.sourceId` | 🟢 _0.70_ | _sourceId from deals_property_history matches source_id based on naming similarities._ |
| `timestamp` | {{ doc("history_timestamp") }} | `deals_property_history.timestamp` | 🟢 _0.70_ | _timestamp from deals_property_history matches timestamp based on naming conventions._ |
| `value` | {{ doc("history_value") }} | `deals_property_history.value` | 🟢 _0.70_ | _value from deals_property_history matches value, typical mapping based on name._ |

### Mapping: Airbyte `engagements` to Fivetran `engagement`


- Table Match Confidence Score: 🟢 _0.85__
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table mapping shows high match quality with a strong correspondence between most fields. However, some fields from the source schema could not be mapped to the target schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping from '_fivetran_synced' to '_airbyte_extracted_at'._ |
| `active` | Whether the engagement is currently being shown in the UI.  PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.active` | ⚠️ _0.60_ | _Mapped to 'engagements.active' with moderate confidence._ |
| `created_at` | A timestamp representing when the engagement was created.  PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.createdAt` | ⚠️ _0.60_ | _Mapped to 'engagements.createdAt' with moderate confidence._ |
| `id` | The ID of the engagement. | `engagements.id` | 🟢 _0.70_ | _Mapped to 'engagements.id', high confidence due to clear correspondence._ |
| `owner_id` | The ID of the engagement's owner. PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.ownerId` | ⚠️ _0.60_ | _Mapped to 'engagements.ownerId' with moderate confidence._ |
| `portal_id` | {{ doc("portal_id") }} | `engagements.portalId` | ⚠️ _0.60_ | _Mapped to 'engagements.portalId' with moderate confidence._ |
| `timestamp` | A timestamp in representing the time that the engagement should appear in the timeline. PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.timestamp` | ⚠️ _0.60_ | _Mapped to 'engagements.timestamp' with moderate confidence._ |
| `type` | One of NOTE, EMAIL, TASK, MEETING, or CALL, the type of the engagement. | `engagements.type` | 🟢 _0.70_ | _Mapped to 'engagements.type', high confidence due to distinct field type categories._ |

### Mapping: Airbyte `companies_property_history` to Fivetran `company_property_history`


- Table Match Confidence Score: 🟢 _0.80__
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table match is strong due to the consistent naming and field availability between the source and target. All fields have been mapped with high confidence except for any potential 'MISSING' fields, which slightly lowers the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `companies_property_history._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at'._ |
| `company_id` | The ID of the related company record. | `companies_property_history.companyId` | 🟢 _0.95_ | _High confidence mapping based on consistent naming and usage._ |
| `name` | {{ doc("history_name") }} | `companies_property_history.properties.name` | 🟢 _0.70_ | _Reasonable match based on naming convention and context._ |
| `source` | {{ doc("history_source") }} | `companies_property_history.sourceType` | 🟢 _0.70_ | _Reasonable match based on naming convention and context._ |
| `source_id` | {{ doc("history_source_id") }} | `companies_property_history.sourceId` | 🟢 _0.70_ | _Reasonable match based on naming convention and context._ |
| `timestamp` | {{ doc("history_timestamp") }} | `companies_property_history.timestamp` | 🟢 _0.95_ | _High confidence due to common timestamp usage across schemas._ |
| `value` | {{ doc("history_value") }} | `companies_property_history.value` | 🟢 _0.85_ | _Strong match supported by consistent usage across data sources._ |

## Workshop Models

These models are in the workshop directory and are not yet approved.

### Mapping: Airbyte `contacts_property_history` to Fivetran `contact_property_history`


- Table Match Confidence Score: ⚠️ _0.60__
- Table Completion Score: ❌ _0.43_
- Summary Self-Evaluation: _The mapping involves 7 fields, out of which 4 had direct matches. However, 3 fields are marked as 'MISSING', significantly reducing the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_property_history._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping for '_fivetran_synced' to source stream's '_airbyte_extracted_at'._ |
| `contact_id` | The ID of the related contact record. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `name` | {{ doc("history_name") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `source` | {{ doc("history_source") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `source_id` | {{ doc("history_source_id") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `timestamp` | {{ doc("history_timestamp") }} | `contacts_property_history.timestamp` | 🟢 _0.70_ | _Reasonable confidence that 'contacts_property_history.timestamp' is the correct mapping._ |
| `value` | {{ doc("history_value") }} | `contacts_property_history.value` | 🟢 _0.70_ | _Reasonable confidence that 'contacts_property_history.value' is the correct mapping._ |

### Mapping: Airbyte `forms` to Fivetran `form`


- Table Match Confidence Score: 🟢 _0.90__
- Table Completion Score: 🟢 _0.69_
- Summary Self-Evaluation: _The table mapping score is high because the tables share many common fields, indicating they likely describe similar subjects. However, the completion score is lower due to several fields mapped as 'MISSING'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `forms._airbyte_extracted_at` | 🟢 _1.00_ | _Consistently maps to '_airbyte_extracted_at'._ |
| `created_at` | A timestamp for when the form was created. | `forms.createdAt` | 🟢 _0.80_ | _Mapped to a corresponding timestamp for creation within forms._ |
| `css_class` | The CSS classes assigned to the form. | `forms.displayOptions.cssClass` | 🟢 _0.70_ | _Assigned CSS classes are mapped to a similarly structured path._ |
| `follow_up_id` | This field is no longer used. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `guid` | The internal ID of the form. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `lead_nurturing_campaign_id` | TBD | `forms.properties.hs_marketing_campaign_guid` | ⚠️ _0.60_ | _Mapping to a marketing campaign GUID is a possible but uncertain match._ |
| `method` | This field is no longer used. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `name` | The name of the form. | `forms.name` | 🟢 _0.90_ | _Mapped directly to the form's name, indicating a strong match._ |
| `notify_recipients` | A comma-separated list of user IDs that should receive submission notifications. Email addresses will be returned for individuals who aren't users.  | `forms.configuration.notifyRecipients` | 🟢 _0.80_ | _Correctly identifies a list of user IDs for notifications within the forms._ |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `redirect` | The URL that the visitor will be redirected to after filling out the form. | `forms.configuration.postSubmitAction.value` | 🟢 _0.80_ | _Mapped to a post-submit URL, reflecting the described functionality._ |
| `submit_text` | The text used for the submit button. | `forms.displayOptions.submitButtonText` | 🟢 _0.70_ | _Submit button text mapping aligns with function._ |
| `updated_at` | A timestamp for when the form was last updated. | `forms.updatedAt` | 🟢 _0.80_ | _Mapped to a corresponding timestamp for updates within forms._ |

### Mapping: Airbyte `contact_lists` to Fivetran `contact_list`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table match is relatively strong due to shared data origin (API), but not all fields are present in the source._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contact_lists._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping to source stream's '_airbyte_extracted_at' column._ |
| `created_at` | A timestamp of the time the list was created. | `contact_lists.createdAt` | 🟢 _0.90_ | _Timestamps align well between 'createdAt' and 'created_at'._ |
| `id` | The ID of the contact list. | `contact_lists.listId` | 🟢 _0.90_ | _IDs align well between 'listId' and 'id'._ |
| `name` | The name of the contact list. | `contact_lists.name` | 🟢 _0.90_ | _Names align between 'name' and 'name'._ |
| `updated_at` | A timestamp of the time that the list was last modified. | `contact_lists.updatedAt` | 🟢 _0.90_ | _Timestamps align well between 'updatedAt' and 'updated_at'._ |
| `created_by_id` | The unique identifier of the user who created the contact list. | `contact_lists.authorId` | 🟢 _0.80_ | _Good match between 'authorId' and 'created_by_id'._ |
| `object_type_id` | The ID that corresponds to the type of object stored by the list. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `processing_status` | Indicates the current status of the list's processing, such as 'COMPLETE', 'PROCESSING', 'DONE', or 'FAILED'. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `processing_type` | Specifies the type of processing applied to the list, for example, 'STATIC' for static lists or 'DYNAMIC' for dynamic lists. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `list_version` | Represents the version number of the list, incrementing with each modification. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `filters_updated_at` | The timestamp indicating when the list's filters were last updated. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `metadata_error` | Any errors that happened the last time the list was processed.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData_error` | 🟢 _0.70_ | _Deprecation notice: field may not be populated in future._ |
| `metadata_last_processing_state_change_at` | A timestamp of the last time that the processing state changed.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData_lastProcessingStateChangeAt` | 🟢 _0.70_ | _Deprecation notice: field may not be populated in future._ |
| `metadata_last_size_change_at` | A timestamp of the last time that the size of the list changed.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData_lastSizeChangeAt` | 🟢 _0.70_ | _Deprecation notice: field may not be populated in future._ |
| `metadata_processing` | One of DONE, REFRESHING, INITIALIZING, or PROCESSING. DONE indicates the list has finished processing, any other value indicates that list membership is being evaluated. NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData_processing` | 🟢 _0.70_ | _Deprecation notice: field may not be populated in future._ |
| `metadata_size` | The approximate number of contacts in the list. NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData_size` | 🟢 _0.70_ | _Deprecation notice: field may not be populated in future._ |
| `portal_id` | '{{ doc("portal_id") }}' NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.portalId` | 🟢 _0.70_ | _Deprecation notice: field may not be populated in future._ |
| `deleteable` | If this is false, this is a system list and cannot be deleted.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.deleteable` | 🟢 _0.70_ | _Deprecation notice: field may not be populated in future._ |
| `dynamic` | Whether the contact list is dynamic. NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.dynamic` | 🟢 _0.70_ | _Deprecation notice: field may not be populated in future._ |

### Mapping: Airbyte `ticket_pipelines` to Fivetran `ticket_pipeline`


- Table Match Confidence Score: ⚠️ _0.65__
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table and field mappings include several 'MISSING' entries, indicating incomplete mapping. However, certain fields like '_fivetran_synced' have confident mappings based on standard conventions. Moreover, fields like 'display_order', 'label', 'created_at', and 'updated_at' have plausible mappings, albeit with less confidence due to lack of complete corroboration across source and target schemas._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `ticket_pipelines._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping to '_airbyte_extracted_at' column._ |
| `active` | Boolean indicating whether the pipeline is active. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `display_order` | Used to determine the order in which the stages appear when viewed in HubSpot. | `ticket_pipelines.displayOrder` | ⚠️ _0.65_ | _Mapped to 'ticket_pipelines.displayOrder', indicating similar intents._ |
| `label` | The human-readable label for the stage. The label is used when showing the stage in HubSpot. | `ticket_pipelines.label` | ⚠️ _0.65_ | _Mapped to 'ticket_pipelines.label', indicating similar intents._ |
| `object_type_id` | Reference to the object type. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `pipeline_id` | Reference to the pipeline. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `created_at` | A timestamp representing when the record was created. | `ticket_pipelines.createdAt` | ⚠️ _0.65_ | _Timestamp mapped to 'ticket_pipelines.createdAt', consistent with documentation._ |
| `updated_at` | A timestamp representing when the record was updated. | `ticket_pipelines.updatedAt` | ⚠️ _0.65_ | _Timestamp mapped to 'ticket_pipelines.updatedAt', consistent with documentation._ |

### Mapping: Airbyte `engagements_calls` to Fivetran `engagement_call`


- Table Match Confidence Score: 🟢 _0.80__
- Table Completion Score: ❌ _0.43_
- Summary Self-Evaluation: _The table match score is relatively high due to the commonality in the API usage and consistent field naming conventions between source and target schemas. However, the completion score is low due to missing expressions in key fields, which significantly impacts the ability to map data comprehensively._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_calls._airbyte_extracted_at` | 🟢 _1.00_ | __fivetran_synced is mapped to a source stream's _airbyte_extracted_at column, which is a standard mapping._ |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `_fivetran_deleted` | Boolean to mark rows that were deleted in the source database. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `property_hs_createdate` | This field marks the call's time of creation and determines where the call sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_calls.properties.hs_createdate` | 🟢 _0.70_ | _This field has a fairly direct matching in the source properties._ |
| `timestamp` | This field marks the call's time of occurrence and determines where the call sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `property_hubspot_owner_id` | The ID of the owner associated with the call. This field determines the user listed as the call creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_calls.properties.hubspot_owner_id` | 🟢 _0.70_ | _This field has a moderate confidence match based on the HubSpot API version context._ |
| `property_hubspot_team_id` | The ID of the team associated with the call. This field determines the team listed as the call creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_calls.properties.hubspot_team_id` | 🟢 _0.70_ | _This field has a moderate confidence match based on the HubSpot API version context._ |

### Mapping: Airbyte `deals` to Fivetran `deal`


- Table Match Confidence Score: 🟢 _0.75__
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The table mapping reflects a generally good match between source and target tables, as most fields are correctly mapped. However, there are a few fields that could not be matched and are marked as 'MISSING', which affects completion._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `deal_id` | The ID of the deal. | `deals.properties.hs_object_id` | 🟢 _0.90_ | _Matched field 'deal_id' confidently._ |
| `is_deleted` | Whether the record was deleted. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `deal_pipeline_id` | The ID of the deal's pipeline. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `deal_pipeline_stage_id` | The ID of the deal's pipeline stage. | `deals.properties.dealstage` | 🟢 _0.85_ | _Matched field 'deal_pipeline_stage_id' confidently._ |
| `owner_id` | The ID of the deal's owner. | `deals.properties_hubspot_owner_id` | 🟢 _0.85_ | _Matched field 'owner_id' confidently._ |
| `property_dealname` | The name you have given this deal. | `deals.properties.dealname` | 🟢 _0.90_ | _Matched field 'property_dealname' confidently._ |
| `property_description` | A brief description of the deal. | `deals.properties.description` | 🟢 _0.90_ | _Matched field 'property_description' confidently._ |
| `property_amount` | The total value of the deal in the deal's currency. | `deals.properties.amount` | 🟢 _0.90_ | _Matched field 'property_amount' confidently._ |
| `property_closedate` | The day the deal is expected to close, or was closed. | `deals.properties.closedate` | 🟢 _0.90_ | _Matched field 'property_closedate' confidently._ |
| `property_createdate` | The date the deal was created. This property is set automatically by HubSpot. | `deals.properties.createdate` | 🟢 _0.90_ | _Matched field 'property_createdate' confidently._ |

### Mapping: Airbyte `subscription_changes` to Fivetran `email_subscription_change`


- Table Match Confidence Score: ⚠️ _0.65__
- Table Completion Score: ❌ _0.25_
- Summary Self-Evaluation: _The table match score indicates a moderate level of confidence that the source and target tables describe similar subject matter. The completion score is low due to multiple 'MISSING' expressions for field mappings, which suggests incomplete mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `subscription_changes._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping rule applied: '_fivetran_synced' is always mapped to '_airbyte_extracted_at'. No penalty or reward._ |
| `caused_by_event_id` | The ID of the event that caused the subscription change. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `change` | The change which occurred. This enumeration is specific to the 'changeType'; see below for the possible values. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `change_type` | The type of change which occurred. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `email_subscription_id` | The ID of the related email subscription. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `portal_id` | {{ doc("portal_id") }} | `subscription_changes.portalId` | ⚠️ _0.65_ | _Mapping is considered likely since 'portal_id' matches 'subscription_changes.portalId'._ |
| `recipient` | The email address of the related contact. | `subscription_changes.recipient` | ⚠️ _0.65_ | _Mapping is considered likely since 'recipient' matches 'subscription_changes.recipient'._ |
| `source` | The source of the subscription change. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `timestamp` | The timestamp when this change occurred. If 'causedByEvent' is present, this will be absent. | `subscription_changes.timestamp` | ⚠️ _0.65_ | _Mapping is considered likely since 'timestamp' matches 'subscription_changes.timestamp'._ |
