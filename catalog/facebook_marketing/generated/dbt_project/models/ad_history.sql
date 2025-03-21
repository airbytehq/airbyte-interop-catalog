
-- ad_history model
-- Generated from mapping: facebook_marketing.fivetran-interop/ad_history
-- Description: Each record in this table reflects a version of a Facebook ad.

WITH
ad_historys AS (
    SELECT * FROM {{ source('facebook_marketing', 'ad_historys') }}
)


SELECT
    NULL AS id, -- The ID of this ad.
    NULL AS account_id, -- The ID of the ad account that this ad belongs to.
    NULL AS ad_set_id, -- ID of the ad set that contains the ad.
    NULL AS campaign_id, -- Ad campaign that contains this ad.
    NULL AS creative_id, -- The ID of the ad creative to be used by this ad.
    NULL AS name, -- Name of the ad.
    NULL AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    NULL AS updated_time, -- {{ doc('updated_time') }}
    NULL AS conversion_domain -- The domain you've configured the ad to convert to.
FROM ad_historys
