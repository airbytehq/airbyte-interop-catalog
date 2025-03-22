
-- ad_set_history model
-- Generated from mapping: facebook_marketing.fivetran-interop/ad_set_history
-- Description: Each record in this table reflects a version of a Facebook ad set.

WITH
ad_sets AS (
    SELECT * FROM {{ source('facebook_marketing', 'ad_sets') }}
)


SELECT
    ad_sets.id AS id, -- The ID of the ad set.
    ad_sets.account_id AS account_id, -- The ID of the ad account that this ad set belongs to.
    ad_sets.campaign_id AS campaign_id, -- The ID of the campaign that contains this ad set.
    ad_sets.name AS name, -- The name of the ad set.
    _airbyte_extracted_at AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    ad_sets.updated_time AS updated_time, -- {{ doc('updated_time') }}
    ad_sets.created_time AS created_time, -- The time the ad set was created.
    ad_sets.start_time AS start_time, -- Timestamp of designated ad set start time.
    ad_sets.end_time AS end_time, -- Timestamp of designated ad set end time.
    ad_sets.daily_budget AS daily_budget, -- Daily budget of ad set.
    ad_sets.budget_remaining AS budget_remaining, -- Remaining budget of ad set.
    ad_sets.lifetime_budget AS lifetime_budget, -- Lifetime budget of the ad set.
    ad_sets.status AS status -- Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'.
FROM ad_sets
