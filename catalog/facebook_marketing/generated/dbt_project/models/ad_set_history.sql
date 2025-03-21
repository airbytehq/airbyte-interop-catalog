
-- ad_set_history model
-- Generated from mapping: facebook_marketing.fivetran-interop/ad_set_history
-- Description: Each record in this table reflects a version of a Facebook ad set.

WITH
UNKNOWN AS (
    SELECT * FROM {{ source('default', 'UNKNOWN') }}
)


SELECT
    NULL AS id, -- The ID of the ad set.
    NULL AS account_id, -- The ID of the ad account that this ad set belongs to.
    NULL AS campaign_id, -- Ad campaign that contains this ad set.
    NULL AS name, -- The name of the ad set.
    NULL AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    NULL AS updated_time, -- {{ doc('updated_time') }}
    NULL AS start_time, -- Timestamp of designated ad set start time.
    NULL AS end_time, -- Timestamp of designated ad set end time.
    NULL AS bid_strategy, -- Bid strategy values are - 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', 'LOWEST_COST_WITH_MIN_ROAS'.
    NULL AS daily_budget, -- Daily budget of ad set.
    NULL AS budget_remaining, -- Remaining budget of ad set.
    NULL AS status, -- Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'.
    NULL AS optimization_goal -- The optimization goal this ad set is using. Possible values defined [here](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/#fields).
FROM UNKNOWN
