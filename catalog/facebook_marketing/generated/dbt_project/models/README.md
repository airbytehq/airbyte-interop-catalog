# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

## campaign_history




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| campaigns | facebook_marketing | campaigns |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| id | campaigns.id | The ID of the campaign. |
| account_id | campaigns.account_id | The ID of the ad account that this campaign belongs to. |
| name | campaigns.name | The name of the campaign. |
| _fivetran_synced | _airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| updated_time | campaigns.updated_time | {{ doc('updated_time') }} |
| created_time | campaigns.created_time | The time the campaign was created. |
| start_time | campaigns.start_time | Timestamp of designated campaign start time. |
| stop_time | campaigns.stop_time | Timestamp of designated campaign end time. |
| daily_budget | campaigns.daily_budget | Daily budget of campaign. |
| budget_remaining | campaigns.budget_remaining | Remaining budget of campaign. |
| lifetime_budget | campaigns.lifetime_budget | Lifetime budget of the campaign. |
| status | campaigns.status | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. |



## basic_ad




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ads_insights | facebook_marketing | ads_insights |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| ad_id | ads_insights.ad_id | The ID of the ad the report relates to. |
| ad_name | ads_insights.ad_name | Name of the ad the report relates to. |
| adset_name | MISSING | Name of the ad set the report relates to. |
| date | MISSING | The date of the reported performance. |
| account_id | ads_insights.account_id | The ID of the ad account that this ad belongs to. |
| impressions | ads_insights.impressions | The number of impressions the ad had on the given day. |
| inline_link_clicks | MISSING | The number of clicks the ad had on the given day. |
| spend | ads_insights.spend | The spend on the ad in the given day. |
| reach | ads_insights.reach | The number of people who saw any content from your Page or about your Page. This metric is estimated. |
| frequency | ads_insights.frequency | The average number of times each person saw your ad; it is calculated as impressions divided by reach. |
| _fivetran_synced | _airbyte_extracted_at | {{ doc('_fivetran_synced') }} |



## creative_history




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ad_creatives | facebook_marketing | ad_creatives |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_id | MISSING | Unique record identifier |
| page_link | ad_creatives.link_url | URL destination of Facebook ads. |
| template_page_link | ad_creatives.template_url | URL destination of Facebook dynamic ads. |
| id | ad_creatives.id | Unique ID for an ad creative. |
| account_id | ad_creatives.account_id | Ad account ID for the account this ad creative belongs to. |
| name | ad_creatives.name | Name of this ad creative as seen in the ad account's library. |
| url_tags | ad_creatives.url_tags | A set of query string parameters which will replace or be appended to urls clicked from page post ads, message of the post, and canvas app install creatives only. |
| _fivetran_synced | ad_creatives._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| asset_feed_spec_link_urls | MISSING | Link to the asset feed spec |
| object_story_link_data_child_attachments | MISSING | Link of the object story child attachments |
| object_story_link_data_caption | MISSING | Link of the object story caption |
| object_story_link_data_description | MISSING | Link of the object story description |
| object_story_link_data_link | MISSING | Link of the object story link |
| object_story_link_data_message | MISSING | Link of the object story message |
| template_app_link_spec_ios | MISSING | Link of the object story spec for ios |
| template_app_link_spec_ipad | MISSING | Link of the template app spec for ipad |
| template_app_link_spec_android | MISSING | Link of the template app for android |
| template_app_link_spec_iphone | MISSING | Link of the template app for iphone |



## ad_set_history




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ad_sets | facebook_marketing | ad_sets |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| id | ad_sets.id | The ID of the ad set. |
| account_id | ad_sets.account_id | The ID of the ad account that this ad set belongs to. |
| campaign_id | ad_sets.campaign_id | Ad campaign that contains this ad set. |
| name | ad_sets.name | The name of the ad set. |
| _fivetran_synced | _airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| updated_time | ad_sets.updated_time | {{ doc('updated_time') }} |
| start_time | ad_sets.start_time | Timestamp of designated ad set start time. |
| end_time | ad_sets.end_time | Timestamp of designated ad set end time. |
| bid_strategy | ad_sets.bid_strategy | Bid strategy values are - 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', 'LOWEST_COST_WITH_MIN_ROAS'. |
| daily_budget | ad_sets.daily_budget | Daily budget of ad set. |
| budget_remaining | ad_sets.budget_remaining | Remaining budget of ad set. |
| status | MISSING | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. |
| optimization_goal | MISSING | The optimization goal this ad set is using. Possible values defined [here](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/#fields). |



## basic_ad_actions




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ads_insights | facebook_marketing | ads_insights |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _1_d_view | ads_insights.actions | Conversion metric value using an attribution window of "1 day after viewing the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. |
| _7_d_click | ads_insights.ad_click_actions | Conversion metric value using an attribution window of "7 days after clicking the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. |
| _28_d_click | ads_insights.action_values | Conversion metric value using an attribution window of "28 days after clicking the ad". Deprecated by Facebook due to digital privacy initiatives. Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. |
| _fivetran_id | ads_insights._airbyte_raw_id | Defunct field. |
| _fivetran_synced | ads_insights._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| action_type | ads_insights.action_values | The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions prepended by app_custom_event come from mobile app events and actions prepended by offsite_conversion come from the Facebook Pixel.
 |
| ad_id | ads_insights.ad_id | The ID of the ad the report relates to. |
| date | ads_insights.date_start | The date of the reported performance. |
| index | ads_insights.auction_max_competitor_bid | Index reflecting the `action_type` tracked for this ad on this day. Column of not much consequence. |
| inline | ads_insights.inline_link_clicks | Conversion metric value using the attribution window that occurs on the ad itself. Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. |
| value | ads_insights.conversion_values | Conversion metric value using the default attribution window. |



## basic_ad_action_values




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ads_insights_action_type | facebook_marketing | ads_insights_action_type |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _7_d_click | MISSING | Conversion metric value using an attribution window of "7 days after clicking the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var. |
| _fivetran_id | MISSING | Defunct field. |
| _fivetran_synced | _airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| action_type | ads_insights_action_type.action_type | The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions prepended by app_custom_event come from mobile app events and actions prepended by offsite_conversion come from the Facebook Pixel.
 |
| ad_id | ads_insights_action_type.ad_id | The ID of the ad the report relates to. |
| date | MISSING | The date of the reported performance. |
| index | MISSING | Index reflecting the `action_type` tracked for this ad on this day. Column of not much consequence. |
| value | ads_insights_action_type.value | Monetary value associated with the convesion action using the default attribution window. |



## account_history




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ad_account | facebook_marketing | ad_account |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| id | ad_account.id | The ID of the ad account. |
| name | ad_account.name | Name of the account. |
| _fivetran_synced | ad_account._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| account_status | ad_account.account_status | Current status of account. |
| business_country_code | ad_account.business_country_code | Country code of business associated to account. |
| created_time | ad_account.created_time | The time account was created. |
| currency | ad_account.currency | Currency associated with account. |
| timezone_name | ad_account.timezone_name | Timezone associated with account. |



## ad_history




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ads | facebook_marketing | ads |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| id | ads.id | The ID of this ad. |
| account_id | ads.account_id | The ID of the ad account that this ad belongs to. |
| ad_set_id | ads.adset_id | ID of the ad set that contains the ad. |
| campaign_id | ads.campaign_id | Ad campaign that contains this ad. |
| creative_id | ads.creative | The ID of the ad creative to be used by this ad. |
| name | ads.name | Name of the ad. |
| _fivetran_synced | ads._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| updated_time | ads.updated_time | {{ doc('updated_time') }} |
| conversion_domain | ads.source_ad_id | The domain you've configured the ad to convert to. |


