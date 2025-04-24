# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `ad_groups` to Fivetran `adgroup_history`


- Table Match Confidence Score: ❌ _0.30_
- Table Completion Score: ❌ _0.20_
- Summary Self-Evaluation: _The overall match quality of the table is low with significant mismatches in field coverage and meaning between the source and target. Many fields from the source either do not serialize into the target or are placed as 'MISSING' due to lack of a good match._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `adgroup_id` | Ad group ID | `ad_groups.adgroup_id` | 🟢 _1.00_ | *Perfect match with field in source and target.* |
| `updated_at` | Time the record was updated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `advertiser_id` | Advertiser ID | `ad_groups.advertiser_id` | 🟢 _1.00_ | *Perfect match with field in source and target.* |
| `campaign_id` | The Ad group's campaign ID. | `ad_groups.campaign_id` | 🟢 _1.00_ | *Perfect match with field in source and target.* |
| `action_categories` | IDs of the action categories (behaviors) that you want to target. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `action_days` | The number of days of the time period to include action from. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `adgroup_name` | Ad group name. Character limit is 512 and cannot contain emoji. | `ad_groups.adgroup_name` | 🟢 _1.00_ | *Perfect match with field in source and target.* |
| `age_groups` | Age groups you want to target. This is the newest version of the field `age`, which was renamed after the Tiktok Ads v1.3 API release.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `android_osv` | Minimum Android version. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `app_download_url` | App download link | `ad_groups.app_download_url` | 🟢 _1.00_ | *Perfect match with field in source and target.* |
| `app_id` | The Application id of the promoted app | `ad_groups.app_id` | 🟢 _1.00_ | *Perfect match with field in source and target.* |
| `app_name` | App name. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `app_type` | App type. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `audience` | A list of audience IDs. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `audience_type` | Audience Type | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `bid` | CPC, CPM bidding, oCPM learning bidding | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `bid_type` | Bidding Strategy | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_event` | Bid method. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `budget` | Ad budget. Returns 0.0 when Campaign Budget Optimization (budget_optimize_switch) is on. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `budget_mode` | Budget mode. This field will be ignored when Campaign Budget Optimization (budget_optimize_switch) is enabled. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `carriers` | Carriers that you want to target. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `category` | Ad group category. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `click_tracking_url` | Click monitoring URL. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `connection_type` | Device connection types that you want to target. Default; unlimited. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `conversion_bid` | oCPM conversion bid | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cpv_video_duration` | Video playback duration, required if optimize_goal is VIDEO_VIEW.  Allowed values; SIX_SECONDS (video playback 6s), TWO_SECONDS (video playback 2s)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `creative_material_mode` | Creative delivery mode. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `dayparting` | Ad delivery period, the default is always and the format is 48 * 7 character string, represented by 0 or 1. > That is, with half an hour as the minimum granularity, a day (24 hours) is divided by the minimum granularity(30 mins) from Monday to Sunday. Resulting in a 48*7 format.0 represents not to be delivered, 1 represents delivery. no transmission, full transmission 0, full transmission 1 all represent full time delivery | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deep_bid_type` | Bidding strategy for in-app events. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deep_cpabid` | Deep bid | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deep_external_action` | Deep conversion event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `display_name` | Display name of ad group. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `enable_inventory_filter` | Inventory filtering (Unsafe videos will not be displayed). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `excluded_audience` | A list of audience ID to be excluded. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_action` | Conversion event for the ad group. It is required when the promoted object is an app with tracking urls, or when pixel_id is specified. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `fallback_type` | Fallback Type. If the audience do not have the app installed, you can have them fall back to install the app, or to view a specific web page. Not applicable for Deferred Deeplink. Allowed values; APP_INSTALL, WEBSITE, UNSET. If website is chosen, you need to specify the url via landing_page_url field.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `frequency` | frequency, together with frequency_schedule, controls how often people see your ad (only available for REACH ads).  For example, frequency = 2 frequency_schedule = 3 means "show ads no more than twice every 3 day".  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `frequency_schedule` | frequency, together with frequency, controls how often people see your ad (only available for REACH ads). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `gender` | Gender that you want to target. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `impression_tracking_url` | Display monitoring URL. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `interest_category_v2` | Interest classification. If the interest is specified, users that do not meet interest target will be excluded during delivery. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `ios_osv` | Minimum iOS version. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_comment_disable` | Whether to allow comments on your ads on TikTok, Vigo, Helo. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_hfss` | Whether the promoted content is HFSS foods (foods that are high in fat, salt, or sugar). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_new_structure` | Whether the campaign is a new structure. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `keywords` | Keywords used. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `landing_page_url` | Landing page URL. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `languages` | Codes of the languages that you want to target. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `location` | IDs of the locations that you want to target. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `open_url` | The specific location where you want your audience to go if they have your app installed. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `open_url_type` | The open URL type. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `operation_system` | Device operating systems that you want to target. | `MISSING` | ❌ _0.00_ | *No good match found.undiPlaceholder Day* |

### Mapping: Airbyte `ads` to Fivetran `ad_history`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The fields largely match the target schema indicating a high quality mapping, yet several fields marked 'MISSING' decrease the overall completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `ad_id` | Ad ID | `ads.ad_id` | 🟢 _1.00_ | *Exact match found.* |
| `updated_at` | Time the record was updated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `adgroup_id` | Ad group ID | `ads.adgroup_id` | 🟢 _1.00_ | *Exact match found.* |
| `advertiser_id` | Advertiser ID | `ads.advertiser_id` | 🟢 _1.00_ | *Exact match found.* |
| `campaign_id` | Campaign ID | `ads.campaign_id` | 🟢 _1.00_ | *Exact match found.* |
| `ad_name` | Ad Name. | `ads.ad_name` | 🟢 _1.00_ | *Exact match found.* |
| `ad_text` | The ad text. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `app_name` | The display name of app download ad. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `call_to_action` | Call to action values. | `ads.call_to_action` | 🟢 _1.00_ | *Exact match found.* |
| `click_tracking_url` | Click monitoring URL. | `ads.click_tracking_url` | 🟢 _1.00_ | *Exact match found.* |
| `create_time` | Time at which the ad was created. | `ads.create_time` | 🟢 _1.00_ | *Exact match found.* |
| `display_name` | The display name of landing page or pure exposure ad. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `image_ids` | A list of image IDs. | `ads.image_ids` | 🟢 _1.00_ | *Exact match found.* |
| `impression_tracking_url` | Display monitoring URL. | `ads.impression_tracking_url` | 🟢 _1.00_ | *Exact match found.* |
| `is_aco` | Whether the ad is an automated ad. | `ads.is_aco` | 🟢 _1.00_ | *Exact match found.* |
| `is_creative_authorized` | Whether you grant displaying some of your ads in our TikTok For Business Creative Center. Only valid for non-US advertisers, the default value is false.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `is_new_structure` | Whether the campaign is a new structure. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `landing_page_url` | Landing page URL. | `ads.landing_page_url` | 🟢 _1.00_ | *Exact match found.* |
| `open_url` | The specific location where you want your audience to go if they have your app installed. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `opt_status` | Operation status. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `playable_url` | Playable material url. | `ads.playable_url` | 🟢 _1.00_ | *Exact match found.* |
| `profile_image` | Avatar URL. | `ads.profile_image_url` | 🟢 _1.00_ | *Exact match found.* |
| `status` | Ad status. | `ads.secondary_status` | 🟢 _1.00_ | *Exact match found.* |
| `video_id` | The video ID. | `ads.video_id` | 🟢 _1.00_ | *Exact match found.* |

### Mapping: Airbyte `campaigns_reports_hourly` to Fivetran `campaign_report_hourly`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _Since all fields have their expressions set to 'MISSING', indicating a complete lack of data mapping from the source to the target schema, the overall table matching confidence and completion are rated at zero. There has been no successful data mapping between the schemas, reflecting a complete absence of overlap or correspondence._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `campaigns_reports_hourly._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables from `_airbyte_extracted_at` to `_fivetran_synced`.* |
| `campaign_id` | Campaign id | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `stat_time_hour` | Hour of activity | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cost_per_conversion` | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_conversion` | Number of times your ad resulted in the optimization event you selected. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cpc` | The average amount of money you've spent on a click. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_play_actions` | The number of times your video starts to play. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `conversion_rate` | The percentage of results you received out of all the clicks of your ads.   (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_views_p_75` | The number of times your video was played at 75% of its length. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `result` | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_views_p_50` | The number of times your video was played at 50% of its length. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `impressions` | The number of times your ads were on screen. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `comments` | The number of comments your video creative received within 1 day of a user seeing a paid ad. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_cost_per_result` | As a campaign may have different optimization goals, the total number of result  is not supported in campaign section now, please go to the ad group section to view the cost  per Result. (The total count is based on when the conversion actually happened.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `conversion` | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_result` | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_view_p_100` | The number of times your video was played at 100% of its length. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shares` | The number of shares your video creative received within 1 day of a user seeing a paid ad. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cost_per_secondary_goal_result` | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `secondary_goal_result_rate` | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `clicks` | The number of clicks on your ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cost_per_1000_reached` | The average cost to reach 1,000 unique users. This metric is estimated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_views_p_25` | The number of times your video was played at 25% of its length. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `reach` | The number of unique users who saw your ads at least once. This metric is estimated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_cost_per_conversion` | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `profile_visits_rate` | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `average_video_play` | The average time your video was played per single video view, including any time spent replaying the video. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `profile_visits` | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cpm` | The average amount of money you've spent per 1,000 impressions. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `ctr` | The percentage of times people saw your ad and performed a click. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_watched_2_s` | The number of times your video played for at least 2 seconds. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `follows` | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `result_rate` | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_watched_6_s` | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `secondary_goal_result` | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cost_per_result` | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `average_video_play_per_user` | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_result_rate` | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to  view the Result Rate. (The total count is based on when the conversion actually happened.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `spend` | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `likes` | The number of likes your video creative received within 1 day of a user seeing a paid ad. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_purchase_value` | The total value of purchase events that occurred in your app that were recorded by your measurement partner. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_sales_lead_value` | The monetary worth or potential value assigned to a lead generated through ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `ads_reports_hourly` to Fivetran `ad_report_hourly`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _All mappings were set to MISSING due to a lack of information for confident matches._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `ads_reports_hourly._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables.* |
| `ad_id` | Ad id | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `stat_time_hour` | Hour of activity | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cost_per_conversion` | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_conversion` | Number of times your ad resulted in the optimization event you selected. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cpc` | The average amount of money you've spent on a click. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_play_actions` | The number of times your video starts to play. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `conversion_rate` | The percentage of results you received out of all the clicks of your ads.   (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_views_p_75` | The number of times your video was played at 75% of its length. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `result` | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_views_p_50` | The number of times your video was played at 50% of its length. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `impressions` | The number of times your ads were on screen. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `comments` | The number of comments your video creative received within 1 day of a user seeing a paid ad. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_cost_per_result` | As a campaign may have different optimization goals, the total number of result   is not supported in campaign section now, please go to the ad group section to view the cost per Result. (The total count is based on when the conversion actually happened.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `conversion` | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns.  Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_result` | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_view_p_100` | The number of times your video was played at 100% of its length. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shares` | The number of shares your video creative received within 1 day of a user seeing a paid ad. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cost_per_secondary_goal_result` | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `secondary_goal_result_rate` | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `clicks` | The number of clicks on your ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cost_per_1000_reached` | The average cost to reach 1,000 unique users. This metric is estimated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_views_p_25` | The number of times your video was played at 25% of its length. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `reach` | The number of unique users who saw your ads at least once. This metric is estimated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_cost_per_conversion` | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `profile_visits_rate` | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `average_video_play` | The average time your video was played per single video view, including any time spent replaying the video. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `profile_visits` | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cpm` | The average amount of money you've spent per 1,000 impressions. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `ctr` | The percentage of times people saw your ad and performed a click. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_watched_2_s` | The number of times your video played for at least 2 seconds. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `follows` | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `result_rate` | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_watched_6_s` | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `secondary_goal_result` | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cost_per_result` | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `average_video_play_per_user` | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `real_time_result_rate` | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to view the Result Rate. (The total count is based on when the conversion actually happened.) | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `spend` | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `likes` | The number of likes your video creative received within 1 day of a user seeing a paid ad. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_purchase_value` | The total value of purchase events that occurred in your app that were recorded by your measurement partner. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_sales_lead_value` | The monetary worth or potential value assigned to a lead generated through ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |
