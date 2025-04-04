# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

## contact_property_history




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| contacts_property_history | hubspot | contacts_property_history |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | contacts_property_history._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| contact_id | MISSING | The ID of the related contact record. |
| name | MISSING | {{ doc("history_name") }} |
| source | MISSING | {{ doc("history_source") }} |
| source_id | MISSING | {{ doc("history_source_id") }} |
| timestamp | contacts_property_history.timestamp | {{ doc("history_timestamp") }} |
| value | contacts_property_history.value | {{ doc("history_value") }} |



## email_event




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| email_events | hubspot | email_events |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | email_events._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| app_id | email_events.appId | The ID of the app that sent the email. |
| caused_by_created | email_events.causedBy.created | The timestamp of the event that caused this event. |
| caused_by_id | email_events.causedBy.id | The event ID which uniquely identifies the event which directly caused this event. If not applicable, this property is omitted. |
| created | email_events.created | The created timestamp of the event. |
| email_campaign_id | email_events.emailCampaignId | The ID of the related email campaign. |
| filtered_event | email_events.filteredEvent | A boolean representing whether the event has been filtered out of reporting based on customer reports settings or not. |
| id | email_events.id | The ID of the event. |
| obsoleted_by_created | email_events.obsoletedBy.created | The timestamp of the event that made the current event obsolete. |
| obsoleted_by_id | email_events.obsoletedBy.id | The event ID which uniquely identifies the follow-on event which makes this current event obsolete. If not applicable, this property is omitted. |
| portal_id | email_events.portalId | {{ doc("portal_id") }} |
| recipient | email_events.recipient | The email address of the contact related to the event. |
| sent_by_created | email_events.sentBy.created | The timestamp of the SENT event related to this event. |
| sent_by_id | email_events.sentBy.id | The event ID which uniquely identifies the email message's SENT event. If not applicable, this property is omitted. |
| type | email_events.type | The type of event. |



## deal_pipeline




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| deal_pipelines | hubspot | deal_pipelines |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc("_fivetran_deleted") }} |
| _fivetran_synced | deal_pipelines._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| active | deal_pipelines.active | Whether the stage is currently in use. |
| display_order | deal_pipelines.displayOrder | Used to determine the order in which the pipelines appear when viewed in HubSpot. |
| label | deal_pipelines.label | The human-readable label for the pipeline. The label is used when showing the pipeline in HubSpot. |
| pipeline_id | deal_pipelines.pipelineId | The ID of the pipeline. |
| created_at | deal_pipelines.createdAt | A timestamp representing when the record was created. |
| updated_at | deal_pipelines.updatedAt | A timestamp representing when the record was updated. |



## form




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| forms | hubspot | forms |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc("_fivetran_deleted") }} |
| _fivetran_synced | forms._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| created_at | forms.createdAt | A timestamp for when the form was created. |
| css_class | forms.displayOptions.cssClass | The CSS classes assigned to the form. |
| follow_up_id | MISSING | This field is no longer used. |
| guid | MISSING | The internal ID of the form. |
| lead_nurturing_campaign_id | forms.properties.hs_marketing_campaign_guid | TBD |
| method | MISSING | This field is no longer used. |
| name | forms.name | The name of the form. |
| notify_recipients | forms.configuration.notifyRecipients | A comma-separated list of user IDs that should receive submission notifications.
Email addresses will be returned for individuals who aren't users.
 |
| portal_id | MISSING | {{ doc("portal_id") }} |
| redirect | forms.configuration.postSubmitAction.value | The URL that the visitor will be redirected to after filling out the form. |
| submit_text | forms.displayOptions.submitButtonText | The text used for the submit button. |
| updated_at | forms.updatedAt | A timestamp for when the form was last updated. |



## email_event_print




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| email_events | hubspot | email_events |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | email_events._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| browser | email_events.browser | {{ doc("email_event_browser") }} |
| id | email_events.id | The ID of the event. |
| ip_address | email_events.ipAddress | {{ doc("email_event_ip_address") }} |
| location | email_events.location | {{ doc("email_event_location") }} |
| user_agent | email_events.userAgent | {{ doc("email_event_user_agent") }} |



## engagement_email




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| engagements_emails | hubspot | engagements_emails |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | engagements_emails._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| engagement_id | engagements_emails.id | The ID of the engagement. |
| property_hs_createdate | engagements_emails.properties.hs_createdate | This field marks the email's time of creation and determines where the email sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| timestamp | engagements_emails.properties_hs_timestamp | This field marks the email's time of occurrence and determines where the email sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| property_hubspot_owner_id | engagements_emails.properties.hubspot_owner_id | The ID of the owner associated with the email. This field determines the user listed as the email creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| property_hubspot_team_id | engagements_emails.properties.hubspot_team_id | The ID of the team associated with the email. This field determines the team listed as the email creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.
 |



## contact_list




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| contact_lists | hubspot | contact_lists |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc("_fivetran_deleted") }} |
| _fivetran_synced | contact_lists._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| created_at | contact_lists.createdAt | A timestamp of the time the list was created. |
| id | contact_lists.listId | The ID of the contact list. |
| name | contact_lists.name | The name of the contact list. |
| updated_at | contact_lists.updatedAt | A timestamp of the time that the list was last modified. |
| created_by_id | contact_lists.authorId | The unique identifier of the user who created the contact list. |
| object_type_id | MISSING | The ID that corresponds to the type of object stored by the list. |
| processing_status | MISSING | Indicates the current status of the list's processing, such as 'COMPLETE', 'PROCESSING', 'DONE', or 'FAILED'. |
| processing_type | MISSING | Specifies the type of processing applied to the list, for example, 'STATIC' for static lists or 'DYNAMIC' for dynamic lists. |
| list_version | MISSING | Represents the version number of the list, incrementing with each modification. |
| filters_updated_at | MISSING | The timestamp indicating when the list's filters were last updated. |
| metadata_error | contact_lists.metaData_error | Any errors that happened the last time the list was processed.
 NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 |
| metadata_last_processing_state_change_at | contact_lists.metaData_lastProcessingStateChangeAt | A timestamp of the last time that the processing state changed.
 NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 |
| metadata_last_size_change_at | contact_lists.metaData_lastSizeChangeAt | A timestamp of the last time that the size of the list changed.
 NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 |
| metadata_processing | contact_lists.metaData_processing | One of DONE, REFRESHING, INITIALIZING, or PROCESSING. DONE indicates the list has finished processing, any other value indicates that list membership is being evaluated.
NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 |
| metadata_size | contact_lists.metaData_size | The approximate number of contacts in the list.
NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 |
| portal_id | contact_lists.portalId | '{{ doc("portal_id") }}'
NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 |
| deleteable | contact_lists.deleteable | If this is false, this is a system list and cannot be deleted.
 NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 |
| dynamic | contact_lists.dynamic | Whether the contact list is dynamic.
NOTE: This field is deprecated and will not be populated for connectors utilizing the HubSpot v3 API. This field will be removed in a future release.
 |



## ticket_pipeline




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ticket_pipelines | hubspot | ticket_pipelines |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc("_fivetran_deleted") }} |
| _fivetran_synced | ticket_pipelines._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| active | MISSING | Boolean indicating whether the pipeline is active. |
| display_order | ticket_pipelines.displayOrder | Used to determine the order in which the stages appear when viewed in HubSpot. |
| label | ticket_pipelines.label | The human-readable label for the stage. The label is used when showing the stage in HubSpot. |
| object_type_id | MISSING | Reference to the object type. |
| pipeline_id | MISSING | Reference to the pipeline. |
| created_at | ticket_pipelines.createdAt | A timestamp representing when the record was created. |
| updated_at | ticket_pipelines.updatedAt | A timestamp representing when the record was updated. |



## engagement_note




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| engagements_notes | hubspot | engagements_notes |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | engagements_notes._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| body | engagements_notes.properties.hs_note_body | The body of the note. The body has a limit of 65536 characters. |
| engagement_id | MISSING | The ID of the engagement. |
| property_hs_createdate | engagements_notes.properties.hs_createdate | This field marks the note's time of creation and determines where the note sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| timestamp | engagements_notes.properties.hs_timestamp | This field marks the note's time of occurrence and determines where the note sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| property_hubspot_owner_id | engagements_notes.properties.hubspot_owner_id | The ID of the owner associated with the note. This field determines the user listed as the note creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| property_hubspot_team_id | engagements_notes.properties.hubspot_team_id | The ID of the team associated with the note. This field determines the team listed as the note creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.
 |



## email_event_delivered




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| email_events | hubspot | email_events |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | email_events._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| id | email_events.id | The ID of the event. |
| response | email_events.response | The full response from the recipient's email server. |
| smtp_id | email_events.smtpId | An ID attached to the message by HubSpot. |



## company




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| companies | hubspot | companies |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | companies._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| id | companies.id | The ID of the company. |
| portal_id | MISSING | {{ doc("portal_id") }} |
| is_deleted | companies.archived | {{ doc("is_deleted") }} |
| property_name | companies.properties.name | The name of the company. |
| property_description | companies.properties.description | A short statement about the company's mission and goals. |
| property_createdate | companies.properties.createdate | The date the company was added to your account. |
| property_industry | companies.properties.industry | The type of business the company performs. |
| property_address | companies.properties.address | The street address of the company. |
| property_address_2 | companies.properties.address2 | Additional address information for the company. |
| property_city | companies.properties.city | The city where the company is located. |
| property_state | MISSING | The state where the company is located. |
| property_country | companies.properties.country | The country where the company is located. |
| property_annualrevenue | companies.properties.annualrevenue | The actual or estimated annual revenue of the company. |



## contact_list_member




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| contacts_list_memberships | hubspot | contacts_list_memberships |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc("_fivetran_deleted") }} |
| _fivetran_synced | contacts_list_memberships._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| added_at | MISSING | The timestamp a contact was added to a list. |
| contact_id | contacts_list_memberships.vid | The ID of the related contact. |
| contact_list_id | contacts_list_memberships.static_list_id | The ID of the related contact list. |



## engagement_meeting




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| engagements_meetings | hubspot | engagements_meetings |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | engagements_meetings._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| engagement_id | MISSING | The ID of the engagement. |
| property_hs_createdate | engagements_meetings.properties_hs_createdate | This field marks the meeting's time of creation and determines where the meeting sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| timestamp | engagements_meetings.properties_hs_timestamp | This field marks the meeting's time of occurrence and determines where the meeting sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| property_hubspot_owner_id | engagements_meetings.properties_hubspot_owner_id | The ID of the owner associated with the meeting. This field determines the user listed as the meeting creator on the record timeline.
 PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| property_hubspot_team_id | engagements_meetings.properties_hubspot_team_id | The ID of the team associated with the meeting. This field determines the team listed as the meeting creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.
 |



## engagement_task




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| engagements_tasks | hubspot | engagements_tasks |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | engagements_tasks._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| engagement_id | MISSING | The ID of the engagement. |
| property_hs_createdate | engagements_tasks.properties_hs_createdate | This field marks the task's time of creation and determines where the task sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| timestamp | engagements_tasks.properties_hs_timestamp | This field marks the task's time of occurrence and determines where the task sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| property_hubspot_owner_id | engagements_tasks.properties_hubspot_owner_id | The ID of the owner associated with the task. This field determines the user listed as the task creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| property_hubspot_team_id | engagements_tasks.properties_hubspot_team_id | The ID of the team associated with the task. This field determines the team listed as the task creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.
 |



## ticket




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| tickets | hubspot | tickets |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | tickets._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| id | tickets.id | ID of the ticket. |
| is_deleted | tickets.archived | Whether the record was deleted (v2 endpoint). |
| _fivetran_deleted | tickets.archived | Whether the record was deleted (v3 endpoint). |
| portal_id | MISSING | {{ doc("portal_id") }} |
| property_closed_date | tickets.properties.closed_date | The date the ticket was closed. |
| property_createdate | tickets.properties_createdate | The date the ticket was created. |
| property_first_agent_reply_date | tickets.properties_first_agent_reply_date | the date for the first agent reply on the ticket. |
| property_hs_pipeline | tickets.properties.hs_pipeline | The ID of the ticket's pipeline. |
| property_hs_pipeline_stage | tickets.properties.hs_pipeline_stage | The ID of the ticket's pipeline stage. |
| property_hs_ticket_priority | tickets.properties.hs_ticket_priority | The priority of the ticket. |
| property_hs_ticket_category | tickets.properties.hs_ticket_category | The category of the ticket. |
| property_hubspot_owner_id | tickets.properties_hubspot_owner_id | The ID of the deal's owner. |
| property_subject | tickets.properties.subject | Short summary of ticket. |
| property_content | tickets.properties.content | Text in body of the ticket. |



## engagement_call




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| engagements_calls | hubspot | engagements_calls |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | engagements_calls._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| engagement_id | MISSING | The ID of the engagement. |
| _fivetran_deleted | MISSING | Boolean to mark rows that were deleted in the source database. |
| property_hs_createdate | engagements_calls.properties.hs_createdate | This field marks the call's time of creation and determines where the call sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| timestamp | MISSING | This field marks the call's time of occurrence and determines where the call sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| property_hubspot_owner_id | engagements_calls.properties.hubspot_owner_id | The ID of the owner associated with the call. This field determines the user listed as the call creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version. For the pre HubSpot v3 versions, this value may be found within the parent `engagement` table.
 |
| property_hubspot_team_id | engagements_calls.properties.hubspot_team_id | The ID of the team associated with the call. This field determines the team listed as the call creator on the record timeline.
PLEASE NOTE: This field will only be populated for connectors utilizing the HubSpot v3 API version.
 |



## deal




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| deals | hubspot | deals |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| deal_id | deals.properties.hs_object_id | The ID of the deal. |
| is_deleted | MISSING | Whether the record was deleted. |
| portal_id | MISSING | {{ doc("portal_id") }} |
| deal_pipeline_id | MISSING | The ID of the deal's pipeline. |
| deal_pipeline_stage_id | deals.properties.dealstage | The ID of the deal's pipeline stage. |
| owner_id | deals.properties_hubspot_owner_id | The ID of the deal's owner. |
| property_dealname | deals.properties.dealname | The name you have given this deal. |
| property_description | deals.properties.description | A brief description of the deal. |
| property_amount | deals.properties.amount | The total value of the deal in the deal's currency. |
| property_closedate | deals.properties.closedate | The day the deal is expected to close, or was closed. |
| property_createdate | deals.properties.createdate | The date the deal was created. This property is set automatically by HubSpot. |



## email_subscription




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| email_subscriptions | hubspot | email_subscriptions |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | email_subscriptions._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| active | email_subscriptions.active | Whether the subscription is active. |
| description | email_subscriptions.description | The description of the subscription. |
| id | email_subscriptions.id | The ID of the email subscription. |
| name | email_subscriptions.name | The name of the email subscription. |
| portal_id | email_subscriptions.portalId | {{ doc("portal_id") }} |



## contact




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| contacts | hubspot | contacts |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc("_fivetran_deleted") }} |
| _fivetran_synced | contacts._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| id | contacts.id | The ID of the contact. |
| property_email_1 | contacts.properties_email | The email address of the contact. |
| property_company | contacts.properties_company | The name of the contact's company. |
| property_firstname | contacts.properties_firstname | The contact's first name. |
| property_lastname | contacts.properties_lastname | The contact's last name. |
| property_email | contacts.properties_email | The contact's email. |
| property_createdate | contacts.properties_createdate | The date that the contact was created in your HubSpot account. |
| property_jobtitle | contacts.properties_jobtitle | The contact's job title. |
| property_annualrevenue | contacts.properties_annualrevenue | The contact's annual company revenue. |
| property_hs_calculated_merged_vids | contacts.properties_hs_calculated_merged_vids | List of mappings representing contact IDs that have been merged into the contact at hand. Format: <merged_contact_id>:<merged_at_in_epoch_time>;<second_merged_contact_id>:<merged_at_in_epoch_time> This field has replaced the `CONTACT_MERGE_AUDIT` table, which was deprecated by the Hubspot v3 CRM API.
 |



## email_subscription_change




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| subscription_changes | hubspot | subscription_changes |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | subscription_changes._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| caused_by_event_id | MISSING | The ID of the event that caused the subscription change. |
| change | MISSING | The change which occurred. This enumeration is specific to the 'changeType'; see below for the possible values. |
| change_type | MISSING | The type of change which occurred. |
| email_subscription_id | MISSING | The ID of the related email subscription. |
| portal_id | subscription_changes.portalId | {{ doc("portal_id") }} |
| recipient | subscription_changes.recipient | The email address of the related contact. |
| source | MISSING | The source of the subscription change. |
| timestamp | subscription_changes.timestamp | The timestamp when this change occurred. If 'causedByEvent' is present, this will be absent. |



## contact_merge_audit




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| contacts_merged_audit | hubspot | contacts_merged_audit |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | contacts_merged_audit._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| canonical_vid | contacts_merged_audit.canonical_vid | The contact ID of the contact which the vid_to_merge contact was merged into. |
| contact_id | MISSING | The ID of the contact. |
| entity_id | contacts_merged_audit.entity_id | The ID of the related entity. |
| first_name | contacts_merged_audit.first_name | The contact's first name. |
| last_name | contacts_merged_audit.last_name | The contact's last name. |
| num_properties_moved | contacts_merged_audit.num_properties_moved | The number of properties which were removed from the merged contact. |
| timestamp | contacts_merged_audit.timestamp | Timestamp of when the contacts were merged. |
| user_id | contacts_merged_audit.user_id | The ID of the user. |
| vid_to_merge | contacts_merged_audit.vid_to_merge | The ID of the contact which was merged. |



## owner




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| owners | hubspot | owners |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | owners._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| created_at | owners.createdAt | A timestamp for when the owner was created. |
| email | owners.email | The email address of the owner. |
| first_name | owners.firstName | The first name of the owner. |
| last_name | owners.lastName | The last name of the owner. |
| owner_id | owners.userId | The ID of the owner. |
| portal_id | MISSING | {{ doc("portal_id") }} |
| type | MISSING | The type of owner. |
| updated_at | owners.updatedAt |  |



## contact_form_submission




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| contacts_form_submissions | hubspot | contacts_form_submissions |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | contacts_form_submissions._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| contact_id | MISSING | The ID of the related contact. |
| conversion_id | contacts_form_submissions.conversion_id | A Unique ID for the specific form conversion. |
| form_id | contacts_form_submissions.form_id | The GUID of the form that the submission belongs to. |
| page_url | contacts_form_submissions.canonical_url | The URL that the form was submitted on, if applicable. |
| portal_id | contacts_form_submissions.portal_id | {{ doc("portal_id") }} |
| timestamp | contacts_form_submissions.timestamp | A Unix timestamp in milliseconds of the time the submission occurred. |
| title | contacts_form_submissions.page_title | The title of the page that the form was submitted on. This will default to the name of the form if no title is provided. |



## deal_property_history




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| deals_property_history | hubspot | deals_property_history |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | deals_property_history._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| deal_id | deals_property_history.dealId | The ID of the related deal record. |
| name | MISSING | {{ doc("history_name") }} |
| source | deals_property_history.sourceType | {{ doc("history_source") }} |
| source_id | deals_property_history.sourceId | {{ doc("history_source_id") }} |
| timestamp | deals_property_history.timestamp | {{ doc("history_timestamp") }} |
| value | deals_property_history.value | {{ doc("history_value") }} |



## engagement




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| engagements | hubspot | engagements |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | engagements._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| active | engagements.active | Whether the engagement is currently being shown in the UI.
 PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.
 |
| created_at | engagements.createdAt | A timestamp representing when the engagement was created.
 PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.
 |
| id | engagements.id | The ID of the engagement. |
| owner_id | engagements.ownerId | The ID of the engagement's owner.
PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.
 |
| portal_id | engagements.portalId | {{ doc("portal_id") }} |
| timestamp | engagements.timestamp | A timestamp in representing the time that the engagement should appear in the timeline.
PLEASE NOTE: This field will not be populated for connectors utilizing the HubSpot v3 API version. This field will be deprecated in a future release.
 |
| type | engagements.type | One of NOTE, EMAIL, TASK, MEETING, or CALL, the type of the engagement. |



## company_property_history




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| companies_property_history | hubspot | companies_property_history |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | companies_property_history._airbyte_extracted_at | {{ doc("_fivetran_synced") }} |
| company_id | companies_property_history.companyId | The ID of the related company record. |
| name | companies_property_history.properties.name | {{ doc("history_name") }} |
| source | companies_property_history.sourceType | {{ doc("history_source") }} |
| source_id | companies_property_history.sourceId | {{ doc("history_source_id") }} |
| timestamp | companies_property_history.timestamp | {{ doc("history_timestamp") }} |
| value | companies_property_history.value | {{ doc("history_value") }} |


