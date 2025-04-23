# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `Account` to Fivetran `account`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: ❌ _0.30_
- Summary Self-Evaluation: _The primary field mappings including key identifiers have been successfully matched, although several fields crucial to the completeness of the dataset, such as numerous billing and shipping details, remain unmatched, indicating partial mapping completeness._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The unique, system-generated ID assigned during creation | `Account.Id` | 🟢 _1.00_ | *Direct match found based on standard identifiers and consistent naming.* |
| `_fivetran_synced` | The time at which fivetran last synced this record | `Account._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for synchronization timestamps.* |
| `_fivetran_active` | True if record is active, used to filter out only active records if History Mode is enabled | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `account_number` | Account number assigned to this account (not the unique, system-generated ID assigned during creation). | `Account.AccountNumber` | 🟢 _1.00_ | *Direct match found based on consistent naming and usage across systems.* |
| `account_source` | The source of the account record. For example, Advertisement, Data.com, or Trade Show. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `annual_revenue` | Estimated annual revenue of the account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_city` | Details for the billing address of this account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_country` | Details for the billing address of this account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_country_code` | The ISO country code for the account’s billing address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_geocode_accuracy` | Accuracy level of the geocode for the billing address. See Compound Field Considerations and Limitations for details on geolocation compound fields. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_latitude` | Used with BillingLongitude to specify the precise geolocation of a billing address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_longitude` | Used with BillingLatitude to specify the precise geolocation of a billing address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_postal_code` | Details for the billing address of this account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_state` | Details for the billing address of this account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_state_code` | The ISO state code for the account’s billing address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_street` | Street address for the billing address of this account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `description` | Text description of the account. | `Account.Description` | 🟢 _1.00_ | *Direct match found based on descriptive consistency across sources.* |
| `fax` | Fax number for the account. | `Account.Fax` | 🟢 _1.00_ | *Direct match located with identical naming and semantic relevance.* |
| `industry` | An industry associated with this account. | `Account.Industry` | 🟢 _1.00_ | *Consistent field across sources with identical interpretations.* |
| `is_deleted` | Indicates whether the object has been moved to the Recycle Bin (true) or not (false). | `Account.IsDeleted` | 🟢 _1.00_ | *Matching based on common deletion flag semantics across systems.* |
| `jigsaw_company_id` | References the ID of a company in Data.com. If an account has a value in this field, it means that the account was imported from Data.com. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_activity_date` | Value is one of the following, whichever is the most recent | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_referenced_date` | The timestamp when the current user last accessed this record, a record related to this record, or a list view. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_viewed_date` | The timestamp when the current user last viewed this record or list view. If this value is null, the user might have only accessed this record or list view (LastReferencedDate) but not viewed it. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `master_record_id` | If this object was deleted as the result of a merge, this field contains the ID of the record that was kept. If this object was deleted for any other reason, or has not been deleted, the value is null. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | Required. Name of the account. | `Account.Name` | 🟢 _1.00_ | *Direct mapping assures high confidence due to consistent naming convention.* |
| `number_of_employees` | Number of employees working at the company represented by this account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `owner_id` | The ID of the user who currently owns this account. | `Account.OwnerId` | 🟢 _1.00_ | *Exact match found due to identical purpose and naming pattern in source and target schemas.* |
| `ownership` | Ownership type for the account, for example Private, Public, or Subsidiary. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `parent_id` | ID of the parent object, if any. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `phone` | Phone number for this account. | `Account.Phone` | 🟢 _1.00_ | *High confidence achieved due to consistent presence and identical naming across sources.* |
| `photo_url` | Path to be combined with the URL of a Salesforce instance (for example, https://yourInstance.salesforce.com/) to generate a URL to request the social network profile image associated with the account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `rating` | The account’s prospect rating, for example Hot, Warm, or Cold. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `record_type_id` | ID of the record type assigned to this object. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_city` | Details of the shipping address for this account | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_country` | Details of the shipping address for this account. Country | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_country_code` | The ISO country code for the account’s shipping address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_geocode_accuracy` | Accuracy level of the geocode for the shipping address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_latitude` | Used with ShippingLongitude to specify the precise geolocation of a shipping address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_longitude` | Used with ShippingLatitude to specify the precise geolocation of an address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_postal_code` | Details of the shipping address for this account. Postal code | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_state` | Details of the shipping address for this account. State | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_state_code` | The ISO state code for the account’s shipping address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_street` | The street address of the shipping address for this account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sic` | Standard Industrial Classification code of the company’s main business categorization, for example, 57340 for Electronics. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sic_desc` | A brief description of an organization’s line of business, based on its SIC code. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `site` | Name of the account’s location, for example Headquarters or London. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `ticker_symbol` | The stock market symbol for this account. This field is available on business accounts, not person accounts. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `type` | Type of account, for example, Customer, Competitor, or Partner. | `Account.Type` | 🟢 _1.00_ | *Consistency in type classification across sources ensures high confidence.* |
| `website` | The website of this account. | `Account.Website` | 🟢 _1.00_ | *Consistent field present in both source and target, ensuring high confidence.* |

### Mapping: Airbyte `LeadHistory` to Fivetran `lead`


- Table Match Confidence Score: ⚠️ _0.50_
- Table Completion Score: ❌ _0.15_
- Summary Self-Evaluation: _The table match score indicates a moderate likelihood that the source and target tables describe the same subject matter, however, the majority of fields are labeled as 'MISSING' indicating a low completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The unique, system-generated ID assigned during creation. | `LeadHistory.Id` | 🟢 _1.00_ | *Perfect match found for unique system-generated ID fields.* |
| `_fivetran_synced` | The time at which fivetran last synced this record | `LeadHistory._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for '_fivetran_synced' to '_airbyte_extracted_at' is always correct.* |
| `_fivetran_active` | True if record is active, used to filter out only active records if History Mode is enabled | `LeadHistory.IsDeleted` | 🟢 _0.70_ | *Reasonable match for indicating active records, mapped with minor contextual adjustment.* |
| `annual_revenue` | Annual revenue for the lead’s company. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `city` | City for the lead’s address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `company` | Required. The lead’s company. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `converted_account_id` | Object reference ID that points to the account into which the lead converted. This is a relationship field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `converted_contact_id` | Object reference ID that points to the contact into which the lead converted. This is a relationship field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `converted_date` | Date on which this lead was converted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `converted_opportunity_id` | Object reference ID that points to the opportunity into which the lead has been converted. This is a relationship field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `country` | The lead’s country. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `country_code` | The ISO country code for the lead’s address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_by_id` | Created By ID | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_date` | Created Date | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `description` | The lead’s description. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email` | The lead’s email address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email_bounced_date` | If bounce management is activated and an email sent to the lead bounced, the date and time of the bounce. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email_bounced_reason` | If bounce management is activated and an email sent to the lead bounced, the reason for the bounce. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `fax` | The lead’s fax number. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `first_name` | The lead’s first name up to 40 characters. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `geocode_accuracy` | Accuracy level of the geocode for the address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `has_opted_out_of_email` | Indicates whether the lead doesn’t want to receive email from Salesforce (true) or does (false). Label is Email Opt Out. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `individual_id` | ID of the data privacy record associated with this lead. This field is available if you enabled Data Protection and Privacy in Setup. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `industry` | Industry in which the lead works. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_converted` | Indicates whether the lead has been converted (true) or not (false). Label is Converted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_deleted` | Indicates whether the object has been moved to the Recycle Bin (true) or not (false). Label is Deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_unread_by_owner` | If true, lead has been assigned, but not yet viewed. See Unread Leads for more information. Label is Unread By Owner. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `jigsaw_contact_id` | Jigsaw Contact ID | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_activity_date` | 'Value is the most recent of either: Due date of the most recent event logged against the record. Due date of the most recently closed task associated with the record.'  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_modified_by_id` | Last Modified By ID | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_modified_date` | Last Modified Date | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_name` | Required. Last name of the lead up to 80 characters. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_referenced_date` | The timestamp when the current user last accessed this record, a record related to this record, or a list view. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_viewed_date` | The timestamp when the current user last viewed this record or list view. If this value is null, the user might have only accessed this record or list view (LastReferencedDate) but not viewed it. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `latitude` | Used with Longitude to specify the precise geolocation of an address. Acceptable values are numbers between –90 and 90 up to 15 decimal places. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `lead_source` | The lead’s source. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `longitude` | Used with Latitude to specify the precise geolocation of an address. Acceptable values are numbers between –180 and 180 up to 15 decimal places. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `master_record_id` | If this record was deleted as the result of a merge, this field contains the ID of the record that was kept. If this record was deleted for any other reason, or has not been deleted, the value is null. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `mobile_phone` | The lead’s mobile phone number. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | Concatenation of FirstName, MiddleName, LastName, and Suffix up to 203 characters, including whitespaces. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `number_of_employees` | Number of employees at the lead’s company. Label is Employees. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `owner_id` | ID of the lead’s owner. This is a polymorphic relationship field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `phone` | The lead’s phone number. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `photo_url` | Path to be combined with the URL of a Salesforce instance | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `postal_code` | Postal code for the address of the lead. Label is Zip/Postal Code. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `salutation` | Salutation for the lead. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `state` | State for the address of the lead. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `state_code` | The ISO state code for the lead’s address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status` | Status code for this converted lead. Status codes are defined in Status and represented in the API by the LeadStatus object. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `street` | Street number and name for the address of the lead. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `system_modstamp` | System Modstamp | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `title` | Title for the lead, such as CFO or CEO. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `website` | Website for the lead. | `MISSING` | ❌ _0.00_ | *No good match found.* |
