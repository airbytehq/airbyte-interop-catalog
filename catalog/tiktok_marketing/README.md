# Mapping Guide: Airbyte-to-Fivetran

The below guide will help you map Airbyte schemas to corresponding Fivetran schemas. Guidance is AI-generated and includes confidence scores (with explanation) for each table and field mapping.

## Companion Project for `dbt` Users

Please see the companion [airbyte-interop-dbt-project](./airbyte-interop-dbt-project) directory, which contains a `dbt` project with ready-to-use SQL models for each of the below mappings.

## Table-Level Mappings

### How to Use these Mappings

The below guides, and the companion dbt project, will help you shape your new Airbyte datasets to more closely match your legacy Fivetran dataset schemas.

This can be helpful if:

1. You have existing code that relies on Fivetran-shaped datasets.
2. You have one or more dependencies on Fivetran-managed dbt packages.
3. You have custom code that needs to be updated to leverage Airbyte data schemas, where you previously ingested Fivetran-shaped datasets.

In any of these cases, you can use the below mapping logic to shape your new data to fit old data schema requirements and **save time** in your migration.

> ![Tip]
> Use the right-hand navigation to quickly browse available dataset mappings.

> ![Warning]
> AI-generated results may contain errors. Please sanity check results and adapt these resources to your needs accordingly.


### Mapping: Airbyte `campaigns` to Fivetran `campaign_history`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping score is high indicating a good correspondence between source and target schema fields. The completion score is also high, showing most fields have been successfully mapped with high confidence._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `campaign_id` | Campaign ID | `campaigns.campaign_id` | 🟢 _1.00_ | *Exact match on field name and context.* |
| `updated_at` | Time the record was updated. | `campaigns.modify_time` | 🟢 _0.95_ | *Close match, slight difference in time descriptors but same context.* |
| `advertiser_id` | Advertiser ID | `campaigns.advertiser_id` | 🟢 _1.00_ | *Exact match on field name and context.* |
| `budget` | Campaign budget | `campaigns.budget` | 🟢 _1.00_ | *Exact match on field name and context.* |
| `budget_mode` | Budget type | `campaigns.budget_mode` | 🟢 _0.90_ | *Slight terminological difference but same concept.* |
| `campaign_name` | Campaign name | `campaigns.campaign_name` | 🟢 _1.00_ | *Exact match on field name and context.* |
| `campaign_type` | Campaign Type, indicates the campaign is a regular campaign or iOS 14 campaign. | `campaigns.campaign_type` | 🟢 _0.80_ | *Terminological nuances between regular and iOS 14 campaign considered.* |
| `create_time` | Time at which the campaign was created. | `campaigns.create_time` | 🟢 _0.95_ | *Close match, slight difference in time descriptors but same context.* |
| `is_new_structure` | Whether the campaign is a new structure (for the same campaign, the structure of campaign, adgroups and ads are the same) | `campaigns.is_new_structure` | 🟢 _1.00_ | *Exact match on field name and context.* |
| `objective_type` | Advertising objective. | `campaigns.objective_type` | 🟢 _0.90_ | *Slight terminological difference but same objective.* |
| `opt_status` | Operation status. | `campaigns.operation_status` | 🟢 _0.80_ | *Close match but slight differences in status terminology.* |
| `status` | Campaign status | `campaigns.secondary_status` | 🟢 _0.70_ | *Generic term with potential overlaps in meaning is guarded.* |
| `split_test_variable` | Split Test variables. Optional values; TARGETING, BIDDING_OPTIMIZATION , CREATIVE. | `campaigns.split_test_variable` | 🟢 _0.75_ | *Contextual evidence supports similarity in testing variables despite different categorical terminology.* |

### Mapping: Airbyte `advertisers` to Fivetran `advertiser`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The overall table match is quite high, suggesting the source and target are closely related. The completion score reflects a majority of fields mapped, although some are missing or poorly matched_

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Advertiser ID | `advertisers.advertiser_id` | 🟢 _1.00_ | *Exact match on customer identifier* |
| `address` | Advertiser address information | `advertisers.address` | 🟢 _1.00_ | *Exact match on advertiser's address* |
| `balance` | Account available balance | `MISSING` | ❌ _0.00_ | *No good match found* |
| `cellphone_number` | Contact mobile number, desensitised data. This is the newest version of the field `phone_number`, which was renamed after the Tiktok Ads v1.3 API release.  | `advertisers.cellphone_number` | ⚠️ _0.60_ | *Since 'phone_number' was renamed in newer API versions, the match is plausible but not certain* |
| `company` | Advertiser's company name | `advertisers.company` | 🟢 _1.00_ | *Exact match on advertiser's company name* |
| `contacter` | Contact Person | `advertisers.contacter` | 🟢 _1.00_ | *Exact match on contact person* |
| `country` | The advertiser's country | `advertisers.country` | 🟢 _1.00_ | *Exact match on advertiser's country* |
| `create_time` | Advertiser's create time | `advertisers.create_time` | 🟢 _1.00_ | *Exact match on advertiser's create time* |
| `currency` | Type of currency used by advertisers | `advertisers.currency` | 🟢 _1.00_ | *Exact match on the type of currency used* |
| `description` | Brand description, i.e. promotional content | `advertisers.description` | 🟢 _1.00_ | *Exact match on brand description* |
| `email` | Advertiser contact email, desensitised data | `advertisers.email` | 🟢 _1.00_ | *Exact match on advertiser contact email* |
| `industry` | Advertiser industry category | `advertisers.industry` | 🟢 _1.00_ | *Exact match on advertiser industry category* |
| `language` | Language used by advertisers | `advertisers.language` | 🟢 _1.00_ | *Exact match on language used* |
| `license_no` | License number | `advertisers.license_no` | 🟢 _1.00_ | *Exact match on license number* |
| `license_url` | License preview address, the link is valid for an hour by default. | `advertisers.license_url` | 🟢 _1.00_ | *Exact match on license preview address* |
| `name` | Advertiser name | `advertisers.name` | 🟢 _1.00_ | *Exact match on advertiser name* |
| `phone_number` | Contact mobile number, desensitised data. IMPORTANT: This field will not be populated for connectors utilizing the Tiktok Ads v1.3 API version, as the column was renamed.  The new column name is `cellphone_number`.  | `MISSING` | ❌ _0.00_ | *No good match found as it is not used due to renamed field 'cellphone_number'* |
| `promotion_area` | Operation area | `advertisers.promotion_area` | 🟢 _1.00_ | *Exact match on operation area* |
| `reason` | Reason for rejection | `advertisers.rejection_reason` | 🟢 _1.00_ | *Exact match on reason for rejection* |
| `role` | Advertiser role | `advertisers.role` | 🟢 _1.00_ | *Exact match on advertiser role* |
| `status` | Advertiser status | `advertisers.status` | 🟢 _1.00_ | *Exact match on advertiser status* |
| `telephone` | Fixed phone number, desensitised data IMPORTANT: This field will not be populated for connectors utilizing the Tiktok Ads v1.3 API version, as the column was renamed.  The new column name is `telephone_number`.  | `advertisers.telephone_number` | ❌ _0.00_ | *No good match found as it is not used due to renamed field 'telephone_number'* |
| `telephone_number` | Fixed phone number, desensitised data This is the newest version of the field `telephone`, which was renamed after the Tiktok Ads v1.3 API release.  | `advertisers.telephone_number` | ⚠️ _0.60_ | *Due to renaming, this match is plausible but not certain* |
| `timezone` | Ad account time zone including GMT offset | `advertisers.timezone` | 🟢 _1.00_ | *Exact match on time zone* |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `advertisers._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping between '_fivetran_synced' and '_airbyte_extracted_at' matches perfectly.* |

### Mapping: Airbyte `ad_groups_reports_hourly` to Fivetran `adgroup_report_hourly`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _High level of conformity between source and target fields. Given that most fields match structurally, adjustments for a few fields with divergences are recommended to enhance mutual interoperability._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `adgroup_id` | Ad group id | `ad_groups_reports_hourly.adgroup_id` | 🟢 _1.00_ | *Exact match on primary key field mapping.* |
| `stat_time_hour` | Hour of activity | `ad_groups_reports_hourly.stat_time_hour` | 🟢 _1.00_ | *Mapped directly with time field.* |
| `cost_per_conversion` | The average amount of money you've spent on a conversion.  (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.cost_per_conversion` | 🟢 _1.00_ | *Exact match found.* |
| `real_time_conversion` | Number of times your ad resulted in the optimization event you selected. | `ad_groups_reports_hourly.metrics.real_time_conversion` | 🟢 _1.00_ | *Mapped directly to its reporting metric field.* |
| `cpc` | The average amount of money you've spent on a click. | `ad_groups_reports_hourly.metrics.cpc` | 🟢 _1.00_ | *Cost per click aligns exactly with recorded metric field.* |
| `video_play_actions` | The number of times your video starts to play. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_play_actions` | 🟢 _1.00_ | *Metric matches directly with the target field.* |
| `conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is calculated based on the time each ad impression occurred.) | `ad_groups_reports_hourly.metrics.conversion_rate` | 🟢 _1.00_ | *Conversion rate field matched appropriately.* |
| `video_views_p_75` | The number of times your video was played at 75% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p75` | 🟢 _1.00_ | *Video play to 75% matches directly.* |
| `result` | The number of times your ad achieved an outcome, based on the optimization goal  you selected. As one campaign may have a number of different optimization goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view the results.  (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.result` | 🟢 _1.00_ | *Result outcomes match effectively with the target ad performance metric.* |
| `video_views_p_50` | The number of times your video was played at 50% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p50` | 🟢 _1.00_ | *Direct match found for video playback to 50% of its length.* |
| `impressions` | The number of times your ads were on screen. | `ad_groups_reports_hourly.metrics.impressions` | 🟢 _1.00_ | *Mapped directly with the impressions metric field.* |
| `comments` | The number of comments your video creative received within 1 day of a user seeing a paid ad. | `ad_groups_reports_hourly.metrics.comments` | 🟢 _1.00_ | *Directly mapped to comments received metric.* |
| `real_time_cost_per_result` | As a campaign may have different optimization goals, the total number of result  is not supported in campaign section now, please go to the ad group section to view the cost  per Result. (The total count is based on when the conversion actually happened.)  | `ad_groups_reports_hourly.metrics.real_time_cost_per_result` | 🟢 _1.00_ | *Appropriate mapping to metric that represents real-time ad spend per result achieved.* |
| `conversion` | The number of times your ad achieved an outcome, based on the secondary goal you selected.  As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns.  Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.conversion` | 🟢 _0.95_ | *High probability match for secondary goal outcomes in ads.* |
| `real_time_result` | The number of times your ad achieved an outcome, based on the optimization goal you selected.  As a campaign may have different optimization goals, the total number of result is not supported in campaign section now , Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.)  | `ad_groups_reports_hourly.metrics.real_time_result` | 🟢 _1.00_ | *Direct match to the real-time results metric.* |
| `video_view_p_100` | The number of times your video was played at 100% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p100` | 🟢 _1.00_ | *Matches exactly for video plays to 100%.* |
| `shares` | The number of shares your video creative received within 1 day of a user seeing a paid ad. | `ad_groups_reports_hourly.metrics.shares` | 🟢 _1.00_ | *Shares metric maps directly.* |
| `real_time_conversion_rate` | The percentage of results you received out of all the clicks of your ads. (The total count is based on when the conversion actually happened.) | `ad_groups_reports_hourly.metrics.real_time_conversion_rate` | 🟢 _1.00_ | *Mapped directly to real-time performance metric.* |
| `cost_per_secondary_goal_result` | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals,  this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.cost_per_secondary_goal_result` | 🟢 _0.90_ | *High probability match to secondary goal result cost.* |
| `secondary_goal_result_rate` | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. The total count is calculated based on the time each ad impression occurred.  | `ad_groups_reports_hourly.metrics.secondary_goal_result_rate` | 🟢 _1.00_ | *Mapped appropriately to secondary goal result rate.* |
| `clicks` | The number of clicks on your ads. | `ad_groups_reports_hourly.metrics.clicks` | 🟢 _1.00_ | *Clicks metric linked directly.* |
| `cost_per_1000_reached` | The average cost to reach 1,000 unique users. This metric is estimated. | `ad_groups_reports_hourly.metrics.cost_per_1000_reached` | 🟢 _1.00_ | *Mapped appropriately for cost estimates per 1,000 reached.* |
| `video_views_p_25` | The number of times your video was played at 25% of its length. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_views_p25` | 🟢 _1.00_ | *Direct match found for 25% video play.* |
| `reach` | The number of unique users who saw your ads at least once. This metric is estimated. | `ad_groups_reports_hourly.metrics.reach` | 🟢 _1.00_ | *Mapped directly to unique user reach metric.* |
| `real_time_cost_per_conversion` | The average amount of money you've spent on a conversion. (The total count is based on when the conversion actually happened.) | `ad_groups_reports_hourly.metrics.real_time_cost_per_conversion` | 🟢 _1.00_ | *Mapped appropriately to real-time ad spend on conversions.* |
| `profile_visits_rate` | The rate of profile visits per impression the paid ad drove during the campaign. This metric is only for Boosted TikToks. | `ad_groups_reports_hourly.metrics.profile_visits_rate` | 🟢 _1.00_ | *Profile visits per impression metric matches directly.* |
| `average_video_play` | The average time your video was played per single video view, including any time spent replaying the video. | `ad_groups_reports_hourly.metrics.average_video_play` | 🟢 _1.00_ | *Average play time per video view mapped effectively.* |
| `profile_visits` | The number of profile visits the ad drove during the campaign. This metric is only for Boosted TikToks. | `ad_groups_reports_hourly.metrics.profile_visits` | 🟢 _1.00_ | *Matches directly with the profile visits driven metric.* |
| `cpm` | The average amount of money you've spent per 1,000 impressions. | `ad_groups_reports_hourly.metrics.cpm` | 🟢 _1.00_ | *Mapped to cost per thousand impressions with exact alignment.* |
| `ctr` | The percentage of times people saw your ad and performed a click. | `ad_groups_reports_hourly.metrics.ctr` | 🟢 _1.00_ | *Click-through rate mapped directly.* |
| `video_watched_2_s` | The number of times your video played for at least 2 seconds. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_watched_2s` | 🟢 _1.00_ | *Mapped to metric for minimum video watch duration of 2 seconds.* |
| `follows` | The number of new followers that were gained within 1 day of a user seeing a paid ad. This metric is only for Boosted TikToks. | `ad_groups_reports_hourly.metrics.follows` | 🟢 _1.00_ | *Mapped effectively to follows gained within a day of ad engagement.* |
| `result_rate` | The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number  of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate.  (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.result_rate` | 🟢 _1.00_ | *Result rate statistic aligned well.* |
| `video_watched_6_s` | The number of times your video played for at least 6 seconds, or completely played. Replays will not be counted. | `ad_groups_reports_hourly.metrics.video_watched_6s` | 🟢 _1.00_ | *Mapped to 6 seconds minimum play or until the end.* |
| `secondary_goal_result` | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number  of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. (The total count is  calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.secondary_goal_result` | 🟢 _0.80_ | *Mapped with high confidence to secondary goal outcome field.* |
| `cost_per_result` | The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic  is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.)  | `ad_groups_reports_hourly.metrics.cost_per_result` | 🟢 _1.00_ | *Directly mapped to cost per ad result metric.* |
| `average_video_play_per_user` | The average time your video was played per person, including any time spent replaying the video. This metric is estimated. | `ad_groups_reports_hourly.metrics.average_video_play_per_user` | 🟢 _1.00_ | *Mapped effectively to average play duration per user.* |
| `real_time_result_rate` | As a campaign may have different optimization goals, the total number of result is not supported in campaign section now ,Please go to the ad group section to view the Result Rate.  (The total count is based on when the conversion actually happened.)  | `ad_groups_reports_hourly.metrics.real_time_result_rate` | 🟢 _1.00_ | *Mapped directly to real-time result rate based on conversions.* |
| `spend` | The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. | `ad_groups_reports_hourly.metrics.spend` | 🟢 _1.00_ | *Mapped to approximate total campaign spend.* |
| `likes` | The number of likes your video creative received within 1 day of a user seeing a paid ad. | `ad_groups_reports_hourly.metrics.likes` | 🟢 _1.00_ | *Mapped to likes received from ad exposure.* |
| `_fivetran_synced` | Timestamp of when Fivetran synced a record. | `ad_groups_reports_hourly._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for table synchronization timestamps.* |
| `total_purchase_value` | The total value of purchase events that occurred in your app that were recorded by your measurement partner. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_sales_lead_value` | The monetary worth or potential value assigned to a lead generated through ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
