# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping from Airbyte `campaigns` to Fivetran `campaign_history`

- Table Match Confidence Score: 🟢 1.00

- Table Completion Score: 🟢 1.00

#### Evaluation

All provided field mappings closely correspond to the source fields for the campaigns table, thus the highest confidence scores apply for the overall table and field mappings.


#### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of the campaign. | `campaigns.id` | 🟢 1.00 | Direct match with the field 'campaigns.id'. |
| `account_id` | The ID of the ad account that this campaign belongs to. | `campaigns.account_id` | 🟢 1.00 | Direct match with the field 'campaigns.account_id'. |
| `name` | The name of the campaign. | `campaigns.name` | 🟢 1.00 | Direct match with the field 'campaigns.name'. |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `campaigns._airbyte_extracted_at` | 🟢 1.00 | Standard match for '_fivetran_synced' with 'campaigns._airbyte_extracted_at'. |
| `updated_time` | {{ doc('updated_time') }} | `campaigns.updated_time` | 🟢 1.00 | Direct match with the field 'campaigns.updated_time'. |
| `created_time` | The time the campaign was created. | `campaigns.created_time` | 🟢 1.00 | Direct match with the field 'campaigns.created_time'. |
| `start_time` | Timestamp of designated campaign start time. | `campaigns.start_time` | 🟢 1.00 | Direct match with the field 'campaigns.start_time'. |
| `stop_time` | Timestamp of designated campaign end time. | `campaigns.stop_time` | 🟢 1.00 | Direct match with the field 'campaigns.stop_time'. |
| `daily_budget` | Daily budget of campaign. | `campaigns.daily_budget` | 🟢 1.00 | Direct match with the field 'campaigns.daily_budget'. |
| `budget_remaining` | Remaining budget of campaign. | `campaigns.budget_remaining` | 🟢 1.00 | Direct match with the field 'campaigns.budget_remaining'. |
| `lifetime_budget` | Lifetime budget of the campaign. | `campaigns.lifetime_budget` | 🟢 1.00 | Direct match with the field 'campaigns.lifetime_budget'. |
| `status` | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | `campaigns.status` | 🟢 1.00 | Direct match with the field 'campaigns.status'. The status values are assumed to directly correspond. |


### Mapping from Airbyte `ads_insights` to Fivetran `basic_ad`

- Table Match Confidence Score: 🟢 0.90

- Table Completion Score: 🟢 0.95

#### Evaluation

The mapping is very comprehensive and the fields provided closely match the target schema. Most fields have a clear counterpart in the target schema, providing high confidence scores.


#### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `ad_id` | The ID of the ad the report relates to. | `ads_insights.ad_id` | 🟢 1.00 | Exact match found for ad_id. |
| `ad_name` | Name of the ad the report relates to. | `ads_insights.ad_name` | 🟢 1.00 | Exact match found for ad_name. |
| `adset_name` | Name of the ad set the report relates to. | `ads_insights.adset_name` | 🟢 1.00 | Exact match found for adset_name. |
| `date` | The date of the reported performance. | `ads_insights.date_start` | 🟢 1.00 | Exact match found for date. |
| `account_id` | The ID of the ad account that this ad belongs to. | `ads_insights.account_id` | 🟢 1.00 | Exact match found for account_id. |
| `impressions` | The number of impressions the ad had on the given day. | `ads_insights.impressions` | 🟢 1.00 | Exact match found for impressions. |
| `inline_link_clicks` | The number of clicks the ad had on the given day. | `ads_insights.inline_link_clicks` | 🟢 1.00 | Exact match found for inline_link_clicks. |
| `spend` | The spend on the ad in the given day. | `ads_insights.spend` | 🟢 1.00 | Exact match found for spend. |
| `reach` | The number of people who saw any content from your Page or about your Page. This metric is estimated. | `ads_insights.reach` | 🟢 1.00 | Exact match found for reach. |
| `frequency` | The average number of times each person saw your ad; it is calculated as impressions divided by reach. | `ads_insights.frequency` | 🟢 1.00 | Exact match found for frequency. |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ads_insights._airbyte_extracted_at` | 🟢 1.00 | Mapped to _airbyte_extracted_at as per standard procedure. |


### Mapping from Airbyte `ad_sets` to Fivetran `ad_set_history`

- Table Match Confidence Score: 🟢 0.85

- Table Completion Score: 🟢 0.75

#### Evaluation

The table mapping evaluation indicates a moderate to high confidence in the table subject matching, primarily based on shared semantics derived from similar schemas in the source and target tables, both of which are generated from equivalent API endpoints. However, there are significant disparities in the field mappings, particularly with undefined fields marked as 'MISSING', which affects the completion score.


#### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of the ad set. | `ad_sets.id` | 🟢 0.95 | The 'id' field has a clear and direct match between source and target. |
| `account_id` | The ID of the ad account that this ad set belongs to. | `ad_sets.account_id` | 🟢 0.95 | The 'account_id' field is well matched, sharing common semantics between the source and target implementations. |
| `campaign_id` | Ad campaign that contains this ad set. | `ad_sets.campaign_id` | 🟢 0.95 | The 'campaign_id' field links directly to the same concept in both source and target schemas. |
| `name` | The name of the ad set. | `ad_sets.name` | 🟢 0.95 | The 'name' field matches perfectly, consistent across the source and target mappings. |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ad_sets._airbyte_extracted_at` | 🟢 1.00 | Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at', which is always given a score of 1.00. |
| `updated_time` | {{ doc('updated_time') }} | `ad_sets.updated_time` | 🟢 0.95 | The 'updated_time' field shows a strong match, representing the same data in the source and target. |
| `start_time` | Timestamp of designated ad set start time. | `ad_sets.start_time` | 🟢 0.95 | The 'start_time' field is matched accurately, denoting identical timestamps. |
| `end_time` | Timestamp of designated ad set end time. | `ad_sets.end_time` | 🟢 0.95 | The 'end_time' field mapping is confident, referring to the same entity in both schemas. |
| `bid_strategy` | Bid strategy values are - 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', 'LOWEST_COST_WITH_MIN_ROAS'. | `ad_sets.bid_strategy` | 🟢 0.95 | The 'bid_strategy' field matches well, reflecting identical bid configurations. |
| `daily_budget` | Daily budget of ad set. | `ad_sets.daily_budget` | 🟢 0.95 | The 'daily_budget' field is well matched with aligned semantics in both implementations. |
| `budget_remaining` | Remaining budget of ad set. | `ad_sets.budget_remaining` | 🟢 0.95 | The 'budget_remaining' field corresponds well to the remaining budget information in both schemas. |
| `status` | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | `ad_sets.effective_status` | 🟢 0.95 | The 'status' field shows high confidence due to consistent enumerated value definitions. |
| `optimization_goal` | The optimization goal this ad set is using. Possible values defined [here](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/#fields). | `MISSING` | ❌ 0.00 | No good match found. |


### Mapping from Airbyte `ad_account` to Fivetran `account_history`

- Table Match Confidence Score: 🟢 0.85

- Table Completion Score: 🟢 0.90

#### Evaluation

The table mapping is strong with most fields mapped accurately from source to target. Standard mappings and casing differences align correctly. No significant mismatches found that would lower confidence.


#### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of the ad account. | `ad_account.id` | 🟢 0.95 | Source field 'ad_account.id' matches closely with expected target field 'id'. |
| `name` | Name of the account. | `ad_account.name` | 🟢 0.95 | Source field 'ad_account.name' matches closely with expected target field 'name'. |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ad_account._airbyte_extracted_at` | 🟢 1.00 | Standard mapping of '_fivetran_synced' to 'ad_account._airbyte_extracted_at'. |
| `account_status` | Current status of account. | `ad_account.account_status` | 🟢 0.90 | The field 'ad_account.account_status' matches well with the target expectation of 'account_status'. |
| `business_country_code` | Country code of business associated to account. | `ad_account.business_country_code` | 🟢 0.90 | Field 'ad_account.business_country_code' has a high confidence mapping to 'business_country_code'. |
| `created_time` | The time account was created. | `ad_account.created_time` | 🟢 0.90 | Field 'ad_account.created_time' is expected to match the target 'created_time' well. |
| `currency` | Currency associated with account. | `ad_account.currency` | 🟢 0.90 | The field 'ad_account.currency' maps confidently to 'currency'. |
| `timezone_name` | Timezone associated with account. | `ad_account.timezone_name` | 🟢 0.90 | The source field 'ad_account.timezone_name' matches well with 'timezone_name'. |


### Mapping from Airbyte `ads` to Fivetran `ad_history`

- Table Match Confidence Score: 🟢 0.80

- Table Completion Score: 🟢 0.90

#### Evaluation

The table mapping is highly confident; all fields except 'conversion_domain' are well-matched. Matches from source to target are clear and relevant.


#### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of this ad. | `ads.id` | 🟢 1.00 | Exact match for 'id' field. |
| `account_id` | The ID of the ad account that this ad belongs to. | `ads.account_id` | 🟢 1.00 | Exact match for 'account_id' field. |
| `ad_set_id` | ID of the ad set that contains the ad. | `ads.adset_id` | 🟢 1.00 | Exact match for 'ad_set_id' field. |
| `campaign_id` | Ad campaign that contains this ad. | `ads.campaign_id` | 🟢 1.00 | Exact match for 'campaign_id' field. |
| `creative_id` | The ID of the ad creative to be used by this ad. | `ads.creative.creative_id` | 🟢 1.00 | Exact match for 'creative_id' field. |
| `name` | Name of the ad. | `ads.name` | 🟢 1.00 | Exact match for 'name' field. |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ads._airbyte_extracted_at` | 🟢 1.00 | Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at'. |
| `updated_time` | {{ doc('updated_time') }} | `ads.updated_time` | 🟢 1.00 | Exact match for 'updated_time' field. |
| `conversion_domain` | The domain you've configured the ad to convert to. | `MISSING` | ❌ 0.00 | No good match found. |


## Workshop Models

These models are in the workshop directory and are not yet approved.

### Mapping from Airbyte `ad_creatives` to Fivetran `creative_history`

- Table Match Confidence Score: 🟢 0.95

- Table Completion Score: 🟢 0.82

#### Evaluation

The table mappings are from similar source and target schemas with consistent subject matter. However, some fields were missing a good match. The table has a high match score due to strong alignment in identifiers and account fields, but completion is not perfect due to missing fields.


#### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_id` | Unique record identifier | `MISSING` | ❌ 0.00 | No good match found. |
| `page_link` | URL destination of Facebook ads. | `MISSING` | ❌ 0.00 | No good match found. |
| `template_page_link` | URL destination of Facebook dynamic ads. | `MISSING` | ❌ 0.00 | No good match found. |
| `id` | Unique ID for an ad creative. | `ad_creatives.id` | 🟢 0.80 | Mapping is specific and contextually appropriate. |
| `account_id` | Ad account ID for the account this ad creative belongs to. | `ad_creatives.account_id` | 🟢 0.80 | Mapping is specific and contextually appropriate. |
| `name` | Name of this ad creative as seen in the ad account's library. | `ad_creatives.name` | 🟢 0.80 | Mapping is specific and contextually appropriate. |
| `url_tags` | A set of query string parameters which will replace or be appended to urls clicked from page post ads, message of the post, and canvas app install creatives only. | `ad_creatives.url_tags` | 🟢 0.80 | Mapping is specific and contextually appropriate. |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ad_creatives._airbyte_extracted_at` | 🟢 1.00 | Standard mapping for synchronization fields. |
| `asset_feed_spec_link_urls` | Link to the asset feed spec | `ad_creatives.asset_feed_spec.link_urls` | ⚠️ 0.50 | Possible match but not certain. |
| `object_story_link_data_child_attachments` | Link of the object story child attachments | `ad_creatives.object_story_spec.link_data.child_attachments` | ⚠️ 0.50 | Possible match but not certain. |
| `object_story_link_data_caption` | Link of the object story caption | `ad_creatives.object_story_spec.link_data.caption` | ⚠️ 0.50 | Possible match but not certain. |
| `object_story_link_data_description` | Link of the object story description | `ad_creatives.object_story_spec.link_data.description` | ⚠️ 0.50 | Possible match but not certain. |
| `object_story_link_data_link` | Link of the object story link | `ad_creatives.object_story_spec.link_data.link` | ⚠️ 0.50 | Possible match but not certain. |
| `object_story_link_data_message` | Link of the object story message | `ad_creatives.object_story_spec.link_data.message` | ⚠️ 0.50 | Possible match but not certain. |
| `template_app_link_spec_ios` | Link of the object story spec for ios | `ad_creatives.object_story_spec.template_data.app_link_spec.ios` | ⚠️ 0.50 | Possible match but not certain. |
| `template_app_link_spec_ipad` | Link of the template app spec for ipad | `ad_creatives.object_story_spec.template_data.app_link_spec.ipad` | ⚠️ 0.50 | Possible match but not certain. |
| `template_app_link_spec_android` | Link of the template app for android | `ad_creatives.object_story_spec.template_data.app_link_spec.android` | ⚠️ 0.50 | Possible match but not certain. |
| `template_app_link_spec_iphone` | Link of the template app for iphone | `ad_creatives.object_story_spec.template_data.app_link_spec.iphone` | ⚠️ 0.50 | Possible match but not certain. |


### Mapping from Airbyte `ads_insights` to Fivetran `basic_ad_actions`

- Table Match Confidence Score: ⚠️ 0.65

- Table Completion Score: ❌ 0.40

#### Evaluation

The table mapping shows a moderate match given the context of the fields provided. Some fields have been mapped with confidence, but there are significant number of fields missing a valid match, impacting the overall completion.


#### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_1_d_view` | Conversion metric value using an attribution window of "1 day after viewing the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ 0.00 | No good match found. |
| `_7_d_click` | Conversion metric value using an attribution window of "7 days after clicking the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ 0.00 | No good match found. |
| `_28_d_click` | Conversion metric value using an attribution window of "28 days after clicking the ad". Deprecated by Facebook due to digital privacy initiatives. Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ 0.00 | No good match found. |
| `_fivetran_id` | Defunct field. | `MISSING` | ❌ 0.00 | No good match found. |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ads_insights._airbyte_extracted_at` | 🟢 1.00 | _fivetran_synced is correctly mapped to ads_insights._airbyte_extracted_at. |
| `action_type` | The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions prepended by app_custom_event come from mobile app events and actions prepended by offsite_conversion come from the Facebook Pixel.  | `ads_insights.actions` | 🟢 0.70 | action_type is mapped to ads_insights.actions based on contextual similarity. |
| `ad_id` | The ID of the ad the report relates to. | `ads_insights.ad_id` | 🟢 0.70 | ad_id is mapped to ads_insights.ad_id based on direct name and purpose matching. |
| `date` | The date of the reported performance. | `ads_insights.date_start` | 🟢 0.70 | date is matched to ads_insights.date_start. This matches the purpose of recording performance date. |
| `index` | Index reflecting the `action_type` tracked for this ad on this day. Column of not much consequence. | `MISSING` | ❌ 0.00 | No good match found. |
| `inline` | Conversion metric value using the attribution window that occurs on the ad itself. Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `MISSING` | ❌ 0.00 | No good match found. |
| `value` | Conversion metric value using the default attribution window. | `MISSING` | ❌ 0.00 | No good match found. |


### Mapping from Airbyte `ads_insights` to Fivetran `basic_ad_action_values`

- Table Match Confidence Score: ❌ 0.00

- Table Completion Score: ❌ 0.25

#### Evaluation

The table match score is 0.0 as the fields do not suggest a coherent table matching due to missing and unclear mappings. The completion score is 0.25 because only 2 out of 8 fields are precisely mapped or have clear logic, primarily due to 2 'MISSING' expressions indicating a failure to map necessary fields.


#### Field Mapping Logic

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_7_d_click` | Conversion metric value using an attribution window of "7 days after clicking the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. | `ads_insights.attribution_setting` | ⚠️ 0.55 | The field '_7_d_click' is not directly mapped in a clear manner to the source and is somewhat inferred. Given name usage could broadly match Facebook ad insights overlap but lacks clear matching. |
| `_fivetran_id` | Defunct field. | `MISSING` | ❌ 0.00 | Expression is 'MISSING'. No good match found. |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ads_insights._airbyte_extracted_at` | 🟢 1.00 | Standard mapping to `_airbyte_extracted_at`. Always scores 1.00. |
| `action_type` | The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions prepended by app_custom_event come from mobile app events and actions prepended by offsite_conversion come from the Facebook Pixel.  | `ads_insights.actions` | ⚠️ 0.65 | The expression 'ads_insights.actions' commonly refers to ad actions but could encompass broad category types with possible good fit due to description match. |
| `ad_id` | The ID of the ad the report relates to. | `MISSING` | ❌ 0.00 | Expression is 'MISSING'. No good match found. |
| `date` | The date of the reported performance. | `ads_insights.date_start` | ⚠️ 0.60 | The 'date' maps well to 'ads_insights.date_start', showing date logic but slightly unclear due to name plurality variance. |
| `index` | Index reflecting the `action_type` tracked for this ad on this day. Column of not much consequence. | `ads_insights.conversion_rate_ranking` | ⚠️ 0.55 | The mapping to 'ads_insights.conversion_rate_ranking' is a possible vague match in concept but lacks better contextual linking. |
| `value` | Monetary value associated with the convesion action using the default attribution window. | `ads_insights.conversion_values` | 🟢 0.70 | Expression 'ads_insights.conversion_values' aligns with conversion metric insights provided by Facebook, showing fairly high mapping confidence. |

