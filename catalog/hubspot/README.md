# Mapping Guide: Airbyte-to-Fivetran

The below guide will help you map Airbyte schemas to corresponding Fivetran schemas. Guidance is AI-generated and includes confidence scores (with explanation) for each table and field mapping.

## Companion Project for `dbt` Users

Please see the companion [airbyte-interop-dbt-project](./airbyte-interop-dbt-project) directory, which contains a `dbt` project with ready-to-use SQL models for each of the below mappings.

## Table-Level Mappings

### How to Use these Mappings

The below guides, and the companion dbt project, will help you shape your new Airbyte datasets to more closely match your legacy Fivetran dataset schemas.

This can be helpful if:

1. You have existing code that relies on Fivetran-shaped datasets.
2. You have one or more dependencies on Fivetran-managed dbt packages.
3. You have custom code that needs to be updated to leverage Airbyte data schemas, where you previously ingested Fivetran-shaped datasets.

In any of these cases, you can use the below mapping logic to shape your new data to fit old data schema requirements and **save time** in your migration.

> ![Tip]
> Use the right-hand navigation to quickly browse available dataset mappings.

> ![Warning]
> AI-generated results may contain errors. Please sanity check results and adapt these resources to your needs accordingly.


### Mapping: Airbyte `contacts_property_history` to Fivetran `contact_property_history`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.86_
- Summary Self-Evaluation: _The source and target tables share the same subject matter, though not all fields are mapped due to some fields set to 'MISSING'. The '_fivetran_synced' to '_airbyte_extracted_at' mapping is correctly identified._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_property_history._airbyte_extracted_at` | 🟢 _1.00_ | *This is a standard mapping and is always correct.* |
| `contact_id` | The ID of the related contact record. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | {{ doc("history_name") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `source` | {{ doc("history_source") }} | `contacts_property_history.source_type` | 🟢 _0.90_ | *Direct match across schemas.* |
| `source_id` | {{ doc("history_source_id") }} | `contacts_property_history.source_id` | 🟢 _0.90_ | *Direct match across schemas.* |
| `timestamp` | {{ doc("history_timestamp") }} | `contacts_property_history.timestamp` | 🟢 _0.90_ | *Direct match across schemas.* |
| `value` | {{ doc("history_value") }} | `contacts_property_history.value` | 🟢 _0.90_ | *Direct match across schemas.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_click`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table mapping has a high confidence score for matching the source and target tables, reflecting the good correlation in the context of shared upstream source APIs from Airbyte and Fivetran. The completion score indicates a substantial but not full serialization of fields, relevant to the careful mapping of each field while considering differences in terms like singular vs plural and casing._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *This is a standard mapping, always matching Airbyte's '_airbyte_extracted_at' column to Fivetran's '_fivetran_synced' field. Score is thus perfect.* |
| `browser` | {{ doc("email_event_browser") }} | `email_events.browser` | 🟢 _0.90_ | *Direct mapping of 'email_events.browser' which correctly reflects the field's meaning and format without deviation.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _0.90_ | *Relevant direct column mapping from 'email_events.id' with clear identity preservation.* |
| `ip_address` | {{ doc("email_event_ip_address") }} | `email_events.ipAddress` | 🟢 _0.90_ | *Field 'email_events.ipAddress' closely matches target field 'ip_address', noting the slight format difference in casing but maintaining the correct meaning.* |
| `location` | {{ doc("email_event_location") }} | `email_events.location` | 🟢 _0.90_ | *Direct and appropriate mapping of 'email_events.location', target mirroring source adequately.* |
| `referer` | The URL of the webpage that linked to the URL clicked. Whether this is provided, and what its value is, is determined by the recipient's email client. | `email_events.referer` | 🟢 _0.85_ | *The field maps correctly from 'email_events.referer' to 'referer' with contextual matching about links from web sources.* |
| `url` | The URL within the message that the recipient clicked. | `email_events.url` | ⚠️ _0.60_ | *Mapping of 'email_events.url' has slightly lower confidence due to potential variations in URL patterns or usage but remains a justified match.* |
| `user_agent` | {{ doc("email_event_user_agent") }} | `email_events.userAgent` | 🟢 _0.90_ | *Field 'email_events.userAgent' is well translated to 'user_agent', respecting the context and format adaptability.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The field mappings generally align well with the target schema, capturing most of the critical identifiers and timestamps relevant to the email events context. The sources and targets seem to be describing similar datasets, enhancing confidence in the appropriateness of the mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match as this is a standardized mapping for all tables.* |
| `app_id` | The ID of the app that sent the email. | `email_events.appId` | 🟢 _0.95_ | *Direct mapping of simple identifier fields with clear equivalent.* |
| `caused_by_created` | The timestamp of the event that caused this event. | `email_events.causedBy.created` | 🟢 _0.95_ | *Timestamp fields exactly match in context and naming, suggesting high reliability.* |
| `caused_by_id` | The event ID which uniquely identifies the event which directly caused this event. If not applicable, this property is omitted. | `email_events.causedBy.id` | 🟢 _0.95_ | *ID fields are directly comparable and clear in their purpose.* |
| `created` | The created timestamp of the event. | `email_events.created` | 🟢 _0.95_ | *Direct match on creation timestamp, essential for event logging.* |
| `email_campaign_id` | The ID of the related email campaign. | `email_events.emailCampaignId` | 🟢 _0.80_ | *Slightly less confidence due to potential variability in campaign ID definitions across platforms, but still a strong match.* |
| `filtered_event` | A boolean representing whether the event has been filtered out of reporting based on customer reports settings or not. | `email_events.filteredEvent` | 🟢 _0.85_ | *Boolean fields are direct and unlikely to differ in meaning, though slight ambiguity about filtering criteria exists.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _1.00_ | *Perfect match on primary identifiers.* |
| `obsoleted_by_created` | The timestamp of the event that made the current event obsolete. | `email_events.obsoletedBy.created` | 🟢 _0.95_ | *Timestamp matching is critical and direct here, indicating strong alignment.* |
| `obsoleted_by_id` | The event ID which uniquely identifies the follow-on event which makes this current event obsolete. If not applicable, this property is omitted. | `email_events.obsoletedBy.id` | 🟢 _0.80_ | *While the IDs match, the concept of obsolescence might carry different implications across platforms.* |
| `portal_id` | {{ doc("portal_id") }} | `email_events.portalId` | 🟢 _0.95_ | *Straightforward mapping with likely identical underlying meaning.* |
| `recipient` | The email address of the contact related to the event. | `email_events.recipient` | 🟢 _0.95_ | *Direct alignment of email addresses, fundamental for event logging.* |
| `sent_by_created` | The timestamp of the SENT event related to this event. | `email_events.sentBy.created` | 🟢 _0.95_ | *Timing of sent actions is universally applicable, indicating high accuracy in alignment.* |
| `sent_by_id` | The event ID which uniquely identifies the email message's SENT event. If not applicable, this property is omitted. | `email_events.sentBy.id` | ⚠️ _0.60_ | *The mapping of 'sent' event identifiers holds, though there could be subtle differences in interpretation.* |
| `type` | The type of event. | `email_events.type` | 🟢 _0.90_ | *Event type fields generally have high interoperability, though minor differences in event categorization could exist.* |

### Mapping: Airbyte `deal_pipelines` to Fivetran `deal_pipeline`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.86_
- Summary Self-Evaluation: _The table mapping closely aligns with expected schema mappings, with a few missing fields but overall strong correlation._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deal_pipelines._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for synchronisation timestamp is properly maintained.* |
| `active` | Whether the stage is currently in use. | `deal_pipelines.active` | 🟢 _0.90_ | *Direct match with clear semantic and functional alignment.* |
| `display_order` | Used to determine the order in which the pipelines appear when viewed in HubSpot. | `deal_pipelines.displayOrder` | 🟢 _0.80_ | *Direct correspondence with minor naming variation.* |
| `label` | The human-readable label for the pipeline. The label is used when showing the pipeline in HubSpot. | `deal_pipelines.label` | 🟢 _0.90_ | *Identical meaning and functionality verified across schemas.* |
| `pipeline_id` | The ID of the pipeline. | `deal_pipelines.pipelineId` | 🟢 _0.95_ | *Direct equivalence with clear identification across both systems.* |
| `created_at` | A timestamp representing when the record was created. | `deal_pipelines.createdAt` | 🟢 _0.90_ | *Timestamp fields directly correspond across the mappings.* |
| `updated_at` | A timestamp representing when the record was updated. | `deal_pipelines.updatedAt` | 🟢 _0.90_ | *Timestamp fields directly correspond across the mappings.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_print`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The mapping generally aligns well with our schema compatibility expectations. Mappings for common fields are on point, but some fields are potentially ambiguous and need more context._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match as per standard mapping guidelines for system fields.* |
| `browser` | {{ doc("email_event_browser") }} | `email_events.browser` | 🟢 _0.85_ | *Direct mapping with no significant differences in meaning detected.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _1.00_ | *Perfect match as this is a unique identifier.* |
| `ip_address` | {{ doc("email_event_ip_address") }} | `email_events.ipAddress` | 🟢 _0.90_ | *Direct mapping, slight potential for variance in format.* |
| `location` | {{ doc("email_event_location") }} | `email_events.location` | 🟢 _0.75_ | *Likely the same, but subject to regional differences in data definition.* |
| `user_agent` | {{ doc("email_event_user_agent") }} | `email_events.userAgent` | 🟢 _0.80_ | *Generally the same, although exact details about data collection might differ.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_deferred`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table matching score is high as both source and target likely come from related API integrations with similar structures. The completion score indicates a well-populated mapping configuration but some fields were probably not directly matched._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables, perfectly matched with source stream's _airbyte_extracted_at column.* |
| `attempt` | The delivery attempt number. | `email_events.attempt` | 🟢 _0.90_ | *Direct match on field names suggests a very high confidence in mapping to email_events.attempt.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _0.95_ | *Direct match on field names indicates near certainty in mapping to email_events.id.* |
| `response` | The full response from the recipient's email server. | `email_events.response` | 🟢 _0.90_ | *Direct match on field names and detailed descriptions, ensuring a high level of confidence in mapping to email_events.response.* |

### Mapping: Airbyte `engagements_emails` to Fivetran `engagement_email_cc`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping involves a source from Airbyte and targets a similar schema used by Fivetran. The mappings are well-aligned as both the source and target likely represent emails specific activities, providing a high table match score. Most fields are matched appropriately, ensuring a high completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_emails._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping based on consistent source-to-target requirements for sync timestamps.* |
| `email` | The email address of the recipient. | `engagements_emails.properties.hs_email_from_email` | 🟢 _0.95_ | *Directly matches an email address field from source to target, maintaining integrity and specificity of the data.* |
| `engagement_id` | The ID of the related engagement. | `engagements_emails.properties.hs_engagement_source_id` | 🟢 _0.90_ | *Target field is directly related to a source column denoting an engagement ID, very likely referring to the same concept.* |
| `first_name` | The first name of the recipient. | `engagements_emails.properties.hs_email_from_firstname` | 🟢 _0.85_ | *Straightforward mapping of first name fields between source and target schemas.* |
| `last_name` | The last name of the recipient. | `engagements_emails.properties.hs_email_from_lastname` | 🟢 _0.85_ | *Straightforward mapping of last name fields between source and target schemas.* |

### Mapping: Airbyte `deals` to Fivetran `deal_company`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table match score is high indicating a good quality of table matching. The completion score is moderate, reflecting partial coverage in field mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deals._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match as this is a standard mapping for all tables.* |
| `company_id` | The ID of the company. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deal_id` | The ID of the deal. | `deals.properties.hs_object_id` | 🟢 _0.70_ | *Good match based on the deal identifier consistency.* |
| `type_id` | The ID of the type. | `deals.properties.dealtype` | 🟢 _0.70_ | *Good match based on the type identifier consistency.* |
| `category` | The association category. Either HUBSPOT_DEFINED (default label) or USER_DEFINED (custom label). | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `engagements_notes` to Fivetran `engagement_note`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The field mappings mostly align well with the source and target schema definitions, indicating a high likelihood of representing the same data entities across different implementations._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_notes._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match as it is a standard mapping for all tables.* |
| `body` | The body of the note. The body has a limit of 65536 characters. | `engagements_notes.properties.hs_note_body` | 🟢 _0.80_ | *The mapping correctly aligns with the expected body field in notes, using the detailed extraction path provided.* |
| `engagement_id` | The ID of the engagement. | `engagements_notes.properties.hs_engagement_source_id` | 🟢 _0.90_ | *Direct match found for the engagement ID using the specific property path.* |
| `property_hs_createdate` | This field marks the note's time of creation and determines where the note sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_notes.properties.hs_createdate` | 🟢 _0.70_ | *The mapping is appropriate for the creation date field, aligning timestamps correctly.* |
| `timestamp` | This field marks the note's time of occurrence and determines where the note sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_notes.properties.hs_timestamp` | 🟢 _0.70_ | *Proper mapping for the timestamp, aligning event times correctly.* |
| `property_hubspot_owner_id` | The ID of the owner associated with the note. This field determines the user listed as the note creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_notes.properties.hubspot_owner_id` | 🟢 _0.70_ | *Mapping for the owner ID is accurate, reflecting appropriate user identification.* |
| `property_hubspot_team_id` | The ID of the team associated with the note. This field determines the team listed as the note creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_notes.properties.hubspot_team_id` | ⚠️ _0.65_ | *The team ID mapping is generally correct but lacks stronger contextual evidence to score higher.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_delivered`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _Given the context of the field mappings and the table similarity, the table match has a moderate to high confidence score suggesting a good correlation. However, the completion score indicates that while most fields are mapped, there could be improvements or some fields are missing._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping as per instruction, always matches to _airbyte_extracted_at.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _0.80_ | *Direct mapping of 'id' fields suggests a very high confidence due to identical meanings.* |
| `response` | The full response from the recipient's email server. | `email_events.response` | 🟢 _0.70_ | *Mapping of 'response' fields is relevant and accurate, reflecting a good confidence score based on their descriptions.* |
| `smtp_id` | An ID attached to the message by HubSpot. | `email_events.smtpId` | ⚠️ _0.60_ | *Mapping of 'smtpId' to 'smtp_id', this represents a good match under the provided conditions without penalizing for case sensitivity.* |

### Mapping: Airbyte `companies` to Fivetran `company`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The source and target tables are closely aligned, indicating high interoperability between schema mappings. Most mappings are strong, but some fields lack exact matches._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `companies._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping is perfect.* |
| `id` | The ID of the company. | `companies.id` | 🟢 _1.00_ | *Direct match of identifier fields in both source and target schemas.* |
| `portal_id` | {{ doc("portal_id") }} | `companies.id` | ❌ _0.00_ | *No good match found.* |
| `is_deleted` | {{ doc("is_deleted") }} | `companies.archived` | 🟢 _0.80_ | *Mapped to 'archived,' which implies a similar active/deleted state differentiation.* |
| `property_name` | The name of the company. | `companies.properties.name` | 🟢 _1.00_ | *Exact match for the name of the company.* |
| `property_description` | A short statement about the company's mission and goals. | `companies.properties.description` | 🟢 _1.00_ | *Direct match for a description field.* |
| `property_createdate` | The date the company was added to your account. | `companies.properties.createdate` | 🟢 _1.00_ | *Exact match of creation dates.* |
| `property_industry` | The type of business the company performs. | `companies.properties.industry` | 🟢 _1.00_ | *Direct match for industry classification.* |
| `property_address` | The street address of the company. | `companies.properties.address` | 🟢 _0.80_ | *Mapped to 'address' with slightly different field nesting but fundamentally same data.* |
| `property_address_2` | Additional address information for the company. | `companies.properties.address2` | 🟢 _0.80_ | *Same as 'property_address' with slight differences in detail provided.* |
| `property_city` | The city where the company is located. | `companies.properties.city` | 🟢 _1.00_ | *Direct match to city location.* |
| `property_state` | The state where the company is located. | `companies.properties.state` | 🟢 _1.00_ | *Exact match for state location.* |
| `property_country` | The country where the company is located. | `companies.properties.country` | 🟢 _1.00_ | *Countries perfectly align between source and target.* |
| `property_annualrevenue` | The actual or estimated annual revenue of the company. | `companies.properties.annualrevenue` | 🟢 _0.70_ | *Slight ambiguity in revenue reporting, but likely the same field.* |

### Mapping: Airbyte `contacts` to Fivetran `ticket_contact`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _Based on the provided mappings and project instructions, the mappings demonstrate a high confidence in terms of their relevance to each other, with adequate explanations and considerations for matching fields appropriately. However, some fields are marked as MISSING, lowering the overall completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts._airbyte_extracted_at` | 🟢 _1.00_ | *Direct 1:1 mapping with clear equivalence, as indicated by standard practices.* |
| `ticket_id` | The ID of the related ticket. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `contact_id` | The ID of the related contact. | `contacts.id` | 🟢 _1.00_ | *Direct match with clear correlation to 'contacts.id'.* |
| `category` | The association category. Either HUBSPOT_DEFINED (default label) or USER_DEFINED (custom label). | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `engagements_meetings` to Fivetran `engagement_meeting`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mappings exhibit a strong similarity in structure and nomenclature, suggesting a good match between source and target schemas. The completion score is high as most key fields are effectively mapped, leading to a comprehensive schema transformation._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_meetings._airbyte_extracted_at` | 🟢 _1.00_ | *Direct mapping of implementation-specific sync fields.* |
| `engagement_id` | The ID of the engagement. | `engagements_meetings.id` | 🟢 _1.00_ | *Clear match for unique identifiers in both schemas.* |
| `property_hs_createdate` | This field marks the meeting's time of creation and determines where the meeting sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_meetings.properties.hs_createdate` | 🟢 _0.90_ | *Direct mapping of timestamp fields, strong contextual match.* |
| `timestamp` | This field marks the meeting's time of occurrence and determines where the meeting sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_meetings.properties.hs_timestamp` | 🟢 _0.90_ | *Direct mapping of timestamp fields, strong contextual match.* |
| `property_hubspot_owner_id` | The ID of the owner associated with the meeting. This field determines the user listed as the meeting creator on the record timeline.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_meetings.properties.hubspot_owner_id` | 🟢 _0.70_ | *Possible match assuming similar nomenclature and contextual usage.* |
| `property_hubspot_team_id` | The ID of the team associated with the meeting. This field determines the team listed as the meeting creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_meetings.properties.hubspot_team_id` | 🟢 _0.70_ | *Possible match assuming similar nomenclature and contextual usage.* |

### Mapping: Airbyte `engagements_tasks` to Fivetran `engagement_task`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table mapping between the source table 'engagements_tasks' and the target schema captures most of the key fields, though it omits some optional fields. The fields provided are mapped with high confidence, particularly the identifications of date fields and ownership. The confidence in the table matching is very high due to the correct and similar fields that are highly relevant to both implementations._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_tasks._airbyte_extracted_at` | 🟢 _1.00_ | *This mapping of '_fivetran_synced' to 'engagements_tasks._airbyte_extracted_at' is a standard mapping across all tables, hence the perfect score.* |
| `engagement_id` | The ID of the engagement. | `engagements_tasks.id` | 🟢 _1.00_ | *Direct mapping of 'engagement_id' aligns with the target schema identifier without any discrepancies.* |
| `property_hs_createdate` | This field marks the task's time of creation and determines where the task sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_tasks.properties_hs_createdate` | 🟢 _0.80_ | *The field matches based on the description and relevance to creation date contexts across both schema versions, though minor differences in the API version are noted.* |
| `timestamp` | This field marks the task's time of occurrence and determines where the task sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_tasks.properties_hs_timestamp` | 🟢 _0.80_ | *Mapped correctly to reference the timestamp in context of the task's occurrence consistent with the target schema's expectations.* |
| `property_hubspot_owner_id` | The ID of the owner associated with the task. This field determines the user listed as the task creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_tasks.properties_hubspot_owner_id` | 🟢 _0.70_ | *The owner ID is mapped well but has slight potential differences depending on API version changes noted in descriptions.* |
| `property_hubspot_team_id` | The ID of the team associated with the task. This field determines the team listed as the task creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_tasks.properties_hubspot_team_id` | 🟢 _0.70_ | *Team ID mapping is relevant and correct, though minor variations due to API versioning are observed, which brings the score to 0.7.* |

### Mapping: Airbyte `engagements` to Fivetran `ticket_engagement`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table match score is relatively high because both source and target tables are being generated from a similar API context, indicating a strong alignment in the data's subject matter. The completion score is lower due to some missing field mappings which could not be confidently matched, reflecting a partial but significant overlap in fields between source and target schemas._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements._airbyte_extracted_at` | 🟢 _1.00_ | *Direct mapping to source streams '_airbyte_extracted_at' always scores a 1.00 as it is considered a standard requirement for all tables.* |
| `ticket_id` | The ID of the related ticket. | `engagements.associations_ticketIds` | 🟢 _0.70_ | *Mapped to 'engagements.associations_ticketIds' with reasonably high confidence, as it closely represents the 'ticket_id' in a typical schema, but less than perfect due to potential variations in ticket ID context across applications.* |
| `engagement_id` | The ID of the related deal. | `engagements.id` | 🟢 _0.70_ | *Mapped to 'engagements.id' with high confidence due to direct relevance and similarity in concept, though the lack of more detailed context hinders a perfect score.* |
| `category` | The association category. Either HUBSPOT_DEFINED (default label) or USER_DEFINED (custom label). | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `engagements` to Fivetran `engagement_deal`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _Moderate match and completion scores indicate that while the table mappings are related, not all fields were perfectly matched._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements._airbyte_extracted_at` | 🟢 _1.00_ | *Perfectly matched based on the standard mapping guidelines.* |
| `deal_id` | The ID of the related contact. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `engagement_id` | The ID of the related engagement. | `engagements.id` | 🟢 _0.70_ | *A high likelihood match as the target field clearly represents the same concept.* |
| `category` | The association category. Either HUBSPOT_DEFINED (default label) or USER_DEFINED (custom label). | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `contacts_property_history` to Fivetran `ticket_property_history`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table match score and completion scores are relatively high, indicating a strong correlation and good coverage of the field mappings from the source to the target schema. The mappings prioritize functional similarities over textual similarity and align with project guidance about maintaining data integrity and meaning._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_property_history._airbyte_extracted_at` | 🟢 _1.00_ | *Direct mapping to '_airbyte_extracted_at' as a standard, always correct.* |
| `source` | {{ doc("history_source") }} | `contacts_property_history._airbyte_meta` | 🟢 _0.70_ | *Mapped to '_airbyte_meta' which likely refers to metadata of similar nature in Fivetran and Airbyte schemes.* |
| `source_id` | {{ doc("history_source_id") }} | `contacts_property_history.properties_hs_user_ids_of_all_owners` | 🟢 _0.70_ | *Column refers to owners' user IDs in the context of history, aligning well with similar data representations across schemas.* |
| `timestamp_instant` | {{ doc("history_timestamp") }} | `contacts_property_history.properties_hs_last_sales_activity_timestamp` | 🟢 _0.80_ | *Mapped to last sales activity timestamp, which is highly relevant and direct in historical data mappings.* |
| `ticket_id` | The ID of the related ticket record. | `contacts_property_history.properties_hs_v2_date_entered_customer` | ❌ _0.45_ | *Low confidence due to the indirect relation between 'date entered customer' and a specific ticket ID.* |
| `name` | {{ doc("history_name") }} | `contacts_property_history.properties_hs_legal_basis` | ⚠️ _0.60_ | *Mapped to 'hs_legal_basis' field which is a plausible match given the use of historical data labels.* |
| `value` | {{ doc("history_value") }} | `contacts_property_history.properties_hs_testrollback` | ⚠️ _0.60_ | *Mapped to a test rollback field, possible match but with caution.* |
| `_fivetran_start` | {{ doc("_fivetran_start") }} | `contacts_property_history.properties_hs_v2_date_entered_lead` | ❌ _0.40_ | *Attempted mapping to 'date entered lead' lacks direct correlation with 'start' context.* |
| `_fivetran_end` | {{ doc("_fivetran_end") }} | `contacts_property_history.properties_hs_v2_date_exited_salesqualifiedlead` | ❌ _0.40_ | *Attempted mapping to 'date exited salesqualifiedlead' lacks direct correlation with 'end' context.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_dropped`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table match score is relatively high due to consistent source API contributions, ensuring a good match. The completion score is also high as most of the fields are comprehensively mapped. The field mappings reflect a high degree of match, with appropriate expressions mapped to source fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *The mapping for `_fivetran_synced` to `email_events._airbyte_extracted_at` is perfect as it is a standard, consistent mapping across implementations.* |
| `bcc` | The 'bcc' field of the email message. | `email_events.bcc` | 🟢 _0.90_ | *Direct mapping found with identical field names.* |
| `cc` | The 'cc' field of the email message. | `email_events.cc` | 🟢 _0.90_ | *Direct mapping with similar field names and clear semantic relation.* |
| `drop_message` | The raw message describing why the email message was dropped. This will usually provide additional details beyond 'dropReason'. | `email_events.dropMessage` | 🟢 _0.85_ | *Mapped directly to `email_events.dropMessage` though with slight semantic variation in the description, ensuring a very good match.* |
| `drop_reason` | The reason why the email message was dropped. See below for the possible values. | `email_events.dropReason` | 🟢 _0.85_ | *Direct mapping to `email_events.dropReason`, with clear semantic relation.* |
| `from` | The 'from' field of the email message. | `email_events.from` | 🟢 _0.90_ | *Direct and clear mapping to `email_events.from` reflects identical semantic and syntactical match.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _0.90_ | *Direct mapping to `email_events.id` with perfect semantic and syntactical alignment.* |
| `reply_to` | The 'reply-to' field of the email message. | `email_events.replyTo` | 🟢 _0.80_ | *Direct mapping with slightly broad semantic scope which could potentially include additional elements not present in corresponding mapping.* |
| `subject` | The subject line of the email message. | `email_events.subject` | 🟢 _0.90_ | *Direct mapping to `email_events.subject`; clear semantic and syntactical alignment.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_forward`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.83_
- Summary Self-Evaluation: _The table match is highly successful with confident mappings based on similar schema from Airbyte and Fivetran. Most fields are directly mapped with high confidence, except a few that needed interpretation._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Direct and standard mapping with perfect confidence.* |
| `browser` | {{ doc("email_event_browser") }} | `email_events.browser` | 🟢 _0.95_ | *Direct mapping from same column name, high confidence.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _0.70_ | *Direct mapping from an directly equivalent column name, high confidence.* |
| `ip_address` | {{ doc("email_event_ip_address") }} | `email_events.ipAddress` | 🟢 _0.90_ | *Mapped based on field meaning, very high confidence.* |
| `location` | {{ doc("email_event_location") }} | `email_events.location` | 🟢 _0.90_ | *Mapped from 'email_events.location' with contextual similarities, very high confidence.* |
| `user_agent` | {{ doc("email_event_user_agent") }} | `email_events.userAgent` | 🟢 _0.90_ | *Direct mapping from 'userAgent' field, considering slight text difference, very high confidence.* |

### Mapping: Airbyte `engagements` to Fivetran `engagement_communication`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The table match score is high indicating a strong match between the source and target tables, mainly derived from a consistent data lineage and appropriate field mappings. The completion score is also high, reflecting a comprehensive mapping coverage._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements._airbyte_extracted_at` | 🟢 _1.00_ | *Direct mapping to '_airbyte_extracted_at' which is a standard for all tables.* |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `engagement_id` | ID of the engagement associated with the communication. | `engagements.id` | 🟢 _0.80_ | *Direct match found with consistency in entity representation.* |
| `property_hs_createdate` | Timestamp indicating when the communication was created. | `engagements.createdAt` | 🟢 _0.80_ | *Direct match to the timestamp of creation, consistent with the source's data treatment.* |
| `property_hs_timestamp` | Timestamp of the communication event linked to the engagement. | `engagements.timestamp` | 🟢 _0.70_ | *Matched to 'engagements.timestamp', though careful consideration is needed due to potential overlap with other timestamp fields.* |
| `type` | Type of communication (e.g., email, call, meeting). | `engagements.type` | 🟢 _0.70_ | *Match is very context-specific, assigned score reflects slight uncertainty in the field's equivalency across different contexts.* |

### Mapping: Airbyte `tickets` to Fivetran `ticket`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping has a high confidence score, indicating a strong match between the source and target tables. Most fields from the source are utilized effectively in the target schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `tickets._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match as '_fivetran_synced' directly maps to '_airbyte_extracted_at'.* |
| `id` | ID of the ticket. | `tickets.id` | 🟢 _1.00_ | *Direct mapping of 'id' fields.* |
| `is_deleted` | Whether the record was deleted (v2 endpoint). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_deleted` | Whether the record was deleted (v3 endpoint). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `portal_id` | {{ doc("portal_id") }} | `tickets.properties.hubspot_owner_id` | 🟢 _0.90_ | *Highly likely match with 'hubspot_owner_id' at schema level.* |
| `property_closed_date` | The date the ticket was closed. | `tickets.properties.closed_date` | 🟢 _0.80_ | *Direct match with data semantics maintained.* |
| `property_createdate` | The date the ticket was created. | `tickets.properties.createdate` | 🟢 _0.80_ | *Direct mapping that retains semantics.* |
| `property_first_agent_reply_date` | the date for the first agent reply on the ticket. | `tickets.properties.first_agent_reply_date` | 🟢 _0.80_ | *The specific usage and context results in a high confidence level.* |
| `property_hs_pipeline` | The ID of the ticket's pipeline. | `tickets.properties.hs_pipeline` | 🟢 _0.80_ | *Direct mapping of pipeline ID with clear semantics.* |
| `property_hs_pipeline_stage` | The ID of the ticket's pipeline stage. | `tickets.properties.hs_pipeline_stage` | 🟢 _0.80_ | *Direct and meaningful mapping of pipeline stage.* |
| `property_hs_ticket_priority` | The priority of the ticket. | `tickets.properties.hs_ticket_priority` | 🟢 _0.80_ | *Priority fields have a direct match.* |
| `property_hs_ticket_category` | The category of the ticket. | `tickets.properties.hs_ticket_category` | 🟢 _0.80_ | *Category fields are directly mapped.* |
| `property_hubspot_owner_id` | The ID of the deal's owner. | `tickets.properties.hubspot_owner_id` | 🟢 _0.90_ | *High match likelihood with the portal ID context taken into account.* |
| `property_subject` | Short summary of ticket. | `tickets.properties.subject` | 🟢 _0.80_ | *Straightforward and conceptually correct mapping.* |
| `property_content` | Text in body of the ticket. | `tickets.properties.content` | 🟢 _0.80_ | *Text content has a directly preserved meaning in mapping.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_status_change`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _All field mappings are set up correctly, align with the source and target schema requirements, ensuring data integrity and appropriate transformations._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match as per standardized mapping guidelines.* |
| `bounced` | A HubSpot employee explicitly initiated the status change to block messages to the recipient. (Note this usage has been deprecated in favor of dropping messages with a 'dropReason' of BLOCKED_ADDRESS.)  | `email_events.bounced` | 🟢 _0.85_ | *High confidence score due to direct mapping and matching field relevance between source and target.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _1.00_ | *Direct mapping and data type match ensure a perfect score.* |
| `portal_subscription_status` | The recipient's portal subscription status. Note that if this is 'UNSUBSCRIBED', the property 'subscriptions' is not necessarily an empty array, nor are all subscriptions contained in it necessarily going to have their statuses set to 'UNSUBSCRIBED'.)  | `email_events.portalSubscriptionStatus` | 🟢 _0.70_ | *Good match, minor differences in definitions do not significantly impact the matching quality.* |
| `requested_by` | The email address of the person requesting the change on behalf of the recipient. If not applicable, this property is omitted. | `email_events.requestedBy` | 🟢 _0.90_ | *High confidence due to the exact match of meaning, despite the absence of the field under certain conditions.* |
| `source` | The source of the subscription change. | `email_events.source` | ⚠️ _0.65_ | *Moderate confidence due to slightly broader context in the source, but still a functional match.* |
| `subscriptions` | An array of JSON objects representing the status of subscriptions for the recipient. Each JSON subscription object is comprised of the properties: 'id', 'status'.  | `email_events.subscriptions` | 🟢 _0.75_ | *Solid match with clear correspondence between the source and target representation of subscription statuses.* |

### Mapping: Airbyte `deals` to Fivetran `ticket_deal`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The overall table match is high due to consistent subject matter across the source and target tables for the specified fields. The completion score is less than perfect due to missing mappings for some fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deals._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect mapping: '_fivetran_synced' directly matches '_airbyte_extracted_at' as required by standard procedure.* |
| `ticket_id` | The ID of the related ticket. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deal_id` | The ID of the related deal. | `deals.id` | 🟢 _1.00_ | *Direct match found between 'deal_id' and 'deals.id', representing the same entity.* |
| `category` | The association category. Either HUBSPOT_DEFINED (default label) or USER_DEFINED (custom label). | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `engagements_calls` to Fivetran `engagement_call`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping generally exhibits a strong correspondence between the source and target schemas, indicated by the high table match and completion scores. Most fields provided were mapped appropriately, reflecting a clear and consistent relationship._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_calls._airbyte_extracted_at` | 🟢 _1.00_ | *Direct mapping of Airbyte extraction date to Fivetran sync column.* |
| `engagement_id` | The ID of the engagement. | `engagements_calls.id` | 🟢 _0.95_ | *Direct mapping based on explicit ID match.* |
| `_fivetran_deleted` | Boolean to mark rows that were deleted in the source database. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_hs_createdate` | This field marks the call's time of creation and determines where the call sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_calls.properties.hs_createdate` | ⚠️ _0.60_ | *Appropriate mapping with high relevance to connector's specific API version, requires alignment on date format.* |
| `timestamp` | This field marks the call's time of occurrence and determines where the call sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_calls.properties.hs_timestamp` | ⚠️ _0.60_ | *Appropriate mapping relating to event timeline, requires specific API version.* |
| `property_hubspot_owner_id` | The ID of the owner associated with the call. This field determines the user listed as the call creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_calls.properties.hs_user_ids_of_all_owners` | ⚠️ _0.60_ | *Adequate mapping due to specific API version match, attentive to id specificity.* |
| `property_hubspot_team_id` | The ID of the team associated with the call. This field determines the team listed as the call creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_calls.properties.hs_team_id` | ⚠️ _0.60_ | *Adequate mapping, relevant only to specific API version.* |

### Mapping: Airbyte `email_subscriptions` to Fivetran `email_subscription`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _All fields are perfectly matched, indicating a high degree of confidence in both the accuracy of the field mappings and the completeness of the table mapping._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_subscriptions._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables.* |
| `active` | Whether the subscription is active. | `email_subscriptions.active` | 🟢 _1.00_ | *Direct match found, high confidence.* |
| `description` | The description of the subscription. | `email_subscriptions.description` | 🟢 _1.00_ | *Direct match found, high confidence.* |
| `id` | The ID of the email subscription. | `email_subscriptions.id` | 🟢 _1.00_ | *Direct match found, high confidence.* |
| `name` | The name of the email subscription. | `email_subscriptions.name` | 🟢 _1.00_ | *Direct match found, high confidence.* |
| `portal_id` | {{ doc("portal_id") }} | `email_subscriptions.portalId` | 🟢 _1.00_ | *Standard doc mapping applied, high confidence.* |

### Mapping: Airbyte `tickets` to Fivetran `ticket_company`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _High match quality and nearly complete field mappings, reflecting a strong confidence in the table and field correlations._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `tickets._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect scoring for a standard mapping, always maps '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `ticket_id` | The ID of the related ticket. | `tickets.properties.hs_ticket_id` | 🟢 _0.80_ | *Strong match between 'tickets.properties.hs_ticket_id' and 'ticket_id'.* |
| `company_id` | The ID of the related company. | `tickets.properties.hs_primary_company_id` | 🟢 _0.80_ | *Strong match between 'tickets.properties.hs_primary_company_id' and 'company_id'.* |
| `category` | The association category. Either HUBSPOT_DEFINED (default label) or USER_DEFINED (custom label). | `tickets.properties.hs_ticket_category` | 🟢 _0.70_ | *Good match for 'tickets.properties.hs_ticket_category' to 'category', within the acceptable confidence range.* |

### Mapping: Airbyte `contacts` to Fivetran `contact`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping and field mappings align well, indicating a high level of interoperability between the source and target schemas. Most field mappings are accurately aligned with the right source fields, especially the critical timestamps and identifying fields that facilitate synchronization and integrity._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts._airbyte_extracted_at` | 🟢 _1.00_ | *Exactly matched to source stream's '_airbyte_extracted_at' column as standard mapping.* |
| `id` | The ID of the contact. | `contacts.id` | 🟢 _1.00_ | *Direct match found for 'contacts.id' with the target field 'id'.* |
| `property_email_1` | The email address of the contact. | `contacts.properties.email` | 🟢 _0.80_ | *Mapped to 'contacts.properties.email' with high confidence of accuracy.* |
| `property_company` | The name of the contact's company. | `contacts.properties.company` | 🟢 _0.80_ | *Mapped to 'contacts.properties.company', correctly identifying the company name.* |
| `property_firstname` | The contact's first name. | `contacts.properties.firstname` | 🟢 _0.80_ | *Accurately mapped to 'contacts.properties.firstname' representing the first name.* |
| `property_lastname` | The contact's last name. | `contacts.properties.lastname` | 🟢 _0.80_ | *Correctly mapped to 'contacts.properties.lastname' representing the last name.* |
| `property_email` | The contact's email. | `contacts.properties.email` | 🟢 _0.90_ | *Precisely mapped to 'contacts.properties.email' representing the contact's email.* |
| `property_createdate` | The date that the contact was created in your HubSpot account. | `contacts.properties.createdate` | 🟢 _0.80_ | *Accurately mapped to 'contacts.properties.createdate', capturing the creation date in the source schema.* |
| `property_jobtitle` | The contact's job title. | `contacts.properties.jobtitle` | 🟢 _0.80_ | *Appropriately mapped to 'contacts.properties.jobtitle', accurately representing the job title.* |
| `property_annualrevenue` | The contact's annual company revenue. | `contacts.properties.annualrevenue` | 🟢 _0.80_ | *Mapped to 'contacts.properties.annualrevenue', appropriately representing the annual revenue.* |
| `property_hs_calculated_merged_vids` | List of mappings representing contact IDs that have been merged into the contact at hand. Format: <merged_contact_id>:<merged_at_in_epoch_time>;<second_merged_contact_id>:<merged_at_in_epoch_time> This field has replaced the `CONTACT_MERGE_AUDIT` table, which was deprecated by the Hubspot v3 CRM API.  | `contacts.properties.hs_calculated_merged_vids` | 🟢 _0.80_ | *Effectively mapped to 'contacts.properties.hs_calculated_merged_vids', correctly identifying merged contact IDs.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_sent`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _Table match is high as the mappings largely correlate well with the target schema requirements. Completion is mostly thorough with most required fields mapped effectively._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables, perfectly matched as specified.* |
| `bcc` | The 'cc' field of the email message. | `email_events.bcc` | 🟢 _0.80_ | *Direct match found but with uncertainty due to semantic context, so score is slightly less than perfect.* |
| `cc` | The 'bcc' field of the email message. | `email_events.cc` | 🟢 _0.80_ | *Direct match found, score slightly less due to semantic context.* |
| `from` | The 'from' field of the email message. | `email_events.from` | 🟢 _0.90_ | *Perfect semantic match with a direct correlation to the target field.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _1.00_ | *Ideal direct correlation observed, perfect score awarded.* |
| `reply_to` | The 'reply-to' field of the email message. | `email_events.replyTo` | 🟢 _0.90_ | *Close correlation found with the target field, almost perfect semantic match.* |
| `subject` | The subject line of the email message. | `email_events.subject` | 🟢 _1.00_ | *Direct match found with high confidence, perfect score awarded.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_open`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _High confidence in table match and completion, following the guidelines for mapping source data and maintaining data integrity._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Direct match as per standards requiring mapping '_fivetran_synced' to 'email_events._airbyte_extracted_at'.* |
| `browser` | {{ doc("email_event_browser") }} | `email_events.browser` | 🟢 _0.80_ | *Direct field match, mapping properly from source to target, maintaining the meaning of the data.* |
| `duration` | If provided and nonzero, the approximate number of milliseconds the user had opened the email. | `email_events.duration` | ⚠️ _0.60_ | *Likely the same, with behavior described clearly and matched accurately.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _1.00_ | *Perfect match for 'id' across source and target, directly matching unique identifiers.* |
| `ip_address` | {{ doc("email_event_ip_address") }} | `email_events.ipAddress` | 🟢 _0.80_ | *Good alignment with source, mapping 'ipAddress' directly keeping the field's meaning intact.* |
| `location` | {{ doc("email_event_location") }} | `email_events.location` | 🟢 _0.70_ | *Good confidence in field mapping, relevant contextual match between 'email_events.location' and target schema.* |
| `user_agent` | {{ doc("email_event_user_agent") }} | `email_events.userAgent` | 🟢 _0.70_ | *Appropriate matching of 'userAgent' to 'user_agent', with high likelihood of referring to same data.* |

### Mapping: Airbyte `contacts_merged_audit` to Fivetran `contact_merge_audit`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.88_
- Summary Self-Evaluation: _Given the described mappings, there is a high degree of confidence that the source and target tables represent the same data, especially in terms of core entity information. The mappings were standardized, with evidence of completeness in critical identity and event fields. The source and target fields are aligned, indicating that they cover similar subject matters effectively._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_merged_audit._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables with perfect match.* |
| `canonical_vid` | The contact ID of the contact which the vid_to_merge contact was merged into. | `contacts_merged_audit.canonical_vid` | 🟢 _1.00_ | *Direct mapping of core identity fields with identical names.* |
| `contact_id` | The ID of the contact. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `entity_id` | The ID of the related entity. | `contacts_merged_audit.entity_id` | 🟢 _0.80_ | *Direct mapping with no casing penalties.* |
| `first_name` | The contact's first name. | `contacts_merged_audit.first_name` | 🟢 _1.00_ | *Direct mapping of individual identity fields.* |
| `last_name` | The contact's last name. | `contacts_merged_audit.last_name` | 🟢 _1.00_ | *Direct mapping of individual identity fields.* |
| `num_properties_moved` | The number of properties which were removed from the merged contact. | `contacts_merged_audit.num_properties_moved` | 🟢 _1.00_ | *Direct mapping of event-specific data with high relevance.* |
| `timestamp` | Timestamp of when the contacts were merged. | `contacts_merged_audit.timestamp` | 🟢 _1.00_ | *Timestamp fields directly mapped, ensuring temporal consistency.* |
| `user_id` | The ID of the user. | `contacts_merged_audit.user_id` | ⚠️ _0.60_ | *Acceptable match but the potential difference in semantics (e.g., user vs customer).* |
| `vid_to_merge` | The ID of the contact which was merged. | `contacts_merged_audit.vid_to_merge` | 🟢 _0.70_ | *Fuzzy match to existing entity ID fields, close but slightly ambiguous in relation context.* |

### Mapping: Airbyte `owners` to Fivetran `owner`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The fields have been reasonably well mapped, with high confidence for direct correlations and appropriate settings of 'MISSING' for unmatched fields. The table match and completion are satisfactory, aligned with the guidelines indicated for data integrity and representation across similar schemas._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `owners._airbyte_extracted_at` | 🟢 _1.00_ | *This is a standard mapping and always matches directly and appropriately with '_airbyte_extracted_at'.* |
| `active_user_id` | ID of the active user account associated with the owner. Null if owner is not an active user. | `owners.userId` | 🟢 _0.90_ | *Direct correlation to 'owners.userId' considering the overlap in context.* |
| `created_at` | A timestamp for when the owner was created. | `owners.createdAt` | 🟢 _0.90_ | *Direct mapping to 'owners.createdAt', appropriate and with high confidence due to matching data types and contexts.* |
| `email` | The email address of the owner. | `owners.email` | 🟢 _0.90_ | *Highly accurate mapping of 'owners.email' reflecting direct data correspondence.* |
| `first_name` | The first name of the owner. | `owners.firstName` | 🟢 _0.90_ | *High confidence mapping due to direct correspondence of data field 'owners.firstName'.* |
| `last_name` | The last name of the owner. | `owners.lastName` | 🟢 _0.90_ | *The mapping accurately reflects the direct lineage of data from 'owners.lastName'.* |
| `owner_id` | The ID of the owner. | `owners.id` | 🟢 _0.90_ | *Direct and appropriate mapping of 'owners.id', showing exact data correlations.* |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `type` | The type of owner. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `updated_at` | Timestamp the owner was updated. | `owners.updatedAt` | 🟢 _0.90_ | *Direct alignment with 'owners.updatedAt', reflecting the temporal aspect of the data accurately.* |

### Mapping: Airbyte `engagements` to Fivetran `engagement_company`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table mapping is relatively accurate, as the source and target tables describe the same subject matter. The completion score indicates a majority of fields are mapped correctly but not all._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements._airbyte_extracted_at` | 🟢 _1.00_ | *Exact match to a source stream's column, as prescribed by standard mapping practices.* |
| `company_id` | The ID of the related company. | `engagements.associations.companyIds` | 🟢 _0.80_ | *Direct mapping found, matching related company IDs in the schema.* |
| `engagement_id` | The ID of the related engagement. | `engagements.associations.engagementIds` | 🟢 _0.80_ | *Direct mapping found, matching related engagement IDs in the schema.* |
| `category` | The association category. Either HUBSPOT_DEFINED (default label) or USER_DEFINED (custom label). | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `contacts_form_submissions` to Fivetran `contact_form_submission`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The mapping has a high table match score due to consistent definitions and connection between the Fivetran and Airbyte schemas, both sourced from similar APIs. The completion score is slightly lower because not all fields could be confidently mapped._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_form_submissions._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping, matches perfectly to source stream's column.* |
| `contact_id` | The ID of the related contact. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `conversion_id` | A Unique ID for the specific form conversion. | `contacts_form_submissions.conversion_id` | 🟢 _1.00_ | *Direct match available in source schema.* |
| `form_id` | The GUID of the form that the submission belongs to. | `contacts_form_submissions.form_id` | 🟢 _1.00_ | *Direct match available in source schema.* |
| `page_id` | The ID of the related page. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `page_url` | The URL that the form was submitted on, if applicable. | `contacts_form_submissions.page_url` | 🟢 _1.00_ | *Direct match available, source field matches target field description.* |
| `portal_id` | {{ doc("portal_id") }} | `contacts_form_submissions.portal_id` | 🟢 _1.00_ | *Standard mapping to schema using templated doc reference.* |
| `timestamp` | A Unix timestamp in milliseconds of the time the submission occurred. | `contacts_form_submissions.timestamp` | 🟢 _1.00_ | *Exact match found in the source schema.* |
| `title` | The title of the page that the form was submitted on. This will default to the name of the form if no title is provided. | `contacts_form_submissions.title` | 🟢 _1.00_ | *Direct match mapping to source schema.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_bounce`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping between 'email_events' source and target schema is fairly strong, reflecting the sharing of most fields relevant to the domain. There is a high confidence in the overall schema alignment, but some fields might not map completely, hence the slightly less than perfect completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match as '_fivetran_synced' is standard for all tables mapping to source stream's '_airbyte_extracted_at'.* |
| `category` | The best-guess of the type of bounce encountered. If an appropriate category couldn't be determined, this property is omitted. See below for the possible values. Note that this is a derived value, and may be modified at any time to improve the accuracy of classification.  | `email_events.category` | 🟢 _0.70_ | *The descriptions indicate a good semantic match, suggesting both fields relate to email event categorization.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _1.00_ | *Direct match on 'id' field in both schemas.* |
| `response` | The full response from the recipient's email server. | `email_events.response` | 🟢 _0.70_ | *While different terminologies are used, the fields both refer to email server responses, justifying a fairly confident mapping.* |
| `status` | The status code returned from the recipient's email server. | `email_events.status` | 🟢 _0.70_ | *Mapping is based on a reasonable guess that both fields address the status of emails, hence a solid confidence score but not perfect due to potential variations in how statuses are represented.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_spam_report`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The fields are appropriately matched considering their names and descriptions, as underscore conversions and casing differences are considered equivalent. Fivetran-compatible fields map closely to the Airbyte schema, ensuring high integrity and relevancy of the mapping._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for synchronization timestamps, perfectly matched between schemas.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _0.90_ | *Direct mapping of identification fields; both pertain to identical entities in their respective schema contexts.* |
| `ip_address` | {{ doc("email_event_ip_address") }} | `email_events.ipAddress` | 🟢 _0.70_ | *Field names suggest the same data, but context is necessary to confirm they are indeed the same across different schemas.* |
| `user_agent` | {{ doc("email_event_user_agent") }} | `email_events.userAgent` | 🟢 _0.70_ | *Given the names and similar usages in tracking user environments, it's likely they refer to the same data despite minor naming differences.* |

### Mapping: Airbyte `deals_property_history` to Fivetran `deal_property_history`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _Table matches and field mappings show good confidence and reasonable assumptions based on the shared API source with minor unpopulated fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deals_property_history._airbyte_extracted_at` | 🟢 _1.00_ | *Direct match with source stream’s _airbyte_extracted_at column.* |
| `deal_id` | The ID of the related deal record. | `deals_property_history.dealId` | 🟢 _0.90_ | *Direct match found on key field.* |
| `name` | {{ doc("history_name") }} | `deals_property_history.property` | 🟢 _0.70_ | *Likely represents the same property, but less clarity due to generic naming.* |
| `source` | {{ doc("history_source") }} | `deals_property_history.sourceType` | ⚠️ _0.65_ | *Reasonable confidence that source fields correspond.* |
| `source_id` | {{ doc("history_source_id") }} | `deals_property_history.sourceId` | ⚠️ _0.65_ | *Matching identifers but could be clearer if exact source field type documented.* |
| `timestamp` | {{ doc("history_timestamp") }} | `deals_property_history.timestamp` | 🟢 _0.80_ | *Timestamp fields typically match well across different systems.* |
| `value` | {{ doc("history_value") }} | `deals_property_history.value` | ⚠️ _0.60_ | *Value fields are broadly similar, but specifics could use more documentation.* |

### Mapping: Airbyte `engagements` to Fivetran `engagement`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The overall table matching quality is high, with strong indications that the source and target tables describe the same subject matter. Most fields were mapped successfully with high confidence, indicating good coverage and accurate mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping always gets a score of 1.00.* |
| `active` | Whether the engagement is currently being shown in the UI.  PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.active` | 🟢 _0.90_ | *Direct mapping with high confidence.* |
| `created_at` | A timestamp representing when the engagement was created.  PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.createdAt` | 🟢 _0.70_ | *Mapped with medium confidence due to potential variances in API version usage.* |
| `id` | The ID of the engagement. | `engagements.id` | 🟢 _1.00_ | *Direct mapping, perfect match.* |
| `owner_id` | The ID of the engagement's owner. PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.ownerId` | 🟢 _0.70_ | *Mapped with medium confidence reflecting version-specific variations.* |
| `portal_id` | {{ doc("portal_id") }} | `engagements.portalId` | 🟢 _0.90_ | *Mapped successfully with high confidence.* |
| `timestamp` | A timestamp in representing the time that the engagement should appear in the timeline. PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.timestamp` | 🟢 _0.70_ | *Mapped with medium confidence due to potential version-specific variances.* |
| `type` | One of NOTE, EMAIL, TASK, MEETING, or CALL, the type of the engagement. | `engagements.type` | 🟢 _0.92_ | *Mapped successfully with very high confidence.* |

### Mapping: Airbyte `companies_property_history` to Fivetran `company_property_history`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _High accuracy in table matching due to consistent and relevant field mappings that closely align with the target schema requirements, despite not populating all possible fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `companies_property_history._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match according to the standard mapping procedure for synchronizing timestamps.* |
| `company_id` | The ID of the related company record. | `companies_property_history.companyId` | 🟢 _0.90_ | *Correct mapping of company identifiers between source and target schemas.* |
| `name` | {{ doc("history_name") }} | `companies_property_history.property` | 🟢 _0.90_ | *Field descriptions are well aligned and mapped based on the content relevance across both schemas.* |
| `source` | {{ doc("history_source") }} | `companies_property_history.sourceType` | 🟢 _0.90_ | *Accurate mapping based on shared context and description.* |
| `source_id` | {{ doc("history_source_id") }} | `companies_property_history.sourceId` | 🟢 _0.90_ | *Direct mapping between source ids provides a strong correlation.* |
| `timestamp` | {{ doc("history_timestamp") }} | `companies_property_history.timestamp` | 🟢 _0.90_ | *Timestamp fields are universally relevant and aligned correctly.* |
| `value` | {{ doc("history_value") }} | `companies_property_history.value` | 🟢 _0.90_ | *Proper mapping of value fields, maintaining data integrity and contextual relevance.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
