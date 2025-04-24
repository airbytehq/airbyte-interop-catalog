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

> [!Tip]
> Use the right-hand navigation to quickly browse available dataset mappings.

> [!Warning]
> AI-generated results may contain errors. Please sanity check results and adapt these resources to your needs accordingly.


### Mapping: Airbyte `outgoing_caller_ids` to Fivetran `outgoing_caller_id`


- Table Match Confidence Score: 🟢 _0.95_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping is highly reliable with a near-identical structure and format between the source and target schemas, which are derived from comparable API implementations. Most fields are well-aligned, though not all from the source are present in the target, explaining the slightly less than perfect completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | Timestamp of when fivetran synced a record. | `outgoing_caller_ids._airbyte_extracted_at` | 🟢 _1.00_ | *Direct standard mapping of sync times between systems.* |
| `created_at` | The date that this resource was created, given in RFC 2822 format. | `outgoing_caller_ids.date_created` | 🟢 _0.90_ | *Direct match in intent and schema position for date creation fields.* |
| `friendly_name` | A human readable descriptive text for this resource, up to 64 characters long. By default, the FriendlyName is a nicely formatted version of the phone number. | `outgoing_caller_ids.friendly_name` | 🟢 _0.85_ | *High relevance mapping, minor doubts about consistent usage across contexts.* |
| `id` | The unique string that identifies this resource. | `outgoing_caller_ids.sid` | 🟢 _1.00_ | *Universal identifier field, perfectly matched.* |
| `phone_number` | The incoming phone number. Formatted with a '+' and country code e.g., +16175551212 (E.164 format). | `outgoing_caller_ids.phone_number` | 🟢 _0.90_ | *Exact match in data representation and purpose between schemas.* |
| `updated_at` | The date that this resource was last updated, given in RFC 2822 format. | `outgoing_caller_ids.date_updated` | 🟢 _0.85_ | *Direct mapping with high confidence; slight uncertainty due to various update triggers across systems.* |

### Mapping: Airbyte `accounts` to Fivetran `account_history`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table mapping significantly aligns with the target schema with minor differences in field completeness. Most source fields appropriately match the target fields, hinting at a strong semantic correlation._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | Timestamp of when fivetran synced a record. | `accounts._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect mapping of standard timestamp fields across systems.* |
| `created_at` | The date and time when the account history record was created. | `accounts.date_created` | 🟢 _0.90_ | *Direct mapping of creation date fields, highly reliable match.* |
| `friendly_name` | A user-friendly name or label associated with the account history event. | `accounts.friendly_name` | 🟢 _0.80_ | *Good semantic match for descriptive labels of accounts.* |
| `id` | The unique identifier for the account history record. | `accounts.sid` | 🟢 _1.00_ | *Direct mapping of unique identifiers, exact match.* |
| `owner_account_id` | The unique id that represents the parent of this account. The OwnerAccountSid of a parent account is it's own sid. | `accounts.owner_account_sid` | 🟢 _0.70_ | *Likely mapping of parent account identifiers, slight potential for misinterpretation.* |
| `status` | The status or state of the account history event. | `accounts.status` | 🟢 _0.70_ | *General term matched to a specific status field, strong likelihood of accurate mapping but not absolute.* |
| `type` | The type or category of the account history event. | `accounts.type` | 🟢 _0.70_ | *Conceptual match between type categories, mostly accurate but with room for ambiguity.* |
| `updated_at` | The date and time when the account history record was last updated. | `accounts.date_updated` | 🟢 _0.90_ | *Direct match for fields indicating the last update time, very reliable mapping.* |

### Mapping: Airbyte `usage_records` to Fivetran `usage_record`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The provided field mappings from source 'usage_records' to target '_fivetran_synced' are well-matched, reflecting a good understanding of the source data. Only minor gaps in field mappings reduce the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | Timestamp of when fivetran synced a record. | `usage_records._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match as per standard practice mapping `_airbyte_extracted_at`.* |
| `account_id` | The unique identifier of the account associated with the usage record. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `as_of` | Usage records up to date as of this timestamp, formatted as YYYY-MM-DDTHH:MM:SS+00:00. All timestamps are in GMT | `usage_records.as_of` | 🟢 _0.90_ | *Direct match based on field name and data format.* |
| `category` | The category of usage. | `usage_records.category` | 🟢 _0.90_ | *Direct match based on field name and usage context.* |
| `count` | The number of usage events, such as the number of calls. | `usage_records.count` | 🟢 _0.90_ | *Direct match based on field name and measurement context.* |
| `count_unit` | The units in which count is measured, such as calls for calls or messages for SMS. | `usage_records.count_unit` | 🟢 _0.90_ | *Direct match based on field name, context of unit measurement matches.* |
| `description` | A brief description or summary of the usage record. | `usage_records.description` | 🟢 _0.90_ | *Descriptive match based on usage and semantics.* |
| `end_date` | The end date of the usage period for the record. | `usage_records.end_date` | 🟢 _0.90_ | *Direct match based on field name and date context.* |
| `price` | The cost or price associated with the resource usage. | `usage_records.price` | 🟢 _0.90_ | *Direct match based on field name and financial context.* |
| `price_unit` | The currency unit for the price. | `usage_records.price_unit` | 🟢 _0.90_ | *Direct match given unit context.* |
| `start_date` | The first date for which usage is included in this UsageRecord. The date is specified in GMT and formatted as YYYY-MM-DD. | `usage_records.start_date` | 🟢 _0.90_ | *Direct match based on field name and date context.* |
| `usage` | The amount used to bill usage and measured in units described in usage_unit. | `usage_records.usage` | 🟢 _0.90_ | *Direct field semantic match.* |
| `usage_unit` | The units in which usage is measured, such as minutes for calls or messages for SMS. | `usage_records.usage_unit` | 🟢 _0.90_ | *Direct match focused on unit measurement context.* |

### Mapping: Airbyte `messages` to Fivetran `message`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _Table match is highly compatible based on field comparisons and matching specific data elements. Almost all fields have high-confidence mappings except a few which couldn't be mapped._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | Timestamp of when fivetran synced a record. | `messages._airbyte_extracted_at` | 🟢 _1.00_ | *Direct mapping from messages._airbyte_extracted_at, as specified.* |
| `account_id` | The unique identifier of the Account that sent or received the message. | `messages.account_sid` | 🟢 _1.00_ | *Direct mapping from messages.account_sid, perfectly aligns with target schema.* |
| `body` | The text of the message. | `messages.body` | 🟢 _1.00_ | *Direct mapping from messages.body, perfectly aligns with target schema.* |
| `created_at` | The timestamp indicating when the message was created. | `messages.date_created` | 🟢 _1.00_ | *Direct mapping from messages.date_created, perfectly aligns with target schema.* |
| `date_sent` | The timestamp indicating when the message was sent. | `messages.date_sent` | 🟢 _1.00_ | *Direct mapping from messages.date_sent, perfectly aligns with target schema.* |
| `direction` | The direction of the message.  Can be inbound for incoming messages, outbound-api for messages initiated by a REST API, outbound-call for messages initiated during a call, or outbound-reply for messages initiated in response to an incoming message. | `messages.direction` | 🟢 _1.00_ | *Direct mapping from messages.direction, perfectly aligns with target schema.* |
| `error_code` | The error code associated with the message, if applicable. | `messages.error_code` | 🟢 _1.00_ | *Direct mapping from messages.error_code, perfectly aligns with target schema.* |
| `error_message` | The description of the error_code if your message status is failed or undelivered. If the message was successful, this value is null. | `messages.error_message` | 🟢 _1.00_ | *Direct mapping from messages.error_message, perfectly aligns with target schema.* |
| `from` | The phone number or sender ID that sent the message. | `messages.from` | 🟢 _1.00_ | *Direct mapping from messages.from, perfectly aligns with target schema.* |
| `id` | The unique identifier for the message. | `messages.sid` | 🟢 _1.00_ | *Direct mapping from messages.sid, perfectly aligns with target schema.* |
| `messaging_service_sid` | The unique identifier of the messaging service associated with the message. | `messages.messaging_service_sid` | 🟢 _1.00_ | *Direct mapping from messages.messaging_service_sid, perfectly aligns with target schema.* |
| `num_media` | The number of media (e.g., images, videos) included in the message. | `messages.num_media` | 🟢 _1.00_ | *Direct mapping from messages.num_media, perfectly aligns with target schema.* |
| `num_segments` | The number of segments the message contains. A message body that is too large to be sent in a single SMS message is segmented and charged as multiple messages. Inbound messages over 160 characters are reassembled when the message is received. Note, when using a Messaging Service to send messages, num_segments will always be 0 in Twilio's response to your API request. | `messages.num_segments` | 🟢 _1.00_ | *Direct mapping from messages.num_segments, perfectly aligns with target schema.* |
| `price` | The cost of the message. | `messages.price` | ⚠️ _0.60_ | *Mapping from messages.price, slightly lower score due to potential differences in precision and format.* |
| `price_unit` | The currency unit for the message cost. | `messages.price_unit` | ⚠️ _0.60_ | *Mapping from messages.price_unit, slightly lower score due to potential differences in currency format.* |
| `status` | The status of the message. Can be accepted, scheduled, canceled, queued, sending, sent, failed, delivered, undelivered, receiving, received, or read (WhatsApp only). | `messages.status` | 🟢 _1.00_ | *Direct mapping from messages.status, perfectly aligns with target schema.* |
| `to` | The phone number or recipient ID that received the message. | `messages.to` | 🟢 _1.00_ | *Direct mapping from messages.to, perfectly aligns with target schema.* |
| `updated_at` | The timestamp indicating when the message was last updated. | `messages.date_updated` | 🟢 _1.00_ | *Direct mapping from messages.date_updated, perfectly aligns with target schema.* |

### Mapping: Airbyte `incoming_phone_numbers` to Fivetran `incoming_phone_number`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The overall confidence in the table mapping is high due to a strong correlation in the intended use of the source and target schemas, and most field mappings have been successfully aligned. However, the presence of some field mappings marked as 'MISSING' slightly lowers the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | Timestamp of when fivetran synced a record. | `incoming_phone_numbers._airbyte_extracted_at` | 🟢 _1.00_ | *Correct standard mapping for all tables.* |
| `account_id` | The unique identifier of the Account that owns this phone number resource. | `incoming_phone_numbers.account_sid` | 🟢 _0.95_ | *Direct match found for the account identifier.* |
| `address_id` | The unique identifier of the Address resource responsible for the phone number. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `address_requirements` | The specific requirements for the Address on this phone number. | `incoming_phone_numbers.address_requirements` | 🟢 _0.80_ | *Field names suggest a match in requirements specifications.* |
| `beta` | Whether this phone number is a beta number. | `incoming_phone_numbers.beta` | 🟢 _0.90_ | *Exact match found in field names and purpose.* |
| `capabilities_mms` | Indicates whether this phone number is capable of sending and receiving MMS messages. | `incoming_phone_numbers.capabilities.mms` | 🟢 _0.90_ | *Exact field found matching capabilities for MMS.* |
| `capabilities_sms` | Indicates whether this phone number is capable of sending and receiving SMS messages. | `incoming_phone_numbers.capabilities.sms` | 🟢 _0.90_ | *Exact field found matching capabilities for SMS.* |
| `capabilities_voice` | Indicates whether this phone number is capable of making and receiving voice calls. | `incoming_phone_numbers.capabilities.voice` | 🟢 _0.90_ | *Exact field found matching capabilities for voice services.* |
| `created_at` | The date and time this phone number resource was created. | `incoming_phone_numbers.date_created` | 🟢 _0.90_ | *Mapping date fields which represent similar creation timestamp information.* |
| `emergency_address_id` | The unique identifier of the Address resource to be used in case of an emergency. | `incoming_phone_numbers.emergency_address_sid` | ❌ _0.00_ | *No good match found.* |
| `emergency_status` | The emergency status of the phone number. | `incoming_phone_numbers.emergency_status` | 🟢 _0.80_ | *Both fields detail the emergency status, aligning well in functionality.* |
| `friendly_name` | A human-readable name associated with the phone number. | `incoming_phone_numbers.friendly_name` | 🟢 _0.90_ | *Direct match found for the descriptor name of the phone number.* |
| `id` | The unique identifier for this phone number resource. | `incoming_phone_numbers.sid` | 🟢 _1.00_ | *Exact match for the main identifier of the resource.* |
| `origin` | The origination type of the phone number. | `incoming_phone_numbers.origin` | 🟢 _0.70_ | *Both fields refer to the source or origin, suitable match.* |
| `phone_number` | The phone number in E.164 format. | `incoming_phone_numbers.phone_number` | 🟢 _0.90_ | *Exact match for standard phone number representation in E.164 format.* |
| `trunk_id` | The unique identifier of the Trunk resource responsible for the phone number. | `incoming_phone_numbers.trunk_sid` | ❌ _0.00_ | *No good match found.* |
| `updated_at` | The date and time this phone number resource was last updated. | `incoming_phone_numbers.date_updated` | 🟢 _0.90_ | *Fields represent the same concept of the last update time.* |
| `voice_caller_id_lookup` | Indicates whether the phone number performs a lookup of the caller ID. | `incoming_phone_numbers.voice_caller_id_lookup` | 🟢 _0.80_ | *Both fields relate to caller ID lookup functionality.* |
| `voice_url` | The URL Twilio will request when receiving a voice call to this phone number. | `incoming_phone_numbers.voice_url` | 🟢 _0.85_ | *Both fields specify the URL for handling voice calls, aligning well.* |

### Mapping: Airbyte `addresses` to Fivetran `address`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The source and target tables are closely matching since they originate from APIs serving similar structures. Most fields have clear and highly compatible mappings, but a complete perfection in field population was not achieved._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | Timestamp of when fivetran synced a record. | `addresses._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping that perfectly matches the requirement.* |
| `account_id` | The unique identifier of the account associated with the address. | `addresses.account_sid` | 🟢 _0.90_ | *Direct match of account identifiers.* |
| `city` | The city or locality of the address. | `addresses.city` | 🟢 _0.70_ | *Direct mapping of city/locality names.* |
| `created_at` | The timestamp indicating when the address record was created. | `addresses.date_created` | 🟢 _0.90_ | *Direct mapping of creation timestamps.* |
| `customer_name` | The name of the customer or contact associated with the address. | `addresses.customer_name` | 🟢 _0.80_ | *Clear match for customer names.* |
| `emergency_enabled` | A boolean value indicating whether emergency services are enabled for the address. | `addresses.emergency_enabled` | ⚠️ _0.60_ | *Boolean values aligned correctly, moderate certainty in context.* |
| `friendly_name` | A user-friendly name or label associated with the address. | `addresses.friendly_name` | 🟢 _0.80_ | *Names match well, given their descriptive nature.* |
| `id` | The unique identifier for the address record. | `addresses.sid` | 🟢 _0.90_ | *Direct match of unique identifiers.* |
| `iso_country` | The ISO country code of the address. | `addresses.iso_country` | 🟢 _0.70_ | *ISO country codes are standardized.* |
| `postal_code` | The postal code or ZIP code of the address. | `addresses.postal_code` | 🟢 _0.80_ | *Direct match of postal code fields.* |
| `region` | The region or state of the address. | `addresses.region` | ⚠️ _0.65_ | *Good fit, though some ambiguity in regional terminology.* |
| `street` | The street address. | `addresses.street` | 🟢 _0.80_ | *Direct mapping of street address fields.* |
| `updated_at` | The timestamp indicating when the address record was last updated. | `addresses.date_updated` | 🟢 _0.90_ | *Direct mapping of update timestamps.* |
| `validated` | A boolean value indicating whether the address has been validated. | `addresses.validated` | ⚠️ _0.60_ | *Boolean value representing validation status aligns well.* |
| `verified` | A boolean value indicating whether the address has been verified. | `addresses.verified` | ⚠️ _0.60_ | *Boolean values for verification status are appropriately matched.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
