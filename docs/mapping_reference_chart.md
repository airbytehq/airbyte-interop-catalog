# Facebook Marketing Mapping Reference Chart

This document provides a reference for mapping source streams from the Airbyte Facebook Marketing connector to target tables in the Fivetran schema.

## Source to Target Mappings

| Source Stream | Target Table | Description |
|---------------|--------------|-------------|
| `ad_account` | `account_history` | Information about Facebook ad accounts |
| `ads` | `ad_history` | Information about Facebook ads |
| `ad_sets` | `ad_set_history` | Information about Facebook ad sets |
| `campaigns` | `campaign_history` | Information about Facebook campaigns |
| `ad_creatives` | `creative_history` | Information about Facebook ad creatives |
| `ads_insights` | `basic_ad` | Daily performance metrics for Facebook ads |
| `ads_insights_action_type` | `basic_ad_actions` | Conversion performance metrics by action type |
| `ads_insights_action_type` | `basic_ad_action_values` | Conversion value metrics by action type |

## Field Mapping Patterns

### Standard Field Mappings

- `_fivetran_synced` should map to `_airbyte_extracted_at` in all mapping files
- Source field references should use the format `{source_alias}.{field_name}`
- Fields marked with `MISSING` need to be evaluated for appropriate source fields

### Common Field Patterns

- ID fields typically map directly (e.g., `ads.id` → `id`)
- Account ID fields typically map directly (e.g., `ads.account_id` → `account_id`)
- Name fields typically map directly (e.g., `ads.name` → `name`)
- Timestamp fields may require format conversion

## Verification Strategy

After completing the mappings:
1. Ensure all "from" clauses are correctly specified
2. Ensure all field expressions are properly mapped
3. Check for any remaining `MISSING` expressions that need to be addressed
4. Verify field types match between source and target
