# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.

### Mapping: Airbyte `deals_property_history` to Fivetran `deal_property_history`


- Table Match Confidence Score: 🟢 _0.72_
- Table Completion Score: 🟢 _0.86_
- Summary Self-Evaluation: _The table match score is relatively high, indicating a good match between source and target tables based on similar schema elements. However, one field has an expression marked as 'MISSING', lowering the completion score due to incomplete mapping._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deals_property_history._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for _fivetran_synced to _airbyte_extracted_at.* |
| `deal_id` | The ID of the related deal record. | `deals_property_history.dealId` | 🟢 _0.70_ | *dealId from deals_property_history is likely to match deal_id based on naming and context.* |
| `name` | {{ doc("history_name") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `source` | {{ doc("history_source") }} | `deals_property_history.sourceType` | 🟢 _0.70_ | *sourceType from deals_property_history matches source based on name and typical usage.* |
| `source_id` | {{ doc("history_source_id") }} | `deals_property_history.sourceId` | 🟢 _0.70_ | *sourceId from deals_property_history matches source_id based on naming similarities.* |
| `timestamp` | {{ doc("history_timestamp") }} | `deals_property_history.timestamp` | 🟢 _0.70_ | *timestamp from deals_property_history matches timestamp based on naming conventions.* |
| `value` | {{ doc("history_value") }} | `deals_property_history.value` | 🟢 _0.70_ | *value from deals_property_history matches value, typical mapping based on name.* |

### Mapping: Airbyte `engagements_notes` to Fivetran `engagement_note`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: ⚠️ _0.57_
- Summary Self-Evaluation: _The table mapping reflects the same conceptual entity between the source and target. However, one of the field mappings is missing, impacting the completion score. The table map aligns well with data source structures typically shared via similar APIs, thereby achieving a high table match score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_notes._airbyte_extracted_at` | 🟢 _1.00_ | *This is a standard mapping for all tables and is always mapped to '_airbyte_extracted_at'.* |
| `body` | The body of the note. The body has a limit of 65536 characters. | `engagements_notes.properties.hs_note_body` | 🟢 _0.80_ | *The field 'body' maps well to 'hs_note_body' indicating a similar content purpose, thus achieving a high confidence score.* |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_hs_createdate` | This field marks the note's time of creation and determines where the note sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_notes.properties.hs_createdate` | 🟢 _0.70_ | *This field marks the note's time of creation; mapped to 'hs_createdate' reflecting likely indiscernible temporal data. Meeting specified criteria.* |
| `timestamp` | This field marks the note's time of occurrence and determines where the note sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_notes.properties.hs_timestamp` | 🟢 _0.70_ | *This field marks the note's time of occurrence; mapped to 'hs_timestamp', aligns contextually similar to creation date.* |
| `property_hubspot_owner_id` | The ID of the owner associated with the note. This field determines the user listed as the note creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_notes.properties.hubspot_owner_id` | 🟢 _0.70_ | *Reflects ownership of the note, aligning contextually with 'hubspot_owner_id', maintaining entity tracking consistency.* |
| `property_hubspot_team_id` | The ID of the team associated with the note. This field determines the team listed as the note creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_notes.properties.hubspot_team_id` | 🟢 _0.70_ | *Reflects team ownership of the note, aligning consistently with 'hubspot_team_id', reinforcing entity clarity.* |

### Mapping: Airbyte `contacts` to Fivetran `contact`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.91_
- Summary Self-Evaluation: _The mapping is generally strong, showing a high level of confidence that the target schema fields align with the source fields. The completion is high, indicating most source fields have corresponding target fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts._airbyte_extracted_at` | 🟢 _1.00_ | *_fivetran_synced perfectly maps to contacts._airbyte_extracted_at.* |
| `id` | The ID of the contact. | `contacts.id` | 🟢 _1.00_ | *The 'id' field perfectly matches the target schema.* |
| `property_email_1` | The email address of the contact. | `contacts.properties_email` | 🟢 _0.70_ | *Partial match with some uncertainty due to potential overlapping with similar fields.* |
| `property_company` | The name of the contact's company. | `contacts.properties_company` | 🟢 _1.00_ | *The 'company' field is clearly matched.* |
| `property_firstname` | The contact's first name. | `contacts.properties_firstname` | 🟢 _1.00_ | *The 'first name' field is correctly aligned.* |
| `property_lastname` | The contact's last name. | `contacts.properties_lastname` | 🟢 _1.00_ | *The 'last name' field is correctly aligned.* |
| `property_email` | The contact's email. | `contacts.properties_email` | 🟢 _0.70_ | *Partial match with some uncertainty due to potential duplicate mappings.* |
| `property_createdate` | The date that the contact was created in your HubSpot account. | `contacts.properties_createdate` | 🟢 _1.00_ | *Creation date field matches perfectly.* |
| `property_jobtitle` | The contact's job title. | `contacts.properties_jobtitle` | 🟢 _1.00_ | *The 'job title' field is well matched.* |
| `property_annualrevenue` | The contact's annual company revenue. | `contacts.properties_annualrevenue` | 🟢 _1.00_ | *Annual revenue field is an exact match.* |
| `property_hs_calculated_merged_vids` | List of mappings representing contact IDs that have been merged into the contact at hand. Format: <merged_contact_id>:<merged_at_in_epoch_time>;<second_merged_contact_id>:<merged_at_in_epoch_time> This field has replaced the `CONTACT_MERGE_AUDIT` table, which was deprecated by the Hubspot v3 CRM API.  | `contacts.properties_hs_calculated_merged_vids` | ⚠️ _0.65_ | *Field partially matched with high confidence for underlying meaning, but lacking precise mapping.* |

### Mapping: Airbyte `owners` to Fivetran `owner`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The mappings are largely appropriate for the given context with `_fivetran_synced` mapping perfectly, but there are unknown fields marked as 'MISSING'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `owners._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `created_at` | A timestamp for when the owner was created. | `owners.createdAt` | 🟢 _0.90_ | *High confidence match with 'owners.createdAt' given the context.* |
| `email` | The email address of the owner. | `owners.email` | 🟢 _0.90_ | *High confidence match with 'owners.email' based on field name and context.* |
| `first_name` | The first name of the owner. | `owners.firstName` | 🟢 _0.90_ | *High confidence match with 'owners.firstName' due to similar naming and context.* |
| `last_name` | The last name of the owner. | `owners.lastName` | 🟢 _0.90_ | *High confidence match with 'owners.lastName' based on context similarity.* |
| `owner_id` | The ID of the owner. | `owners.userId` | 🟢 _0.90_ | *High confidence that 'owner_id' and 'owners.userId' refer to the same entity.* |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `type` | The type of owner. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `updated_at` |  | `owners.updatedAt` | 🟢 _0.90_ | *High confidence in matching 'owners.updatedAt' with 'updated_at'.* |

### Mapping: Airbyte `contacts_list_memberships` to Fivetran `contact_list_member`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table mappings suggest a moderate confidence that the source and target tables describe similar subjects. The completion score indicates that some fields are well-mapped, but others are missing mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_list_memberships._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables.* |
| `added_at` | The timestamp a contact was added to a list. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `contact_id` | The ID of the related contact. | `contacts_list_memberships.vid` | 🟢 _0.70_ | *Good match with 'contacts_list_memberships.vid'.* |
| `contact_list_id` | The ID of the related contact list. | `contacts_list_memberships.static_list_id` | 🟢 _0.70_ | *Good match with 'contacts_list_memberships.static_list_id'.* |

### Mapping: Airbyte `companies_property_history` to Fivetran `company_property_history`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table match is strong due to the consistent naming and field availability between the source and target. All fields have been mapped with high confidence except for any potential 'MISSING' fields, which slightly lowers the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `companies_property_history._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `company_id` | The ID of the related company record. | `companies_property_history.companyId` | 🟢 _0.95_ | *High confidence mapping based on consistent naming and usage.* |
| `name` | {{ doc("history_name") }} | `companies_property_history.properties.name` | 🟢 _0.70_ | *Reasonable match based on naming convention and context.* |
| `source` | {{ doc("history_source") }} | `companies_property_history.sourceType` | 🟢 _0.70_ | *Reasonable match based on naming convention and context.* |
| `source_id` | {{ doc("history_source_id") }} | `companies_property_history.sourceId` | 🟢 _0.70_ | *Reasonable match based on naming convention and context.* |
| `timestamp` | {{ doc("history_timestamp") }} | `companies_property_history.timestamp` | 🟢 _0.95_ | *High confidence due to common timestamp usage across schemas.* |
| `value` | {{ doc("history_value") }} | `companies_property_history.value` | 🟢 _0.85_ | *Strong match supported by consistent usage across data sources.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_delivered`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mappings are likely to be very similar due to shared API origins. However, the completion score reflects the slight differences in implementations._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to _airbyte_extracted_at, which is always a perfect match.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _0.80_ | *The ID field is likely to be similar, but due to potential differing usages across systems, a score of 0.8 is appropriate.* |
| `response` | The full response from the recipient's email server. | `email_events.response` | 🟢 _0.70_ | *The response field is matched based on the content expected; however, different systems might use different levels of detail or format.* |
| `smtp_id` | An ID attached to the message by HubSpot. | `email_events.smtpId` | 🟢 _0.75_ | *This ID corresponds to a message-specific identifier used in email systems, and matches are likely but not guaranteed to be identical.* |

### Mapping: Airbyte `contacts_form_submissions` to Fivetran `contact_form_submission`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.88_
- Summary Self-Evaluation: _The table match confidence is high due to the presence of common fields in the source and target tables, such as conversion_id and form_id, which are indicative of form submissions. However, the completion is partly reduced as a result of a 'MISSING' field and some other mapped fields having a close match score instead of perfect._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_form_submissions._airbyte_extracted_at` | 🟢 _1.00_ | *The field '_fivetran_synced' is correctly mapped to '_airbyte_extracted_at' as per standard mapping rules.* |
| `contact_id` | The ID of the related contact. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `conversion_id` | A Unique ID for the specific form conversion. | `contacts_form_submissions.conversion_id` | 🟢 _0.70_ | *Close confidence since 'conversion_id' appears to match correctly with the source.* |
| `form_id` | The GUID of the form that the submission belongs to. | `contacts_form_submissions.form_id` | 🟢 _0.70_ | *Reasonable confidence as 'form_id' corresponds within the submission context.* |
| `page_url` | The URL that the form was submitted on, if applicable. | `contacts_form_submissions.canonical_url` | 🟢 _0.70_ | *Matches with 'canonical_url' reasonably well for a form submission context.* |
| `portal_id` | {{ doc("portal_id") }} | `contacts_form_submissions.portal_id` | 🟢 _0.70_ | *Field 'portal_id' mapped with standard naming conventions.* |
| `timestamp` | A Unix timestamp in milliseconds of the time the submission occurred. | `contacts_form_submissions.timestamp` | 🟢 _0.70_ | *Field 'timestamp' appears to match the context of form submission times.* |
| `title` | The title of the page that the form was submitted on. This will default to the name of the form if no title is provided. | `contacts_form_submissions.page_title` | 🟢 _0.70_ | *Field 'title' matches the common context in form submission metadata.* |

### Mapping: Airbyte `companies` to Fivetran `company`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.86_
- Summary Self-Evaluation: _Table match confidence is reasonably high, considering the target schema's table fields are closely matched with source fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `companies._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables.* |
| `id` | The ID of the company. | `companies.id` | 🟢 _1.00_ | *Exact match found with the corresponding source field.* |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_deleted` | {{ doc("is_deleted") }} | `companies.archived` | 🟢 _0.70_ | *Matches a logical field in the source schema.* |
| `property_name` | The name of the company. | `companies.properties.name` | 🟢 _1.00_ | *Exact match found with the source field.* |
| `property_description` | A short statement about the company's mission and goals. | `companies.properties.description` | 🟢 _1.00_ | *Exact match found based on description.* |
| `property_createdate` | The date the company was added to your account. | `companies.properties.createdate` | 🟢 _1.00_ | *Exact match found based on purpose.* |
| `property_industry` | The type of business the company performs. | `companies.properties.industry` | 🟢 _1.00_ | *Exact match found for describing business type.* |
| `property_address` | The street address of the company. | `companies.properties.address` | 🟢 _1.00_ | *Exact match found for street address.* |
| `property_address_2` | Additional address information for the company. | `companies.properties.address2` | 🟢 _1.00_ | *Matches additional address information.* |
| `property_city` | The city where the company is located. | `companies.properties.city` | 🟢 _1.00_ | *Exact match found for city location.* |
| `property_state` | The state where the company is located. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_country` | The country where the company is located. | `companies.properties.country` | 🟢 _1.00_ | *Exact match found for country location.* |
| `property_annualrevenue` | The actual or estimated annual revenue of the company. | `companies.properties.annualrevenue` | 🟢 _1.00_ | *Exact match found for annual revenue.* |

### Mapping: Airbyte `email_subscriptions` to Fivetran `email_subscription`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _Table mapping between the source and target is a strong match due to alignment of fields and standardized mappings. Completion score is perfect as all required fields are mapped._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_subscriptions._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to '_airbyte_extracted_at' with full confidence.* |
| `active` | Whether the subscription is active. | `email_subscriptions.active` | 🟢 _0.70_ | *Mapped to a field with a closely matching name and plausible function.* |
| `description` | The description of the subscription. | `email_subscriptions.description` | 🟢 _0.70_ | *Mapped to a field with a closely matching name and plausible function.* |
| `id` | The ID of the email subscription. | `email_subscriptions.id` | 🟢 _0.70_ | *Mapped to a field with a closely matching name and plausible function.* |
| `name` | The name of the email subscription. | `email_subscriptions.name` | 🟢 _0.70_ | *Mapped to a field with a closely matching name and plausible function.* |
| `portal_id` | {{ doc("portal_id") }} | `email_subscriptions.portalId` | 🟢 _0.70_ | *Mapped to a field with a closely matching name and plausible function.* |

### Mapping: Airbyte `deal_pipelines` to Fivetran `deal_pipeline`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: 🟢 _0.88_
- Summary Self-Evaluation: _All fields were matched with high confidence, except for _fivetran_deleted which was missing a corresponding match._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deal_pipelines._airbyte_extracted_at` | 🟢 _1.00_ | *_fivetran_synced is always mapped to _airbyte_extracted_at.* |
| `active` | Whether the stage is currently in use. | `deal_pipelines.active` | 🟢 _1.00_ | *Active state has a direct mapping match in target schema.* |
| `display_order` | Used to determine the order in which the pipelines appear when viewed in HubSpot. | `deal_pipelines.displayOrder` | 🟢 _1.00_ | *Display order is mapped correctly to the target field.* |
| `label` | The human-readable label for the pipeline. The label is used when showing the pipeline in HubSpot. | `deal_pipelines.label` | 🟢 _1.00_ | *Label field matches correctly to target schema.* |
| `pipeline_id` | The ID of the pipeline. | `deal_pipelines.pipelineId` | 🟢 _1.00_ | *Pipeline ID field is correctly matched.* |
| `created_at` | A timestamp representing when the record was created. | `deal_pipelines.createdAt` | 🟢 _1.00_ | *Created at timestamp field is well mapped.* |
| `updated_at` | A timestamp representing when the record was updated. | `deal_pipelines.updatedAt` | 🟢 _1.00_ | *Updated at timestamp field is correctly matched.* |

### Mapping: Airbyte `engagements_tasks` to Fivetran `engagement_task`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.83_
- Summary Self-Evaluation: _The table mapping uses similar source and target models with high confidence. However, one field expression is missing, reducing the overall completion._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_tasks._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for '_fivetran_synced' to '_airbyte_extracted_at' with perfect confidence.* |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_hs_createdate` | This field marks the task's time of creation and determines where the task sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_tasks.properties_hs_createdate` | 🟢 _0.70_ | *Mapping is likely correct based on similar meaning of creation date fields.* |
| `timestamp` | This field marks the task's time of occurrence and determines where the task sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_tasks.properties_hs_timestamp` | 🟢 _0.70_ | *Mapping matches timestamp meaning, considering API version context.* |
| `property_hubspot_owner_id` | The ID of the owner associated with the task. This field determines the user listed as the task creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_tasks.properties_hubspot_owner_id` | 🟢 _0.70_ | *Mapping likely correct for owner linkage based on API versioning details.* |
| `property_hubspot_team_id` | The ID of the team associated with the task. This field determines the team listed as the task creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_tasks.properties_hubspot_team_id` | 🟢 _0.70_ | *Mapping likely correct for team linkage given API versioning restrictions.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event_print`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mapping suggests a strong correlation with email events, commonly found in both source and target schemas. Most fields have been appropriately matched to their equivalents._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping from _fivetran_synced to _airbyte_extracted_at.* |
| `browser` | {{ doc("email_event_browser") }} | `email_events.browser` | 🟢 _0.70_ | *'browser' matched directly from 'email_events.browser', which is likely a direct mapping of user browsing data.* |
| `id` | The ID of the event. | `email_events.id` | ⚠️ _0.65_ | *'id' matched to 'email_events.id', typically an identifier field directly shared between schemas.* |
| `ip_address` | {{ doc("email_event_ip_address") }} | `email_events.ipAddress` | 🟢 _0.70_ | *Direct match of 'ip_address' to 'email_events.ipAddress', common mapping for IP recording.* |
| `location` | {{ doc("email_event_location") }} | `email_events.location` | 🟢 _0.70_ | *Matched 'location' to 'email_events.location', generally indicating the same concept.* |
| `user_agent` | {{ doc("email_event_user_agent") }} | `email_events.userAgent` | ⚠️ _0.65_ | *Directly mapped 'user_agent' to 'email_events.userAgent', reflecting similar user metadata tracking.* |

### Mapping: Airbyte `engagements_meetings` to Fivetran `engagement_meeting`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.67_
- Summary Self-Evaluation: _The table mapping is of high quality due to the good alignment between source and target tables. However, the completion score is lower due to one missing field mapping and some field-level uncertainty._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_meetings._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables. Mapped '_fivetran_synced' to source stream's '_airbyte_extracted_at' column.* |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_hs_createdate` | This field marks the meeting's time of creation and determines where the meeting sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_meetings.properties_hs_createdate` | 🟢 _0.70_ | *The expression shows a direct alignment although with slight contextual uncertainties.* |
| `timestamp` | This field marks the meeting's time of occurrence and determines where the meeting sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_meetings.properties_hs_timestamp` | 🟢 _0.70_ | *The expression shows a direct alignment although with slight contextual uncertainties.* |
| `property_hubspot_owner_id` | The ID of the owner associated with the meeting. This field determines the user listed as the meeting creator on the record timeline.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_meetings.properties_hubspot_owner_id` | 🟢 _0.70_ | *The expression shows a direct alignment although with slight contextual uncertainties.* |
| `property_hubspot_team_id` | The ID of the team associated with the meeting. This field determines the team listed as the meeting creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_meetings.properties_hubspot_team_id` | 🟢 _0.70_ | *The expression shows a direct alignment although with slight contextual uncertainties.* |

### Mapping: Airbyte `contacts_merged_audit` to Fivetran `contact_merge_audit`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The source and target tables are highly likely describing the same subject matter since the fields have meaningful mappings. However, there's a missing match affecting the completion score slightly._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_merged_audit._airbyte_extracted_at` | 🟢 _1.00_ | *_fivetran_synced is perfectly mapped to _airbyte_extracted_at as per standard convention.* |
| `canonical_vid` | The contact ID of the contact which the vid_to_merge contact was merged into. | `contacts_merged_audit.canonical_vid` | 🟢 _0.90_ | *The contact ID canonical_vid matches strongly to a similar ID field, indicating a high confidence.* |
| `contact_id` | The ID of the contact. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `entity_id` | The ID of the related entity. | `contacts_merged_audit.entity_id` | 🟢 _0.80_ | *entity_id has a reasonable match with fields in the target schema that relate to entities.* |
| `first_name` | The contact's first name. | `contacts_merged_audit.first_name` | 🟢 _0.80_ | *The first name field aligns well with a similarly purposed field in the target schema.* |
| `last_name` | The contact's last name. | `contacts_merged_audit.last_name` | 🟢 _0.80_ | *The last name field aligns well with a similarly purposed field in the target schema.* |
| `num_properties_moved` | The number of properties which were removed from the merged contact. | `contacts_merged_audit.num_properties_moved` | 🟢 _0.70_ | *The field num_properties_moved relates closely to a count of properties, suggesting reasonable confidence.* |
| `timestamp` | Timestamp of when the contacts were merged. | `contacts_merged_audit.timestamp` | 🟢 _0.85_ | *The timestamp field is a direct match with a similarly intended field in the target.* |
| `user_id` | The ID of the user. | `contacts_merged_audit.user_id` | 🟢 _0.70_ | *user_id matches a user-related field sufficiently, though not perfectly.* |
| `vid_to_merge` | The ID of the contact which was merged. | `contacts_merged_audit.vid_to_merge` | 🟢 _0.90_ | *The field vid_to_merge has a strong correlation with a similar structure in the target.* |

### Mapping: Airbyte `engagements` to Fivetran `engagement`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table mapping shows high match quality with a strong correspondence between most fields. However, some fields from the source schema could not be mapped to the target schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping from '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `active` | Whether the engagement is currently being shown in the UI.  PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.active` | ⚠️ _0.60_ | *Mapped to 'engagements.active' with moderate confidence.* |
| `created_at` | A timestamp representing when the engagement was created.  PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.createdAt` | ⚠️ _0.60_ | *Mapped to 'engagements.createdAt' with moderate confidence.* |
| `id` | The ID of the engagement. | `engagements.id` | 🟢 _0.70_ | *Mapped to 'engagements.id', high confidence due to clear correspondence.* |
| `owner_id` | The ID of the engagement's owner. PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.ownerId` | ⚠️ _0.60_ | *Mapped to 'engagements.ownerId' with moderate confidence.* |
| `portal_id` | {{ doc("portal_id") }} | `engagements.portalId` | ⚠️ _0.60_ | *Mapped to 'engagements.portalId' with moderate confidence.* |
| `timestamp` | A timestamp in representing the time that the engagement should appear in the timeline. PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.  | `engagements.timestamp` | ⚠️ _0.60_ | *Mapped to 'engagements.timestamp' with moderate confidence.* |
| `type` | One of NOTE, EMAIL, TASK, MEETING, or CALL, the type of the engagement. | `engagements.type` | 🟢 _0.70_ | *Mapped to 'engagements.type', high confidence due to distinct field type categories.* |

### Mapping: Airbyte `email_events` to Fivetran `email_event`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The table match score is high because the field mappings consistently relate similar data across both schemas. The completion score is also high, reflecting that each field has been thoughtfully mapped with minimal missing data._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `email_events._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of _fivetran_synced to _airbyte_extracted_at.* |
| `app_id` | The ID of the app that sent the email. | `email_events.appId` | 🟢 _0.90_ | *app_id maps directly to email_events.appId with high confidence due to exact naming and expected context.* |
| `caused_by_created` | The timestamp of the event that caused this event. | `email_events.causedBy.created` | 🟢 _0.90_ | *Field matches email_events.causedBy.created based on context and similar naming structure.* |
| `caused_by_id` | The event ID which uniquely identifies the event which directly caused this event. If not applicable, this property is omitted. | `email_events.causedBy.id` | 🟢 _0.85_ | *Mapping to email_events.causedBy.id, given the context of event causality and ID purpose.* |
| `created` | The created timestamp of the event. | `email_events.created` | 🟢 _0.90_ | *Created timestamp exactly matches email_events.created field.* |
| `email_campaign_id` | The ID of the related email campaign. | `email_events.emailCampaignId` | 🟢 _0.90_ | *Direct match to email_events.emailCampaignId, likely identical due to naming and purpose.* |
| `filtered_event` | A boolean representing whether the event has been filtered out of reporting based on customer reports settings or not. | `email_events.filteredEvent` | 🟢 _0.80_ | *Somewhat clear mapping to email_events.filteredEvent, representing the same filter logic.* |
| `id` | The ID of the event. | `email_events.id` | 🟢 _0.90_ | *Matching event IDs with email_events.id is direct and accurate.* |
| `obsoleted_by_created` | The timestamp of the event that made the current event obsolete. | `email_events.obsoletedBy.created` | 🟢 _0.80_ | *Logically aligns with email_events.obsoletedBy.created; naming suggests a correct match.* |
| `obsoleted_by_id` | The event ID which uniquely identifies the follow-on event which makes this current event obsolete. If not applicable, this property is omitted. | `email_events.obsoletedBy.id` | 🟢 _0.80_ | *Seems to correctly match with email_events.obsoletedBy.id as per the purpose of the field.* |
| `portal_id` | {{ doc("portal_id") }} | `email_events.portalId` | 🟢 _0.85_ | *Likely matches as portal_id is a common field shared across systems, direct naming helps.* |
| `recipient` | The email address of the contact related to the event. | `email_events.recipient` | 🟢 _0.90_ | *Email recipient logically and directly relates to email_events.recipient.* |
| `sent_by_created` | The timestamp of the SENT event related to this event. | `email_events.sentBy.created` | 🟢 _0.85_ | *Sensible mapping with email_events.sentBy.created based on timestamp semantics.* |
| `sent_by_id` | The event ID which uniquely identifies the email message's SENT event. If not applicable, this property is omitted. | `email_events.sentBy.id` | 🟢 _0.85_ | *SentBy ID maps well to email_events.sentBy.id given similar roles in event tracking.* |
| `type` | The type of event. | `email_events.type` | 🟢 _0.90_ | *Event type accurately maps to email_events.type, supported by consistent terminology.* |

### Mapping: Airbyte `engagements_emails` to Fivetran `engagement_email`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The table mapping is evaluated with a relatively high confidence due to the presence of standard mappings like `_fivetran_synced` to `_airbyte_extracted_at` and typical fields seen in similar schemas. However, there are fields that exhibit uncertainty, lowering the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_emails._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of `_fivetran_synced` to `_airbyte_extracted_at`.* |
| `engagement_id` | The ID of the engagement. | `engagements_emails.id` | 🟢 _0.80_ | *Direct mapping with high confidence, common field name indicating unique identifier.* |
| `property_hs_createdate` | This field marks the email's time of creation and determines where the email sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_emails.properties.hs_createdate` | ⚠️ _0.65_ | *Field corresponds to a timestamp, but specific conditions in the description suggest slight differences in data presence.* |
| `timestamp` | This field marks the email's time of occurrence and determines where the email sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_emails.properties_hs_timestamp` | ⚠️ _0.65_ | *Another timestamp field, similar explanation as property_hs_createdate.* |
| `property_hubspot_owner_id` | The ID of the owner associated with the email. This field determines the user listed as the email creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_emails.properties.hubspot_owner_id` | 🟢 _0.70_ | *Likely mapping for owner ID, but conditional existence in description affects confidence.* |
| `property_hubspot_team_id` | The ID of the team associated with the email. This field determines the team listed as the email creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_emails.properties.hubspot_team_id` | 🟢 _0.70_ | *Likely mapping for team ID, but conditional existence in description affects confidence.* |

### Mapping: Airbyte `tickets` to Fivetran `ticket`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.93_
- Summary Self-Evaluation: _The table mapping was evaluated with a high level of confidence due to significant field coverage and strong matching logic between the two systems, despite minor imperfect mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `tickets._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping directly from the source's `_airbyte_extracted_at` column.* |
| `id` | ID of the ticket. | `tickets.id` | 🟢 _0.80_ | *Direct match with `tickets.id`, indicating strong correspondence between source and target hierarchy.* |
| `is_deleted` | Whether the record was deleted (v2 endpoint). | `tickets.archived` | 🟢 _0.70_ | *Mapped to `tickets.archived`, which likely indicates a similar field purpose.* |
| `_fivetran_deleted` | Whether the record was deleted (v3 endpoint). | `tickets.archived` | 🟢 _0.70_ | *Also mapped to `tickets.archived`, showing another potential logical mapping.* |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_closed_date` | The date the ticket was closed. | `tickets.properties.closed_date` | 🟢 _0.90_ | *Mapped to `tickets.properties.closed_date`, indicating direct mapping with proper context.* |
| `property_createdate` | The date the ticket was created. | `tickets.properties_createdate` | 🟢 _0.90_ | *Mapped to `tickets.properties_createdate` with apparent logical equivalence and context correctness.* |
| `property_first_agent_reply_date` | the date for the first agent reply on the ticket. | `tickets.properties_first_agent_reply_date` | 🟢 _0.90_ | *Mapped to `tickets.properties_first_agent_reply_date`, indicating a clear logical match.* |
| `property_hs_pipeline` | The ID of the ticket's pipeline. | `tickets.properties.hs_pipeline` | 🟢 _0.90_ | *Mapped to `tickets.properties.hs_pipeline`, a logical match confirming field integrity.* |
| `property_hs_pipeline_stage` | The ID of the ticket's pipeline stage. | `tickets.properties.hs_pipeline_stage` | 🟢 _0.90_ | *Corresponds directly to `tickets.properties.hs_pipeline_stage`, with strong contextual alignment.* |
| `property_hs_ticket_priority` | The priority of the ticket. | `tickets.properties.hs_ticket_priority` | 🟢 _0.90_ | *Aligned with `tickets.properties.hs_ticket_priority`, serving an identical purpose.* |
| `property_hs_ticket_category` | The category of the ticket. | `tickets.properties.hs_ticket_category` | 🟢 _0.90_ | *Mapped identically to `tickets.properties.hs_ticket_category` with contextual accuracy.* |
| `property_hubspot_owner_id` | The ID of the deal's owner. | `tickets.properties_hubspot_owner_id` | 🟢 _0.90_ | *Mapped to `tickets.properties_hubspot_owner_id`, reflecting identical field usage.* |
| `property_subject` | Short summary of ticket. | `tickets.properties.subject` | 🟢 _0.90_ | *Mapped to `tickets.properties.subject`, demonstrating a strong match.* |
| `property_content` | Text in body of the ticket. | `tickets.properties.content` | 🟢 _0.90_ | *Mapped correctly to `tickets.properties.content`, supporting the mapping's validity.* |
