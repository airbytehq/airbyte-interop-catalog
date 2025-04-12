# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping: Airbyte `ad_account` to Fivetran `account_history`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping is strong with most fields mapped accurately from source to target. Standard mappings and casing differences align correctly. No significant mismatches found that would lower confidence._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of the ad account. | `ad_account.id` | 🟢 _0.95_ | *Source field 'ad_account.id' matches closely with expected target field 'id'.* |
| `name` | Name of the account. | `ad_account.name` | 🟢 _0.95_ | *Source field 'ad_account.name' matches closely with expected target field 'name'.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ad_account._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to 'ad_account._airbyte_extracted_at'.* |
| `account_status` | Current status of account. | `ad_account.account_status` | 🟢 _0.90_ | *The field 'ad_account.account_status' matches well with the target expectation of 'account_status'.* |
| `business_country_code` | Country code of business associated to account. | `ad_account.business_country_code` | 🟢 _0.90_ | *Field 'ad_account.business_country_code' has a high confidence mapping to 'business_country_code'.* |
| `created_time` | The time account was created. | `ad_account.created_time` | 🟢 _0.90_ | *Field 'ad_account.created_time' is expected to match the target 'created_time' well.* |
| `currency` | Currency associated with account. | `ad_account.currency` | 🟢 _0.90_ | *The field 'ad_account.currency' maps confidently to 'currency'.* |
| `timezone_name` | Timezone associated with account. | `ad_account.timezone_name` | 🟢 _0.90_ | *The source field 'ad_account.timezone_name' matches well with 'timezone_name'.* |

### Mapping: Airbyte `ad_sets` to Fivetran `ad_set_history`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table mapping evaluation indicates a moderate to high confidence in the table subject matching, primarily based on shared semantics derived from similar schemas in the source and target tables, both of which are generated from equivalent API endpoints. However, there are significant disparities in the field mappings, particularly with undefined fields marked as 'MISSING', which affects the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of the ad set. | `ad_sets.id` | 🟢 _0.95_ | *The 'id' field has a clear and direct match between source and target.* |
| `account_id` | The ID of the ad account that this ad set belongs to. | `ad_sets.account_id` | 🟢 _0.95_ | *The 'account_id' field is well matched, sharing common semantics between the source and target implementations.* |
| `campaign_id` | Ad campaign that contains this ad set. | `ad_sets.campaign_id` | 🟢 _0.95_ | *The 'campaign_id' field links directly to the same concept in both source and target schemas.* |
| `name` | The name of the ad set. | `ad_sets.name` | 🟢 _0.95_ | *The 'name' field matches perfectly, consistent across the source and target mappings.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ad_sets._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at', which is always given a score of 1.00.* |
| `updated_time` | {{ doc('updated_time') }} | `ad_sets.updated_time` | 🟢 _0.95_ | *The 'updated_time' field shows a strong match, representing the same data in the source and target.* |
| `start_time` | Timestamp of designated ad set start time. | `ad_sets.start_time` | 🟢 _0.95_ | *The 'start_time' field is matched accurately, denoting identical timestamps.* |
| `end_time` | Timestamp of designated ad set end time. | `ad_sets.end_time` | 🟢 _0.95_ | *The 'end_time' field mapping is confident, referring to the same entity in both schemas.* |
| `bid_strategy` | Bid strategy values are - 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', 'LOWEST_COST_WITH_MIN_ROAS'. | `ad_sets.bid_strategy` | 🟢 _0.95_ | *The 'bid_strategy' field matches well, reflecting identical bid configurations.* |
| `daily_budget` | Daily budget of ad set. | `ad_sets.daily_budget` | 🟢 _0.95_ | *The 'daily_budget' field is well matched with aligned semantics in both implementations.* |
| `budget_remaining` | Remaining budget of ad set. | `ad_sets.budget_remaining` | 🟢 _0.95_ | *The 'budget_remaining' field corresponds well to the remaining budget information in both schemas.* |
| `status` | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | `ad_sets.effective_status` | 🟢 _0.95_ | *The 'status' field shows high confidence due to consistent enumerated value definitions.* |
| `optimization_goal` | The optimization goal this ad set is using. Possible values defined [here](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/#fields). | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `campaigns` to Fivetran `campaign_history`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _All provided field mappings closely correspond to the source fields for the campaigns table, thus the highest confidence scores apply for the overall table and field mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of the campaign. | `campaigns.id` | 🟢 _1.00_ | *Direct match with the field 'campaigns.id'.* |
| `account_id` | The ID of the ad account that this campaign belongs to. | `campaigns.account_id` | 🟢 _1.00_ | *Direct match with the field 'campaigns.account_id'.* |
| `name` | The name of the campaign. | `campaigns.name` | 🟢 _1.00_ | *Direct match with the field 'campaigns.name'.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `campaigns._airbyte_extracted_at` | 🟢 _1.00_ | *Standard match for '_fivetran_synced' with 'campaigns._airbyte_extracted_at'.* |
| `updated_time` | {{ doc('updated_time') }} | `campaigns.updated_time` | 🟢 _1.00_ | *Direct match with the field 'campaigns.updated_time'.* |
| `created_time` | The time the campaign was created. | `campaigns.created_time` | 🟢 _1.00_ | *Direct match with the field 'campaigns.created_time'.* |
| `start_time` | Timestamp of designated campaign start time. | `campaigns.start_time` | 🟢 _1.00_ | *Direct match with the field 'campaigns.start_time'.* |
| `stop_time` | Timestamp of designated campaign end time. | `campaigns.stop_time` | 🟢 _1.00_ | *Direct match with the field 'campaigns.stop_time'.* |
| `daily_budget` | Daily budget of campaign. | `campaigns.daily_budget` | 🟢 _1.00_ | *Direct match with the field 'campaigns.daily_budget'.* |
| `budget_remaining` | Remaining budget of campaign. | `campaigns.budget_remaining` | 🟢 _1.00_ | *Direct match with the field 'campaigns.budget_remaining'.* |
| `lifetime_budget` | Lifetime budget of the campaign. | `campaigns.lifetime_budget` | 🟢 _1.00_ | *Direct match with the field 'campaigns.lifetime_budget'.* |
| `status` | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | `campaigns.status` | 🟢 _1.00_ | *Direct match with the field 'campaigns.status'. The status values are assumed to directly correspond.* |

### Mapping: Airbyte `ads` to Fivetran `ad_history`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping is highly confident; all fields except 'conversion_domain' are well-matched. Matches from source to target are clear and relevant._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID of this ad. | `ads.id` | 🟢 _1.00_ | *Exact match for 'id' field.* |
| `account_id` | The ID of the ad account that this ad belongs to. | `ads.account_id` | 🟢 _1.00_ | *Exact match for 'account_id' field.* |
| `ad_set_id` | ID of the ad set that contains the ad. | `ads.adset_id` | 🟢 _1.00_ | *Exact match for 'ad_set_id' field.* |
| `campaign_id` | Ad campaign that contains this ad. | `ads.campaign_id` | 🟢 _1.00_ | *Exact match for 'campaign_id' field.* |
| `creative_id` | The ID of the ad creative to be used by this ad. | `ads.creative.creative_id` | 🟢 _1.00_ | *Exact match for 'creative_id' field.* |
| `name` | Name of the ad. | `ads.name` | 🟢 _1.00_ | *Exact match for 'name' field.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ads._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `updated_time` | {{ doc('updated_time') }} | `ads.updated_time` | 🟢 _1.00_ | *Exact match for 'updated_time' field.* |
| `conversion_domain` | The domain you've configured the ad to convert to. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `ads_insights` to Fivetran `basic_ad`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The mapping is very comprehensive and the fields provided closely match the target schema. Most fields have a clear counterpart in the target schema, providing high confidence scores._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `ad_id` | The ID of the ad the report relates to. | `ads_insights.ad_id` | 🟢 _1.00_ | *Exact match found for ad_id.* |
| `ad_name` | Name of the ad the report relates to. | `ads_insights.ad_name` | 🟢 _1.00_ | *Exact match found for ad_name.* |
| `adset_name` | Name of the ad set the report relates to. | `ads_insights.adset_name` | 🟢 _1.00_ | *Exact match found for adset_name.* |
| `date` | The date of the reported performance. | `ads_insights.date_start` | 🟢 _1.00_ | *Exact match found for date.* |
| `account_id` | The ID of the ad account that this ad belongs to. | `ads_insights.account_id` | 🟢 _1.00_ | *Exact match found for account_id.* |
| `impressions` | The number of impressions the ad had on the given day. | `ads_insights.impressions` | 🟢 _1.00_ | *Exact match found for impressions.* |
| `inline_link_clicks` | The number of clicks the ad had on the given day. | `ads_insights.inline_link_clicks` | 🟢 _1.00_ | *Exact match found for inline_link_clicks.* |
| `spend` | The spend on the ad in the given day. | `ads_insights.spend` | 🟢 _1.00_ | *Exact match found for spend.* |
| `reach` | The number of people who saw any content from your Page or about your Page. This metric is estimated. | `ads_insights.reach` | 🟢 _1.00_ | *Exact match found for reach.* |
| `frequency` | The average number of times each person saw your ad; it is calculated as impressions divided by reach. | `ads_insights.frequency` | 🟢 _1.00_ | *Exact match found for frequency.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `ads_insights._airbyte_extracted_at` | 🟢 _1.00_ | *Mapped to _airbyte_extracted_at as per standard procedure.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
