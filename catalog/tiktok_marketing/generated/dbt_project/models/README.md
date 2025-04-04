# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

## adgroup_report_hourly




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ad_groups_reports_hourly | tiktok_marketing | ad_groups_reports_hourly |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| adgroup_id | ad_groups_reports_hourly.adgroup_id | Ad group id |
| stat_time_hour | ad_groups_reports_hourly.stat_time_hour | Hour of activity |
| cost_per_conversion | ad_groups_reports_hourly.metrics.cost_per_conversion | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)
 |
| real_time_conversion | ad_groups_reports_hourly.metrics.real_time_conversion | Number of times your ad resulted in the optimization event you selected. |
| cpc | ad_groups_reports_hourly.metrics.cpc | The average amount of money you've spent on a click. |
| video_play_actions | ad_groups_reports_hourly.metrics.video_play_actions | The number of times your video starts to play. Replays will not be counted. |
| conversion_rate | ad_groups_reports_hourly.metrics.conversion_rate | The percentage of results you received out of all the clicks of your ads. (The total count is calculated based on the time each ad impression occurred.) |
| video_views_p_75 | ad_groups_reports_hourly.metrics.video_views_p75 | The number of times your video was played at 75% of its length. Replays will not be counted. |
| result | ad_groups_reports_hourly.metrics.result | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)
 |
| video_views_p_50 | ad_groups_reports_hourly.metrics.video_views_p50 | The number of times your video was played at 50% of its length. Replays will not be counted. |
| impressions | ad_groups_reports_hourly.metrics.impressions | The number of times your ads were on screen. |
| comments | ad_groups_reports_hourly.metrics.comments | The number of comments your video creative received within 1 day of a user seeing a paid ad. |
| real_time_cost_per_result | ad_groups_reports_hourly.metrics.real_time_cost_per_result | As a campaign may have different optimization goals, the total number of result  is not supported in campaign section now, please go to the ad group section to view the cost  per Result. (The total count is based on when the conversion actually happened.)
 |
| conversion | ad_groups_reports_hourly.metrics.conversion | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns.  Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)
 |
| real_time_result | ad_groups_reports_hourly.metrics.real_time_result | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)
 |
| video_view_p_100 | ad_groups_reports_hourly.metrics.video_views_p100 | The number of times your video was played at 100% of its length. Replays will not be counted. |
| shares | ad_groups_reports_hourly.metrics.shares | The number of shares your video creative received within 1 day of a user seeing a paid ad. |
| real_time_conversion_rate | ad_groups_reports_hourly.metrics.real_time_conversion_rate | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) |
| cost_per_secondary_goal_result | ad_groups_reports_hourly.metrics.cost_per_secondary_goal_result | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)
 |
| secondary_goal_result_rate | ad_groups_reports_hourly.metrics.secondary_goal_result_rate | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.
 |
| clicks | ad_groups_reports_hourly.metrics.clicks | The number of clicks on your ads. |
| cost_per_1000_reached | ad_groups_reports_hourly.metrics.cost_per_1000_reached | The average cost to reach 1,000 unique users. This metric is estimated. |
| video_views_p_25 | ad_groups_reports_hourly.metrics.video_views_p25 | The number of times your video was played at 25% of its length. Replays will not be counted. |
| reach | ad_groups_reports_hourly.metrics.reach | The number of unique users who saw your ads at least once. This metric is estimated. |
| real_time_cost_per_conversion | ad_groups_reports_hourly.metrics.real_time_cost_per_conversion | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) |
| profile_visits_rate | ad_groups_reports_hourly.metrics.profile_visits_rate | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. |
| average_video_play | ad_groups_reports_hourly.metrics.average_video_play | The average time your video was played per single video view, including any time spent replaying the video. |
| profile_visits | ad_groups_reports_hourly.metrics.profile_visits | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. |
| cpm | ad_groups_reports_hourly.metrics.cpm | The average amount of money you've spent per 1,000 impressions. |
| ctr | ad_groups_reports_hourly.metrics.ctr | The percentage of times people saw your ad and performed a click. |
| video_watched_2_s | ad_groups_reports_hourly.metrics.video_watched_2s | The number of times your video played for at least 2 seconds. Replays will not be counted. |
| follows | ad_groups_reports_hourly.metrics.follows | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. |
| result_rate | ad_groups_reports_hourly.metrics.result_rate | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)
 |
| video_watched_6_s | ad_groups_reports_hourly.metrics.video_watched_6s | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. |
| secondary_goal_result | ad_groups_reports_hourly.metrics.secondary_goal_result | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)
 |
| cost_per_result | ad_groups_reports_hourly.metrics.cost_per_result | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)
 |
| average_video_play_per_user | ad_groups_reports_hourly.metrics.average_video_play_per_user | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. |
| real_time_result_rate | ad_groups_reports_hourly.metrics.real_time_result_rate | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to view the Result Rate.  (The total count is based on when the conversion actually happened.)
 |
| spend | ad_groups_reports_hourly.metrics.spend | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. |
| likes | ad_groups_reports_hourly.metrics.likes | The number of likes your video creative received within 1 day of a user seeing a paid ad. |
| _fivetran_synced | ad_groups_reports_hourly._airbyte_extracted_at | Timestamp of when Fivetran synced a record. |
| total_purchase_value | ad_groups_reports_hourly.metrics.total_purchase_value | The total value of purchase events that occurred in your app that were recorded by your measurement partner. |
| total_sales_lead_value | MISSING | The monetary worth or potential value assigned to a lead generated through ads. |



## campaign_history




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| campaigns | tiktok_marketing | campaigns |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| campaign_id | campaigns.campaign_id | Campaign ID |
| updated_at | campaigns._airbyte_extracted_at | Time the record was updated. |
| advertiser_id | campaigns.advertiser_id | Advertiser ID |
| budget | campaigns.budget | Campaign budget |
| budget_mode | campaigns.budget_mode | Budget type |
| campaign_name | campaigns.campaign_name | Campaign name |
| campaign_type | campaigns.campaign_type | Campaign Type, indicates the campaign is a regular campaign or iOS 14 campaign. |
| create_time | campaigns.create_time | Time at which the campaign was created. |
| is_new_structure | campaigns.is_new_structure | Whether the campaign is a new structure (for the same campaign, the structure of campaign, adgroups and ads are the same) |
| objective_type | campaigns.objective_type | Advertising objective. |
| opt_status | MISSING | Operation status. |
| status | MISSING | Campaign status |
| split_test_variable | campaigns.split_test_variable | Split Test variables. Optional values; TARGETING, BIDDING_OPTIMIZATION , CREATIVE. |



## adgroup_history




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ad_groups | tiktok_marketing | ad_groups |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| adgroup_id | ad_groups.adgroup_id | Ad group ID |
| updated_at | ad_groups.modify_time | Time the record was updated. |
| advertiser_id | ad_groups.advertiser_id | Advertiser ID |
| campaign_id | ad_groups.campaign_id | The Ad group's campaign ID. |
| action_categories | MISSING | IDs of the action categories (behaviors) that you want to target. |
| action_days | MISSING | The number of days of the time period to include action from. |
| adgroup_name | ad_groups.adgroup_name | Ad group name. Character limit is 512 and cannot contain emoji. |
| age_groups | MISSING | Age groups you want to target. This is the newest version of the field `age`, which was renamed after the Tiktok Ads v1.3 API release.
 |
| android_osv | ad_groups.min_android_version | Minimum Android version. |
| app_download_url | ad_groups.app_download_url | App download link |
| app_id | ad_groups.app_id | The Application id of the promoted app |
| app_name | MISSING | App name. |
| app_type | ad_groups.app_type | App type. |
| audience | MISSING | A list of audience IDs. |
| audience_type | ad_groups.audience_type | Audience Type |
| bid | MISSING | CPC, CPM bidding, oCPM learning bidding |
| bid_type | MISSING | Bidding Strategy |
| billing_event | ad_groups.billing_event | Bid method. |
| budget | ad_groups.budget | Ad budget. Returns 0.0 when Campaign Budget Optimization (budget_optimize_switch) is on. |
| budget_mode | ad_groups.budget_mode | Budget mode. This field will be ignored when Campaign Budget Optimization (budget_optimize_switch) is enabled. |
| carriers | ad_groups.carriers | Carriers that you want to target. |
| category | ad_groups.category_id | Ad group category. |
| click_tracking_url | MISSING | Click monitoring URL. |
| connection_type | MISSING | Device connection types that you want to target. Default; unlimited. |
| conversion_bid | MISSING | oCPM conversion bid |
| cpv_video_duration | MISSING | Video playback duration, required if optimize_goal is VIDEO_VIEW.  Allowed values; SIX_SECONDS (video playback 6s), TWO_SECONDS (video playback 2s)
 |
| creative_material_mode | ad_groups.creative_material_mode | Creative delivery mode. |
| dayparting | MISSING | Ad delivery period, the default is always and the format is 48 * 7 character string, represented by 0 or 1. > That is, with half an hour as the minimum granularity, a day (24 hours) is divided by the minimum granularity(30 mins) from Monday to Sunday. Resulting in a 48*7 format.0 represents not to be delivered, 1 represents delivery. no transmission, full transmission 0, full transmission 1 all represent full time delivery |
| deep_bid_type | MISSING | Bidding strategy for in-app events. |
| deep_cpabid | MISSING | Deep bid |
| deep_external_action | MISSING | Deep conversion event. |
| display_name | MISSING | Display name of ad group. |
| enable_inventory_filter | ad_groups.inventory_filter_enabled | Inventory filtering (Unsafe videos will not be displayed). |
| excluded_audience | MISSING | A list of audience ID to be excluded. |
| external_action | MISSING | Conversion event for the ad group. It is required when the promoted object is an app with tracking urls, or when pixel_id is specified. |
| fallback_type | MISSING | Fallback Type. If the audience do not have the app installed, you can have them fall back to install the app, or to view a specific web page. Not applicable for Deferred Deeplink. Allowed values; APP_INSTALL, WEBSITE, UNSET. If website is chosen, you need to specify the url via landing_page_url field.
 |
| frequency | ad_groups.frequency | frequency, together with frequency_schedule, controls how often people see your ad (only available for REACH ads).  For example, frequency = 2 frequency_schedule = 3 means "show ads no more than twice every 3 day".
 |
| frequency_schedule | ad_groups.frequency_schedule | frequency, together with frequency, controls how often people see your ad (only available for REACH ads). |
| gender | ad_groups.gender | Gender that you want to target. |
| impression_tracking_url | MISSING | Display monitoring URL. |
| interest_category_v2 | ad_groups.interest_category_ids | Interest classification. If the interest is specified, users that do not meet interest target will be excluded during delivery. |
| ios_osv | ad_groups.min_ios_version | Minimum iOS version. |
| is_comment_disable | ad_groups.comment_disabled | Whether to allow comments on your ads on TikTok, Vigo, Helo. |
| is_hfss | ad_groups.is_hfss | Whether the promoted content is HFSS foods (foods that are high in fat, salt, or sugar). |
| is_new_structure | ad_groups.is_new_structure | Whether the campaign is a new structure. |
| keywords | ad_groups.keywords | Keywords used. |
| landing_page_url | MISSING | Landing page URL. |
| languages | ad_groups.languages | Codes of the languages that you want to target. |
| location | ad_groups.location_ids | IDs of the locations that you want to target. |
| open_url | ad_groups.promotion_website_type | The specific location where you want your audience to go if they have your app installed. |
| open_url_type | MISSING | The open URL type. |
| operation_system | ad_groups.operating_systems | Device operating systems that you want to target. |
| opt_status | ad_groups.operation_status | Operation status. |
| optimize_goal | ad_groups.optimization_goal | Optimization goal. |
| pacing | ad_groups.pacing | You can choose between PACING_MODE_SMOOTH and PACING_MODE_FAST. For PACING_MODE_SMOOTH, the budget is allocated evenly within the scheduled time.  PACING_MODE_FAST would consume budget and produce results as soon as possible. 
 |
| package | MISSING | Package name. |
| pangle_block_app_list_id | MISSING | Pangle app block list ID. |
| pixel_id | ad_groups.pixel_id | Pixel ID. Only application for landing pages. |
| placement | MISSING | The apps where you want to deliver your ads. |
| placement_type | ad_groups.placement_type | Placement type. |
| profile_image | MISSING | Avatar URL. |
| schedule_end_time | ad_groups.schedule_end_time | Ad delivery end time (UTC+0). Format should be YYYY-MM-DD HH:MM:SS |
| schedule_start_time | ad_groups.schedule_start_time | Ad delivery start time (UTC+0). Format should be YYYY-MM-DD HH:MM:SS |
| schedule_type | ad_groups.schedule_type | The schedule type, which can be either SCHEDULE_START_END or SCHEDULE_FROM_NOW. |
| skip_learning_phase | MISSING | Whether to skip the learning stage. |
| statistic_type | MISSING | conversion bid statistic type |
| status | MISSING | Ad group status |
| video_actions | ad_groups.video_actions | Number of video actions. |
| video_download | ad_groups.video_download_disabled | Whether users can download your video ads on TikTok(cannot be updated once created). |



## advertiser




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| advertisers | tiktok_marketing | advertisers |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| id | advertisers.advertiser_id | Advertiser ID |
| address | advertisers.address | Advertiser address information |
| balance | advertisers.balance | Account available balance |
| cellphone_number | advertisers.cellphone_number | Contact mobile number, desensitised data. This is the newest version of the field `phone_number`, which was renamed after the Tiktok Ads v1.3 API release.
 |
| company | advertisers.company | Advertiser's company name |
| contacter | advertisers.contacter | Contact Person |
| country | advertisers.country | The advertiser's country |
| create_time | advertisers.create_time | Advertiser's create time |
| currency | advertisers.currency | Type of currency used by advertisers |
| description | advertisers.description | Brand description, i.e. promotional content |
| email | advertisers.email | Advertiser contact email, desensitised data |
| industry | advertisers.industry | Advertiser industry category |
| language | advertisers.language | Language used by advertisers |
| license_no | advertisers.license_no | License number |
| license_url | advertisers.license_url | License preview address, the link is valid for an hour by default. |
| name | advertisers.name | Advertiser name |
| phone_number | MISSING | Contact mobile number, desensitised data. IMPORTANT: This field will not be populated for connectors utilizing the Tiktok Ads v1.3 API version, as the column was renamed.  The new column name is `cellphone_number`.
 |
| promotion_area | advertisers.promotion_area | Operation area |
| reason | advertisers.rejection_reason | Reason for rejection |
| role | advertisers.role | Advertiser role |
| status | advertisers.status | Advertiser status |
| telephone | MISSING | Fixed phone number, desensitised data IMPORTANT: This field will not be populated for connectors utilizing the Tiktok Ads v1.3 API version, as the column was renamed.  The new column name is `telephone_number`.
 |
| telephone_number | advertisers.telephone_number | Fixed phone number, desensitised data This is the newest version of the field `telephone`, which was renamed after the Tiktok Ads v1.3 API release.
 |
| timezone | advertisers.timezone | Ad account time zone including GMT offset |
| _fivetran_synced | advertisers._airbyte_extracted_at | Timestamp of when Fivetran synced a record. |



## campaign_report_hourly




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| campaigns_reports_hourly | tiktok_marketing | campaigns_reports_hourly |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| campaign_id | campaigns_reports_hourly.campaign_id | Campaign id |
| stat_time_hour | campaigns_reports_hourly.stat_time_hour | Hour of activity |
| cost_per_conversion | campaigns_reports_hourly.metrics.cost_per_conversion | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)
 |
| real_time_conversion | campaigns_reports_hourly.metrics.real_time_conversion | Number of times your ad resulted in the optimization event you selected. |
| cpc | campaigns_reports_hourly.metrics.cpc | The average amount of money you've spent on a click. |
| video_play_actions | campaigns_reports_hourly.metrics.video_play_actions | The number of times your video starts to play. Replays will not be counted. |
| conversion_rate | campaigns_reports_hourly.metrics.conversion_rate | The percentage of results you received out of all the clicks of your ads.   (The total count is calculated based on the time each ad impression occurred.)
 |
| video_views_p_75 | campaigns_reports_hourly.metrics.video_views_p75 | The number of times your video was played at 75% of its length. Replays will not be counted. |
| result | campaigns_reports_hourly.metrics.result | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)
 |
| video_views_p_50 | campaigns_reports_hourly.metrics.video_views_p50 | The number of times your video was played at 50% of its length. Replays will not be counted. |
| impressions | campaigns_reports_hourly.metrics.impressions | The number of times your ads were on screen. |
| comments | campaigns_reports_hourly.metrics.comments | The number of comments your video creative received within 1 day of a user seeing a paid ad. |
| real_time_cost_per_result | campaigns_reports_hourly.metrics.real_time_cost_per_result | As a campaign may have different optimization goals, the total number of result  is not supported in campaign section now, please go to the ad group section to view the cost  per Result. (The total count is based on when the conversion actually happened.)
 |
| conversion | campaigns_reports_hourly.metrics.conversion | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)
 |
| real_time_result | campaigns_reports_hourly.metrics.real_time_result | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)
 |
| video_view_p_100 | campaigns_reports_hourly.metrics.video_views_p100 | The number of times your video was played at 100% of its length. Replays will not be counted. |
| shares | campaigns_reports_hourly.metrics.shares | The number of shares your video creative received within 1 day of a user seeing a paid ad. |
| real_time_conversion_rate | campaigns_reports_hourly.metrics.real_time_conversion_rate | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) |
| cost_per_secondary_goal_result | campaigns_reports_hourly.metrics.cost_per_secondary_goal_result | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)
 |
| secondary_goal_result_rate | campaigns_reports_hourly.metrics.secondary_goal_result_rate | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.
 |
| clicks | campaigns_reports_hourly.metrics.clicks | The number of clicks on your ads. |
| cost_per_1000_reached | campaigns_reports_hourly.metrics.cost_per_1000_reached | The average cost to reach 1,000 unique users. This metric is estimated. |
| video_views_p_25 | campaigns_reports_hourly.metrics.video_views_p25 | The number of times your video was played at 25% of its length. Replays will not be counted. |
| reach | campaigns_reports_hourly.metrics.reach | The number of unique users who saw your ads at least once. This metric is estimated. |
| real_time_cost_per_conversion | campaigns_reports_hourly.metrics.real_time_cost_per_conversion | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) |
| profile_visits_rate | MISSING | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. |
| average_video_play | campaigns_reports_hourly.metrics.average_video_play | The average time your video was played per single video view, including any time spent replaying the video. |
| profile_visits | campaigns_reports_hourly.metrics.profile_visits | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. |
| cpm | campaigns_reports_hourly.metrics.cpm | The average amount of money you've spent per 1,000 impressions. |
| ctr | campaigns_reports_hourly.metrics.ctr | The percentage of times people saw your ad and performed a click. |
| video_watched_2_s | campaigns_reports_hourly.metrics.video_watched_2s | The number of times your video played for at least 2 seconds. Replays will not be counted. |
| follows | campaigns_reports_hourly.metrics.follows | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. |
| result_rate | campaigns_reports_hourly.metrics.result_rate | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)
 |
| video_watched_6_s | campaigns_reports_hourly.metrics.video_watched_6s | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. |
| secondary_goal_result | campaigns_reports_hourly.metrics.secondary_goal_result | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)
 |
| cost_per_result | campaigns_reports_hourly.metrics.cost_per_result | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)
 |
| average_video_play_per_user | campaigns_reports_hourly.metrics.average_video_play_per_user | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. |
| real_time_result_rate | campaigns_reports_hourly.metrics.real_time_result_rate | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to  view the Result Rate. (The total count is based on when the conversion actually happened.)
 |
| spend | campaigns_reports_hourly.metrics.spend | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. |
| likes | campaigns_reports_hourly.metrics.likes | The number of likes your video creative received within 1 day of a user seeing a paid ad. |
| _fivetran_synced | campaigns_reports_hourly._airbyte_extracted_at | Timestamp of when Fivetran synced a record. |
| total_purchase_value | campaigns_reports_hourly.metrics.total_purchase_value | The total value of purchase events that occurred in your app that were recorded by your measurement partner. |
| total_sales_lead_value | MISSING | The monetary worth or potential value assigned to a lead generated through ads. |



## ad_history




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ads | tiktok_marketing | ads |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| ad_id | ads.ad_id | Ad ID |
| updated_at | ads._airbyte_extracted_at | Time the record was updated. |
| adgroup_id | ads.adgroup_id | Ad group ID |
| advertiser_id | ads.advertiser_id | Advertiser ID |
| campaign_id | ads.campaign_id | Campaign ID |
| ad_name | ads.ad_name | Ad Name. |
| ad_text | ads.ad_text | The ad text. |
| app_name | ads.app_name | The display name of app download ad. |
| call_to_action | ads.call_to_action | Call to action values. |
| click_tracking_url | ads.click_tracking_url | Click monitoring URL. |
| create_time | ads.create_time | Time at which the ad was created. |
| display_name | ads.display_name | The display name of landing page or pure exposure ad. |
| image_ids | ads.image_ids | A list of image IDs. |
| impression_tracking_url | ads.impression_tracking_url | Display monitoring URL. |
| is_aco | ads.is_aco | Whether the ad is an automated ad. |
| is_creative_authorized | ads.creative_authorized | Whether you grant displaying some of your ads in our TikTok For Business Creative Center. Only valid for non-US advertisers, the default value is false.
 |
| is_new_structure | ads.is_new_structure | Whether the campaign is a new structure. |
| landing_page_url | ads.landing_page_url | Landing page URL. |
| open_url | ads.deeplink | The specific location where you want your audience to go if they have your app installed. |
| opt_status | ads.operation_status | Operation status. |
| playable_url | ads.playable_url | Playable material url. |
| profile_image | ads.profile_image_url | Avatar URL. |
| status | ads.secondary_status | Ad status. |
| video_id | ads.video_id | The video ID. |



## ad_report_hourly




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| ads_reports_hourly | tiktok_marketing | ads_reports_hourly |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| ad_id | ads_reports_hourly.ad_id | Ad id |
| stat_time_hour | ads_reports_hourly.stat_time_hour | Hour of activity |
| cost_per_conversion | ads_reports_hourly.metrics.cost_per_conversion | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)
 |
| real_time_conversion | ads_reports_hourly.metrics.real_time_conversion | Number of times your ad resulted in the optimization event you selected. |
| cpc | ads_reports_hourly.metrics.cpc | The average amount of money you've spent on a click. |
| video_play_actions | ads_reports_hourly.metrics.video_play_actions | The number of times your video starts to play. Replays will not be counted. |
| conversion_rate | ads_reports_hourly.metrics.conversion_rate | The percentage of results you received out of all the clicks of your ads.   (The total count is calculated based on the time each ad impression occurred.)
 |
| video_views_p_75 | ads_reports_hourly.metrics.video_views_p75 | The number of times your video was played at 75% of its length. Replays will not be counted. |
| result | ads_reports_hourly.metrics.result | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)
 |
| video_views_p_50 | ads_reports_hourly.metrics.video_views_p50 | The number of times your video was played at 50% of its length. Replays will not be counted. |
| impressions | ads_reports_hourly.metrics.impressions | The number of times your ads were on screen. |
| comments | ads_reports_hourly.metrics.comments | The number of comments your video creative received within 1 day of a user seeing a paid ad. |
| real_time_cost_per_result | ads_reports_hourly.metrics.real_time_cost_per_result | As a campaign may have different optimization goals, the total number of result   is not supported in campaign section now, please go to the ad group section to view the cost per Result. (The total count is based on when the conversion actually happened.)
 |
| conversion | ads_reports_hourly.metrics.conversion | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns.  Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)
 |
| real_time_result | ads_reports_hourly.metrics.real_time_result | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)
 |
| video_view_p_100 | ads_reports_hourly.metrics.video_views_p100 | The number of times your video was played at 100% of its length. Replays will not be counted. |
| shares | ads_reports_hourly.metrics.shares | The number of shares your video creative received within 1 day of a user seeing a paid ad. |
| real_time_conversion_rate | ads_reports_hourly.metrics.real_time_conversion_rate | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) |
| cost_per_secondary_goal_result | ads_reports_hourly.metrics.cost_per_secondary_goal_result | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)
 |
| secondary_goal_result_rate | ads_reports_hourly.metrics.secondary_goal_result_rate | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.
 |
| clicks | ads_reports_hourly.metrics.clicks | The number of clicks on your ads. |
| cost_per_1000_reached | ads_reports_hourly.metrics.cost_per_1000_reached | The average cost to reach 1,000 unique users. This metric is estimated. |
| video_views_p_25 | ads_reports_hourly.metrics.video_views_p25 | The number of times your video was played at 25% of its length. Replays will not be counted. |
| reach | ads_reports_hourly.metrics.reach | The number of unique users who saw your ads at least once. This metric is estimated. |
| real_time_cost_per_conversion | ads_reports_hourly.metrics.real_time_cost_per_conversion | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) |
| profile_visits_rate | ads_reports_hourly.metrics.profile_visits_rate | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. |
| average_video_play | ads_reports_hourly.metrics.average_video_play | The average time your video was played per single video view, including any time spent replaying the video. |
| profile_visits | ads_reports_hourly.metrics.profile_visits | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. |
| cpm | MISSING | The average amount of money you've spent per 1,000 impressions. |
| ctr | ads_reports_hourly.metrics.ctr | The percentage of times people saw your ad and performed a click. |
| video_watched_2_s | ads_reports_hourly.metrics.video_watched_2s | The number of times your video played for at least 2 seconds. Replays will not be counted. |
| follows | ads_reports_hourly.metrics.follows | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. |
| result_rate | ads_reports_hourly.metrics.result_rate | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)
 |
| video_watched_6_s | ads_reports_hourly.metrics.video_watched_6s | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. |
| secondary_goal_result | ads_reports_hourly.metrics.secondary_goal_result | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)
 |
| cost_per_result | ads_reports_hourly.metrics.cost_per_result | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)
 |
| average_video_play_per_user | ads_reports_hourly.metrics.average_video_play_per_user | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. |
| real_time_result_rate | ads_reports_hourly.metrics.real_time_result_rate | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to view the Result Rate. (The total count is based on when the conversion actually happened.) |
| spend | ads_reports_hourly.metrics.spend | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. |
| likes | ads_reports_hourly.metrics.likes | The number of likes your video creative received within 1 day of a user seeing a paid ad. |
| _fivetran_synced | ads_reports_hourly._airbyte_extracted_at | Timestamp of when Fivetran synced a record. |
| total_purchase_value | ads_reports_hourly.metrics.total_purchase_value | The total value of purchase events that occurred in your app that were recorded by your measurement partner. |
| total_sales_lead_value | MISSING | The monetary worth or potential value assigned to a lead generated through ads. |


