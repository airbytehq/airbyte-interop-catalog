# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `calls` to Fivetran `call`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _Overall, the mappings provided accurately represent the intrinsic relationships between source and target schemas, ensuring comprehensive but cautious transformation of data from the Airbyte source to the Fivetran-like schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | Timestamp of when fivetran synced a record. | `calls._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match of standardized syncing timestamps.* |
| `account_id` | The unique identifier for the Account responsible for this Call. | `calls.account_sid` | 🟢 _0.95_ | *Direct match between source and target for unique account identifiers.* |
| `annotation` | A user-defined string that provides additional information about the Call. | `calls.annotation` | 🟢 _0.90_ | *The descriptions and field names align very well between source and target.* |
| `answered_by` | The identity of the recipient that answered the Call. | `calls.answered_by` | 🟢 _0.90_ | *The semantic meaning and role of this field in call handling are consistent between the two systems.* |
| `caller_name` | The caller's name, if available. | `calls.caller_name` | 🟢 _0.88_ | *Name mapping is generally consistent, with high confidence of identical data roles.* |
| `created_at` | The date and time when the Call was created, given as GMT in RFC 2822 format. | `calls.date_created` | 🟢 _0.95_ | *Direct mapping of creation timestamps with high relevance and format consistency.* |
| `direction` | The direction of the Call - `inbound` for incoming calls, `outbound-api` for calls initiated via the REST API, and `outbound-dial` for calls initiated by a TwiML `<Dial` verb. | `calls.direction` | 🟢 _0.90_ | *Field meaning is directly transferable and description is exactly matching.* |
| `duration` | The duration of the Call in seconds. | `calls.duration` | 🟢 _0.95_ | *Unambiguous match of call duration fields, directly comparable.* |
| `end_time` | The date and time when the Call ended, given as GMT in RFC 2822 format. | `calls.end_time` | 🟢 _0.95_ | *Highly consistent mapping for end timing of events, ensuring data synchronization.* |
| `forwarded_from` | The phone number that initiated the Call, if applicable. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `from` | The phone number or client identifier that made the Call. | `calls.from` | 🟢 _0.95_ | *Direct correspondence found in originating identifiers.* |
| `from_formatted` | The formatted version of the `from` phone number or client identifier. | `calls.from_formatted` | 🟢 _0.95_ | *The formatted version of the from field matches perfectly.* |
| `group_id` | The unique identifier for the grouping of related Calls. | `calls.group_sid` | 🟢 _0.90_ | *Unique identifiers for group relations are consistent across schemas.* |
| `id` | The unique identifier for the Call resource. | `calls.sid` | 🟢 _0.95_ | *Direct mapping of unique call identifiers.* |
| `outgoing_caller_id` | The unique identifier for the Outgoing Caller ID resource associated with the Call. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `parent_call_id` | The unique identifier for the Call that created this Call as a result of executing TwiML. | `calls.parent_call_sid` | 🟢 _0.90_ | *Hierarchical relationship preserved with high confidence in mapping.* |
| `price` | The cost of the Call in the specified `price_unit`. | `calls.price` | 🟢 _0.90_ | *The price fields align well in terms of currency context and value meaning.* |
| `price_unit` | The currency unit in which the `price` is measured. | `calls.price_unit` | 🟢 _0.90_ | *Currencies representation matches with complete semantic alignment.* |
| `queue_time` | The time spent in the queue before the Call is placed, in milliseconds. | `calls.queue_time` | 🟢 _0.90_ | *Timestamp significance and role accurately mapped from source to target.* |
| `start_time` | The date and time when the Call started, given as GMT in RFC 2822 format. | `calls.start_time` | 🟢 _0.95_ | *The start times sync perfectly across the temporal context of both schemas.* |
| `status` | The current status of the Call - `queued`, `ringing`, `in-progress`, `completed`, `busy`, `failed`, `no-answer`, or `canceled`. | `calls.status` | 🟢 _0.95_ | *Status fields correlate well, reflecting similar stages in the call lifecycle between schemas.* |
| `to` | The phone number or client identifier that received the Call. | `calls.to` | 🟢 _0.95_ | *Recipient identifier mappings are concise and accurate.* |
| `to_formatted` | The formatted version of the `to` phone number or client identifier. | `calls.to_formatted` | 🟢 _0.95_ | *Formatted recipient information matches perfectly, reflecting a clear and direct equivalence.* |
| `trunk_id` | The unique identifier for the Trunk resource associated with the Call. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `updated_at` | The date and time when the Call record was last updated, given as GMT in RFC 2822 format. | `calls.date_updated` | 🟢 _0.95_ | *Update timestamps match with high relevance and similar formatting.* |

### Mapping: Airbyte `conversations` to Fivetran `messaging_service`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The source and target tables are known to be generated from the same upstream source, demonstrating a high correspondence in content and purpose. However, numerous 'MISSING' assignments of expressions for the target schema reduces the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | Timestamp of when fivetran synced a record. | `conversations._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping as prescribed.* |
| `account_id` | The unique identifier of the account that owns the messaging service. | `conversations.account_sid` | 🟢 _1.00_ | *Directly corresponds to the source field 'conversations.account_sid'.* |
| `area_code_geomatch` | Boolean of whether phone numbers used by this messaging service are required to be geo-matched to the message sender's area code. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | The date and time when the messaging service was created. | `conversations.date_created` | 🟢 _1.00_ | *Directly maps to 'conversations.date_created' from source.* |
| `fallback_method` | The HTTP method Twilio will use to send requests to the fallback URL when an error occurs in the messaging service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `fallback_to_long_code` | Specifies whether to fallback to long code phone numbers when short code phone numbers are not available or cannot be used. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `fallback_url` | The URL that Twilio will request  if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `friendly_name` | A human-readable descriptive name for the messaging service. | `conversations.friendly_name` | 🟢 _1.00_ | *Mapped to 'conversations.friendly_name' from source.* |
| `id` | The unique identifier of the messaging service. | `conversations.messaging_service_sid` | 🟢 _1.00_ | *Mapped to 'conversations.messaging_service_sid' from source.* |
| `inbound_method` | The HTTP method Twilio will use to send requests to the inbound request URL of the messaging service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `inbound_request_url` | The URL we call using inbound_method when a message is received by any phone number or short code in the Service. When this property is null, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the use_inbound_webhook_on_number field is enabled then the webhook url defined on the phone number will override the inbound_request_url defined for the Messaging Service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `mms_converter` | Specifies the method to convert outbound MMS content. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `scan_message_content` | Specifies whether to scan the content of outbound messages sent using the messaging service for harmful or unwanted content. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `smart_encoding` | Specifies whether Twilio should attempt to optimize the message encoding for the messaging service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status_callback` | The URL that Twilio will request to pass status updates of sent messages to the messaging service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sticky_sender` | Specifies whether to assign a single sender phone number for all outbound messages sent from the messaging service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `synchronous_validation` | Specifies whether to enable or disable synchronous validation of requests to the messaging service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `updated_at` | The date and time when the messaging service was last updated. | `conversations.date_updated` | 🟢 _1.00_ | *Mapped to 'conversations.date_updated' from source.* |
| `us_app_to_person_registered` | Specifies whether to enable or disable routing inbound messages to the messaging service using US App-to-Person (A2P) routing. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `use_inbound_webhook_on_number` | Specifies whether to use inbound webhooks for handling incoming messages to the messaging service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `usecase` | Specifies the intended use case of the messaging service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `validity_period` | How long, in seconds, messages sent from the Service are valid. Can be an integer from 1 to 14,400. | `MISSING` | ❌ _0.00_ | *No good match found.* |
