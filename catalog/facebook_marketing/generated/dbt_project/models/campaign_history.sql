
-- campaign_history model
-- Generated from mapping: facebook_marketing.fivetran-interop/campaign_history
-- Description: Each record in this table reflects a version of a Facebook campaign.

WITH
campaign_historys AS (
    SELECT * FROM {{ source('facebook_marketing', 'campaign_historys') }}
)


SELECT
    NULL AS id, -- The ID of the campaign.
    NULL AS account_id, -- The ID of the ad account that this campaign belongs to.
    NULL AS name, -- The name of the campaign.
    NULL AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    NULL AS updated_time, -- {{ doc('updated_time') }}
    NULL AS created_time, -- The time the campaign was created.
    NULL AS start_time, -- Timestamp of designated campaign start time.
    NULL AS stop_time, -- Timestamp of designated campaign end time.
    NULL AS daily_budget, -- Daily budget of campaign.
    NULL AS budget_remaining, -- Remaining budget of campaign.
    NULL AS lifetime_budget, -- Lifetime budget of the campaign.
    NULL AS status -- Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'.
FROM campaign_historys
