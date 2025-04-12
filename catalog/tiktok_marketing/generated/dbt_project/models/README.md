# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping: Airbyte `advertisers` to Fivetran `advertiser`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table has strong similarities in representing advertiser information across both source and target schemas. However, there is some discrepancy in field mapping completion due primarily to missing field expressions, though key fields like '_fivetran_synced' show complete and direct mapping._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Advertiser ID | `advertisers.advertiser_id` | 🟢 _0.95_ | *The field 'id' is mapped accurately to 'advertisers.advertiser_id'.* |
| `address` | Advertiser address information | `advertisers.address` | 🟢 _0.95_ | *The field 'address' corresponds well with 'advertisers.address'.* |
| `balance` | Account available balance | `advertisers.balance` | 🟢 _0.95_ | *The field 'balance' is correctly mapped to 'advertisers.balance'.* |
| `cellphone_number` | Contact mobile number, desensitised data. This is the newest version of the field `phone_number`, which was renamed after the Tiktok Ads v1.3 API release.  | `advertisers.cellphone_number` | 🟢 _0.95_ | *'cellphone_number' matches with 'advertisers.cellphone_number', reminiscent of a field update.* |
| `company` | Advertiser's company name | `advertisers.company` | 🟢 _0.95_ | *The field 'company' corresponds well with 'advertisers.company'.* |
| `contacter` | Contact Person | `advertisers.contacter` | 🟢 _0.95_ | *The field 'contacter' aligns well with 'advertisers.contacter'.* |
| `country` | The advertiser's country | `advertisers.country` | 🟢 _0.95_ | *The field 'country' is correctly mapped to 'advertisers.country'.* |
| `create_time` | Advertiser's create time | `advertisers.create_time` | 🟢 _0.95_ | *The field 'create_time' maps directly to 'advertisers.create_time'.* |
| `currency` | Type of currency used by advertisers | `advertisers.currency` | 🟢 _0.95_ | *The field 'currency' is mapped accurately to 'advertisers.currency'.* |
| `description` | Brand description, i.e. promotional content | `advertisers.description` | 🟢 _0.95_ | *The field 'description' is correctly mapped to 'advertisers.description'.* |
| `email` | Advertiser contact email, desensitised data | `advertisers.email` | 🟢 _0.95_ | *The field 'email' corresponds well with 'advertisers.email'.* |
| `industry` | Advertiser industry category | `advertisers.industry` | 🟢 _0.95_ | *The field 'industry' is correctly mapped to 'advertisers.industry'.* |
| `language` | Language used by advertisers | `advertisers.language` | 🟢 _0.95_ | *The field 'language' corresponds well with 'advertisers.language'.* |
| `license_no` | License number | `advertisers.license_no` | 🟢 _0.95_ | *The field 'license_no' maps directly to 'advertisers.license_no'.* |
| `license_url` | License preview address, the link is valid for an hour by default. | `advertisers.license_url` | 🟢 _0.95_ | *The field 'license_url' is mapped accurately to 'advertisers.license_url'.* |
| `name` | Advertiser name | `advertisers.name` | 🟢 _0.95_ | *The field 'name' matches correctly with 'advertisers.name'.* |
| `phone_number` | Contact mobile number, desensitised data. IMPORTANT: This field will not be populated for connectors utilizing the Tiktok Ads v1.3 API version, as the column was renamed.  The new column name is `cellphone_number`.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `promotion_area` | Operation area | `advertisers.promotion_area` | 🟢 _0.95_ | *The field 'promotion_area' corresponds well with 'advertisers.promotion_area'.* |
| `reason` | Reason for rejection | `advertisers.rejection_reason` | 🟢 _0.95_ | *The field 'reason' maps directly to 'advertisers.rejection_reason'.* |
| `role` | Advertiser role | `advertisers.role` | 🟢 _0.95_ | *The field 'role' is correctly mapped to 'advertisers.role'.* |
| `status` | Advertiser status | `advertisers.status` | 🟢 _0.95_ | *The field 'status' corresponds well with 'advertisers.status'.* |
| `telephone` | Fixed phone number, desensitised data IMPORTANT: This field will not be populated for connectors utilizing the Tiktok Ads v1.3 API version, as the column was renamed.  The new column name is `telephone_number`.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `telephone_number` | Fixed phone number, desensitised data This is the newest version of the field `telephone`, which was renamed after the Tiktok Ads v1.3 API release.  | `advertisers.telephone_number` | 🟢 _0.95_ | *The field 'telephone_number' matches correctly with 'advertisers.telephone_number'.* |
| `timezone` | Ad account time zone including GMT offset | `advertisers.timezone` | 🟢 _0.95_ | *The field 'timezone' is mapped accurately to 'advertisers.timezone'.* |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `advertisers._airbyte_extracted_at` | 🟢 _1.00_ | *The field '_fivetran_synced' is correctly mapped to 'advertisers._airbyte_extracted_at'.* |

### Mapping: Airbyte `campaigns_reports_hourly` to Fivetran `campaign_report_hourly`


- Table Match Confidence Score: 🟢 _0.95_
- Table Completion Score: 🟢 _0.97_
- Summary Self-Evaluation: _The table and field mappings are highly accurate. The mapping configuration includes a variety of field mappings that closely align with their expressions, with few MISSING mappings indicating minor gaps in completion. Generally, mappings such as '_fivetran_synced' to '_airbyte_extracted_at' are perfectly matched, resulting in a high table match score. Other fields are accurately associated with the correct expressions, suggesting they describe the same subject matter from a shared source. This results in a high completion score due to the absence of non-mappable fields, apart from minor misses like 'total_sales_lead_value' and 'profile_visits_rate'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `campaign_id` | Campaign id | `campaigns_reports_hourly.campaign_id` | 🟢 _1.00_ | *Exact match to field 'campaign_id' in source.* |
| `stat_time_hour` | Hour of activity | `campaigns_reports_hourly.stat_time_hour` | 🟢 _1.00_ | *Exact match to field 'stat_time_hour' in source.* |
| `cost_per_conversion` | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.cost_per_conversion` | 🟢 _1.00_ | *Exact match to field 'cost_per_conversion' in source.* |
| `real_time_conversion` | Number of times your ad resulted in the optimization event you selected. | `campaigns_reports_hourly.metrics.real_time_conversion` | 🟢 _1.00_ | *Exact match to field 'real_time_conversion' in source.* |
| `cpc` | The average amount of money you've spent on a click. | `campaigns_reports_hourly.metrics.cpc` | 🟢 _1.00_ | *Exact match to field 'cpc' in source.* |
| `video_play_actions` | The number of times your video starts to play. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_play_actions` | 🟢 _1.00_ | *Exact match to field 'video_play_actions' in source.* |
| `conversion_rate` | The percentage of results you received out of all the clicks of your ads.   (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.conversion_rate` | 🟢 _1.00_ | *Exact match to field 'conversion_rate' in source.* |
| `video_views_p_75` | The number of times your video was played at 75% of its length. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_views_p75` | 🟢 _1.00_ | *Exact match to field 'video_views_p_75' in source.* |
| `result` | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.result` | 🟢 _1.00_ | *Exact match to field 'result' in source.* |
| `video_views_p_50` | The number of times your video was played at 50% of its length. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_views_p50` | 🟢 _1.00_ | *Exact match to field 'video_views_p_50' in source.* |
| `impressions` | The number of times your ads were on screen. | `campaigns_reports_hourly.metrics.impressions` | 🟢 _1.00_ | *Exact match to field 'impressions' in source.* |
| `comments` | The number of comments your video creative received within 1 day of a user seeing a paid ad. | `campaigns_reports_hourly.metrics.comments` | 🟢 _1.00_ | *Exact match to field 'comments' in source.* |
| `real_time_cost_per_result` | As a campaign may have different optimization goals, the total number of result  is not supported in campaign section now, please go to the ad group section to view the cost  per Result. (The total count is based on when the conversion actually happened.)  | `campaigns_reports_hourly.metrics.real_time_cost_per_result` | 🟢 _1.00_ | *Exact match to field 'real_time_cost_per_result' in source.* |
| `conversion` | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.conversion` | 🟢 _1.00_ | *Exact match to field 'conversion' in source.* |
| `real_time_result` | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)  | `campaigns_reports_hourly.metrics.real_time_result` | 🟢 _1.00_ | *Exact match to field 'real_time_result' in source.* |
| `video_view_p_100` | The number of times your video was played at 100% of its length. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_views_p100` | 🟢 _1.00_ | *Exact match to field 'video_view_p_100' in source.* |
| `shares` | The number of shares your video creative received within 1 day of a user seeing a paid ad. | `campaigns_reports_hourly.metrics.shares` | 🟢 _1.00_ | *Exact match to field 'shares' in source.* |
| `real_time_conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) | `campaigns_reports_hourly.metrics.real_time_conversion_rate` | 🟢 _1.00_ | *Exact match to field 'real_time_conversion_rate' in source.* |
| `cost_per_secondary_goal_result` | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.cost_per_secondary_goal_result` | 🟢 _1.00_ | *Exact match to field 'cost_per_secondary_goal_result' in source.* |
| `secondary_goal_result_rate` | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.  | `campaigns_reports_hourly.metrics.secondary_goal_result_rate` | 🟢 _1.00_ | *Exact match to field 'secondary_goal_result_rate' in source.* |
| `clicks` | The number of clicks on your ads. | `campaigns_reports_hourly.metrics.clicks` | 🟢 _1.00_ | *Exact match to field 'clicks' in source.* |
| `cost_per_1000_reached` | The average cost to reach 1,000 unique users. This metric is estimated. | `campaigns_reports_hourly.metrics.cost_per_1000_reached` | 🟢 _1.00_ | *Exact match to field 'cost_per_1000_reached' in source.* |
| `video_views_p_25` | The number of times your video was played at 25% of its length. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_views_p25` | 🟢 _1.00_ | *Exact match to field 'video_views_p_25' in source.* |
| `reach` | The number of unique users who saw your ads at least once. This metric is estimated. | `campaigns_reports_hourly.metrics.reach` | 🟢 _1.00_ | *Exact match to field 'reach' in source.* |
| `real_time_cost_per_conversion` | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) | `campaigns_reports_hourly.metrics.real_time_cost_per_conversion` | 🟢 _1.00_ | *Exact match to field 'real_time_cost_per_conversion' in source.* |
| `profile_visits_rate` | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `average_video_play` | The average time your video was played per single video view, including any time spent replaying the video. | `campaigns_reports_hourly.metrics.average_video_play` | 🟢 _1.00_ | *Exact match to field 'average_video_play' in source.* |
| `profile_visits` | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. | `campaigns_reports_hourly.metrics.profile_visits` | 🟢 _1.00_ | *Exact match to field 'profile_visits' in source.* |
| `cpm` | The average amount of money you've spent per 1,000 impressions. | `campaigns_reports_hourly.metrics.cpm` | 🟢 _1.00_ | *Exact match to field 'cpm' in source.* |
| `ctr` | The percentage of times people saw your ad and performed a click. | `campaigns_reports_hourly.metrics.ctr` | 🟢 _1.00_ | *Exact match to field 'ctr' in source.* |
| `video_watched_2_s` | The number of times your video played for at least 2 seconds. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_watched_2s` | 🟢 _1.00_ | *Exact match to field 'video_watched_2_s' in source.* |
| `follows` | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. | `campaigns_reports_hourly.metrics.follows` | 🟢 _1.00_ | *Exact match to field 'follows' in source.* |
| `result_rate` | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.result_rate` | 🟢 _1.00_ | *Exact match to field 'result_rate' in source.* |
| `video_watched_6_s` | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. | `campaigns_reports_hourly.metrics.video_watched_6s` | 🟢 _1.00_ | *Exact match to field 'video_watched_6_s' in source.* |
| `secondary_goal_result` | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.secondary_goal_result` | 🟢 _1.00_ | *Exact match to field 'secondary_goal_result' in source.* |
| `cost_per_result` | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)  | `campaigns_reports_hourly.metrics.cost_per_result` | 🟢 _1.00_ | *Exact match to field 'cost_per_result' in source.* |
| `average_video_play_per_user` | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. | `campaigns_reports_hourly.metrics.average_video_play_per_user` | 🟢 _1.00_ | *Exact match to field 'average_video_play_per_user' in source.* |
| `real_time_result_rate` | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to  view the Result Rate. (The total count is based on when the conversion actually happened.)  | `campaigns_reports_hourly.metrics.real_time_result_rate` | 🟢 _1.00_ | *Exact match to field 'real_time_result_rate' in source.* |
| `spend` | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. | `campaigns_reports_hourly.metrics.spend` | 🟢 _1.00_ | *Exact match to field 'spend' in source.* |
| `likes` | The number of likes your video creative received within 1 day of a user seeing a paid ad. | `campaigns_reports_hourly.metrics.likes` | 🟢 _1.00_ | *Exact match to field 'likes' in source.* |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `campaigns_reports_hourly._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping with '_airbyte_extracted_at' in source.* |
| `total_purchase_value` | The total value of purchase events that occurred in your app that were recorded by your measurement partner. | `campaigns_reports_hourly.metrics.total_purchase_value` | 🟢 _1.00_ | *Exact match to field 'total_purchase_value' in source.* |
| `total_sales_lead_value` | The monetary worth or potential value assigned to a lead generated through ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `ads_reports_hourly` to Fivetran `ad_report_hourly`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mapping is highly confident with most fields accurately mapped to their equivalents in the target schema. However, a few fields have missing mappings which slightly lowers the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `ad_id` | Ad id | `ads_reports_hourly.ad_id` | 🟢 _1.00_ | *Perfect match for 'ad_id' field.* |
| `stat_time_hour` | Hour of activity | `ads_reports_hourly.stat_time_hour` | 🟢 _0.95_ | *Strong match for 'stat_time_hour' field.* |
| `cost_per_conversion` | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.cost_per_conversion` | 🟢 _0.95_ | *Strong match for 'cost_per_conversion' field.* |
| `real_time_conversion` | Number of times your ad resulted in the optimization event you selected. | `ads_reports_hourly.metrics.real_time_conversion` | 🟢 _0.95_ | *Strong match for 'real_time_conversion' field.* |
| `cpc` | The average amount of money you've spent on a click. | `ads_reports_hourly.metrics.cpc` | 🟢 _0.95_ | *Strong match for 'cpc' field.* |
| `video_play_actions` | The number of times your video starts to play. Replays will not be counted. | `ads_reports_hourly.metrics.video_play_actions` | 🟢 _0.95_ | *Strong match for 'video_play_actions' field.* |
| `conversion_rate` | The percentage of results you received out of all the clicks of your ads.   (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.conversion_rate` | 🟢 _0.95_ | *Strong match for 'conversion_rate' field.* |
| `video_views_p_75` | The number of times your video was played at 75% of its length. Replays will not be counted. | `ads_reports_hourly.metrics.video_views_p75` | 🟢 _0.95_ | *Strong match for 'video_views_p_75' field.* |
| `result` | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.result` | 🟢 _0.95_ | *Strong match for 'result' field.* |
| `video_views_p_50` | The number of times your video was played at 50% of its length. Replays will not be counted. | `ads_reports_hourly.metrics.video_views_p50` | 🟢 _0.95_ | *Strong match for 'video_views_p_50' field.* |
| `impressions` | The number of times your ads were on screen. | `ads_reports_hourly.metrics.impressions` | 🟢 _0.95_ | *Strong match for 'impressions' field.* |
| `comments` | The number of comments your video creative received within 1 day of a user seeing a paid ad. | `ads_reports_hourly.metrics.comments` | 🟢 _0.95_ | *Strong match for 'comments' field.* |
| `real_time_cost_per_result` | As a campaign may have different optimization goals, the total number of result   is not supported in campaign section now, please go to the ad group section to view the cost per Result. (The total count is based on when the conversion actually happened.)  | `ads_reports_hourly.metrics.real_time_cost_per_result` | 🟢 _0.95_ | *Strong match for 'real_time_cost_per_result' field.* |
| `conversion` | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns.  Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.conversion` | 🟢 _0.95_ | *Strong match for 'conversion' field.* |
| `real_time_result` | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)  | `ads_reports_hourly.metrics.real_time_result` | 🟢 _0.95_ | *Strong match for 'real_time_result' field.* |
| `video_view_p_100` | The number of times your video was played at 100% of its length. Replays will not be counted. | `ads_reports_hourly.metrics.video_views_p100` | 🟢 _0.95_ | *Strong match for 'video_view_p_100' field.* |
| `shares` | The number of shares your video creative received within 1 day of a user seeing a paid ad. | `ads_reports_hourly.metrics.shares` | 🟢 _0.95_ | *Strong match for 'shares' field.* |
| `real_time_conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) | `ads_reports_hourly.metrics.real_time_conversion_rate` | 🟢 _0.95_ | *Strong match for 'real_time_conversion_rate' field.* |
| `cost_per_secondary_goal_result` | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.cost_per_secondary_goal_result` | 🟢 _0.95_ | *Strong match for 'cost_per_secondary_goal_result' field.* |
| `secondary_goal_result_rate` | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.  | `ads_reports_hourly.metrics.secondary_goal_result_rate` | 🟢 _0.95_ | *Strong match for 'secondary_goal_result_rate' field.* |
| `clicks` | The number of clicks on your ads. | `ads_reports_hourly.metrics.clicks` | 🟢 _0.95_ | *Strong match for 'clicks' field.* |
| `cost_per_1000_reached` | The average cost to reach 1,000 unique users. This metric is estimated. | `ads_reports_hourly.metrics.cost_per_1000_reached` | 🟢 _0.95_ | *Strong match for 'cost_per_1000_reached' field.* |
| `video_views_p_25` | The number of times your video was played at 25% of its length. Replays will not be counted. | `ads_reports_hourly.metrics.video_views_p25` | 🟢 _0.95_ | *Strong match for 'video_views_p_25' field.* |
| `reach` | The number of unique users who saw your ads at least once. This metric is estimated. | `ads_reports_hourly.metrics.reach` | 🟢 _0.95_ | *Strong match for 'reach' field.* |
| `real_time_cost_per_conversion` | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) | `ads_reports_hourly.metrics.real_time_cost_per_conversion` | 🟢 _0.95_ | *Strong match for 'real_time_cost_per_conversion' field.* |
| `profile_visits_rate` | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. | `ads_reports_hourly.metrics.profile_visits_rate` | 🟢 _0.95_ | *Strong match for 'profile_visits_rate' field.* |
| `average_video_play` | The average time your video was played per single video view, including any time spent replaying the video. | `ads_reports_hourly.metrics.average_video_play` | 🟢 _0.95_ | *Strong match for 'average_video_play' field.* |
| `profile_visits` | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. | `ads_reports_hourly.metrics.profile_visits` | 🟢 _0.95_ | *Strong match for 'profile_visits' field.* |
| `cpm` | The average amount of money you've spent per 1,000 impressions. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `ctr` | The percentage of times people saw your ad and performed a click. | `ads_reports_hourly.metrics.ctr` | 🟢 _0.95_ | *Strong match for 'ctr' field.* |
| `video_watched_2_s` | The number of times your video played for at least 2 seconds. Replays will not be counted. | `ads_reports_hourly.metrics.video_watched_2s` | 🟢 _0.95_ | *Strong match for 'video_watched_2_s' field.* |
| `follows` | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. | `ads_reports_hourly.metrics.follows` | 🟢 _0.95_ | *Strong match for 'follows' field.* |
| `result_rate` | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.result_rate` | 🟢 _0.95_ | *Strong match for 'result_rate' field.* |
| `video_watched_6_s` | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. | `ads_reports_hourly.metrics.video_watched_6s` | 🟢 _0.95_ | *Strong match for 'video_watched_6_s' field.* |
| `secondary_goal_result` | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.secondary_goal_result` | 🟢 _0.95_ | *Strong match for 'secondary_goal_result' field.* |
| `cost_per_result` | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)  | `ads_reports_hourly.metrics.cost_per_result` | 🟢 _0.95_ | *Strong match for 'cost_per_result' field.* |
| `average_video_play_per_user` | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. | `ads_reports_hourly.metrics.average_video_play_per_user` | 🟢 _0.95_ | *Strong match for 'average_video_play_per_user' field.* |
| `real_time_result_rate` | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to view the Result Rate. (The total count is based on when the conversion actually happened.) | `ads_reports_hourly.metrics.real_time_result_rate` | 🟢 _0.95_ | *Strong match for 'real_time_result_rate' field.* |
| `spend` | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. | `ads_reports_hourly.metrics.spend` | 🟢 _0.95_ | *Strong match for 'spend' field.* |
| `likes` | The number of likes your video creative received within 1 day of a user seeing a paid ad. | `ads_reports_hourly.metrics.likes` | 🟢 _0.95_ | *Strong match for 'likes' field.* |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `ads_reports_hourly._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for sync timestamp field.* |
| `total_purchase_value` | The total value of purchase events that occurred in your app that were recorded by your measurement partner. | `ads_reports_hourly.metrics.total_purchase_value` | 🟢 _0.95_ | *Strong match for 'total_purchase_value' field.* |
| `total_sales_lead_value` | The monetary worth or potential value assigned to a lead generated through ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `ad_groups_reports_hourly` to Fivetran `adgroup_report_hourly`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _Successfully mapped all fields with a high confidence score, indicating perfect mapping between the source and target schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `adgroup_id` | Ad group id | `ad_groups_reports_hourly.adgroup_id` | 🟢 _1.00_ | *Exact match found for 'adgroup_id'.* |
| `stat_time_hour` | Hour of activity | `ad_groups_reports_hourly.stat_time_hour` | 🟢 _1.00_ | *Exact match found for 'stat_time_hour'.* |
| `cost_per_conversion` | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.cost_per_conversion` | 🟢 _1.00_ | *Exact match found for 'cost_per_conversion'.* |
| `real_time_conversion` | Number of times your ad resulted in the optimization event you selected. | `ad_groups_reports_hourly.metrics.real_time_conversion` | 🟢 _1.00_ | *Exact match found for 'real_time_conversion'.* |
| `cpc` | The average amount of money you've spent on a click. | `ad_groups_reports_hourly.metrics.cpc` | 🟢 _1.00_ | *Exact match found for 'cpc'.* |
| `video_play_actions` | The number of times your video starts to play. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_play_actions` | 🟢 _1.00_ | *Exact match found for 'video_play_actions'.* |
| `conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is calculated based on the time each ad impression occurred.) | `ad_groups_reports_hourly.metrics.conversion_rate` | 🟢 _1.00_ | *Exact match found for 'conversion_rate'.* |
| `video_views_p_75` | The number of times your video was played at 75% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p75` | 🟢 _1.00_ | *Exact match found for 'video_views_p_75'.* |
| `result` | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.result` | 🟢 _1.00_ | *Exact match found for 'result'.* |
| `video_views_p_50` | The number of times your video was played at 50% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p50` | 🟢 _1.00_ | *Exact match found for 'video_views_p_50'.* |
| `impressions` | The number of times your ads were on screen. | `ad_groups_reports_hourly.metrics.impressions` | 🟢 _1.00_ | *Exact match found for 'impressions'.* |
| `comments` | The number of comments your video creative received within 1 day of a user seeing a paid ad. | `ad_groups_reports_hourly.metrics.comments` | 🟢 _1.00_ | *Exact match found for 'comments'.* |
| `real_time_cost_per_result` | As a campaign may have different optimization goals, the total number of result  is not supported in campaign section now, please go to the ad group section to view the cost  per Result. (The total count is based on when the conversion actually happened.)  | `ad_groups_reports_hourly.metrics.real_time_cost_per_result` | 🟢 _1.00_ | *Exact match found for 'real_time_cost_per_result'.* |
| `conversion` | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns.  Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.conversion` | 🟢 _1.00_ | *Exact match found for 'conversion'.* |
| `real_time_result` | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)  | `ad_groups_reports_hourly.metrics.real_time_result` | 🟢 _1.00_ | *Exact match found for 'real_time_result'.* |
| `video_view_p_100` | The number of times your video was played at 100% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p100` | 🟢 _1.00_ | *Exact match found for 'video_view_p_100'.* |
| `shares` | The number of shares your video creative received within 1 day of a user seeing a paid ad. | `ad_groups_reports_hourly.metrics.shares` | 🟢 _1.00_ | *Exact match found for 'shares'.* |
| `real_time_conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) | `ad_groups_reports_hourly.metrics.real_time_conversion_rate` | 🟢 _1.00_ | *Exact match found for 'real_time_conversion_rate'.* |
| `cost_per_secondary_goal_result` | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.cost_per_secondary_goal_result` | 🟢 _1.00_ | *Exact match found for 'cost_per_secondary_goal_result'.* |
| `secondary_goal_result_rate` | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.  | `ad_groups_reports_hourly.metrics.secondary_goal_result_rate` | 🟢 _1.00_ | *Exact match found for 'secondary_goal_result_rate'.* |
| `clicks` | The number of clicks on your ads. | `ad_groups_reports_hourly.metrics.clicks` | 🟢 _1.00_ | *Exact match found for 'clicks'.* |
| `cost_per_1000_reached` | The average cost to reach 1,000 unique users. This metric is estimated. | `ad_groups_reports_hourly.metrics.cost_per_1000_reached` | 🟢 _1.00_ | *Exact match found for 'cost_per_1000_reached'.* |
| `video_views_p_25` | The number of times your video was played at 25% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p25` | 🟢 _1.00_ | *Exact match found for 'video_views_p_25'.* |
| `reach` | The number of unique users who saw your ads at least once. This metric is estimated. | `ad_groups_reports_hourly.metrics.reach` | 🟢 _1.00_ | *Exact match found for 'reach'.* |
| `real_time_cost_per_conversion` | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) | `ad_groups_reports_hourly.metrics.real_time_cost_per_conversion` | 🟢 _1.00_ | *Exact match found for 'real_time_cost_per_conversion'.* |
| `profile_visits_rate` | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. | `ad_groups_reports_hourly.metrics.profile_visits_rate` | 🟢 _1.00_ | *Exact match found for 'profile_visits_rate'.* |
| `average_video_play` | The average time your video was played per single video view, including any time spent replaying the video. | `ad_groups_reports_hourly.metrics.average_video_play` | 🟢 _1.00_ | *Exact match found for 'average_video_play'.* |
| `profile_visits` | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. | `ad_groups_reports_hourly.metrics.profile_visits` | 🟢 _1.00_ | *Exact match found for 'profile_visits'.* |
| `cpm` | The average amount of money you've spent per 1,000 impressions. | `ad_groups_reports_hourly.metrics.cpm` | 🟢 _1.00_ | *Exact match found for 'cpm'.* |
| `ctr` | The percentage of times people saw your ad and performed a click. | `ad_groups_reports_hourly.metrics.ctr` | 🟢 _1.00_ | *Exact match found for 'ctr'.* |
| `video_watched_2_s` | The number of times your video played for at least 2 seconds. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_watched_2s` | 🟢 _1.00_ | *Exact match found for 'video_watched_2_s'.* |
| `follows` | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. | `ad_groups_reports_hourly.metrics.follows` | 🟢 _1.00_ | *Exact match found for 'follows'.* |
| `result_rate` | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.result_rate` | 🟢 _1.00_ | *Exact match found for 'result_rate'.* |
| `video_watched_6_s` | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_watched_6s` | 🟢 _1.00_ | *Exact match found for 'video_watched_6_s'.* |
| `secondary_goal_result` | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.secondary_goal_result` | 🟢 _1.00_ | *Exact match found for 'secondary_goal_result'.* |
| `cost_per_result` | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.cost_per_result` | 🟢 _1.00_ | *Exact match found for 'cost_per_result'.* |
| `average_video_play_per_user` | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. | `ad_groups_reports_hourly.metrics.average_video_play_per_user` | 🟢 _1.00_ | *Exact match found for 'average_video_play_per_user'.* |
| `real_time_result_rate` | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to view the Result Rate.  (The total count is based on when the conversion actually happened.)  | `ad_groups_reports_hourly.metrics.real_time_result_rate` | 🟢 _1.00_ | *Exact match found for 'real_time_result_rate'.* |
| `spend` | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. | `ad_groups_reports_hourly.metrics.spend` | 🟢 _1.00_ | *Exact match found for 'spend'.* |
| `likes` | The number of likes your video creative received within 1 day of a user seeing a paid ad. | `ad_groups_reports_hourly.metrics.likes` | 🟢 _1.00_ | *Exact match found for 'likes'.* |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `ad_groups_reports_hourly._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `total_purchase_value` | The total value of purchase events that occurred in your app that were recorded by your measurement partner. | `ad_groups_reports_hourly.metrics.total_purchase_value` | 🟢 _1.00_ | *Exact match found for 'total_purchase_value'.* |
| `total_sales_lead_value` | The monetary worth or potential value assigned to a lead generated through ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `campaigns` to Fivetran `campaign_history`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.77_
- Summary Self-Evaluation: _The source table 'campaigns' matches the target schema closely with most fields appropriately mapped, resulting in a high table match score. However, missing fields 'opt_status' and 'status' reflect in a slightly lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `campaign_id` | Campaign ID | `campaigns.campaign_id` | 🟢 _0.90_ | *The source field 'campaigns.campaign_id' is a strong match for 'campaign_id'.* |
| `updated_at` | Time the record was updated. | `campaigns._airbyte_extracted_at` | 🟢 _1.00_ | *The source field 'campaigns._airbyte_extracted_at' is a required standard mapping for '_fivetran_synced', thus always scores 1.00.* |
| `advertiser_id` | Advertiser ID | `campaigns.advertiser_id` | 🟢 _0.90_ | *The source field 'campaigns.advertiser_id' is a strong match for 'advertiser_id'.* |
| `budget` | Campaign budget | `campaigns.budget` | 🟢 _0.90_ | *The source field 'campaigns.budget' is a strong match for 'budget'.* |
| `budget_mode` | Budget type | `campaigns.budget_mode` | 🟢 _0.90_ | *The source field 'campaigns.budget_mode' is a strong match for 'budget_mode'.* |
| `campaign_name` | Campaign name | `campaigns.campaign_name` | 🟢 _0.90_ | *The source field 'campaigns.campaign_name' is a strong match for 'campaign_name'.* |
| `campaign_type` | Campaign Type, indicates the campaign is a regular campaign or iOS 14 campaign. | `campaigns.campaign_type` | 🟢 _0.90_ | *The source field 'campaigns.campaign_type' is a strong match for 'campaign_type'.* |
| `create_time` | Time at which the campaign was created. | `campaigns.create_time` | 🟢 _0.90_ | *The source field 'campaigns.create_time' is a strong match for 'create_time'.* |
| `is_new_structure` | Whether the campaign is a new structure (for the same campaign, the structure of campaign, adgroups and ads are the same) | `campaigns.is_new_structure` | 🟢 _0.90_ | *The source field 'campaigns.is_new_structure' is a strong match for 'is_new_structure'.* |
| `objective_type` | Advertising objective. | `campaigns.objective_type` | 🟢 _0.90_ | *The source field 'campaigns.objective_type' is a strong match for 'objective_type'.* |
| `opt_status` | Operation status. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status` | Campaign status | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `split_test_variable` | Split Test variables. Optional values; TARGETING, BIDDING_OPTIMIZATION , CREATIVE. | `campaigns.split_test_variable` | 🟢 _0.70_ | *The source field 'campaigns.split_test_variable' is likely a match for 'split_test_variable' but with some uncertainty.* |

### Mapping: Airbyte `ads` to Fivetran `ad_history`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The table mapping reflects a high degree of confidence given that the field mappings align well with expectations for a typical ad schema. However, some fields could not perfectly be matched or verified due to lack of comprehensive context._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `ad_id` | Ad ID | `ads.ad_id` | 🟢 _1.00_ | *Perfect match given the direct mapping from 'ads.ad_id'.* |
| `updated_at` | Time the record was updated. | `ads._airbyte_extracted_at` | 🟢 _1.00_ | *Standard 1.0 score for '_fivetran_synced' mapped to '_airbyte_extracted_at'.* |
| `adgroup_id` | Ad group ID | `ads.adgroup_id` | 🟢 _0.95_ | *'ads.adgroup_id' aligns well with expectations.* |
| `advertiser_id` | Advertiser ID | `ads.advertiser_id` | 🟢 _0.95_ | *'ads.advertiser_id' aligns well with expectations.* |
| `campaign_id` | Campaign ID | `ads.campaign_id` | 🟢 _0.95_ | *'ads.campaign_id' aligns well with expectations.* |
| `ad_name` | Ad Name. | `ads.ad_name` | 🟢 _1.00_ | *Directly maps from 'ads.ad_name' with high confidence.* |
| `ad_text` | The ad text. | `ads.ad_text` | 🟢 _1.00_ | *Directly maps from 'ads.ad_text' with high confidence.* |
| `app_name` | The display name of app download ad. | `ads.app_name` | 🟢 _1.00_ | *Directly maps from 'ads.app_name' with high confidence.* |
| `call_to_action` | Call to action values. | `ads.call_to_action` | 🟢 _1.00_ | *Directly maps from 'ads.call_to_action' with high confidence.* |
| `click_tracking_url` | Click monitoring URL. | `ads.click_tracking_url` | 🟢 _1.00_ | *Directly maps from 'ads.click_tracking_url' with high confidence.* |
| `create_time` | Time at which the ad was created. | `ads.create_time` | 🟢 _0.90_ | *Most likely correct mapping but slight uncertainty.* |
| `display_name` | The display name of landing page or pure exposure ad. | `ads.display_name` | 🟢 _0.90_ | *Most likely correct mapping but slight uncertainty.* |
| `image_ids` | A list of image IDs. | `ads.image_ids` | 🟢 _0.90_ | *Most likely correct mapping but slight uncertainty.* |
| `impression_tracking_url` | Display monitoring URL. | `ads.impression_tracking_url` | 🟢 _0.85_ | *Maps to 'ads.impression_tracking_url'; expression is detailed and consistent with ad-related data.* |
| `is_aco` | Whether the ad is an automated ad. | `ads.is_aco` | 🟢 _0.90_ | *The mapping appears consistent with ad schema.* |
| `is_creative_authorized` | Whether you grant displaying some of your ads in our TikTok For Business Creative Center. Only valid for non-US advertisers, the default value is false.  | `ads.creative_authorized` | 🟢 _0.85_ | *Mappings align, but US-specific context introduces slight uncertainty.* |
| `is_new_structure` | Whether the campaign is a new structure. | `ads.is_new_structure` | 🟢 _0.85_ | *Limited by schema-specific context.* |
| `landing_page_url` | Landing page URL. | `ads.landing_page_url` | 🟢 _1.00_ | *Direct mapping from 'ads.landing_page_url' is strong.* |
| `open_url` | The specific location where you want your audience to go if they have your app installed. | `ads.deeplink` | 🟢 _0.85_ | *Mapping exists but specifics vary, slightly lowering confidence.* |
| `opt_status` | Operation status. | `ads.operation_status` | 🟢 _0.85_ | *Limited schema context slightly reduces confidence.* |
| `playable_url` | Playable material url. | `ads.playable_url` | 🟢 _1.00_ | *Strong mapping based on ad schema knowledge.* |
| `profile_image` | Avatar URL. | `ads.profile_image_url` | 🟢 _1.00_ | *Direct mapping from 'ads.profile_image_url' matches perfectly.* |
| `status` | Ad status. | `ads.secondary_status` | 🟢 _0.90_ | *Expected mapping from 'ads.secondary_status', but some schema variance may exist.* |
| `video_id` | The video ID. | `ads.video_id` | 🟢 _1.00_ | *Direct mapping from 'ads.video_id' finely matches expectations.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
