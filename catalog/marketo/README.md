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


### Mapping: Airbyte `activities_change_data_value` to Fivetran `activity_change_data_value`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The high table match score reflects that both the source and target tables closely align in terms of describing similar aspects of activity and campaign data. The completion score is not perfect due to some fields not being mapped either because no good match was found or they are less relevant to the core dataset._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `api_method_name` | API method used for change, if applicable. | `activities_change_data_value.api_method_name` | 🟢 _0.70_ | *The API method fields are mapped with high confidence as it directly matches API related entities.* |
| `activity_date` | Timestamp of the actvity. | `activities_change_data_value.activityDate` | 🟢 _0.90_ | *Direct match for timestamp data relating to activity logs.* |
| `activity_type_id` | ID of the activity type. | `activities_change_data_value.activityTypeId` | 🟢 _0.90_ | *Identities of activity types match directly between the systems.* |
| `campaign_id` | The ID of the related campaign, if applicable. | `activities_change_data_value.campaignId` | 🟢 _0.90_ | *Campaign IDs mapped accurately reflecting closure in campaign related data.* |
| `id` | ID of the activity. | `activities_change_data_value.marketoGUID` | 🟢 _0.90_ | *Direct mapping of activity IDs.* |
| `lead_id` | Id of the lead associated to the activity. | `activities_change_data_value.leadId` | 🟢 _0.90_ | *Lead IDs match directly showing relevance in both data structures.* |
| `modifying_user` | The user who instigated the change, if applicable. | `activities_change_data_value.modifying_user` | 🟢 _0.70_ | *Matches a user entity involved in changes, though the use case could slightly vary.* |
| `new_value` | New value after the change. | `activities_change_data_value.new_value` | 🟢 _0.85_ | *Excellent match for fields capturing new states in data.* |
| `old_value` | Old value before the change. | `activities_change_data_value.old_value` | 🟢 _0.85_ | *Similar to new_value, old value fields are mapped well.* |
| `primary_attribute_value` | Value of the primary attribute. | `activities_change_data_value.primaryAttributeValue` | 🟢 _0.80_ | *Attributes critical to both systems are matched well.* |
| `primary_attribute_value_id` | ID of the primary attribute field. | `activities_change_data_value.primaryAttributeValueId` | 🟢 _0.80_ | *The primary attribute ID is crucial and matched well.* |
| `reason` | Reason for the data change. | `activities_change_data_value.reason` | ⚠️ _0.60_ | *Reason for changes are relatively mapped, although the context can vary slightly.* |
| `request_id` | ID of the request made. | `activities_change_data_value.request_id` | 🟢 _0.75_ | *Request IDs relate critically in managing data requests across systems.* |

### Mapping: Airbyte `activities_email_bounced` to Fivetran `activity_email_bounced`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table mapping exhibits a high level of confidence that the source 'activities_email_bounced' and target table describe the same subject matter. Most fields have strong mappings with only minor deviations._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `activity_date` | The timestamp the email bounced. | `activities_email_bounced.activityDate` | 🟢 _0.90_ | *Direct correlation between 'activityDate' and 'activity_date'.* |
| `activity_type_id` | The ID of the activity type. | `activities_email_bounced.activityTypeId` | 🟢 _0.90_ | *Direct correlation between 'activityTypeId' and 'activity_type_id'.* |
| `campaign_id` | The ID of the email's campaign. | `activities_email_bounced.campaignId` | 🟢 _0.90_ | *Direct correlation between 'campaignId' and 'campaign_id'.* |
| `campaign_run_id` | The ID of the email's campaign run. | `activities_email_bounced.campaign_run_id` | 🟢 _0.90_ | *Direct correlation between 'campaign_run_id' and 'campaign_run_id'.* |
| `category` | The category associated with bounced email. | `activities_email_bounced.category` | 🟢 _0.90_ | *Direct correlation between 'category' and 'category'.* |
| `choice_number` | The choice number of the current step that triggered the activity. | `activities_email_bounced.choice_number` | 🟢 _0.90_ | *Direct correlation between 'choice_number' and 'choice_number'.* |
| `details` | Details about why the email bounced. | `activities_email_bounced.details` | 🟢 _0.90_ | *Direct correlation between 'details' and 'details'.* |
| `email` | The email address that bounced. | `activities_email_bounced.email` | ❌ _0.00_ | *Mismatch found: 'email' mapping attempts to use an EMAIL field for an email template ID, which is incorrect.* |
| `email_template_id` | The ID of the email's template. | `activities_email_bounced.email` | ❌ _0.00_ | *Mismatch found: 'email' mapping attempts to use an EMAIL field for an email template ID, which is incorrect.* |
| `id` | ID of the activity. | `activities_email_bounced.marketoGUID` | 🟢 _0.90_ | *Direct correlation between 'marketoGUID' and 'id'.* |
| `lead_id` | The ID of the lead related to the activity. | `activities_email_bounced.leadId` | 🟢 _0.90_ | *Direct correlation between 'leadId' and 'lead_id'.* |
| `primary_attribute_value` | The primary attribute of the activity. | `activities_email_bounced.primaryAttributeValue` | 🟢 _0.90_ | *Direct correlation between 'primaryAttributeValue' and 'primary_attribute_value'.* |
| `primary_attribute_value_id` | The ID of the primary attribute of the activity. | `activities_email_bounced.primaryAttributeValueId` | 🟢 _0.90_ | *Direct correlation between 'primaryAttributeValueId' and 'primary_attribute_value_id'.* |
| `step_id` | The Id of the current step in the flow. | `activities_email_bounced.step_id` | 🟢 _0.90_ | *Direct correlation between 'step_id' and 'step_id'.* |
| `subcategory` | The subcategory associated with bounced email. | `activities_email_bounced.subcategory` | 🟢 _0.90_ | *Direct correlation between 'subcategory' and 'subcategory'.* |

### Mapping: Airbyte `activities_delete_lead` to Fivetran `activity_delete_lead`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.57_
- Summary Self-Evaluation: _The overall confidence for the table matching is relatively high as most fields are mapped correctly with good confidence, but some fields are still missing. Mappings for 'campaign' and 'primary_attribute_value' are marked as MISSING, lowering the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `activity_date` | The timestamp the lead was deleted. | `activities_delete_lead.activityDate` | 🟢 _0.90_ | *Direct and clear mapping to source's activityDate field* |
| `activity_type_id` | The ID of the activity type. | `activities_delete_lead.activityTypeId` | 🟢 _0.95_ | *Exact match to source naming, high confidence in mapping.* |
| `campaign_id` | The ID of the campaign related to the activity, if applicable. | `activities_delete_lead.campaignId` | 🟢 _0.80_ | *Direct match to a relevant and clearly identified field, albeit with possible multiple variations in campaign references.* |
| `campaign` | The name of the campaign related to the activity, if applicable. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | ID of the activity. | `activities_delete_lead.marketoGUID` | 🟢 _0.90_ | *Uses marketoGUID, which matches the intended unique identifier purpose of the ID field.* |
| `lead_id` | The ID of the lead related to the activity. | `activities_delete_lead.leadId` | 🟢 _0.88_ | *Direct correlation to the specified lead's unique identifier.* |
| `primary_attribute_value` | The primary attribute of the activity. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `primary_attribute_value_id` | The ID of the primary attribute of the activity. | `activities_delete_lead.primaryAttributeValueId` | 🟢 _0.85_ | *The mapping accurately ties back to a clearly relevant source field.* |

### Mapping: Airbyte `activities_merge_leads` to Fivetran `activity_merge_leads`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table match score is high because the source and target likely describe the same concept, reflecting shared upstream APIs. The completion score is moderately high, although not all fields are serialized equally across implementations._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `activity_date` | The timestamp the lead was deleted. | `activities_merge_leads.activityDate` | 🟢 _0.90_ | *Direct match on activity dates.* |
| `activity_type_id` | The ID of the activity type. | `activities_merge_leads.activityTypeId` | 🟢 _0.90_ | *Exact column match for activity type IDs.* |
| `campaign_id` | The ID of the campaign related to the activity, if applicable. | `activities_merge_leads.campaignId` | 🟢 _0.75_ | *There's a high probability that campaign IDs match, subject to further verification.* |
| `id` | ID of the activity. | `activities_merge_leads.marketoGUID` | 🟢 _0.90_ | *ID fields tend to be consistent across similar schemas.* |
| `lead_id` | The ID of the lead related to the activity. | `activities_merge_leads.leadId` | 🟢 _0.90_ | *Direct match on identification for lead.* |
| `primary_attribute_value` | The primary attribute of the activity. | `activities_merge_leads.primaryAttributeValue` | 🟢 _0.80_ | *High confidence in matching primary attribute value.* |
| `primary_attribute_value_id` | The ID of the primary attribute of the activity. | `activities_merge_leads.primaryAttributeValueId` | 🟢 _0.80_ | *Primary attribute IDs highly match the contextual expectations.* |
| `merge_ids` | ID of the lead that the lead was merged into. | `activities_merge_leads.merge_ids` | ❌ _0.35_ | *Uncertainty exists; the context of merging might differ substantially.* |

### Mapping: Airbyte `activities_click_email` to Fivetran `activity_click_email`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.71_
- Summary Self-Evaluation: _The table match is of high confidence due to the alignment of most source schema fields with the target schema. The completion score reflects the presence of several field mappings but not all are complete._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `activity_date` | The date of the activity. | `activities_click_email.activityDate` | 🟢 _1.00_ | *Direct and exact match with the target schema.* |
| `activity_type_id` | The ID of the activity type. | `activities_click_email.activityTypeId` | 🟢 _1.00_ | *Direct and exact match with the target schema.* |
| `campaign_id` | The ID of the email's campaign. | `activities_click_email.campaignId` | 🟢 _1.00_ | *Direct and exact match with the target schema.* |
| `campaign_run_id` | The ID of the email's campaign run. | `activities_click_email.campaign_run_id` | 🟢 _0.80_ | *Field reference is very close, and likely considered equivalent.* |
| `choice_number` | The choice number of the current step that triggered the activity. | `activities_click_email.choice_number` | 🟢 _1.00_ | *Direct and exact match with the target schema.* |
| `device` | The device type the activity occurred on. | `activities_click_email.device` | 🟢 _1.00_ | *Direct and exact match with the target schema.* |
| `email_template_id` | The ID of the email's template. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | ID of the activity. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_mobile_device` | Whether the activity occurred on a mobile device. | `activities_click_email.is_mobile_device` | 🟢 _1.00_ | *Direct and exact match with the target schema.* |
| `lead_id` | The ID of the lead related to the activity. | `activities_click_email.leadId` | 🟢 _1.00_ | *Direct and exact match with the target schema.* |
| `link` | The URL of the link clicked. | `activities_click_email.link` | 🟢 _1.00_ | *Direct and exact match with the target schema.* |
| `primary_attribute_value` | The primary attribute of the activity. | `activities_click_email.primaryAttributeValue` | 🟢 _1.00_ | *Direct and exact match with the target schema.* |
| `primary_attribute_value_id` | The ID of the primary attribute of the activity. | `activities_click_email.primaryAttributeValueId` | 🟢 _1.00_ | *Direct and exact match with the target schema.* |
| `step_id` | The Id of the current step in the flow. | `activities_click_email.step_id` | 🟢 _0.80_ | *Field reference is very close, and likely considered equivalent.* |
| `user_agent` | The Web browser user agent information obtained when the lead clicked the email link. | `activities_click_email.user_agent` | 🟢 _1.00_ | *Direct and exact match with the target schema.* |

### Mapping: Airbyte `activities_unsubscribe_email` to Fivetran `activity_unsubscribe_email`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table match is strong, indicating a high likelihood that the source and target tables describe the same subject matter. The completion score is also high, showing that most fields are populated with reasonable mappings, although some mappings like 'email_template_id' had to be marked as 'MISSING' due to the lack of available data._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `activity_date` | The timestamp the lead unsubscribed. | `activities_unsubscribe_email.activityDate` | 🟢 _0.90_ | *Proper mapping with detailed reference to activity date.* |
| `activity_type_id` | The ID of the activity type. | `activities_unsubscribe_email.activityTypeId` | 🟢 _0.90_ | *Accurate mapping to the ID of the activity type.* |
| `campaign_id` | The ID of the email's campaign. | `activities_unsubscribe_email.campaignId` | 🟢 _0.85_ | *Correct mapping to the corresponding email campaign ID.* |
| `campaign_run_id` | The ID of the email's campaign run. | `activities_unsubscribe_email.campaign_run_id` | 🟢 _0.85_ | *Correct mapping of the campaign run ID, corresponding directly to the source.* |
| `client_ip_address` | The IP address of the client that unsubscribed. | `activities_unsubscribe_email.client_ip_address` | 🟢 _0.85_ | *Direct and accurate mapping of the IP address.* |
| `email_template_id` | The ID of the email's template. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `form_fields` | The query parameters contained within the URL. | `activities_unsubscribe_email.form_fields` | 🟢 _0.80_ | *Mapped correctly to form fields containing URL query parameters.* |
| `id` | ID of the activity. | `activities_unsubscribe_email.marketoGUID` | 🟢 _0.90_ | *Accurately mapped to the Market GUID in the source.* |
| `lead_id` | The ID of the lead related to the activity. | `activities_unsubscribe_email.leadId` | 🟢 _0.90_ | *Matches well to the source lead ID, appropriate mapping confirmed.* |
| `primary_attribute_value` | The primary attribute of the activity. | `activities_unsubscribe_email.primaryAttributeValue` | 🟢 _0.85_ | *Proper mapping of the primary attribute value.* |
| `primary_attribute_value_id` | The ID of the primary attribute of the activity. | `activities_unsubscribe_email.primaryAttributeValueId` | 🟢 _0.85_ | *Correct mapping for the primary attribute value ID.* |
| `query_parameters` | The query parameters contained within the URL. | `activities_unsubscribe_email.query_parameters` | 🟢 _0.80_ | *Correctly mapped to encapsulate all query parameters related to the activity.* |
| `referrer_url` | The URL of the referrer used to identify where the form visit originated from. | `activities_unsubscribe_email.referrer_url` | 🟢 _0.80_ | *Accurately accounts for the URL of the form referrer.* |
| `user_agent` | The web browser user agent information obtained when the lead unsubscribed. | `activities_unsubscribe_email.user_agent` | 🟢 _0.80_ | *Correctly mapped the browser user agent from the unsubscribe event.* |
| `webform_id` | The ID of the unsubscribe web page. | `activities_unsubscribe_email.webform_id` | 🟢 _0.85_ | *Direct mapping to the specific ID of the email's webform.* |
| `webpage_id` | The ID of the unsubscribe web form. | `activities_unsubscribe_email.webpage_id` | 🟢 _0.85_ | *Mapped directly to the webpage ID, which is specific and appropriate.* |

### Mapping: Airbyte `activities_send_email` to Fivetran `activity_send_email`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.73_
- Summary Self-Evaluation: _The table match score reflects a good alignment of core concepts between the source and target schema with some variations, particularly in the serialized fields missing in the source implementation. The completion score is fairly high, indicating most target fields have plausible associated source fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `action_result` | The outcome of a specific action performed within the Marketo platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `activity_date` | The timestamp the email was sent. | `activities_send_email.activityDate` | 🟢 _0.80_ | *Direct mapping identified.* |
| `activity_type_id` | The ID of the activity type. | `activities_send_email.activityTypeId` | 🟢 _0.80_ | *Direct mapping identified.* |
| `campaign_id` | The ID of the email's campaign. | `activities_send_email.campaignId` | 🟢 _0.80_ | *Direct mapping identified.* |
| `campaign_run_id` | The ID of the email's campaign run. | `activities_send_email.campaign_run_id` | 🟢 _0.80_ | *Direct mapping identified.* |
| `choice_number` | The choice number of the current step that triggered the activity. | `activities_send_email.choice_number` | 🟢 _0.80_ | *Direct mapping identified.* |
| `email_template_id` | The ID of the email's template. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | ID of the activity. | `activities_send_email.marketoGUID` | 🟢 _0.80_ | *Direct mapping identified.* |
| `lead_id` | The ID of the lead related to the activity. | `activities_send_email.leadId` | 🟢 _0.80_ | *Direct mapping identified.* |
| `primary_attribute_value` | The primary attribute of the activity. | `activities_send_email.primaryAttributeValue` | 🟢 _0.80_ | *Direct mapping identified.* |
| `primary_attribute_value_id` | The ID of the primary attribute of the activity. | `activities_send_email.primaryAttributeValueId` | 🟢 _0.80_ | *Direct mapping identified.* |
| `step_id` | The Id of the current step in the flow. | `activities_send_email.step_id` | 🟢 _0.80_ | *Direct mapping identified.* |

### Mapping: Airbyte `activities_open_email` to Fivetran `activity_open_email`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping shows a high level of confidence that the source and target tables are describing the same subject matter, with almost all fields properly populated._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `activity_date` | The timestamp the email was opened. | `activities_open_email.activityDate` | 🟢 _1.00_ | *Exact match found.* |
| `activity_type_id` | The ID of the activity type. | `activities_open_email.activityTypeId` | 🟢 _0.95_ | *Exact match found.* |
| `campaign_id` | The ID of the email's campaign. | `activities_open_email.campaignId` | 🟢 _0.95_ | *Exact match found.* |
| `campaign_run_id` | The ID of the email's campaign run. | `activities_open_email.campaign_run_id` | 🟢 _0.95_ | *Exact match found.* |
| `choice_number` | The choice number of the current step that triggered the activity. | `activities_open_email.choice_number` | 🟢 _0.95_ | *Exact match found.* |
| `device` | The device that was used to open the email. | `activities_open_email.device` | 🟢 _0.95_ | *Exact match found.* |
| `email_template_id` | The ID of the email's template. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | ID of the activity. | `activities_open_email.marketoGUID` | 🟢 _0.95_ | *Exact match found.* |
| `is_mobile_device` | Identifies whether a mobile device was used to open the email. | `activities_open_email.is_mobile_device` | 🟢 _0.95_ | *Exact match found.* |
| `lead_id` | The ID of the lead related to the activity. | `activities_open_email.leadId` | 🟢 _0.95_ | *Exact match found.* |
| `platform` | The platform that was used to open the email. | `activities_open_email.platform` | 🟢 _0.95_ | *Exact match found.* |
| `primary_attribute_value` | The primary attribute of the activity. | `activities_open_email.primaryAttributeValue` | 🟢 _0.95_ | *Exact match found.* |
| `primary_attribute_value_id` | The ID of the primary attribute of the activity. | `activities_open_email.primaryAttributeValueId` | 🟢 _0.95_ | *Exact match found.* |
| `user_agent` | The web browser user agent information obtained when the email was opened. | `activities_open_email.user_agent` | 🟢 _0.95_ | *Exact match found.* |

### Mapping: Airbyte `activities_email_delivered` to Fivetran `activity_email_delivered`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _Most fields are well mapped, but 'email_template_id' and 'id' have no direct matches, lowering the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `activity_date` | The timestamp the email was delivered. | `activities_email_delivered.activityDate` | 🟢 _0.90_ | *The expression directly matches the target schema's expected field.* |
| `activity_type_id` | The ID of the activity type. | `activities_email_delivered.activityTypeId` | 🟢 _0.90_ | *The expression directly matches the target schema's expected field.* |
| `campaign_id` | The ID of the email's campaign. | `activities_email_delivered.campaignId` | 🟢 _0.90_ | *The expression directly matches the target schema's expected field.* |
| `campaign_run_id` | The ID of the email's campaign run. | `activities_email_delivered.campaign_run_id` | 🟢 _0.90_ | *The expression directly matches the target schema's expected field.* |
| `choice_number` | The choice number of the current step that triggered the activity. | `activities_email_delivered.choice_number` | 🟢 _0.90_ | *The expression directly matches the target schema's expected field.* |
| `email_template_id` | The ID of the email's template. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | ID of the activity. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `lead_id` | The ID of the lead related to the activity. | `activities_email_delivered.leadId` | 🟢 _0.90_ | *The expression directly matches the target schema's expected field.* |
| `primary_attribute_value` | The primary attribute of the activity. | `activities_email_delivered.primaryAttributeValue` | 🟢 _0.90_ | *The expression directly matches the target schema's expected field.* |
| `primary_attribute_value_id` | The ID of the primary attribute of the activity. | `activities_email_delivered.primaryAttributeValueId` | 🟢 _0.90_ | *The expression directly matches the target schema's expected field.* |
| `step_id` | The Id of the current step in the flow. | `activities_email_delivered.step_id` | 🟢 _0.90_ | *The expression directly matches the target schema's expected field.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
