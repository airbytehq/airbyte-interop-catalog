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

> [!Tip]
> Use the right-hand navigation to quickly browse available dataset mappings.

> [!Warning]
> AI-generated results may contain errors. Please sanity check results and adapt these resources to your needs accordingly.

### Mapping: Airbyte `campaigns` to Fivetran `campaign_history`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table matching has a high confidence as both source and target implementations seem to describe similar campaigns data, with slight variations in field serialization. Most fields are well-aligned with clear matching expressions, contributing to a high table match score. The completion score is slightly lower due to a few fields with no exact matches but are generally paired within acceptable thresholds._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of the campaign. | `campaigns.id` | 🟢 _0.95_ | *Direct mapping with identical field naming and context.* |
| `account_id` | The ID of the ad account that this campaign belongs to. | `campaigns.account_id` | 🟢 _0.90_ | *Direct mapping, slight variation in naming but same contextual use.* |
| `name` | The name of the campaign. | `campaigns.name` | 🟢 _0.90_ | *Direct mapping with identical usage and description.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `campaigns._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for system fields, perfectly aligns with '_airbyte_extracted_at'.* |
| `updated_time` | {{ doc('updated_time') }} | `campaigns.updated_time` | 🟢 _0.70_ | *Matches in naming and serves same purpose, but minor differences might exist in how timestamps are handled between systems.* |
| `created_time` | The time the campaign was created. | `campaigns.created_time` | 🟢 _0.90_ | *Direct mapping of timestamp fields showing creation times.* |
| `start_time` | Timestamp of designated campaign start time. | `campaigns.start_time` | 🟢 _0.90_ | *Direct mapping of timestamp fields for campaign start times.* |
| `stop_time` | Timestamp of designated campaign end time. | `campaigns.stop_time` | 🟢 _0.90_ | *Direct mapping of timestamp fields for campaign end times.* |
| `daily_budget` | Daily budget of campaign. | `campaigns.daily_budget` | 🟢 _0.90_ | *Direct mapping, represents the same financial aspect of campaigns.* |
| `budget_remaining` | Remaining budget of campaign. | `campaigns.budget_remaining` | 🟢 _0.90_ | *Direct mapping, closely related financial contexts.* |
| `lifetime_budget` | Lifetime budget of the campaign. | `campaigns.lifetime_budget` | 🟢 _0.90_ | *Direct mapping, operations on financial elements of campaigns are similar.* |
| `status` | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | `campaigns.status` | 🟢 _0.70_ | *Direct naming and context match, slight variation in possible status values but sufficiently similar for high confidence mapping.* |

### Mapping: Airbyte `ads_insights` to Fivetran `basic_ad`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _All mappings are highly accurate and aligned well with the required schema. The source and target schemas describe the same subject matter almost perfectly._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `ad_id` | The ID of the ad the report relates to. | `ads_insights.ad_id` | 🟢 _1.00_ | *Direct match found.* |
| `ad_name` | Name of the ad the report relates to. | `ads_insights.ad_name` | 🟢 _1.00_ | *Direct match found.* |
| `adset_name` | Name of the ad set the report relates to. | `ads_insights.adset_name` | 🟢 _1.00_ | *Direct match found.* |
| `date` | The date of the reported performance. | `ads_insights.date_stop` | 🟢 _1.00_ | *Direct match found for 'date_stop'.* |
| `account_id` | The ID of the ad account that this ad belongs to. | `ads_insights.account_id` | 🟢 _1.00_ | *Direct match found.* |
| `impressions` | The number of impressions the ad had on the given day. | `ads_insights.impressions` | 🟢 _1.00_ | *Direct match found.* |
| `inline_link_clicks` | The number of clicks the ad had on the given day. | `ads_insights.inline_link_clicks` | 🟢 _1.00_ | *Direct match found.* |
| `spend` | The spend on the ad in the given day. | `ads_insights.spend` | 🟢 _1.00_ | *Direct match found.* |
| `reach` | The number of people who saw any content from your Page or about your Page. This metric is estimated. | `ads_insights.reach` | 🟢 _1.00_ | *Direct match found.* |
| `frequency` | The average number of times each person saw your ad; it is calculated as impressions divided by reach. | `ads_insights.frequency` | 🟢 _1.00_ | *Direct match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ads_insights._airbyte_extracted_at` | 🟢 _1.00_ | *Standard transformation matched directly to '_airbyte_extracted_at'.* |

### Mapping: Airbyte `ad_sets` to Fivetran `ad_set_history`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table mapping has a high degree of confidence due to well-matched fields, although some fields required moderate adjustments and assumptions to align with the target schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of the ad set. | `ad_sets.id` | 🟢 _1.00_ | *Direct match found.* |
| `account_id` | The ID of the ad account that this ad set belongs to. | `ad_sets.account_id` | 🟢 _1.00_ | *Direct match found.* |
| `campaign_id` | Ad campaign that contains this ad set. | `ad_sets.campaign_id` | 🟢 _1.00_ | *Direct match found.* |
| `name` | The name of the ad set. | `ad_sets.name` | 🟢 _1.00_ | *Direct match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ad_sets._airbyte_extracted_at` | 🟢 _1.00_ | *Standardized mapping for system timestamps.* |
| `updated_time` | {{ doc('updated_time') }} | `ad_sets.updated_time` | 🟢 _1.00_ | *Direct match found.* |
| `start_time` | Timestamp of designated ad set start time. | `ad_sets.start_time` | 🟢 _0.70_ | *Sufficient contextual evidence supports this mapping.* |
| `end_time` | Timestamp of designated ad set end time. | `ad_sets.end_time` | 🟢 _0.70_ | *Sufficient contextual evidence supports this mapping.* |
| `bid_strategy` | Bid strategy values are - 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', 'LOWEST_COST_WITH_MIN_ROAS'. | `ad_sets.bid_strategy` | 🟢 _0.70_ | *Terms are closely related, scored cautiously given potential semantic differences.* |
| `daily_budget` | Daily budget of ad set. | `ad_sets.daily_budget` | 🟢 _1.00_ | *Direct match found.* |
| `budget_remaining` | Remaining budget of ad set. | `ad_sets.budget_remaining` | 🟢 _1.00_ | *Direct match found.* |
| `status` | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | `ad_sets.effective_status` | 🟢 _1.00_ | *Direct match found.* |
| `optimization_goal` | The optimization goal this ad set is using. Possible values defined [here](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/#fields). | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `ad_account` to Fivetran `account_history`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table match is highly confident, indicating a strong correlation between source and target tables. The field mappings are mostly complete with only minor exceptions._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of the ad account. | `ad_account.id` | 🟢 _0.95_ | *The field directly corresponds to the source's ad_account.id.* |
| `name` | Name of the account. | `ad_account.name` | 🟢 _0.95_ | *The field directly corresponds to the source's ad_account.name.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ad_account._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to the source stream's _airbyte_extracted_at.* |
| `account_status` | Current status of account. | `ad_account.account_status` | 🟢 _0.90_ | *Account status fields match directly.* |
| `business_country_code` | Country code of business associated to account. | `ad_account.business_country_code` | 🟢 _0.90_ | *Direct match for country code.* |
| `created_time` | The time account was created. | `ad_account.created_time` | 🟢 _0.90_ | *The field directly matches the timestamp of the account creation in the source.* |
| `currency` | Currency associated with account. | `ad_account.currency` | 🟢 _0.90_ | *Direct match to the account's currency in the source.* |
| `timezone_name` | Timezone associated with account. | `ad_account.timezone_name` | 🟢 _0.90_ | *Direct match to the source's timezone information.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
