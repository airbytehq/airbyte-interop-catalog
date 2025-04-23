# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `ad_creatives` to Fivetran `creative_history`


- Table Match Confidence Score: ⚠️ _0.50_
- Table Completion Score: ❌ _0.20_
- Summary Self-Evaluation: _Given the numerous 'MISSING' expressions in the field mappings, the table mapping demonstrates an overall low confidence. While the mapping for '_fivetran_synced' is accurate, the lack of valid expressions for other crucial fields significantly lowers the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_id` | Unique record identifier | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `page_link` | URL destination of Facebook ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `template_page_link` | URL destination of Facebook dynamic ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | Unique ID for an ad creative. | `ad_creatives.id` | 🟢 _1.00_ | *Exact field match.* |
| `account_id` | Ad account ID for the account this ad creative belongs to. | `ad_creatives.account_id` | 🟢 _1.00_ | *Exact field match.* |
| `name` | Name of this ad creative as seen in the ad account's library. | `ad_creatives.name` | 🟢 _1.00_ | *Exact field match.* |
| `url_tags` | A set of query string parameters which will replace or be appended to urls clicked from page post ads, message of the post, and canvas app install creatives only. | `ad_creatives.url_tags` | 🟢 _1.00_ | *Exact field match.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ad_creatives._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables.* |
| `asset_feed_spec_link_urls` | Link to the asset feed spec | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `object_story_link_data_child_attachments` | Link of the object story child attachments | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `object_story_link_data_caption` | Link of the object story caption | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `object_story_link_data_description` | Link of the object story description | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `object_story_link_data_link` | Link of the object story link | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `object_story_link_data_message` | Link of the object story message | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `template_app_link_spec_ios` | Link of the object story spec for ios | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `template_app_link_spec_ipad` | Link of the template app spec for ipad | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `template_app_link_spec_android` | Link of the template app for android | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `template_app_link_spec_iphone` | Link of the template app for iphone | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `ads_insights_action_type` to Fivetran `basic_ad_actions`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: ❌ _0.40_
- Summary Self-Evaluation: _Given the high number of MISSING expressions indicating no good matches found for many of the fields, both table match and completion scores are impacted negatively. The presence of one correctly matched field (_fivetran_synced) does contribute positively, but overall the integration of these fields into the target schema is suboptimal._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_1_d_view` | Conversion metric value using an attribution window of "1 day after viewing the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_7_d_click` | Conversion metric value using an attribution window of "7 days after clicking the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_28_d_click` | Conversion metric value using an attribution window of "28 days after clicking the ad". Deprecated by Facebook due to digital privacy initiatives. Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_id` | Defunct field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ads_insights_action_type._airbyte_extracted_at` | 🟢 _1.00_ | *Correctly mapped to source stream's _airbyte_extracted_at column.* |
| `action_type` | The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions prepended by app_custom_event come from mobile app events and actions prepended by offsite_conversion come from the Facebook Pixel.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `ad_id` | The ID of the ad the report relates to. | `ads_insights_action_type.ad_id` | ❌ _0.00_ | *No good match found.* |
| `date` | The date of the reported performance. | `ads_insights_action_type.date_start` | ❌ _0.00_ | *No good match found.* |
| `index` | Index reflecting the `action_type` tracked for this ad on this day. Column of not much consequence. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `inline` | Conversion metric value using the attribution window that occurs on the ad itself. Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `value` | Conversion metric value using the default attribution window. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `ads_insights_action_conversion_device` to Fivetran `basic_ad_action_values`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table matching quality is high based on the standard table structure from a shared API, but the completion of field mappings is not fully achieved due to multiple 'MISSING' expressions._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_7_d_click` | Conversion metric value using an attribution window of "7 days after clicking the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_id` | Defunct field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ads_insights_action_conversion_device._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `action_type` | The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions prepended by app_custom_event come from mobile app events and actions prepended by offsite_conversion come from the Facebook Pixel.  | `ads_insights_action_conversion_device.actions` | 🟢 _0.90_ | *The mapping of 'action_type' closely matches with expected actions taken on ads.* |
| `ad_id` | The ID of the ad the report relates to. | `ads_insights_action_conversion_device.ad_id` | 🟢 _0.90_ | *'ad_id' maps directly to its corresponding ID field in the target, ensuring a high confidence.* |
| `date` | The date of the reported performance. | `ads_insights_action_conversion_device.date_start` | 🟢 _1.00_ | *Perfect mapping of 'date' to 'date_start', reflecting identical data.* |
| `index` | Index reflecting the `action_type` tracked for this ad on this day. Column of not much consequence. | `MISSING` | ⚠️ _0.50_ | *Low relevance of the 'index' makes this a lower confidence mapping.* |
| `value` | Monetary value associated with the convesion action using the default attribution window. | `ads_insights_action_conversion_device.converted_product_value` | 🟢 _0.80_ | *The 'value' maps well to 'converted_product_value', albeit with minor potential discrepancies in context.* |

### Mapping: Airbyte `ad_sets` to Fivetran `ad_history`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table match is highly confident due to correct mappings in most fields, but the completion score reflects that some critical fields are missing proper mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of this ad. | `ad_sets.id` | 🟢 _1.00_ | *Direct mapping to source field.* |
| `account_id` | The ID of the ad account that this ad belongs to. | `ad_sets.account_id` | 🟢 _1.00_ | *Direct mapping to source field.* |
| `ad_set_id` | ID of the ad set that contains the ad. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `campaign_id` | Ad campaign that contains this ad. | `ad_sets.campaign_id` | 🟢 _1.00_ | *Direct mapping to source field.* |
| `creative_id` | The ID of the ad creative to be used by this ad. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | Name of the ad. | `ad_sets.name` | 🟢 _1.00_ | *Direct mapping to source field.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ad_sets._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables to '_airbyte_extracted_at'.* |
| `updated_time` | {{ doc('updated_time') }} | `ad_sets.updated_time` | 🟢 _1.00_ | *Direct mapping to source field.* |
| `conversion_domain` | The domain you've configured the ad to convert to. | `MISSING` | ❌ _0.00_ | *No good match found.* |
