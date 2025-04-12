# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `forms` to Fivetran `form`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.69_
- Summary Self-Evaluation: _The table mapping score is high because the tables share many common fields, indicating they likely describe similar subjects. However, the completion score is lower due to several fields mapped as 'MISSING'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `forms._airbyte_extracted_at` | 🟢 _1.00_ | *Consistently maps to '_airbyte_extracted_at'.* |
| `created_at` | A timestamp for when the form was created. | `forms.createdAt` | 🟢 _0.80_ | *Mapped to a corresponding timestamp for creation within forms.* |
| `css_class` | The CSS classes assigned to the form. | `forms.displayOptions.cssClass` | 🟢 _0.70_ | *Assigned CSS classes are mapped to a similarly structured path.* |
| `follow_up_id` | This field is no longer used. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `guid` | The internal ID of the form. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `lead_nurturing_campaign_id` | TBD | `forms.properties.hs_marketing_campaign_guid` | ⚠️ _0.60_ | *Mapping to a marketing campaign GUID is a possible but uncertain match.* |
| `method` | This field is no longer used. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | The name of the form. | `forms.name` | 🟢 _0.90_ | *Mapped directly to the form's name, indicating a strong match.* |
| `notify_recipients` | A comma-separated list of user IDs that should receive submission notifications. Email addresses will be returned for individuals who aren't users.  | `forms.configuration.notifyRecipients` | 🟢 _0.80_ | *Correctly identifies a list of user IDs for notifications within the forms.* |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `redirect` | The URL that the visitor will be redirected to after filling out the form. | `forms.configuration.postSubmitAction.value` | 🟢 _0.80_ | *Mapped to a post-submit URL, reflecting the described functionality.* |
| `submit_text` | The text used for the submit button. | `forms.displayOptions.submitButtonText` | 🟢 _0.70_ | *Submit button text mapping aligns with function.* |
| `updated_at` | A timestamp for when the form was last updated. | `forms.updatedAt` | 🟢 _0.80_ | *Mapped to a corresponding timestamp for updates within forms.* |

### Mapping: Airbyte `subscription_changes` to Fivetran `email_subscription_change`


- Table Match Confidence Score: ⚠️ _0.65_
- Table Completion Score: ❌ _0.25_
- Summary Self-Evaluation: _The table match score indicates a moderate level of confidence that the source and target tables describe similar subject matter. The completion score is low due to multiple 'MISSING' expressions for field mappings, which suggests incomplete mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `subscription_changes._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping rule applied: '_fivetran_synced' is always mapped to '_airbyte_extracted_at'. No penalty or reward.* |
| `caused_by_event_id` | The ID of the event that caused the subscription change. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `change` | The change which occurred. This enumeration is specific to the 'changeType'; see below for the possible values. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `change_type` | The type of change which occurred. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email_subscription_id` | The ID of the related email subscription. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `portal_id` | {{ doc("portal_id") }} | `subscription_changes.portalId` | ⚠️ _0.65_ | *Mapping is considered likely since 'portal_id' matches 'subscription_changes.portalId'.* |
| `recipient` | The email address of the related contact. | `subscription_changes.recipient` | ⚠️ _0.65_ | *Mapping is considered likely since 'recipient' matches 'subscription_changes.recipient'.* |
| `source` | The source of the subscription change. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `timestamp` | The timestamp when this change occurred. If 'causedByEvent' is present, this will be absent. | `subscription_changes.timestamp` | ⚠️ _0.65_ | *Mapping is considered likely since 'timestamp' matches 'subscription_changes.timestamp'.* |

### Mapping: Airbyte `contact_lists` to Fivetran `contact_list`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table match is relatively strong due to shared data origin (API), but not all fields are present in the source._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contact_lists._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to source stream's '_airbyte_extracted_at' column.* |
| `created_at` | A timestamp of the time the list was created. | `contact_lists.createdAt` | 🟢 _0.90_ | *Timestamps align well between 'createdAt' and 'created_at'.* |
| `id` | The ID of the contact list. | `contact_lists.listId` | 🟢 _0.90_ | *IDs align well between 'listId' and 'id'.* |
| `name` | The name of the contact list. | `contact_lists.name` | 🟢 _0.90_ | *Names align between 'name' and 'name'.* |
| `updated_at` | A timestamp of the time that the list was last modified. | `contact_lists.updatedAt` | 🟢 _0.90_ | *Timestamps align well between 'updatedAt' and 'updated_at'.* |
| `created_by_id` | The unique identifier of the user who created the contact list. | `contact_lists.authorId` | 🟢 _0.80_ | *Good match between 'authorId' and 'created_by_id'.* |
| `object_type_id` | The ID that corresponds to the type of object stored by the list. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `processing_status` | Indicates the current status of the list's processing, such as 'COMPLETE', 'PROCESSING', 'DONE', or 'FAILED'. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `processing_type` | Specifies the type of processing applied to the list, for example, 'STATIC' for static lists or 'DYNAMIC' for dynamic lists. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `list_version` | Represents the version number of the list, incrementing with each modification. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `filters_updated_at` | The timestamp indicating when the list's filters were last updated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `metadata_error` | Any errors that happened the last time the list was processed.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData_error` | 🟢 _0.70_ | *Deprecation notice: field may not be populated in future.* |
| `metadata_last_processing_state_change_at` | A timestamp of the last time that the processing state changed.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData_lastProcessingStateChangeAt` | 🟢 _0.70_ | *Deprecation notice: field may not be populated in future.* |
| `metadata_last_size_change_at` | A timestamp of the last time that the size of the list changed.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData_lastSizeChangeAt` | 🟢 _0.70_ | *Deprecation notice: field may not be populated in future.* |
| `metadata_processing` | One of DONE, REFRESHING, INITIALIZING, or PROCESSING. DONE indicates the list has finished processing, any other value indicates that list membership is being evaluated. NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData_processing` | 🟢 _0.70_ | *Deprecation notice: field may not be populated in future.* |
| `metadata_size` | The approximate number of contacts in the list. NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.metaData_size` | 🟢 _0.70_ | *Deprecation notice: field may not be populated in future.* |
| `portal_id` | '{{ doc("portal_id") }}' NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.portalId` | 🟢 _0.70_ | *Deprecation notice: field may not be populated in future.* |
| `deleteable` | If this is false, this is a system list and cannot be deleted.  NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.deleteable` | 🟢 _0.70_ | *Deprecation notice: field may not be populated in future.* |
| `dynamic` | Whether the contact list is dynamic. NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.  | `contact_lists.dynamic` | 🟢 _0.70_ | *Deprecation notice: field may not be populated in future.* |

### Mapping: Airbyte `deals` to Fivetran `deal`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The table mapping reflects a generally good match between source and target tables, as most fields are correctly mapped. However, there are a few fields that could not be matched and are marked as 'MISSING', which affects completion._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `deal_id` | The ID of the deal. | `deals.properties.hs_object_id` | 🟢 _0.90_ | *Matched field 'deal_id' confidently.* |
| `is_deleted` | Whether the record was deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `portal_id` | {{ doc("portal_id") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deal_pipeline_id` | The ID of the deal's pipeline. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deal_pipeline_stage_id` | The ID of the deal's pipeline stage. | `deals.properties.dealstage` | 🟢 _0.85_ | *Matched field 'deal_pipeline_stage_id' confidently.* |
| `owner_id` | The ID of the deal's owner. | `deals.properties_hubspot_owner_id` | 🟢 _0.85_ | *Matched field 'owner_id' confidently.* |
| `property_dealname` | The name you have given this deal. | `deals.properties.dealname` | 🟢 _0.90_ | *Matched field 'property_dealname' confidently.* |
| `property_description` | A brief description of the deal. | `deals.properties.description` | 🟢 _0.90_ | *Matched field 'property_description' confidently.* |
| `property_amount` | The total value of the deal in the deal's currency. | `deals.properties.amount` | 🟢 _0.90_ | *Matched field 'property_amount' confidently.* |
| `property_closedate` | The day the deal is expected to close, or was closed. | `deals.properties.closedate` | 🟢 _0.90_ | *Matched field 'property_closedate' confidently.* |
| `property_createdate` | The date the deal was created. This property is set automatically by HubSpot. | `deals.properties.createdate` | 🟢 _0.90_ | *Matched field 'property_createdate' confidently.* |

### Mapping: Airbyte `engagements_calls` to Fivetran `engagement_call`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ❌ _0.43_
- Summary Self-Evaluation: _The table match score is relatively high due to the commonality in the API usage and consistent field naming conventions between source and target schemas. However, the completion score is low due to missing expressions in key fields, which significantly impacts the ability to map data comprehensively._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `engagements_calls._airbyte_extracted_at` | 🟢 _1.00_ | *_fivetran_synced is mapped to a source stream's _airbyte_extracted_at column, which is a standard mapping.* |
| `engagement_id` | The ID of the engagement. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_deleted` | Boolean to mark rows that were deleted in the source database. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_hs_createdate` | This field marks the call's time of creation and determines where the call sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_calls.properties.hs_createdate` | 🟢 _0.70_ | *This field has a fairly direct matching in the source properties.* |
| `timestamp` | This field marks the call's time of occurrence and determines where the call sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.  PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `property_hubspot_owner_id` | The ID of the owner associated with the call. This field determines the user listed as the call creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.  | `engagements_calls.properties.hubspot_owner_id` | 🟢 _0.70_ | *This field has a moderate confidence match based on the HubSpot API version context.* |
| `property_hubspot_team_id` | The ID of the team associated with the call. This field determines the team listed as the call creator on the record timeline. PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.  | `engagements_calls.properties.hubspot_team_id` | 🟢 _0.70_ | *This field has a moderate confidence match based on the HubSpot API version context.* |

### Mapping: Airbyte `contacts_property_history` to Fivetran `contact_property_history`


- Table Match Confidence Score: ⚠️ _0.60_
- Table Completion Score: ❌ _0.43_
- Summary Self-Evaluation: _The mapping involves 7 fields, out of which 4 had direct matches. However, 3 fields are marked as 'MISSING', significantly reducing the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `contacts_property_history._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for '_fivetran_synced' to source stream's '_airbyte_extracted_at'.* |
| `contact_id` | The ID of the related contact record. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | {{ doc("history_name") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `source` | {{ doc("history_source") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `source_id` | {{ doc("history_source_id") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `timestamp` | {{ doc("history_timestamp") }} | `contacts_property_history.timestamp` | 🟢 _0.70_ | *Reasonable confidence that 'contacts_property_history.timestamp' is the correct mapping.* |
| `value` | {{ doc("history_value") }} | `contacts_property_history.value` | 🟢 _0.70_ | *Reasonable confidence that 'contacts_property_history.value' is the correct mapping.* |

### Mapping: Airbyte `ticket_pipelines` to Fivetran `ticket_pipeline`


- Table Match Confidence Score: ⚠️ _0.65_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table and field mappings include several 'MISSING' entries, indicating incomplete mapping. However, certain fields like '_fivetran_synced' have confident mappings based on standard conventions. Moreover, fields like 'display_order', 'label', 'created_at', and 'updated_at' have plausible mappings, albeit with less confidence due to lack of complete corroboration across source and target schemas._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc("_fivetran_deleted") }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc("_fivetran_synced") }} | `ticket_pipelines._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to '_airbyte_extracted_at' column.* |
| `active` | Boolean indicating whether the pipeline is active. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `display_order` | Used to determine the order in which the stages appear when viewed in HubSpot. | `ticket_pipelines.displayOrder` | ⚠️ _0.65_ | *Mapped to 'ticket_pipelines.displayOrder', indicating similar intents.* |
| `label` | The human-readable label for the stage. The label is used when showing the stage in HubSpot. | `ticket_pipelines.label` | ⚠️ _0.65_ | *Mapped to 'ticket_pipelines.label', indicating similar intents.* |
| `object_type_id` | Reference to the object type. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `pipeline_id` | Reference to the pipeline. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | A timestamp representing when the record was created. | `ticket_pipelines.createdAt` | ⚠️ _0.65_ | *Timestamp mapped to 'ticket_pipelines.createdAt', consistent with documentation.* |
| `updated_at` | A timestamp representing when the record was updated. | `ticket_pipelines.updatedAt` | ⚠️ _0.65_ | *Timestamp mapped to 'ticket_pipelines.updatedAt', consistent with documentation.* |
