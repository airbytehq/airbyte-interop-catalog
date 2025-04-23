# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `programs` to Fivetran `program`


- Table Match Confidence Score: 🟢 _0.95_
- Table Completion Score: ⚠️ _0.62_
- Summary Self-Evaluation: _The majority of fields have a direct mapping, indicating a strong match between the source and target schema for the 'Programs' table. Several crucial fields like 'id', 'name', and 'description' are well-matched. However, the presence of several 'MISSING' field mappings, such as 'end_date', 'sfdc_id', 'sfdc_name', and 'start_date' lowers the completion score as these are important for complete data transformation but couldn't be appropriately mapped._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `channel` | Channel of the program. | `programs.channel` | 🟢 _0.95_ | *Direct match with the source field 'programs.channel'.* |
| `created_at` | Timestamp the program was created at. | `programs.createdAt` | 🟢 _0.95_ | *Direct match with the source field 'programs.createdAt', high confidence due to exact field name correspondence.* |
| `description` | Description of the program. | `programs.description` | 🟢 _0.95_ | *Direct match with the source field 'programs.description'.* |
| `end_date` | End date of the program. Applicable to event, email, and webinar type programs. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | ID of the program. | `programs.id` | 🟢 _0.95_ | *Direct match with the source field 'programs.id'.* |
| `name` | Name of the program. | `programs.name` | 🟢 _0.95_ | *Direct match with the source field 'programs.name'.* |
| `sfdc_id` | SFDC id of the program if linked to an SFDC campaign. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sfdc_name` | Name of the linked SFDC campaign if applicable. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `start_date` | Start date of program. Applicable to event, email and webinar type programs. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status` | Status of the program. Only valid for Email and engagement program types. Allowed values: locked, unlocked, on, off  | `programs.status` | 🟢 _0.70_ | *There's a clear match with 'programs.status', but the differing conditionals based on the field's value slightly reduce the confidence.* |
| `type` | Type of the program. Allowed values: program, event, webinar, nurture  | `programs.type` | 🟢 _0.95_ | *Direct match with the source field 'programs.type', high confidence due to exact field name correspondence.* |
| `updated_at` | Timestamp the program was most recently updated. | `programs.updatedAt` | 🟢 _0.95_ | *Direct match with the source field 'programs.updatedAt'.* |
| `url` | URL of the program in the Marketo UI. | `programs.url` | 🟢 _0.95_ | *Direct match with the source field 'programs.url'.* |
| `workspace` | Name of the workspace. | `programs.workspace` | 🟢 _0.95_ | *Direct match; both source and target reference the same term 'workspace'.* |
| `_fivetran_deleted` | Boolean created by Fivetran to indicate whether the record has been deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `campaigns` to Fivetran `campaign`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: ❌ _0.40_
- Summary Self-Evaluation: _Overall, the table match quality is high, suggesting a strong correlation between the source and target tables. However, the completion score is relatively low, indicating that many fields from the source are not successfully mapped to the target, reducing the overall confidence in the mapping completeness._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `active` | Whether the campaign is active. Only applicable to trigger campaigns. | `campaigns.active` | 🟢 _1.00_ | *Direct match found between source and target.* |
| `created_at` | Timestamp when the campaign was created. | `campaigns.createdAt` | 🟢 _1.00_ | *Direct match found between source and target.* |
| `description` | Description of the campaign | `campaigns.description` | 🟢 _1.00_ | *Direct match found between source and target.* |
| `id` | Unique integer ID of the campaign. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | Name of the campaign. | `campaigns.name` | 🟢 _1.00_ | *Direct match found between source and target.* |
| `program_id` | ID of the parent program, if applicable. | `campaigns.programId` | 🟢 _1.00_ | *Direct match found between source and target.* |
| `type` | Type of campaign, either 'batch' or 'trigger'. | `campaigns.type` | 🟢 _1.00_ | *Direct match found between source and target.* |
| `updated_at` | Timestamp when the campaign was most recently updated. | `campaigns.updatedAt` | 🟢 _1.00_ | *Direct match found between source and target.* |
| `workspace_name` | Name of the parent workspace, if applicable. | `campaigns.workspaceName` | 🟢 _1.00_ | *Direct match found between source and target.* |
| `computed_url` | The URL of the campaign in Marketo. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `flow_id` | The ID of the flow that the campaign is associated with. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `folder_id` | The ID of the folder that the campaign is stored in. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `folder_type` | The type of folder that the campaign is stored in. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_communication_limit_enabled` | Whether or not the campaign has a communication limit. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_requestable` | Whether or not the campaign can be requested by leads. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_system` | Whether or not the campaign is a system campaign. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `max_members` | The maximum number of members that the campaign can have. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `qualification_rule_type` | The type of qualification rule that the campaign uses. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `qualification_rule_interval` | The interval for the qualification rule. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `qualification_rule_unit` | The unit for the qualification rule. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `recurrence_start_at` | The start date and time for the recurrence. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `recurrence_end_at` | The end date and time for the recurrence. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `recurrence_interval_type` | The type of recurrence interval. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `recurrence_interval` | The value of the recurrence interval. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `recurrence_weekday_only` | Whether or not the recurrence is limited to weekdays. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `recurrence_day_of_month` | The day of the month for the recurrence. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `recurrence_day_of_week` | The day of the week for the recurrence. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `recurrence_week_of_month` | The week of the month for the recurrence. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `smart_list_id` | The ID of the smart list that the campaign is associated with. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status` | The status of the campaign. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_deleted` | Boolean created by Fivetran to indicate whether the record has been deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `leads` to Fivetran `lead`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.92_
- Summary Self-Evaluation: _The table match score reflects a relatively high confidence in matching the core structures of the lead records between the source and target system, as indicated by the largely consistent mapping expressions. The completion score is slightly reduced due to several fields set as 'MISSING' indicating that not all target fields could be populated from the source data._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique integer id of a lead record. | `leads.id` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `created_at` | The timestamp each lead object was created at. | `leads.createdAt` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `updated_at` | The timestamp each lead object was last updated at. | `leads.updatedAt` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `email` | The email address of the lead. | `leads.email` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `first_name` | The first name of the lead. | `leads.firstName` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `last_name` | The last name of the lead. | `leads.lastName` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `phone` | Lead’s Phone Number. | `leads.phone` | 🟢 _0.90_ | *Closely matches expected data.* |
| `main_phone` | Primary phone number of the lead’s company | `leads.mainPhone` | 🟢 _0.90_ | *Closely matches expected data.* |
| `mobile_phone` | Lead’s mobile phone number | `leads.mobilePhone` | 🟢 _0.90_ | *Closely matches expected data.* |
| `company` | Lead’s company name | `leads.company` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `inferred_company` | Company name inferred by reverse IP lookup of the lead’s first recorded web visit | `leads.inferredCompany` | 🟢 _0.90_ | *Closely matches expected data, slightly indirect mapping.* |
| `address_lead` | Second address associated with the lead. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `address` | Lead’s address. | `leads.address` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `city` | Lead’s city | `leads.city` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `state` | Lead’s state | `leads.state` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `state_code` | Alpha-2 code of the Lead’s state | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `country` | Lead’s country | `leads.country` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `country_code` | Alpha-2 code of the Lead’s country | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `postal_code` | Lead’s postal code | `leads.postalCode` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `billing_street` | Billing street address of the lead’s company | `leads.billingStreet` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `billing_city` | City of the lead’s billing address | `leads.billingCity` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `billing_state` | State or province of the lead’s billing address | `leads.billingState` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `billing_state_code` | Alpha-2 code of the state or province of the lead’s billing address | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_country` | Country of the lead’s billing address | `leads.billingCountry` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `billing_country_code` | Alpha-2 code of the country of the lead’s billing address | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_postal_code` | Postal code of the lead’s billing address | `leads.billingPostalCode` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `inferred_city` | Lead’s city inferred by reverse IP lookup of lead’s first recorded web visit. | `leads.inferredCity` | 🟢 _0.90_ | *Closely matches expected data, slightly indirect mapping.* |
| `inferred_state_region` | Lead’s state region inferred by reverse IP lookup of lead’s first recorded web visit. | `leads.inferredStateRegion` | 🟢 _0.90_ | *Closely matches expected data, slightly indirect mapping.* |
| `inferred_country` | Country inferred by reverse IP lookup of the lead’s first recorded web visit | `leads.inferredCountry` | 🟢 _0.90_ | *Closely matches expected data, slightly indirect mapping.* |
| `inferred_postal_code` | Lead’s postal code inferred by reverse IP lookup of lead’s first recorded web visit. | `leads.inferredPostalCode` | 🟢 _0.90_ | *Closely matches expected data, slightly indirect mapping.* |
| `inferred_phone_area_code` | Lead’s phone area code inferred by reverse IP lookup of lead’s first recorded web visit. | `leads.inferredPhoneAreaCode` | 🟢 _0.90_ | *Closely matches expected data, slightly indirect mapping.* |
| `anonymous_ip` | IP address of the lead’s first recorded web visit | `leads.anonymousIP` | 🟢 _0.70_ | *The expression matches, but the use case might differ slightly.* |
| `unsubscribed` | Lead’s email-unsubscribed status (boolean). Partially system managed. Will prevent receipt of non-operational emails if set to true. | `leads.unsubscribed` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `email_invalid` | Email invalid status (boolean). All emails to the address will be blocked if set to true. Bounces indicating that the email is invalid will automatically set this field to true. | `leads.emailInvalid` | 🟢 _1.00_ | *Direct match of field names and purposes.* |
| `do_not_call` | Lead’s do-not-call preference (boolean) | `leads.doNotCall` | 🟢 _1.00_ | *Direct match of field names and purposes.* |

### Mapping: Airbyte `leads` to Fivetran `lead_describe`


- Table Match Confidence Score: ❌ _0.10_
- Table Completion Score: ❌ _0.30_
- Summary Self-Evaluation: _Low scores due to multiple 'MISSING' expressions indicating unresolved field mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `data_type` | Datatype of the field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `display_name` | UI display-name of the field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | Unique integer id of the field. | `leads.id` | 🟢 _1.00_ | *Direct mapping found.* |
| `length` | Max length of the field. Only applicable to text, string, and text area. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `restname` | Description of REST API usage attributes. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `restread_only` | Whether the field is only available via the REST API. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `soapname` | Description of SOAP API usage attributes. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `soapread_only` | Whether the field is only available via the SOAP API. | `MISSING` | ❌ _0.00_ | *No good match found.* |
