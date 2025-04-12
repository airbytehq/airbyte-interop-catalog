# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `ad_groups` to Fivetran `adgroup_history`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table match score is high due to strong alignment between the source and target schemas from similar APIs. However, completion is limited by several 'MISSING' fields that indicate fields present in target schema do not have corresponding entries in the source schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `adgroup_id` | Ad group ID | `ad_groups.adgroup_id` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `updated_at` | Time the record was updated. | `ad_groups.modify_time` | 🟢 _0.70_ | *Likely the correct match based on context and typical usage, but not perfect due to possible alternate interpretations.* |
| `advertiser_id` | Advertiser ID | `ad_groups.advertiser_id` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `campaign_id` | The Ad group's campaign ID. | `ad_groups.campaign_id` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `action_categories` | IDs of the action categories (behaviors) that you want to target. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `action_days` | The number of days of the time period to include action from. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `adgroup_name` | Ad group name. Character limit is 512 and cannot contain emoji. | `ad_groups.adgroup_name` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `age_groups` | Age groups you want to target. This is the newest version of the field `age`, which was renamed after the Tiktok Ads v1.3 API release.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `android_osv` | Minimum Android version. | `ad_groups.min_android_version` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `app_download_url` | App download link | `ad_groups.app_download_url` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `app_id` | The Application id of the promoted app | `ad_groups.app_id` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `app_name` | App name. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `app_type` | App type. | `ad_groups.app_type` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `audience` | A list of audience IDs. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `audience_type` | Audience Type | `ad_groups.audience_type` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `bid` | CPC, CPM bidding, oCPM learning bidding | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `bid_type` | Bidding Strategy | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_event` | Bid method. | `ad_groups.billing_event` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `budget` | Ad budget. Returns 0.0 when Campaign Budget Optimization (budget_optimize_switch) is on. | `ad_groups.budget` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `budget_mode` | Budget mode. This field will be ignored when Campaign Budget Optimization (budget_optimize_switch) is enabled. | `ad_groups.budget_mode` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `carriers` | Carriers that you want to target. | `ad_groups.carriers` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `category` | Ad group category. | `ad_groups.category_id` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `click_tracking_url` | Click monitoring URL. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `connection_type` | Device connection types that you want to target. Default; unlimited. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `conversion_bid` | oCPM conversion bid | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cpv_video_duration` | Video playback duration, required if optimize_goal is VIDEO_VIEW.  Allowed values; SIX_SECONDS (video playback 6s), TWO_SECONDS (video playback 2s)  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `creative_material_mode` | Creative delivery mode. | `ad_groups.creative_material_mode` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `dayparting` | Ad delivery period, the default is always and the format is 48 * 7 character string, represented by 0 or 1. > That is, with half an hour as the minimum granularity, a day (24 hours) is divided by the minimum granularity(30 mins) from Monday to Sunday. Resulting in a 48*7 format.0 represents not to be delivered, 1 represents delivery. no transmission, full transmission 0, full transmission 1 all represent full time delivery | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deep_bid_type` | Bidding strategy for in-app events. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deep_cpabid` | Deep bid | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deep_external_action` | Deep conversion event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `display_name` | Display name of ad group. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `enable_inventory_filter` | Inventory filtering (Unsafe videos will not be displayed). | `ad_groups.inventory_filter_enabled` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `excluded_audience` | A list of audience ID to be excluded. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_action` | Conversion event for the ad group. It is required when the promoted object is an app with tracking urls, or when pixel_id is specified. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `fallback_type` | Fallback Type. If the audience do not have the app installed, you can have them fall back to install the app, or to view a specific web page. Not applicable for Deferred Deeplink. Allowed values; APP_INSTALL, WEBSITE, UNSET. If website is chosen, you need to specify the url via landing_page_url field.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `frequency` | frequency, together with frequency_schedule, controls how often people see your ad (only available for REACH ads).  For example, frequency = 2 frequency_schedule = 3 means "show ads no more than twice every 3 day".  | `ad_groups.frequency` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `frequency_schedule` | frequency, together with frequency, controls how often people see your ad (only available for REACH ads). | `ad_groups.frequency_schedule` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `gender` | Gender that you want to target. | `ad_groups.gender` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `impression_tracking_url` | Display monitoring URL. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `interest_category_v2` | Interest classification. If the interest is specified, users that do not meet interest target will be excluded during delivery. | `ad_groups.interest_category_ids` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `ios_osv` | Minimum iOS version. | `ad_groups.min_ios_version` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `is_comment_disable` | Whether to allow comments on your ads on TikTok, Vigo, Helo. | `ad_groups.comment_disabled` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `is_hfss` | Whether the promoted content is HFSS foods (foods that are high in fat, salt, or sugar). | `ad_groups.is_hfss` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `is_new_structure` | Whether the campaign is a new structure. | `ad_groups.is_new_structure` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `keywords` | Keywords used. | `ad_groups.keywords` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `landing_page_url` | Landing page URL. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `languages` | Codes of the languages that you want to target. | `ad_groups.languages` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `location` | IDs of the locations that you want to target. | `ad_groups.location_ids` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `open_url` | The specific location where you want your audience to go if they have your app installed. | `ad_groups.promotion_website_type` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `open_url_type` | The open URL type. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `operation_system` | Device operating systems that you want to target. | `ad_groups.operating_systems` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `opt_status` | Operation status. | `ad_groups.operation_status` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `optimize_goal` | Optimization goal. | `ad_groups.optimization_goal` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `pacing` | You can choose between PACING_MODE_SMOOTH and PACING_MODE_FAST. For PACING_MODE_SMOOTH, the budget is allocated evenly within the scheduled time.  PACING_MODE_FAST would consume budget and produce results as soon as possible.   | `ad_groups.pacing` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `package` | Package name. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `pangle_block_app_list_id` | Pangle app block list ID. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `pixel_id` | Pixel ID. Only application for landing pages. | `ad_groups.pixel_id` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `placement` | The apps where you want to deliver your ads. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `placement_type` | Placement type. | `ad_groups.placement_type` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `profile_image` | Avatar URL. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `schedule_end_time` | Ad delivery end time (UTC+0). Format should be YYYY-MM-DD HH:MM:SS | `ad_groups.schedule_end_time` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `schedule_start_time` | Ad delivery start time (UTC+0). Format should be YYYY-MM-DD HH:MM:SS | `ad_groups.schedule_start_time` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `schedule_type` | The schedule type, which can be either SCHEDULE_START_END or SCHEDULE_FROM_NOW. | `ad_groups.schedule_type` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `skip_learning_phase` | Whether to skip the learning stage. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `statistic_type` | conversion bid statistic type | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status` | Ad group status | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `video_actions` | Number of video actions. | `ad_groups.video_actions` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
| `video_download` | Whether users can download your video ads on TikTok(cannot be updated once created). | `ad_groups.video_download_disabled` | 🟢 _1.00_ | *Perfect match based on field name and context.* |
