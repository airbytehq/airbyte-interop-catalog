# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping: Airbyte `campaigns` to Fivetran `campaign_history`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table mapping between source campaigns and target campaigns is highly aligned, indicating a strong correlation in the subject matter across both datasets. Fields such as 'id', 'name', and 'updated_at' have direct equivalents, contributing to a high table match score. The completion score is slightly lower due to missing mappings for certain specific fields that could not be accurately matched or were not present in the source._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier of the campaign record | `campaigns.id` | 🟢 _1.00_ | *Direct mapping with identical field names and purposes.* |
| `updated_at` | Last update's timestamp | `campaigns.updatedAt` | 🟢 _0.95_ | *Direct mapping with only slight differences in notation (underscore vs camelCase).* |
| `name` | User defined name of the campaign. | `campaigns.name` | 🟢 _1.00_ | *Perfect match between field names and purposes.* |
| `campaign_state` | State of the campaign. Can be Draft, Ready, Scheduled, Running, Finished, Starting, Aborted or Recurring | `campaigns.campaignState` | 🟢 _0.80_ | *Good match considering likely synonyms in different schema implementations.* |
| `type` | The campaign type. Can be Blast or Triggered | `campaigns.type` | 🟢 _0.70_ | *Reasonable match, although 'type' can be general, the context makes it sufficiently specific.* |
| `send_size` | Size of the campaign. Number of individuals included in the campaign | `campaigns.sendSize` | 🟢 _0.85_ | *Strong match based on field purpose and context.* |
| `start_at` | Start timestamp | `campaigns.startAt` | 🟢 _0.95_ | *Very close match, minor notation differences.* |
| `ended_at` | Ended timestamp | `campaigns.endedAt` | 🟢 _0.95_ | *Very close match, minor notation differences.* |
| `created_at` | Creation timestamp | `campaigns.createdAt` | 🟢 _0.95_ | *Very close match, minor notation differences.* |
| `recurring_campaign_id` | Reference to the recurring campaign, if applicable | `campaigns.recurringCampaignId` | ⚠️ _0.65_ | *A specific match that slightly depends on the overall schema understanding.* |
| `created_by_user_id` | Reference to the user who created the campaign | `campaigns.createdByUserId` | ⚠️ _0.60_ | *Adequate mapping, close relevance but slightly ambiguous without additional context.* |
| `template_id` | Reference to the campaign template | `campaigns.templateId` | ⚠️ _0.65_ | *Reasonable confidence, assuming 'template' refers commonly to a structural element in campaigns.* |
| `updated_by_user_id` | ID of the user who updated this record | `campaigns.updatedByUserId` | ⚠️ _0.60_ | *Adequate mapping, close relevance could vary based on schema definitions.* |
| `message_medium` | The medium that this message was sent via, for example Email or InApp | `campaigns.messageMedium` | ⚠️ _0.50_ | *Borderline acceptable, given the generic nature of 'medium' and specific use in campaign context.* |

### Mapping: Airbyte `channels` to Fivetran `channel`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _Based on the detailed matching criteria provided, there is a relative high confidence that the source and target tables are about the same subject matter, and most expected fields are aligned. Some discrepancies in completeness reduce the total score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier of the channel | `channels.id` | 🟢 _0.95_ | *Direct match on field 'id' with proper correspondence in schema.* |
| `name` | User defined name of the channel | `channels.name` | 🟢 _0.90_ | *Field 'name' matches well, and case insensitivity does not affect the score.* |
| `channel_type` | The channel type | `channels.channelType` | 🟢 _0.85_ | *Field 'channel_type' has a good semantic match even though the terms are not identical.* |
| `message_medium` | The message medium associated with the channel | `channels.messageMedium` | 🟢 _0.70_ | *Field 'message_medium' matches, but the correspondence is less obvious, hence a lower score.* |

### Mapping: Airbyte `lists` to Fivetran `list`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table match score is high at 0.9, indicating a strong likelihood that the source and target tables are describing the same content. The completion score is 0.8, reflecting that most but not all field mappings are confidently populated._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier of the list | `lists.id` | 🟢 _1.00_ | *Direct match found with exact name and context matching between lists.id and target id field, no casing difference.* |
| `name` | User defined name of the list | `lists.name` | 🟢 _1.00_ | *Exact name match and explicit context alignment between lists.name and target name field.* |
| `list_type` | The list type | `lists.listType` | 🟢 _0.90_ | *High confidence due to semantic closeness of 'listType' to 'list_type'.* |
| `created_at` | Creation timestamp | `lists.createdAt` | 🟢 _0.90_ | *Field name casing difference is not penalized, and context supports high match confidence between 'createdAt' and 'created_at'.* |
| `description` | Information about the list | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `email_unsubscribe` to Fivetran `user_unsubscribed_channel_history`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mapping score is high given that the source and target schema both derive from similar APIs ensuring a good field mapping alignment. Except for '_airbyte_extracted_at' aliasing to '_fivetran_synced', the other fields matched relatively closely._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `channel_id` | Reference to the channel from which the user unsubscribed | `email_unsubscribe.channelId` | 🟢 _0.70_ | *Fuzzy match to 'channelId' is reasonable, as both refer to identifiers of a channel in slightly different notations.* |
| `email` | Unique identifier of the user | `email_unsubscribe.email` | 🟢 _0.70_ | *Direct mapping to 'email' is accurate and common across different schemas since this is a standard field identifying unique users.* |
| `updated_at` | Last update timestamp | `email_unsubscribe._airbyte_extracted_at` | 🟢 _1.00_ | *'_airbyte_extracted_at' directly maps to '_fivetran_synced' ensuring a perfect sync of timestamp data across systems.* |

### Mapping: Airbyte `templates` to Fivetran `template_history`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.57_
- Summary Self-Evaluation: _The table match score is relatively high, indicating a good overall match in terms of data subject matter between source and target. However, the completion score is moderately low, reflecting incomplete field mappings, possibly due to missing data serialization in the source compared to the target._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifer of the template | `templates.templateId` | 🟢 _0.90_ | *High confidence: Direct match found with field names and data type.* |
| `name` | User defined name of the template | `templates.name` | 🟢 _0.90_ | *High confidence: Direct match found with field names and data type.* |
| `template_type` | The type of the template | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | Creation timestamp | `templates.createdAt` | 🟢 _0.80_ | *High confidence: Direct match in names indicating a timestamp field.* |
| `client_template_id` | Reference to the client template | `templates.clientTemplateId` | 🟢 _0.70_ | *High confidence: Names suggest a direct reference ID match, slightly nuanced due to potential differences in ID types.* |
| `creator_user_id` | Reference to the user who created the template | `templates.creatorUserId` | 🟢 _0.70_ | *Reasonable match: The names indicate a user ID reference; however, there might be small nuances in the exact type of user referenced.* |
| `message_type_id` | Reference to the message type associated with the template | `templates.messageTypeId` | 🟢 _0.70_ | *Reasonable match: Names imply a direct correlation to message type IDs, although exact match is slightly uncertain.* |
| `updated_at` | Last update timestamp | `templates.updatedAt` | 🟢 _0.80_ | *High confidence: Clearly a timestamp update field, matched directly by name.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
