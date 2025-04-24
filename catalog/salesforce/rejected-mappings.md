# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `Account` to Fivetran `account`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: 🟢 _0.82_
- Summary Self-Evaluation: _Most fields matched well indicating a successful match of the source and target table. However, several fields have no good match found hence a lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The unique, system-generated ID assigned during creation | `Account.Id` | 🟢 _1.00_ | *Direct match with unique ID* |
| `_fivetran_synced` | The time at which fivetran last synced this record | `Account._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables* |
| `_fivetran_active` | True if record is active, used to filter out only active records if History Mode is enabled | `Account.Active__c` | 🟢 _0.70_ | *Likely represents an active record status* |
| `account_number` | Account number assigned to this account (not the unique, system-generated ID assigned during creation). | `Account.AccountNumber` | 🟢 _0.90_ | *Direct match on account identification* |
| `account_source` | The source of the account record. For example, Advertisement, Data.com, or Trade Show. | `Account.AccountSource` | 🟢 _0.90_ | *Direct match indicating the origin of the account* |
| `annual_revenue` | Estimated annual revenue of the account. | `Account.AnnualRevenue` | 🟢 _0.90_ | *Direct match on economic attribute of the account* |
| `billing_city` | Details for the billing address of this account. | `Account.BillingCity` | 🟢 _1.00_ | *Exact match on geographical attribute* |
| `billing_country` | Details for the billing address of this account. | `Account.BillingCountry` | 🟢 _1.00_ | *Exact match on geographical attribute* |
| `billing_country_code` | The ISO country code for the account’s billing address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_geocode_accuracy` | Accuracy level of the geocode for the billing address. See Compound Field Considerations and Limitations for details on geolocation compound fields. | `Account.BillingGeocodeAccuracy` | 🟢 _0.80_ | *High likelihood of matching description* |
| `billing_latitude` | Used with BillingLongitude to specify the precise geolocation of a billing address. | `Account.BillingLatitude` | 🟢 _1.00_ | *Exact match on geographical coordinates* |
| `billing_longitude` | Used with BillingLatitude to specify the precise geolocation of a billing address. | `Account.BillingLongitude` | 🟢 _1.00_ | *Exact match on geographical coordinates* |
| `billing_postal_code` | Details for the billing address of this account. | `Account.BillingPostalCode` | 🟢 _1.00_ | *Exact match on geographical attribute* |
| `billing_state` | Details for the billing address of this account. | `Account.BillingState` | 🟢 _1.00_ | *Exact match on geographical attribute* |
| `billing_state_code` | The ISO state code for the account’s billing address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_street` | Street address for the billing address of this account. | `Account.BillingStreet` | 🟢 _1.00_ | *Exact match on geographical attribute* |
| `description` | Text description of the account. | `Account.Description` | 🟢 _0.92_ | *Direct match on textual description* |
| `fax` | Fax number for the account. | `Account.Fax` | 🟢 _0.80_ | *Commonly matched to contact information* |
| `industry` | An industry associated with this account. | `Account.Industry` | 🟢 _0.90_ | *Direct match linking business sector* |
| `is_deleted` | Indicates whether the object has been moved to the Recycle Bin (true) or not (false). | `Account.IsDeleted` | ⚠️ _0.65_ | *Indicative of record status, moderately matched* |
| `jigsaw_company_id` | References the ID of a company in Data.com. If an account has a value in this field, it means that the account was imported from Data.com. | `Account.JigsawCompanyId` | ❌ _0.40_ | *Potential integrative data identifier but unclear match* |
| `last_activity_date` | Value is one of the following, whichever is the most recent | `Account.LastActivityDate` | 🟢 _0.90_ | *Direct match on account activity* |
| `last_referenced_date` | The timestamp when the current user last accessed this record, a record related to this record, or a list view. | `Account.LastReferencedDate` | 🟢 _1.00_ | *Direct match indicating last interaction* |
| `last_viewed_date` | The timestamp when the current user last viewed this record or list view. If this value is null, the user might have only accessed this record or list view (LastReferencedDate) but not viewed it. | `Account.LastViewedDate` | 🟢 _1.00_ | *Direct match indicating last view interaction* |
| `master_record_id` | If this object was deleted as the result of a merge, this field contains the ID of the record that was kept. If this object was deleted for any other reason, or has not been deleted, the value is null. | `Account.MasterRecordId` | ⚠️ _0.60_ | *Associated with merged records, moderately matched* |
| `name` | Required. Name of the account. | `Account.Name` | 🟢 _1.00_ | *Identically matches the primary identifier* |
| `number_of_employees` | Number of employees working at the company represented by this account. | `Account.NumberOfEmployees` | 🟢 _0.90_ | *Matches business scale attribute* |
| `owner_id` | The ID of the user who currently owns this account. | `Account.OwnerId` | 🟢 _1.00_ | *Matches ownership data* |
| `ownership` | Ownership type for the account, for example Private, Public, or Subsidiary. | `Account.Ownership` | 🟢 _1.00_ | *Matches descriptive ownership type* |
| `parent_id` | ID of the parent object, if any. | `Account.ParentId` | 🟢 _0.70_ | *Indicative of hierarchical link, likely match* |
| `phone` | Phone number for this account. | `Account.Phone` | 🟢 _1.00_ | *Exact match on contact information* |
| `photo_url` | Path to be combined with the URL of a Salesforce instance (for example, https://yourInstance.salesforce.com/) to generate a URL to request the social network profile image associated with the account. | `Account.PhotoUrl` | 🟢 _0.80_ | *Matches representation data* |
| `rating` | The account’s prospect rating, for example Hot, Warm, or Cold. | `Account.Rating` | 🟢 _0.80_ | *Reflects an evaluative attribute* |
| `record_type_id` | ID of the record type assigned to this object. | `MISSING` | ❌ _0.00_ | *No good match found* |
| `shipping_city` | Details of the shipping address for this account | `Account.ShippingCity` | 🟢 _1.00_ | *Exact match on geographical attribute* |
| `shipping_country` | Details of the shipping address for this account. Country | `Account.ShippingCountry` | 🟢 _1.00_ | *Exact match on geographical attribute* |
| `shipping_country_code` | The ISO country code for the account’s shipping address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_geocode_accuracy` | Accuracy level of the geocode for the shipping address. | `Account.ShippingGeocodeAccuracy` | 🟢 _0.80_ | *High likelihood of matching description* |
| `shipping_latitude` | Used with ShippingLongitude to specify the precise geolocation of a shipping address. | `Account.ShippingLatitude` | 🟢 _1.00_ | *Exact match on geographical coordinates* |
| `shipping_longitude` | Used with ShippingLatitude to specify the precise geolocation of an address. | `Account.ShippingLongitude` | 🟢 _1.00_ | *Exact match on geographical coordinates* |
| `shipping_postal_code` | Details of the shipping address for this account. Postal code | `Account.ShippingPostalCode` | 🟢 _1.00_ | *Exact match on geographical attribute* |
| `shipping_state` | Details of the shipping address for this account. State | `Account.ShippingState` | 🟢 _1.00_ | *Exact match on geographical attribute* |
| `shipping_state_code` | The ISO state code for the account’s shipping address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_street` | The street address of the shipping address for this account. | `Account.ShippingStreet` | 🟢 _1.00_ | *Exact match on geographical attribute* |
| `sic` | Standard Industrial Classification code of the company’s main business categorization, for example, 57340 for Electronics. | `Account.Sic` | 🟢 _0.90_ | *Direct business categorization match* |
| `sic_desc` | A brief description of an organization’s line of business, based on its SIC code. | `Account.SicDesc` | 🟢 _0.90_ | *Matches descriptive business categorization* |
| `site` | Name of the account’s location, for example Headquarters or London. | `Account.Site` | 🟢 _0.80_ | *Representative of location-based attribute* |
| `ticker_symbol` | The stock market symbol for this account. This field is available on business accounts, not person accounts. | `Account.TickerSymbol` | 🟢 _0.70_ | *Reflects financial market identification* |
| `type` | Type of account, for example, Customer, Competitor, or Partner. | `Account.Type` | 🟢 _1.00_ | *Matches type categorization directly* |
| `website` | The website of this account. | `Account.Website` | 🟢 _1.00_ | *Matches digital contact attribute directly* |

### Mapping: Airbyte `LeadHistory` to Fivetran `lead`


- Table Match Confidence Score: ⚠️ _0.50_
- Table Completion Score: ❌ _0.40_
- Summary Self-Evaluation: _Given the high number of fields with an expression set to 'MISSING', indicating a lack of a direct or satisfactory match, the overall mapping confidence is moderate. The table match suggests some relation, reflective of a typical Airbyte to Fivetran syncing scenario; however, several critical data points for effective transformation could not be adequately mapped._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The unique, system-generated ID assigned during creation. | `LeadHistory.Id` | 🟢 _0.80_ | *Direct mapping available from 'LeadHistory.Id'* |
| `_fivetran_synced` | The time at which fivetran last synced this record | `LeadHistory._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to '_airbyte_extracted_at' as per guidelines.* |
| `_fivetran_active` | True if record is active, used to filter out only active records if History Mode is enabled | `LeadHistory.IsDeleted` | 🟢 _0.70_ | *Mapping 'LeadHistory.IsDeleted' to '_fivetran_active' reasonably captures the active status based on deletion flag.* |
| `annual_revenue` | Annual revenue for the lead’s company. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `city` | City for the lead’s address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `company` | Required. The lead’s company. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `converted_account_id` | Object reference ID that points to the account into which the lead converted. This is a relationship field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `converted_contact_id` | Object reference ID that points to the contact into which the lead converted. This is a relationship field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `converted_date` | Date on which this lead was converted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `converted_opportunity_id` | Object reference ID that points to the opportunity into which the lead has been converted. This is a relationship field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `country` | The lead’s country. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `country_code` | The ISO country code for the lead’s address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_by_id` | Created By ID | `LeadHistory.CreatedById` | 🟢 _0.80_ | *Direct mapping available from 'LeadHistory.CreatedById'* |
| `created_date` | Created Date | `LeadHistory.CreatedDate` | 🟢 _0.80_ | *Direct mapping available from 'LeadHistory.CreatedDate'* |
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
