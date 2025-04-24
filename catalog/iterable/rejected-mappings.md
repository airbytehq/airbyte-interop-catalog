# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `email_unsubscribe` to Fivetran `user_unsubscribed_message_type`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _Both fields are marked as MISSING, indicating no successful mapping could be established. This results in the lowest possible confidence for both Table Match Score and Completion Score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_id` | A Fivetran-created unique identifier for users, derived from hashing user_id and/or email, depending on project type. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `message_type_id` | Reference to the message type from which the user unsubscribed | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `events` to Fivetran `event`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table matching moderately aligns with the target schema, reflecting some coherent data mapping. However, there are several missing FIELD expressions, indicating partial completion._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_id` | A Fivetran-created unique identifier derived from hashing campaign_id, created_at, and event_name. | `events._airbyte_raw_id` | 🟢 _0.90_ | *Direct match found with minor adjustments.* |
| `campaign_id` | Reference to the campaign from which the event originated | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `content_id` | Reference to the content the event is associated with. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | Creation timestamp | `events.createdAt` | 🟢 _1.00_ | *Perfect match.* |
| `email` | The user's email. User identifier, for email-based projects. Previously was the unique identifier for user records, for Iterable customers before August 2023.  Exists if using the history version of the table. | `events.email` | 🟢 _1.00_ | *Perfect match.* |
| `additional_properties` | json object containing addition event properties | `events.data` | 🟢 _1.00_ | *Direct mapping from a compatible field.* |
| `event_name` | Name provided to the individual event | `events._type` | 🟢 _1.00_ | *Direct mapping of event types.* |
| `message_bus_id` | Reference to the message bus associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `message_id` | Reference to the message the event is associated with | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `message_type_id` | Reference to the type of message the event is associated with | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `recipient_state` | The state of the recipient upon receiving the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status` | Status of the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `transactional_data` | Transactional data associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `unsub_source` | Source of the unsubscribe event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `user_agent` | User agent associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `user_agent_device` | The device of the user agent | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_user_id` | A Fivetran-created unique identifier for users, derived from hashing user_id and/or email, depending on project type. | `events.userId` | 🟢 _1.00_ | *Proper mapping of user ID based on project type.* |

### Mapping: Airbyte `email_unsubscribe` to Fivetran `user_unsubscribed_message_type_history`


- Table Match Confidence Score: ⚠️ _0.60_
- Table Completion Score: ❌ _0.33_
- Summary Self-Evaluation: _The table mapping shows moderate confidence with some fields correctly identified. However, two critical fields are marked as MISSING, significantly lowering the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `message_type_id` | Reference to the message type from which the user unsubscribed | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email` | Unique identifier of the user | `email_unsubscribe.email` | 🟢 _1.00_ | *Direct match found, confidence is high.* |
| `updated_at` | Last update timestamp | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `message_types` to Fivetran `message_type`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table match has a high confidence considering the alignments of some core fields. However, several key fields missing appropriate mappings significantly reduce the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifer of the message type | `message_types.id` | 🟢 _1.00_ | *Exact match found for 'id'.* |
| `name` | User defined name of the message type | `message_types.name` | 🟢 _1.00_ | *Exact match found for 'name'.* |
| `channel_id` | Channel that this message type belongs to | `message_types.channelId` | 🟢 _0.80_ | *A reasonable match found based on the provided column guidelines.* |
| `created_at` | Time when the message type was initially created | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `frequency_cap` | The maximum number of times a message of this type can be sent to a recipient within a specified time period to prevent over-messaging | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `rate_limit_per_minute` | The maximum number of messages of this type that can be sent to recipients in a minute, ensuring controlled message delivery | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `subscription_policy` | Information about the policy or rules governing how users can subscribe to or unsubscribe from this specific message type, like OptOut | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `updated_at` | Time when the message type was last updated or modified | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `events` to Fivetran `event_extension`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _All fields are marked as 'MISSING', indicating no mapping was found. Hence, both scores for table and completion are zero._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_id` | A Fivetran-created unique identifier derived from hashing campaign_id, created_at, and event_name. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `app_already_running` | Boolean indicating if the app is currently running or not | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `badge` | Badge associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `canonical_url_id` | Reference to the url associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `content_available` | Content available from the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `content_id` | Reference to the content associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deeplink_android` | Deeplink associated with the event from an android device | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deeplink_ios` | Deeplink associated with the event from an ios device | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `device` | The device associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email_id` | Reference to the email associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email_subject` | Subject of the email associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `experiment_id` | Reference to the experiment used if the event is an experiment | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `from_phone_number_id` | Reference to the phone number which the event is from | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `from_smssender_id` | Reference to the sms sender which the event is from | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `image_url` | Image url of the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_ghost_push` | Boolean indicating if the event is a result of a ghost push | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `link_id` | Reference to the link associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `link_url` | Url of the link associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `locale` | Locale associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `payload` | Payload resulted from the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `platform_endpoint` | The specific platform endpoint of the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `push_message` | Boolean indicating if the event is a push message | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `region` | Region of the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sms_message` | Boolean indicating if the event is an sms message | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sms_provider_response_code` | sms provider response code from the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sms_provider_response_message` | sms provider response message from the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sms_provider_response_more_info` | sms provider response addition info from the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sms_provider_response_status` | Status of the sms provider response from the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sound` | Boolean indicating if a sound was used with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `to_phone_number` | To phone number associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `url` | Url associated with the event | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `workflow_id` | Reference to the workflow which the event originated | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `workflow_name` | Name of the workflow which the event originated | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `catalog_collection_count` | The count of products or items collected in a catalog associated with the event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `catalog_lookup_count` | The count of times a catalog was looked up or queried during the event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `city` | The city associated with the event, which could be the location of the recipient. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `clicked_url` | The URL that was clicked by the recipient in response to the marketing message. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `country` | The country associated with the event, which could be the location of the recipient. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `error_code` | The error code or message indicating any issues or errors encountered during the event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `expires_at` | The date and time when the event or message is set to expire or become invalid. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `from_phone_number` | The phone number from which the SMS message was sent. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `in_app_body` | The content or body of an in-app message that was sent as part of the event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_sms_estimation` | A boolean indicating whether the SMS message is an estimation or not. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `labels` | Any labels or tags associated with the event, which can be used for categorization or organization. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `message_context` | Additional contextual information related to the marketing message or event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `message_status` | The status of the marketing message, such as sent, delivered, opened, etc. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `mms_send_count` | The count of multimedia messages (MMS) sent as part of the event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `product_recommendation_count` | The count of product recommendations included in the message. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `proxy_source` | Information about the source or proxy used for sending the message. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `reason` | The reason or cause associated with a specific event or action. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sms_send_count` | The count of SMS messages sent as part of the event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `web_push_body` | The content or body of a web push notification sent as part of the event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `web_push_click_action` | The action triggered when a recipient clicks a web push notification. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `web_push_icon` | The icon or image associated with the web push notification. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `web_push_message` | The message or notification sent to web users as part of the event. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `email_unsubscribe` to Fivetran `user_unsubscribed_channel`


- Table Match Confidence Score: ⚠️ _0.50_
- Table Completion Score: ❌ _0.45_
- Summary Self-Evaluation: _Field mappings show variance in confidence due to incomplete or incorrect matches. 'MISSING' mappings significantly lower the confidence._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_id` | A Fivetran-created unique identifier for users, derived from hashing user_id and/or email, depending on project type. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `channel_id` | Reference to the channel from which the user unsubscribed | `email_unsubscribe.channelId` | ⚠️ _0.55_ | *Potentially correct mapping, minor penalties due to uncertainties about table structures.* |
