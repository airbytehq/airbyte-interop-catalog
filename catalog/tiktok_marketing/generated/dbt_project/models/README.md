# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping: Airbyte `ad_groups_reports_hourly` to Fivetran `adgroup_report_hourly`


- Table Match Confidence Score: 🟢 _1.00__
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _Successfully mapped all fields with a high confidence score, indicating perfect mapping between the source and target schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `adgroup_id` | Ad group id | `ad_groups_reports_hourly.adgroup_id` | 🟢 _1.00_ | _Exact match found for 'adgroup_id'._ |
| `stat_time_hour` | Hour of activity | `ad_groups_reports_hourly.stat_time_hour` | 🟢 _1.00_ | _Exact match found for 'stat_time_hour'._ |
| `cost_per_conversion` | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.cost_per_conversion` | 🟢 _1.00_ | _Exact match found for 'cost_per_conversion'._ |
| `real_time_conversion` | Number of times your ad resulted in the optimization event you selected. | `ad_groups_reports_hourly.metrics.real_time_conversion` | 🟢 _1.00_ | _Exact match found for 'real_time_conversion'._ |
| `cpc` | The average amount of money you've spent on a click. | `ad_groups_reports_hourly.metrics.cpc` | 🟢 _1.00_ | _Exact match found for 'cpc'._ |
| `video_play_actions` | The number of times your video starts to play. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_play_actions` | 🟢 _1.00_ | _Exact match found for 'video_play_actions'._ |
| `conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is calculated based on the time each ad impression occurred.) | `ad_groups_reports_hourly.metrics.conversion_rate` | 🟢 _1.00_ | _Exact match found for 'conversion_rate'._ |
| `video_views_p_75` | The number of times your video was played at 75% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p75` | 🟢 _1.00_ | _Exact match found for 'video_views_p_75'._ |
| `result` | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.result` | 🟢 _1.00_ | _Exact match found for 'result'._ |
| `video_views_p_50` | The number of times your video was played at 50% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p50` | 🟢 _1.00_ | _Exact match found for 'video_views_p_50'._ |
| `impressions` | The number of times your ads were on screen. | `ad_groups_reports_hourly.metrics.impressions` | 🟢 _1.00_ | _Exact match found for 'impressions'._ |
| `comments` | The number of comments your video creative received within 1 day of a user seeing a paid ad. | `ad_groups_reports_hourly.metrics.comments` | 🟢 _1.00_ | _Exact match found for 'comments'._ |
| `real_time_cost_per_result` | As a campaign may have different optimization goals, the total number of result  is not supported in campaign section now, please go to the ad group section to view the cost  per Result. (The total count is based on when the conversion actually happened.)  | `ad_groups_reports_hourly.metrics.real_time_cost_per_result` | 🟢 _1.00_ | _Exact match found for 'real_time_cost_per_result'._ |
| `conversion` | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns.  Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.conversion` | 🟢 _1.00_ | _Exact match found for 'conversion'._ |
| `real_time_result` | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)  | `ad_groups_reports_hourly.metrics.real_time_result` | 🟢 _1.00_ | _Exact match found for 'real_time_result'._ |
| `video_view_p_100` | The number of times your video was played at 100% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p100` | 🟢 _1.00_ | _Exact match found for 'video_view_p_100'._ |
| `shares` | The number of shares your video creative received within 1 day of a user seeing a paid ad. | `ad_groups_reports_hourly.metrics.shares` | 🟢 _1.00_ | _Exact match found for 'shares'._ |
| `real_time_conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) | `ad_groups_reports_hourly.metrics.real_time_conversion_rate` | 🟢 _1.00_ | _Exact match found for 'real_time_conversion_rate'._ |
| `cost_per_secondary_goal_result` | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.cost_per_secondary_goal_result` | 🟢 _1.00_ | _Exact match found for 'cost_per_secondary_goal_result'._ |
| `secondary_goal_result_rate` | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.  | `ad_groups_reports_hourly.metrics.secondary_goal_result_rate` | 🟢 _1.00_ | _Exact match found for 'secondary_goal_result_rate'._ |
| `clicks` | The number of clicks on your ads. | `ad_groups_reports_hourly.metrics.clicks` | 🟢 _1.00_ | _Exact match found for 'clicks'._ |
| `cost_per_1000_reached` | The average cost to reach 1,000 unique users. This metric is estimated. | `ad_groups_reports_hourly.metrics.cost_per_1000_reached` | 🟢 _1.00_ | _Exact match found for 'cost_per_1000_reached'._ |
| `video_views_p_25` | The number of times your video was played at 25% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p25` | 🟢 _1.00_ | _Exact match found for 'video_views_p_25'._ |
| `reach` | The number of unique users who saw your ads at least once. This metric is estimated. | `ad_groups_reports_hourly.metrics.reach` | 🟢 _1.00_ | _Exact match found for 'reach'._ |
| `real_time_cost_per_conversion` | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) | `ad_groups_reports_hourly.metrics.real_time_cost_per_conversion` | 🟢 _1.00_ | _Exact match found for 'real_time_cost_per_conversion'._ |
| `profile_visits_rate` | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. | `ad_groups_reports_hourly.metrics.profile_visits_rate` | 🟢 _1.00_ | _Exact match found for 'profile_visits_rate'._ |
| `average_video_play` | The average time your video was played per single video view, including any time spent replaying the video. | `ad_groups_reports_hourly.metrics.average_video_play` | 🟢 _1.00_ | _Exact match found for 'average_video_play'._ |
| `profile_visits` | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. | `ad_groups_reports_hourly.metrics.profile_visits` | 🟢 _1.00_ | _Exact match found for 'profile_visits'._ |
| `cpm` | The average amount of money you've spent per 1,000 impressions. | `ad_groups_reports_hourly.metrics.cpm` | 🟢 _1.00_ | _Exact match found for 'cpm'._ |
| `ctr` | The percentage of times people saw your ad and performed a click. | `ad_groups_reports_hourly.metrics.ctr` | 🟢 _1.00_ | _Exact match found for 'ctr'._ |
| `video_watched_2_s` | The number of times your video played for at least 2 seconds. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_watched_2s` | 🟢 _1.00_ | _Exact match found for 'video_watched_2_s'._ |
| `follows` | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. | `ad_groups_reports_hourly.metrics.follows` | 🟢 _1.00_ | _Exact match found for 'follows'._ |
| `result_rate` | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.result_rate` | 🟢 _1.00_ | _Exact match found for 'result_rate'._ |
| `video_watched_6_s` | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_watched_6s` | 🟢 _1.00_ | _Exact match found for 'video_watched_6_s'._ |
| `secondary_goal_result` | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.secondary_goal_result` | 🟢 _1.00_ | _Exact match found for 'secondary_goal_result'._ |
| `cost_per_result` | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.cost_per_result` | 🟢 _1.00_ | _Exact match found for 'cost_per_result'._ |
| `average_video_play_per_user` | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. | `ad_groups_reports_hourly.metrics.average_video_play_per_user` | 🟢 _1.00_ | _Exact match found for 'average_video_play_per_user'._ |
| `real_time_result_rate` | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to view the Result Rate.  (The total count is based on when the conversion actually happened.)  | `ad_groups_reports_hourly.metrics.real_time_result_rate` | 🟢 _1.00_ | _Exact match found for 'real_time_result_rate'._ |
| `spend` | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. | `ad_groups_reports_hourly.metrics.spend` | 🟢 _1.00_ | _Exact match found for 'spend'._ |
| `likes` | The number of likes your video creative received within 1 day of a user seeing a paid ad. | `ad_groups_reports_hourly.metrics.likes` | 🟢 _1.00_ | _Exact match found for 'likes'._ |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `ad_groups_reports_hourly._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping for '_fivetran_synced' to '_airbyte_extracted_at'._ |
| `total_purchase_value` | The total value of purchase events that occurred in your app that were recorded by your measurement partner. | `ad_groups_reports_hourly.metrics.total_purchase_value` | 🟢 _1.00_ | _Exact match found for 'total_purchase_value'._ |
| `total_sales_lead_value` | The monetary worth or potential value assigned to a lead generated through ads. | `MISSING` | ❌ _0.00_ | _No good match found._ |

### Mapping: Airbyte `campaigns` to Fivetran `campaign_history`


- Table Match Confidence Score: 🟢 _0.85__
- Table Completion Score: 🟢 _0.77_
- Summary Self-Evaluation: _The source table 'campaigns' matches the target schema closely with most fields appropriately mapped, resulting in a high table match score. However, missing fields 'opt_status' and 'status' reflect in a slightly lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `campaign_id` | Campaign ID | `campaigns.campaign_id` | 🟢 _0.90_ | _The source field 'campaigns.campaign_id' is a strong match for 'campaign_id'._ |
| `updated_at` | Time the record was updated. | `campaigns._airbyte_extracted_at` | 🟢 _1.00_ | _The source field 'campaigns._airbyte_extracted_at' is a required standard mapping for '_fivetran_synced', thus always scores 1.00._ |
| `advertiser_id` | Advertiser ID | `campaigns.advertiser_id` | 🟢 _0.90_ | _The source field 'campaigns.advertiser_id' is a strong match for 'advertiser_id'._ |
| `budget` | Campaign budget | `campaigns.budget` | 🟢 _0.90_ | _The source field 'campaigns.budget' is a strong match for 'budget'._ |
| `budget_mode` | Budget type | `campaigns.budget_mode` | 🟢 _0.90_ | _The source field 'campaigns.budget_mode' is a strong match for 'budget_mode'._ |
| `campaign_name` | Campaign name | `campaigns.campaign_name` | 🟢 _0.90_ | _The source field 'campaigns.campaign_name' is a strong match for 'campaign_name'._ |
| `campaign_type` | Campaign Type, indicates the campaign is a regular campaign or iOS 14 campaign. | `campaigns.campaign_type` | 🟢 _0.90_ | _The source field 'campaigns.campaign_type' is a strong match for 'campaign_type'._ |
| `create_time` | Time at which the campaign was created. | `campaigns.create_time` | 🟢 _0.90_ | _The source field 'campaigns.create_time' is a strong match for 'create_time'._ |
| `is_new_structure` | Whether the campaign is a new structure (for the same campaign, the structure of campaign, adgroups and ads are the same) | `campaigns.is_new_structure` | 🟢 _0.90_ | _The source field 'campaigns.is_new_structure' is a strong match for 'is_new_structure'._ |
| `objective_type` | Advertising objective. | `campaigns.objective_type` | 🟢 _0.90_ | _The source field 'campaigns.objective_type' is a strong match for 'objective_type'._ |
| `opt_status` | Operation status. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `status` | Campaign status | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `split_test_variable` | Split Test variables. Optional values; TARGETING, BIDDING_OPTIMIZATION , CREATIVE. | `campaigns.split_test_variable` | 🟢 _0.70_ | _The source field 'campaigns.split_test_variable' is likely a match for 'split_test_variable' but with some uncertainty._ |

### Mapping: Airbyte `advertisers` to Fivetran `advertiser`


- Table Match Confidence Score: 🟢 _0.85__
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table has strong similarities in representing advertiser information across both source and target schemas. However, there is some discrepancy in field mapping completion due primarily to missing field expressions, though key fields like '_fivetran_synced' show complete and direct mapping._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Advertiser ID | `advertisers.advertiser_id` | 🟢 _0.95_ | _The field 'id' is mapped accurately to 'advertisers.advertiser_id'._ |
| `address` | Advertiser address information | `advertisers.address` | 🟢 _0.95_ | _The field 'address' corresponds well with 'advertisers.address'._ |
| `balance` | Account available balance | `advertisers.balance` | 🟢 _0.95_ | _The field 'balance' is correctly mapped to 'advertisers.balance'._ |
| `cellphone_number` | Contact mobile number, desensitised data. This is the newest version of the field `phone_number`, which was renamed after the Tiktok Ads v1.3 API release.  | `advertisers.cellphone_number` | 🟢 _0.95_ | _'cellphone_number' matches with 'advertisers.cellphone_number', reminiscent of a field update._ |
| `company` | Advertiser's company name | `advertisers.company` | 🟢 _0.95_ | _The field 'company' corresponds well with 'advertisers.company'._ |
| `contacter` | Contact Person | `advertisers.contacter` | 🟢 _0.95_ | _The field 'contacter' aligns well with 'advertisers.contacter'._ |
| `country` | The advertiser's country | `advertisers.country` | 🟢 _0.95_ | _The field 'country' is correctly mapped to 'advertisers.country'._ |
| `create_time` | Advertiser's create time | `advertisers.create_time` | 🟢 _0.95_ | _The field 'create_time' maps directly to 'advertisers.create_time'._ |
| `currency` | Type of currency used by advertisers | `advertisers.currency` | 🟢 _0.95_ | _The field 'currency' is mapped accurately to 'advertisers.currency'._ |
| `description` | Brand description, i.e. promotional content | `advertisers.description` | 🟢 _0.95_ | _The field 'description' is correctly mapped to 'advertisers.description'._ |
| `email` | Advertiser contact email, desensitised data | `advertisers.email` | 🟢 _0.95_ | _The field 'email' corresponds well with 'advertisers.email'._ |
| `industry` | Advertiser industry category | `advertisers.industry` | 🟢 _0.95_ | _The field 'industry' is correctly mapped to 'advertisers.industry'._ |
| `language` | Language used by advertisers | `advertisers.language` | 🟢 _0.95_ | _The field 'language' corresponds well with 'advertisers.language'._ |
| `license_no` | License number | `advertisers.license_no` | 🟢 _0.95_ | _The field 'license_no' maps directly to 'advertisers.license_no'._ |
| `license_url` | License preview address, the link is valid for an hour by default. | `advertisers.license_url` | 🟢 _0.95_ | _The field 'license_url' is mapped accurately to 'advertisers.license_url'._ |
| `name` | Advertiser name | `advertisers.name` | 🟢 _0.95_ | _The field 'name' matches correctly with 'advertisers.name'._ |
| `phone_number` | Contact mobile number, desensitised data. IMPORTANT: This field will not be populated for connectors utilizing the Tiktok Ads v1.3 API version, as the column was renamed.  The new column name is `cellphone_number`.  | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `promotion_area` | Operation area | `advertisers.promotion_area` | 🟢 _0.95_ | _The field 'promotion_area' corresponds well with 'advertisers.promotion_area'._ |
| `reason` | Reason for rejection | `advertisers.rejection_reason` | 🟢 _0.95_ | _The field 'reason' maps directly to 'advertisers.rejection_reason'._ |
| `role` | Advertiser role | `advertisers.role` | 🟢 _0.95_ | _The field 'role' is correctly mapped to 'advertisers.role'._ |
| `status` | Advertiser status | `advertisers.status` | 🟢 _0.95_ | _The field 'status' corresponds well with 'advertisers.status'._ |
| `telephone` | Fixed phone number, desensitised data IMPORTANT: This field will not be populated for connectors utilizing the Tiktok Ads v1.3 API version, as the column was renamed.  The new column name is `telephone_number`.  | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `telephone_number` | Fixed phone number, desensitised data This is the newest version of the field `telephone`, which was renamed after the Tiktok Ads v1.3 API release.  | `advertisers.telephone_number` | 🟢 _0.95_ | _The field 'telephone_number' matches correctly with 'advertisers.telephone_number'._ |
| `timezone` | Ad account time zone including GMT offset | `advertisers.timezone` | 🟢 _0.95_ | _The field 'timezone' is mapped accurately to 'advertisers.timezone'._ |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `advertisers._airbyte_extracted_at` | 🟢 _1.00_ | _The field '_fivetran_synced' is correctly mapped to 'advertisers._airbyte_extracted_at'._ |

### Mapping: Airbyte `campaigns_reports_hourly` to Fivetran `campaign_report_hourly`


- Table Match Confidence Score: 🟢 _0.95__
- Table Completion Score: 🟢 _0.97_
- Summary Self-Evaluation: _The table and field mappings are highly accurate. The mapping configuration includes a variety of field mappings that closely align with their expressions, with few MISSING mappings indicating minor gaps in completion. Generally, mappings such as '_fivetran_synced' to '_airbyte_extracted_at' are perfectly matched, resulting in a high table match score. Other fields are accurately associated with the correct expressions, suggesting they describe the same subject matter from a shared source. This results in a high completion score due to the absence of non-mappable fields, apart from minor misses like 'total_sales_lead_value' and 'profile_visits_rate'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `campaign_id` | Campaign id | `campaigns_reports_hourly.campaign_id` | 🟢 _1.00_ | _Exact match to field 'campaign_id' in source._ |
| `stat_time_hour` | Hour of activity | `campaigns_reports_hourly.stat_time_hour` | 🟢 _1.00_ | _Exact match to field 'stat_time_hour' in source._ |
| `cost_per_conversion` | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.cost_per_conversion` | 🟢 _1.00_ | _Exact match to field 'cost_per_conversion' in source._ |
| `real_time_conversion` | Number of times your ad resulted in the optimization event you selected. | `campaigns_reports_hourly.metrics.real_time_conversion` | 🟢 _1.00_ | _Exact match to field 'real_time_conversion' in source._ |
| `cpc` | The average amount of money you've spent on a click. | `campaigns_reports_hourly.metrics.cpc` | 🟢 _1.00_ | _Exact match to field 'cpc' in source._ |
| `video_play_actions` | The number of times your video starts to play. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_play_actions` | 🟢 _1.00_ | _Exact match to field 'video_play_actions' in source._ |
| `conversion_rate` | The percentage of results you received out of all the clicks of your ads.   (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.conversion_rate` | 🟢 _1.00_ | _Exact match to field 'conversion_rate' in source._ |
| `video_views_p_75` | The number of times your video was played at 75% of its length. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_views_p75` | 🟢 _1.00_ | _Exact match to field 'video_views_p_75' in source._ |
| `result` | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.result` | 🟢 _1.00_ | _Exact match to field 'result' in source._ |
| `video_views_p_50` | The number of times your video was played at 50% of its length. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_views_p50` | 🟢 _1.00_ | _Exact match to field 'video_views_p_50' in source._ |
| `impressions` | The number of times your ads were on screen. | `campaigns_reports_hourly.metrics.impressions` | 🟢 _1.00_ | _Exact match to field 'impressions' in source._ |
| `comments` | The number of comments your video creative received within 1 day of a user seeing a paid ad. | `campaigns_reports_hourly.metrics.comments` | 🟢 _1.00_ | _Exact match to field 'comments' in source._ |
| `real_time_cost_per_result` | As a campaign may have different optimization goals, the total number of result  is not supported in campaign section now, please go to the ad group section to view the cost  per Result. (The total count is based on when the conversion actually happened.)  | `campaigns_reports_hourly.metrics.real_time_cost_per_result` | 🟢 _1.00_ | _Exact match to field 'real_time_cost_per_result' in source._ |
| `conversion` | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.conversion` | 🟢 _1.00_ | _Exact match to field 'conversion' in source._ |
| `real_time_result` | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)  | `campaigns_reports_hourly.metrics.real_time_result` | 🟢 _1.00_ | _Exact match to field 'real_time_result' in source._ |
| `video_view_p_100` | The number of times your video was played at 100% of its length. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_views_p100` | 🟢 _1.00_ | _Exact match to field 'video_view_p_100' in source._ |
| `shares` | The number of shares your video creative received within 1 day of a user seeing a paid ad. | `campaigns_reports_hourly.metrics.shares` | 🟢 _1.00_ | _Exact match to field 'shares' in source._ |
| `real_time_conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) | `campaigns_reports_hourly.metrics.real_time_conversion_rate` | 🟢 _1.00_ | _Exact match to field 'real_time_conversion_rate' in source._ |
| `cost_per_secondary_goal_result` | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.cost_per_secondary_goal_result` | 🟢 _1.00_ | _Exact match to field 'cost_per_secondary_goal_result' in source._ |
| `secondary_goal_result_rate` | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.  | `campaigns_reports_hourly.metrics.secondary_goal_result_rate` | 🟢 _1.00_ | _Exact match to field 'secondary_goal_result_rate' in source._ |
| `clicks` | The number of clicks on your ads. | `campaigns_reports_hourly.metrics.clicks` | 🟢 _1.00_ | _Exact match to field 'clicks' in source._ |
| `cost_per_1000_reached` | The average cost to reach 1,000 unique users. This metric is estimated. | `campaigns_reports_hourly.metrics.cost_per_1000_reached` | 🟢 _1.00_ | _Exact match to field 'cost_per_1000_reached' in source._ |
| `video_views_p_25` | The number of times your video was played at 25% of its length. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_views_p25` | 🟢 _1.00_ | _Exact match to field 'video_views_p_25' in source._ |
| `reach` | The number of unique users who saw your ads at least once. This metric is estimated. | `campaigns_reports_hourly.metrics.reach` | 🟢 _1.00_ | _Exact match to field 'reach' in source._ |
| `real_time_cost_per_conversion` | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) | `campaigns_reports_hourly.metrics.real_time_cost_per_conversion` | 🟢 _1.00_ | _Exact match to field 'real_time_cost_per_conversion' in source._ |
| `profile_visits_rate` | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `average_video_play` | The average time your video was played per single video view, including any time spent replaying the video. | `campaigns_reports_hourly.metrics.average_video_play` | 🟢 _1.00_ | _Exact match to field 'average_video_play' in source._ |
| `profile_visits` | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. | `campaigns_reports_hourly.metrics.profile_visits` | 🟢 _1.00_ | _Exact match to field 'profile_visits' in source._ |
| `cpm` | The average amount of money you've spent per 1,000 impressions. | `campaigns_reports_hourly.metrics.cpm` | 🟢 _1.00_ | _Exact match to field 'cpm' in source._ |
| `ctr` | The percentage of times people saw your ad and performed a click. | `campaigns_reports_hourly.metrics.ctr` | 🟢 _1.00_ | _Exact match to field 'ctr' in source._ |
| `video_watched_2_s` | The number of times your video played for at least 2 seconds. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_watched_2s` | 🟢 _1.00_ | _Exact match to field 'video_watched_2_s' in source._ |
| `follows` | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. | `campaigns_reports_hourly.metrics.follows` | 🟢 _1.00_ | _Exact match to field 'follows' in source._ |
| `result_rate` | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.result_rate` | 🟢 _1.00_ | _Exact match to field 'result_rate' in source._ |
| `video_watched_6_s` | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_watched_6s` | 🟢 _1.00_ | _Exact match to field 'video_watched_6_s' in source._ |
| `secondary_goal_result` | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.secondary_goal_result` | 🟢 _1.00_ | _Exact match to field 'secondary_goal_result' in source._ |
| `cost_per_result` | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.cost_per_result` | 🟢 _1.00_ | _Exact match to field 'cost_per_result' in source._ |
| `average_video_play_per_user` | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. | `campaigns_reports_hourly.metrics.average_video_play_per_user` | 🟢 _1.00_ | _Exact match to field 'average_video_play_per_user' in source._ |
| `real_time_result_rate` | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to  view the Result Rate. (The total count is based on when the conversion actually happened.)  | `campaigns_reports_hourly.metrics.real_time_result_rate` | 🟢 _1.00_ | _Exact match to field 'real_time_result_rate' in source._ |
| `spend` | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. | `campaigns_reports_hourly.metrics.spend` | 🟢 _1.00_ | _Exact match to field 'spend' in source._ |
| `likes` | The number of likes your video creative received within 1 day of a user seeing a paid ad. | `campaigns_reports_hourly.metrics.likes` | 🟢 _1.00_ | _Exact match to field 'likes' in source._ |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `campaigns_reports_hourly._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping with '_airbyte_extracted_at' in source._ |
| `total_purchase_value` | The total value of purchase events that occurred in your app that were recorded by your measurement partner. | `campaigns_reports_hourly.metrics.total_purchase_value` | 🟢 _1.00_ | _Exact match to field 'total_purchase_value' in source._ |
| `total_sales_lead_value` | The monetary worth or potential value assigned to a lead generated through ads. | `MISSING` | ❌ _0.00_ | _No good match found._ |

### Mapping: Airbyte `ads` to Fivetran `ad_history`


- Table Match Confidence Score: 🟢 _0.85__
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The table mapping reflects a high degree of confidence given that the field mappings align well with expectations for a typical ad schema. However, some fields could not perfectly be matched or verified due to lack of comprehensive context._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `ad_id` | Ad ID | `ads.ad_id` | 🟢 _1.00_ | _Perfect match given the direct mapping from 'ads.ad_id'._ |
| `updated_at` | Time the record was updated. | `ads._airbyte_extracted_at` | 🟢 _1.00_ | _Standard 1.0 score for '_fivetran_synced' mapped to '_airbyte_extracted_at'._ |
| `adgroup_id` | Ad group ID | `ads.adgroup_id` | 🟢 _0.95_ | _'ads.adgroup_id' aligns well with expectations._ |
| `advertiser_id` | Advertiser ID | `ads.advertiser_id` | 🟢 _0.95_ | _'ads.advertiser_id' aligns well with expectations._ |
| `campaign_id` | Campaign ID | `ads.campaign_id` | 🟢 _0.95_ | _'ads.campaign_id' aligns well with expectations._ |
| `ad_name` | Ad Name. | `ads.ad_name` | 🟢 _1.00_ | _Directly maps from 'ads.ad_name' with high confidence._ |
| `ad_text` | The ad text. | `ads.ad_text` | 🟢 _1.00_ | _Directly maps from 'ads.ad_text' with high confidence._ |
| `app_name` | The display name of app download ad. | `ads.app_name` | 🟢 _1.00_ | _Directly maps from 'ads.app_name' with high confidence._ |
| `call_to_action` | Call to action values. | `ads.call_to_action` | 🟢 _1.00_ | _Directly maps from 'ads.call_to_action' with high confidence._ |
| `click_tracking_url` | Click monitoring URL. | `ads.click_tracking_url` | 🟢 _1.00_ | _Directly maps from 'ads.click_tracking_url' with high confidence._ |
| `create_time` | Time at which the ad was created. | `ads.create_time` | 🟢 _0.90_ | _Most likely correct mapping but slight uncertainty._ |
| `display_name` | The display name of landing page or pure exposure ad. | `ads.display_name` | 🟢 _0.90_ | _Most likely correct mapping but slight uncertainty._ |
| `image_ids` | A list of image IDs. | `ads.image_ids` | 🟢 _0.90_ | _Most likely correct mapping but slight uncertainty._ |
| `impression_tracking_url` | Display monitoring URL. | `ads.impression_tracking_url` | 🟢 _0.85_ | _Maps to 'ads.impression_tracking_url'; expression is detailed and consistent with ad-related data._ |
| `is_aco` | Whether the ad is an automated ad. | `ads.is_aco` | 🟢 _0.90_ | _The mapping appears consistent with ad schema._ |
| `is_creative_authorized` | Whether you grant displaying some of your ads in our TikTok For Business Creative Center. Only valid for non-US advertisers, the default value is false.  | `ads.creative_authorized` | 🟢 _0.85_ | _Mappings align, but US-specific context introduces slight uncertainty._ |
| `is_new_structure` | Whether the campaign is a new structure. | `ads.is_new_structure` | 🟢 _0.85_ | _Limited by schema-specific context._ |
| `landing_page_url` | Landing page URL. | `ads.landing_page_url` | 🟢 _1.00_ | _Direct mapping from 'ads.landing_page_url' is strong._ |
| `open_url` | The specific location where you want your audience to go if they have your app installed. | `ads.deeplink` | 🟢 _0.85_ | _Mapping exists but specifics vary, slightly lowering confidence._ |
| `opt_status` | Operation status. | `ads.operation_status` | 🟢 _0.85_ | _Limited schema context slightly reduces confidence._ |
| `playable_url` | Playable material url. | `ads.playable_url` | 🟢 _1.00_ | _Strong mapping based on ad schema knowledge._ |
| `profile_image` | Avatar URL. | `ads.profile_image_url` | 🟢 _1.00_ | _Direct mapping from 'ads.profile_image_url' matches perfectly._ |
| `status` | Ad status. | `ads.secondary_status` | 🟢 _0.90_ | _Expected mapping from 'ads.secondary_status', but some schema variance may exist._ |
| `video_id` | The video ID. | `ads.video_id` | 🟢 _1.00_ | _Direct mapping from 'ads.video_id' finely matches expectations._ |

### Mapping: Airbyte `ads_reports_hourly` to Fivetran `ad_report_hourly`


- Table Match Confidence Score: 🟢 _0.85__
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mapping is highly confident with most fields accurately mapped to their equivalents in the target schema. However, a few fields have missing mappings which slightly lowers the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `ad_id` | Ad id | `ads_reports_hourly.ad_id` | 🟢 _1.00_ | _Perfect match for 'ad_id' field._ |
| `stat_time_hour` | Hour of activity | `ads_reports_hourly.stat_time_hour` | 🟢 _0.95_ | _Strong match for 'stat_time_hour' field._ |
| `cost_per_conversion` | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.cost_per_conversion` | 🟢 _0.95_ | _Strong match for 'cost_per_conversion' field._ |
| `real_time_conversion` | Number of times your ad resulted in the optimization event you selected. | `ads_reports_hourly.metrics.real_time_conversion` | 🟢 _0.95_ | _Strong match for 'real_time_conversion' field._ |
| `cpc` | The average amount of money you've spent on a click. | `ads_reports_hourly.metrics.cpc` | 🟢 _0.95_ | _Strong match for 'cpc' field._ |
| `video_play_actions` | The number of times your video starts to play. Replays will not be counted. | `ads_reports_hourly.metrics.video_play_actions` | 🟢 _0.95_ | _Strong match for 'video_play_actions' field._ |
| `conversion_rate` | The percentage of results you received out of all the clicks of your ads.   (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.conversion_rate` | 🟢 _0.95_ | _Strong match for 'conversion_rate' field._ |
| `video_views_p_75` | The number of times your video was played at 75% of its length. Replays will not be counted. | `ads_reports_hourly.metrics.video_views_p75` | 🟢 _0.95_ | _Strong match for 'video_views_p_75' field._ |
| `result` | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.result` | 🟢 _0.95_ | _Strong match for 'result' field._ |
| `video_views_p_50` | The number of times your video was played at 50% of its length. Replays will not be counted. | `ads_reports_hourly.metrics.video_views_p50` | 🟢 _0.95_ | _Strong match for 'video_views_p_50' field._ |
| `impressions` | The number of times your ads were on screen. | `ads_reports_hourly.metrics.impressions` | 🟢 _0.95_ | _Strong match for 'impressions' field._ |
| `comments` | The number of comments your video creative received within 1 day of a user seeing a paid ad. | `ads_reports_hourly.metrics.comments` | 🟢 _0.95_ | _Strong match for 'comments' field._ |
| `real_time_cost_per_result` | As a campaign may have different optimization goals, the total number of result   is not supported in campaign section now, please go to the ad group section to view the cost per Result. (The total count is based on when the conversion actually happened.)  | `ads_reports_hourly.metrics.real_time_cost_per_result` | 🟢 _0.95_ | _Strong match for 'real_time_cost_per_result' field._ |
| `conversion` | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns.  Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.conversion` | 🟢 _0.95_ | _Strong match for 'conversion' field._ |
| `real_time_result` | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)  | `ads_reports_hourly.metrics.real_time_result` | 🟢 _0.95_ | _Strong match for 'real_time_result' field._ |
| `video_view_p_100` | The number of times your video was played at 100% of its length. Replays will not be counted. | `ads_reports_hourly.metrics.video_views_p100` | 🟢 _0.95_ | _Strong match for 'video_view_p_100' field._ |
| `shares` | The number of shares your video creative received within 1 day of a user seeing a paid ad. | `ads_reports_hourly.metrics.shares` | 🟢 _0.95_ | _Strong match for 'shares' field._ |
| `real_time_conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) | `ads_reports_hourly.metrics.real_time_conversion_rate` | 🟢 _0.95_ | _Strong match for 'real_time_conversion_rate' field._ |
| `cost_per_secondary_goal_result` | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.cost_per_secondary_goal_result` | 🟢 _0.95_ | _Strong match for 'cost_per_secondary_goal_result' field._ |
| `secondary_goal_result_rate` | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.  | `ads_reports_hourly.metrics.secondary_goal_result_rate` | 🟢 _0.95_ | _Strong match for 'secondary_goal_result_rate' field._ |
| `clicks` | The number of clicks on your ads. | `ads_reports_hourly.metrics.clicks` | 🟢 _0.95_ | _Strong match for 'clicks' field._ |
| `cost_per_1000_reached` | The average cost to reach 1,000 unique users. This metric is estimated. | `ads_reports_hourly.metrics.cost_per_1000_reached` | 🟢 _0.95_ | _Strong match for 'cost_per_1000_reached' field._ |
| `video_views_p_25` | The number of times your video was played at 25% of its length. Replays will not be counted. | `ads_reports_hourly.metrics.video_views_p25` | 🟢 _0.95_ | _Strong match for 'video_views_p_25' field._ |
| `reach` | The number of unique users who saw your ads at least once. This metric is estimated. | `ads_reports_hourly.metrics.reach` | 🟢 _0.95_ | _Strong match for 'reach' field._ |
| `real_time_cost_per_conversion` | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) | `ads_reports_hourly.metrics.real_time_cost_per_conversion` | 🟢 _0.95_ | _Strong match for 'real_time_cost_per_conversion' field._ |
| `profile_visits_rate` | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. | `ads_reports_hourly.metrics.profile_visits_rate` | 🟢 _0.95_ | _Strong match for 'profile_visits_rate' field._ |
| `average_video_play` | The average time your video was played per single video view, including any time spent replaying the video. | `ads_reports_hourly.metrics.average_video_play` | 🟢 _0.95_ | _Strong match for 'average_video_play' field._ |
| `profile_visits` | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. | `ads_reports_hourly.metrics.profile_visits` | 🟢 _0.95_ | _Strong match for 'profile_visits' field._ |
| `cpm` | The average amount of money you've spent per 1,000 impressions. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `ctr` | The percentage of times people saw your ad and performed a click. | `ads_reports_hourly.metrics.ctr` | 🟢 _0.95_ | _Strong match for 'ctr' field._ |
| `video_watched_2_s` | The number of times your video played for at least 2 seconds. Replays will not be counted. | `ads_reports_hourly.metrics.video_watched_2s` | 🟢 _0.95_ | _Strong match for 'video_watched_2_s' field._ |
| `follows` | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. | `ads_reports_hourly.metrics.follows` | 🟢 _0.95_ | _Strong match for 'follows' field._ |
| `result_rate` | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.result_rate` | 🟢 _0.95_ | _Strong match for 'result_rate' field._ |
| `video_watched_6_s` | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. | `ads_reports_hourly.metrics.video_watched_6s` | 🟢 _0.95_ | _Strong match for 'video_watched_6_s' field._ |
| `secondary_goal_result` | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.secondary_goal_result` | 🟢 _0.95_ | _Strong match for 'secondary_goal_result' field._ |
| `cost_per_result` | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.cost_per_result` | 🟢 _0.95_ | _Strong match for 'cost_per_result' field._ |
| `average_video_play_per_user` | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. | `ads_reports_hourly.metrics.average_video_play_per_user` | 🟢 _0.95_ | _Strong match for 'average_video_play_per_user' field._ |
| `real_time_result_rate` | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to view the Result Rate. (The total count is based on when the conversion actually happened.) | `ads_reports_hourly.metrics.real_time_result_rate` | 🟢 _0.95_ | _Strong match for 'real_time_result_rate' field._ |
| `spend` | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. | `ads_reports_hourly.metrics.spend` | 🟢 _0.95_ | _Strong match for 'spend' field._ |
| `likes` | The number of likes your video creative received within 1 day of a user seeing a paid ad. | `ads_reports_hourly.metrics.likes` | 🟢 _0.95_ | _Strong match for 'likes' field._ |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `ads_reports_hourly._airbyte_extracted_at` | 🟢 _1.00_ | _Standard mapping for sync timestamp field._ |
| `total_purchase_value` | The total value of purchase events that occurred in your app that were recorded by your measurement partner. | `ads_reports_hourly.metrics.total_purchase_value` | 🟢 _0.95_ | _Strong match for 'total_purchase_value' field._ |
| `total_sales_lead_value` | The monetary worth or potential value assigned to a lead generated through ads. | `MISSING` | ❌ _0.00_ | _No good match found._ |

## Workshop Models

These models are in the workshop directory and are not yet approved.

### Mapping: Airbyte `ad_groups` to Fivetran `adgroup_history`


- Table Match Confidence Score: 🟢 _0.90__
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table match score is high due to strong alignment between the source and target schemas from similar APIs. However, completion is limited by several 'MISSING' fields that indicate fields present in target schema do not have corresponding entries in the source schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `adgroup_id` | Ad group ID | `ad_groups.adgroup_id` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `updated_at` | Time the record was updated. | `ad_groups.modify_time` | 🟢 _0.70_ | _Likely the correct match based on context and typical usage, but not perfect due to possible alternate interpretations._ |
| `advertiser_id` | Advertiser ID | `ad_groups.advertiser_id` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `campaign_id` | The Ad group's campaign ID. | `ad_groups.campaign_id` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `action_categories` | IDs of the action categories (behaviors) that you want to target. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `action_days` | The number of days of the time period to include action from. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `adgroup_name` | Ad group name. Character limit is 512 and cannot contain emoji. | `ad_groups.adgroup_name` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `age_groups` | Age groups you want to target. This is the newest version of the field `age`, which was renamed after the Tiktok Ads v1.3 API release.  | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `android_osv` | Minimum Android version. | `ad_groups.min_android_version` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `app_download_url` | App download link | `ad_groups.app_download_url` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `app_id` | The Application id of the promoted app | `ad_groups.app_id` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `app_name` | App name. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `app_type` | App type. | `ad_groups.app_type` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `audience` | A list of audience IDs. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `audience_type` | Audience Type | `ad_groups.audience_type` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `bid` | CPC, CPM bidding, oCPM learning bidding | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `bid_type` | Bidding Strategy | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `billing_event` | Bid method. | `ad_groups.billing_event` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `budget` | Ad budget. Returns 0.0 when Campaign Budget Optimization (budget_optimize_switch) is on. | `ad_groups.budget` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `budget_mode` | Budget mode. This field will be ignored when Campaign Budget Optimization (budget_optimize_switch) is enabled. | `ad_groups.budget_mode` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `carriers` | Carriers that you want to target. | `ad_groups.carriers` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `category` | Ad group category. | `ad_groups.category_id` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `click_tracking_url` | Click monitoring URL. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `connection_type` | Device connection types that you want to target. Default; unlimited. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `conversion_bid` | oCPM conversion bid | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `cpv_video_duration` | Video playback duration, required if optimize_goal is VIDEO_VIEW.  Allowed values; SIX_SECONDS (video playback 6s), TWO_SECONDS (video playback 2s)  | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `creative_material_mode` | Creative delivery mode. | `ad_groups.creative_material_mode` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `dayparting` | Ad delivery period, the default is always and the format is 48 * 7 character string, represented by 0 or 1. > That is, with half an hour as the minimum granularity, a day (24 hours) is divided by the minimum granularity(30 mins) from Monday to Sunday. Resulting in a 48*7 format.0 represents not to be delivered, 1 represents delivery. no transmission, full transmission 0, full transmission 1 all represent full time delivery | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `deep_bid_type` | Bidding strategy for in-app events. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `deep_cpabid` | Deep bid | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `deep_external_action` | Deep conversion event. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `display_name` | Display name of ad group. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `enable_inventory_filter` | Inventory filtering (Unsafe videos will not be displayed). | `ad_groups.inventory_filter_enabled` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `excluded_audience` | A list of audience ID to be excluded. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `external_action` | Conversion event for the ad group. It is required when the promoted object is an app with tracking urls, or when pixel_id is specified. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `fallback_type` | Fallback Type. If the audience do not have the app installed, you can have them fall back to install the app, or to view a specific web page. Not applicable for Deferred Deeplink. Allowed values; APP_INSTALL, WEBSITE, UNSET. If website is chosen, you need to specify the url via landing_page_url field.  | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `frequency` | frequency, together with frequency_schedule, controls how often people see your ad (only available for REACH ads).  For example, frequency = 2 frequency_schedule = 3 means "show ads no more than twice every 3 day".  | `ad_groups.frequency` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `frequency_schedule` | frequency, together with frequency, controls how often people see your ad (only available for REACH ads). | `ad_groups.frequency_schedule` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `gender` | Gender that you want to target. | `ad_groups.gender` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `impression_tracking_url` | Display monitoring URL. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `interest_category_v2` | Interest classification. If the interest is specified, users that do not meet interest target will be excluded during delivery. | `ad_groups.interest_category_ids` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `ios_osv` | Minimum iOS version. | `ad_groups.min_ios_version` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `is_comment_disable` | Whether to allow comments on your ads on TikTok, Vigo, Helo. | `ad_groups.comment_disabled` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `is_hfss` | Whether the promoted content is HFSS foods (foods that are high in fat, salt, or sugar). | `ad_groups.is_hfss` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `is_new_structure` | Whether the campaign is a new structure. | `ad_groups.is_new_structure` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `keywords` | Keywords used. | `ad_groups.keywords` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `landing_page_url` | Landing page URL. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `languages` | Codes of the languages that you want to target. | `ad_groups.languages` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `location` | IDs of the locations that you want to target. | `ad_groups.location_ids` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `open_url` | The specific location where you want your audience to go if they have your app installed. | `ad_groups.promotion_website_type` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `open_url_type` | The open URL type. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `operation_system` | Device operating systems that you want to target. | `ad_groups.operating_systems` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `opt_status` | Operation status. | `ad_groups.operation_status` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `optimize_goal` | Optimization goal. | `ad_groups.optimization_goal` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `pacing` | You can choose between PACING_MODE_SMOOTH and PACING_MODE_FAST. For PACING_MODE_SMOOTH, the budget is allocated evenly within the scheduled time.  PACING_MODE_FAST would consume budget and produce results as soon as possible.   | `ad_groups.pacing` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `package` | Package name. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `pangle_block_app_list_id` | Pangle app block list ID. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `pixel_id` | Pixel ID. Only application for landing pages. | `ad_groups.pixel_id` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `placement` | The apps where you want to deliver your ads. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `placement_type` | Placement type. | `ad_groups.placement_type` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `profile_image` | Avatar URL. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `schedule_end_time` | Ad delivery end time (UTC+0). Format should be YYYY-MM-DD HH:MM:SS | `ad_groups.schedule_end_time` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `schedule_start_time` | Ad delivery start time (UTC+0). Format should be YYYY-MM-DD HH:MM:SS | `ad_groups.schedule_start_time` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `schedule_type` | The schedule type, which can be either SCHEDULE_START_END or SCHEDULE_FROM_NOW. | `ad_groups.schedule_type` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `skip_learning_phase` | Whether to skip the learning stage. | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `statistic_type` | conversion bid statistic type | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `status` | Ad group status | `MISSING` | ❌ _0.00_ | _No good match found._ |
| `video_actions` | Number of video actions. | `ad_groups.video_actions` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
| `video_download` | Whether users can download your video ads on TikTok(cannot be updated once created). | `ad_groups.video_download_disabled` | 🟢 _1.00_ | _Perfect match based on field name and context._ |
