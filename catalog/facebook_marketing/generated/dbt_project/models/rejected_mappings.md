# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `ad_creatives` to Fivetran `creative_history`


- Table Match Confidence Score: 🟢 _0.95_
- Table Completion Score: 🟢 _0.82_
- Summary Self-Evaluation: _The table mappings are from similar source and target schemas with consistent subject matter. However, some fields were missing a good match. The table has a high match score due to strong alignment in identifiers and account fields, but completion is not perfect due to missing fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_id` | Unique record identifier | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `page_link` | URL destination of Facebook ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `template_page_link` | URL destination of Facebook dynamic ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | Unique ID for an ad creative. | `ad_creatives.id` | 🟢 _0.80_ | *Mapping is specific and contextually appropriate.* |
| `account_id` | Ad account ID for the account this ad creative belongs to. | `ad_creatives.account_id` | 🟢 _0.80_ | *Mapping is specific and contextually appropriate.* |
| `name` | Name of this ad creative as seen in the ad account's library. | `ad_creatives.name` | 🟢 _0.80_ | *Mapping is specific and contextually appropriate.* |
| `url_tags` | A set of query string parameters which will replace or be appended to urls clicked from page post ads, message of the post, and canvas app install creatives only. | `ad_creatives.url_tags` | 🟢 _0.80_ | *Mapping is specific and contextually appropriate.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ad_creatives._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for synchronization fields.* |
| `asset_feed_spec_link_urls` | Link to the asset feed spec | `ad_creatives.asset_feed_spec.link_urls` | ⚠️ _0.50_ | *Possible match but not certain.* |
| `object_story_link_data_child_attachments` | Link of the object story child attachments | `ad_creatives.object_story_spec.link_data.child_attachments` | ⚠️ _0.50_ | *Possible match but not certain.* |
| `object_story_link_data_caption` | Link of the object story caption | `ad_creatives.object_story_spec.link_data.caption` | ⚠️ _0.50_ | *Possible match but not certain.* |
| `object_story_link_data_description` | Link of the object story description | `ad_creatives.object_story_spec.link_data.description` | ⚠️ _0.50_ | *Possible match but not certain.* |
| `object_story_link_data_link` | Link of the object story link | `ad_creatives.object_story_spec.link_data.link` | ⚠️ _0.50_ | *Possible match but not certain.* |
| `object_story_link_data_message` | Link of the object story message | `ad_creatives.object_story_spec.link_data.message` | ⚠️ _0.50_ | *Possible match but not certain.* |
| `template_app_link_spec_ios` | Link of the object story spec for ios | `ad_creatives.object_story_spec.template_data.app_link_spec.ios` | ⚠️ _0.50_ | *Possible match but not certain.* |
| `template_app_link_spec_ipad` | Link of the template app spec for ipad | `ad_creatives.object_story_spec.template_data.app_link_spec.ipad` | ⚠️ _0.50_ | *Possible match but not certain.* |
| `template_app_link_spec_android` | Link of the template app for android | `ad_creatives.object_story_spec.template_data.app_link_spec.android` | ⚠️ _0.50_ | *Possible match but not certain.* |
| `template_app_link_spec_iphone` | Link of the template app for iphone | `ad_creatives.object_story_spec.template_data.app_link_spec.iphone` | ⚠️ _0.50_ | *Possible match but not certain.* |

### Mapping: Airbyte `ads_insights` to Fivetran `basic_ad_actions`


- Table Match Confidence Score: ⚠️ _0.65_
- Table Completion Score: ❌ _0.40_
- Summary Self-Evaluation: _The table mapping shows a moderate match given the context of the fields provided. Some fields have been mapped with confidence, but there are significant number of fields missing a valid match, impacting the overall completion._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_1_d_view` | Conversion metric value using an attribution window of "1 day after viewing the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_7_d_click` | Conversion metric value using an attribution window of "7 days after clicking the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_28_d_click` | Conversion metric value using an attribution window of "28 days after clicking the ad". Deprecated by Facebook due to digital privacy initiatives. Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_id` | Defunct field. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ads_insights._airbyte_extracted_at` | 🟢 _1.00_ | *_fivetran_synced is correctly mapped to ads_insights._airbyte_extracted_at.* |
| `action_type` | The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions prepended by app_custom_event come from mobile app events and actions prepended by offsite_conversion come from the Facebook Pixel.  | `ads_insights.actions` | 🟢 _0.70_ | *action_type is mapped to ads_insights.actions based on contextual similarity.* |
| `ad_id` | The ID of the ad the report relates to. | `ads_insights.ad_id` | 🟢 _0.70_ | *ad_id is mapped to ads_insights.ad_id based on direct name and purpose matching.* |
| `date` | The date of the reported performance. | `ads_insights.date_start` | 🟢 _0.70_ | *date is matched to ads_insights.date_start. This matches the purpose of recording performance date.* |
| `index` | Index reflecting the `action_type` tracked for this ad on this day. Column of not much consequence. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `inline` | Conversion metric value using the attribution window that occurs on the ad itself. Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `value` | Conversion metric value using the default attribution window. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `ads_insights` to Fivetran `basic_ad_action_values`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.25_
- Summary Self-Evaluation: _The table match score is 0.0 as the fields do not suggest a coherent table matching due to missing and unclear mappings. The completion score is 0.25 because only 2 out of 8 fields are precisely mapped or have clear logic, primarily due to 2 'MISSING' expressions indicating a failure to map necessary fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_7_d_click` | Conversion metric value using an attribution window of "7 days after clicking the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `ads_insights.attribution_setting` | ⚠️ _0.55_ | *The field '_7_d_click' is not directly mapped in a clear manner to the source and is somewhat inferred. Given name usage could broadly match Facebook ad insights overlap but lacks clear matching.* |
| `_fivetran_id` | Defunct field. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING'. No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ads_insights._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to `_airbyte_extracted_at`. Always scores 1.00.* |
| `action_type` | The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions prepended by app_custom_event come from mobile app events and actions prepended by offsite_conversion come from the Facebook Pixel.  | `ads_insights.actions` | ⚠️ _0.65_ | *The expression 'ads_insights.actions' commonly refers to ad actions but could encompass broad category types with possible good fit due to description match.* |
| `ad_id` | The ID of the ad the report relates to. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING'. No good match found.* |
| `date` | The date of the reported performance. | `ads_insights.date_start` | ⚠️ _0.60_ | *The 'date' maps well to 'ads_insights.date_start', showing date logic but slightly unclear due to name plurality variance.* |
| `index` | Index reflecting the `action_type` tracked for this ad on this day. Column of not much consequence. | `ads_insights.conversion_rate_ranking` | ⚠️ _0.55_ | *The mapping to 'ads_insights.conversion_rate_ranking' is a possible vague match in concept but lacks better contextual linking.* |
| `value` | Monetary value associated with the convesion action using the default attribution window. | `ads_insights.conversion_values` | 🟢 _0.70_ | *Expression 'ads_insights.conversion_values' aligns with conversion metric insights provided by Facebook, showing fairly high mapping confidence.* |
