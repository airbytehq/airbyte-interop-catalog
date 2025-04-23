# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `forms` to Fivetran `form`


- Table Match Confidence Score: ⚠️ _0.65_
- Table Completion Score: ❌ _0.45_
- Summary Self-Evaluation: _The table match score indicates a moderate correlation between the source and target tables. However, the completion score is low, reflecting incomplete field mappings. Overall, this configuration has potential but lacks several key mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `guid` | Unique identifier for the form. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `action` | The form action type or endpoint triggered upon submission. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | Timestamp when the form was created. | `forms.properties.hs_createdate` | 🟢 _0.80_ | *Direct mapping found.* |
| `css_class` | CSS class applied to the form for styling purposes. | `forms.displayOptions.cssClass` | 🟢 _0.70_ | *Direct mapping found.* |
| `follow_up_id` | ID of the follow-up action or workflow triggered by the form. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `form_type` | Category of the form, such as regular, pop-up, or embedded form. | `forms.properties_hs_form_type` | 🟢 _0.80_ | *Direct mapping found.* |
| `lead_nurturing_campaign_id` | ID of the associated lead nurturing campaign, if applicable. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `method` | HTTP method used for form submission (typically POST). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | Name of the form as defined in HubSpot. | `forms.properties_hs_name` | 🟢 _0.80_ | *Direct mapping found.* |
| `notify_recipients` | List of email addresses that receive notifications on form submissions. | `forms.configuration.notifyRecipients` | 🟢 _0.80_ | *Direct mapping found.* |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `redirect` | URL users are redirected to after submitting the form. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `submit_text` | Text displayed on the form's submit button. | `forms.displayOptions.submitButtonText` | 🟢 _0.80_ | *Direct mapping found.* |
| `updated_at` | Timestamp when the form was last updated. | `forms.properties_hs_updated_at` | 🟢 _0.80_ | *Direct mapping found.* |

### Mapping: Airbyte `engagements_emails_web_analytics` to Fivetran `engagement_email`


- Table Match Confidence Score: ⚠️ _0.60_
- Table Completion Score: ❌ _0.17_
- Summary Self-Evaluation: _Table matches partially due to similar upstream source APIs, but field mappings largely incomplete or incorrect._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_emails_web_analytics._airbyte_extracted_at` | 🟢 _1.00_ | *Correct mapping: standard mapping for all tables to Airbyte's system fields.* |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_hs_createdate` | This field marks the email's time of creation and determines where the email sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `timestamp` | This field marks the email's time of occurrence and determines where the email sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_hubspot_owner_id` | The ID of the owner associated with the email. This field determines the user listed as the email creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_hubspot_team_id` | The ID of the team associated with the email. This field determines the team listed as the email creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `engagements_emails` to Fivetran `engagement_email_to`


- Table Match Confidence Score: ⚠️ _0.60_
- Table Completion Score: ❌ _0.20_
- Summary Self-Evaluation: _The table match score is moderately high, suggesting a reasonable likelihood that the source and target tables are describing similar subject matter. However, the completion score is low due to many fields marked as 'MISSING', indicating a lack of complete field mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_emails._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match as '_fivetran_synced' is mapped to a source stream's '_airbyte_extracted_at' column as standard mapping.* |
| `email` | The email address of the recipient. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `engagement_id` | The ID of the related engagement. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `first_name` | The first name of the recipient. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_name` | The last name of the recipient. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `contact_lists` to Fivetran `contact_list`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table match score is moderately high suggesting a good level of similarity between the source and target schemas. However, the completion score is lower due to several fields being marked as 'MISSING', indicating incomplete field mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contact_lists._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables to source stream's _airbyte_extracted_at.* |
| `created_at` | A timestamp of the time the list was created. | `contact_lists.createdAt` | 🟢 _1.00_ | *Direct mapping from 'contact_lists.createdAt' to 'created_at'.* |
| `id` | The ID of the contact list. | `contact_lists.listId` | 🟢 _1.00_ | *Direct mapping from 'contact_lists.listId' to 'id'.* |
| `name` | The name of the contact list. | `contact_lists.name` | 🟢 _1.00_ | *Direct mapping from 'contact_lists.name' to 'name'.* |
| `updated_at` | A timestamp of the time that the list was last modified. | `contact_lists.updatedAt` | 🟢 _1.00_ | *Direct mapping from 'contact_lists.updatedAt' to 'updated_at'.* |
| `created_by_id` | The unique identifier of the user who created the contact list. | `contact_lists.authorId` | 🟢 _0.80_ | *High confidence in mapping from 'contact_lists.authorId' to 'created_by_id' based on both representing user identifiers.* |
| `object_type_id` | The ID that corresponds to the type of object stored by the list. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `processing_status` | Indicates the current status of the list's processing, such as 'COMPLETE', 'PROCESSING', 'DONE', or 'FAILED'. | `contact_lists.metaData.processing` | 🟢 _0.80_ | *High confidence mapping from 'contact_lists.metaData.processing' to 'processing_status' representing the processing state of the list.* |
| `processing_type` | Specifies the type of processing applied to the list, for example, 'STATIC' for static lists or 'DYNAMIC' for dynamic lists. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `list_version` | Represents the version number of the list, incrementing with each modification. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `filters_updated_at` | The timestamp indicating when the list's filters were last updated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `metadata_error` | Any errors that happened the last time the list was processed.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData.error` | ⚠️ _0.60_ | *Conditional match to 'contact_lists.metaData.error'. Note, this field is planned for deprecation.* |
| `metadata_last_processing_state_change_at` | A timestamp of the last time that the processing state changed.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData.lastProcessingStateChangeAt` | ⚠️ _0.60_ | *Conditional match to 'contact_lists.metaData.lastProcessingStateChangeAt'. Note, this field is planned for deprecation.* |
| `metadata_last_size_change_at` | A timestamp of the last time that the size of the list changed.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData.lastSizeChangeAt` | ⚠️ _0.60_ | *Conditional match to 'contact_lists.metaData.lastSizeChangeAt'. Note, this field is planned for deprecation.* |
| `metadata_processing` | One of DONE, REFRESHING, INITIALIZING, or PROCESSING. DONE indicates the list has finished processing, any other value indicates that list membership is being evaluated. NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData.processing` | ⚠️ _0.50_ | *Poor confidence due to potential differences in processing states.* |
| `metadata_size` | The approximate number of contacts in the list. NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData.size` | ⚠️ _0.50_ | *Poor confidence due to variance in size measurements.* |
| `portal_id` | '{{ doc("portal_id") }}' NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.portalId` | ❌ _0.00_ | *No good match found.* |
| `deleteable` | If this is false, this is a system list and cannot be deleted.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.deleteable` | ⚠️ _0.50_ | *Poor confidence due to unclear matching criteria.* |
| `dynamic` | Whether the contact list is dynamic. NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.dynamic` | ⚠️ _0.50_ | *Poor confidence due to unclear matching criteria.* |

### Mapping: Airbyte `ticket_pipelines` to Fivetran `ticket_pipeline`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The overall match of the fields between the source and target tables shows a good alignment, except for some fields that have no direct mapping, affecting the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `ticket_pipelines._airbyte_extracted_at` | 🟢 _1.00_ | *Direct mapping to ticket_pipelines._airbyte_extracted_at as per standard.* |
| `active` | Boolean indicating whether the pipeline is active. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `display_order` | Used to determine the order in which the stages appear when viewed in HubSpot. | `ticket_pipelines.displayOrder` | 🟢 _0.90_ | *High confidence based on similar field usage and context in source and target schemas.* |
| `label` | The human-readable label for the stage. The label is used when showing the stage in HubSpot. | `ticket_pipelines.label` | 🟢 _0.90_ | *The label directly corresponds to the similarly purposed field in the target schema.* |
| `object_type_id` | Reference to the object type. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `pipeline_id` | Reference to the pipeline. | `ticket_pipelines.id` | 🟢 _0.90_ | *Direct mapping found with very high confidence level.* |
| `created_at` | A timestamp representing when the record was created. | `ticket_pipelines.createdAt` | 🟢 _0.90_ | *Direct mapping corresponds centrally to the source created timestamp.* |
| `updated_at` | A timestamp representing when the record was updated. | `ticket_pipelines.updatedAt` | 🟢 _0.90_ | *Direct mapping with high confidence of correctly representing the updated timestamp.* |

### Mapping: Airbyte `contacts_list_memberships` to Fivetran `contact_list_member`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table match score is relatively high due to the likelihood that the source and target tables are describing the same subject matter based on API descriptions. The completion score is moderate as not all possible fields are fully mapped or have high confidence mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_list_memberships._airbyte_extracted_at` | 🟢 _1.00_ | *Standard field mapping for synchronization timestamp.* |
| `added_at` | The timestamp a contact was added to a list. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `contact_id` | The ID of the related contact. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `contact_list_id` | The ID of the related contact list. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `deal_pipelines` to Fivetran `deal_pipeline_stage`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The overall table matching score is moderately high, indicating a general alignment between source and target schemas, but the completion score reveals that not all fields are mapped, indicating gaps in data transformation. Some of the key fields like 'probability', 'stage_id', and '_fivetran_deleted' remain unmapped as 'MISSING', significantly lowering the overall confidence in the data mapping completeness._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deal_pipelines._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables, perfectly matches source column '_airbyte_extracted_at'.* |
| `active` | Whether the pipeline stage is currently in use. | `deal_pipelines.active` | 🟢 _1.00_ | *Exact match found in source schema.* |
| `closed_won` | Whether the stage represents a Closed Won deal. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `display_order` | Used to determine the order in which the stages appear when viewed in HubSpot. | `deal_pipelines.displayOrder` | 🟢 _1.00_ | *Exact match found in source schema.* |
| `label` | The human-readable label for the stage. The label is used when showing the stage in HubSpot. | `deal_pipelines.label` | 🟢 _1.00_ | *Exact match found in source schema.* |
| `pipeline_id` | The ID of the related pipeline. | `deal_pipelines.pipelineId` | 🟢 _1.00_ | *Exact match found in source schema.* |
| `probability` | The probability that the deal will close. Used for the deal forecast. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `stage_id` | The ID of the pipeline stage. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | A timestamp representing when the record was created. | `deal_pipelines.createdAt` | 🟢 _1.00_ | *Exact match found in source schema.* |
| `updated_at` | A timestamp representing when the record was updated. | `deal_pipelines.updatedAt` | 🟢 _1.00_ | *Exact match found in source schema.* |

### Mapping: Airbyte `deals` to Fivetran `deal`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _All field mappings are set to 'MISSING', indicating no confidence in any of the field mappings. There are no valid mappings provided._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `deal_id` | The ID of the deal. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_deleted` | Whether the record was deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deal_pipeline_id` | The ID of the deal's pipeline. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deal_pipeline_stage_id` | The ID of the deal's pipeline stage. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `owner_id` | The ID of the deal's owner. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_dealname` | The name you have given this deal. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_description` | A brief description of the deal. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_amount` | The total value of the deal in the deal's currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_closedate` | The day the deal is expected to close, or was closed. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_createdate` | The date the deal was created. This property is set automatically by HubSpot. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `deals` to Fivetran `deal_stage`


- Table Match Confidence Score: ❌ _0.10_
- Table Completion Score: ❌ _0.12_
- Summary Self-Evaluation: _The table matching and field completion scores are low due to lack of available and matching fields. Most fields have a mapping confidence of 0.00 due to having their expression set to 'MISSING', which indicates no suitable mapping found._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_active` | Boolean indicating whether the deal stage is active. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_end` | The Fivetran calculated exist time of the deal stage. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_start` | The date the deal stage was entered. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `deals._airbyte_extracted_at` | 🟢 _1.00_ | *Direct mapping available to source stream's '_airbyte_extracted_at' column.* |
| `date_entered` | The timestamp the deal stage was entered. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deal_id` | Reference to the deal. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `source` | The relevant source of the deal stage. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `source_id` | Reference to the source. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `value` | The value of the deal stage. Typically the name of the stage. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `marketing_emails` to Fivetran `email_campaign`


- Table Match Confidence Score: ⚠️ _0.65_
- Table Completion Score: ❌ _0.40_
- Summary Self-Evaluation: _The table match score is moderate suggesting some similarity between source and target schemas. However, many key fields are missing accurate mappings, indicating a low completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `marketing_emails._airbyte_extracted_at` | 🟢 _1.00_ | *Direct matching standard field '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `app_id` | The app ID. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `app_name` | The app name. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `content_id` | The ID of the content. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | The ID of the email campaign. | `marketing_emails.id` | 🟢 _1.00_ | *Exact match of 'id' field in both schemas.* |
| `name` | The name of the email campaign. | `marketing_emails.name` | 🟢 _1.00_ | *Exact match of 'name' field in both schemas.* |
| `num_included` | The number of messages included as part of the email campaign. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `num_queued` | The number of messages queued as part of the email campaign. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sub_type` | The email campaign sub-type. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `subject` | The subject of the email campaign. | `marketing_emails.subject` | 🟢 _1.00_ | *Exact match of 'subject' field in both schemas.* |
| `type` | The email campaign type. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `contacts` to Fivetran `deal_contact`


- Table Match Confidence Score: ⚠️ _0.60_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table match score suggests a moderate level of confidence that the source and target schemas are describing the same subject matter, but the incomplete field mapping reduces the overall completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts._airbyte_extracted_at` | 🟢 _1.00_ | *Exact match between '_fivetran_synced' and 'contacts._airbyte_extracted_at'. Standard mapping for all tables.* |
| `contact_id` | The ID of the contact. | `contacts.id` | 🟢 _1.00_ | *Exact match, this ID mapping is critical for data integrity.* |
| `deal_id` | The ID of the deal. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `type_id` | The ID of the type. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `category` | The association category. Either HUBSPOT_DEFINED (default label) or USER_DEFINED (custom label). | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `subscription_changes` to Fivetran `email_subscription_change`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.57_
- Summary Self-Evaluation: _The table mapping shows moderate-to-high confidence that the source and target tables are describing the same subject matter. However, several field mappings are missing, which reduces the completion score significantly._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `subscription_changes._airbyte_extracted_at` | 🟢 _1.00_ | *Direct mapping was available for '_fivetran_synced' to 'subscription_changes._airbyte_extracted_at'.* |
| `caused_by_event_id` | The ID of the event that caused the subscription change. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `change` | The change which occurred. This enumeration is specific to the 'changeType'; see below for the possible values. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `change_type` | The type of change which occurred. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email_subscription_id` | The ID of the related email subscription. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `portal_id` | {{ doc("portal_id") }} | `subscription_changes.portalId` | 🟢 _0.80_ | *Existing mapping to 'subscription_changes.portalId' provides high confidence.* |
| `recipient` | The email address of the related contact. | `subscription_changes.recipient` | 🟢 _0.80_ | *Existing mapping to 'subscription_changes.recipient' provides high confidence.* |
| `source` | The source of the subscription change. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `timestamp` | The timestamp when this change occurred. If 'causedByEvent' is present, this will be absent. | `subscription_changes.timestamp` | 🟢 _0.80_ | *Existing mapping to 'subscription_changes.timestamp' provides high confidence.* |

### Mapping: Airbyte `ticket_pipelines` to Fivetran `ticket_pipeline_stage`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The mappings cover most of the essential field mappings with high confidence due to some fields directly matching. However, some fields like 'is_closed' and 'ticket_state' lack expanding data which lowers the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `ticket_pipelines._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match to the schema expected value.* |
| `active` | Boolean indicating whether the pipeline stage is active. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `display_order` | Used to determine the order in which the stages appear when viewed in HubSpot. | `ticket_pipelines.displayOrder` | 🟢 _0.90_ | *Direct mapping exists with proper naming conventions.* |
| `is_closed` | Boolean indicating if the pipeline stage is closed. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `label` | The human-readable label for the stage. The label is used when showing the stage in HubSpot. | `ticket_pipelines.label` | 🟢 _0.90_ | *Direct mapping exists which perfectly aligns with source API field.* |
| `pipeline_id` | The ID of the pipeline. | `ticket_pipelines.id` | 🟢 _0.90_ | *Direct mapping identified with accurate field correlation.* |
| `stage_id` | The ID of the pipeline stage. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `ticket_state` | State of the ticket. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | A timestamp representing when the record was created. | `ticket_pipelines.createdAt` | 🟢 _0.90_ | *Direct mapping identified with accurate time field correlation.* |
| `updated_at` | A timestamp representing when the record was updated. | `ticket_pipelines.updatedAt` | 🟢 _0.90_ | *Accurate mapping of time fields indicating up-to-date record tracking.* |
