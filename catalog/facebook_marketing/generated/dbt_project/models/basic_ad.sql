
-- basic_ad model
-- Generated from mapping: facebook_marketing.fivetran-interop/basic_ad
-- Description: Each record represents the daily performance of an ad in Facebook.

WITH
UNKNOWN AS (
    SELECT * FROM {{ source('default', 'UNKNOWN') }}
)


SELECT
    NULL AS ad_id, -- The ID of the ad the report relates to.
    NULL AS ad_name, -- Name of the ad the report relates to.
    NULL AS adset_name, -- Name of the ad set the report relates to.
    NULL AS date, -- The date of the reported performance.
    NULL AS account_id, -- The ID of the ad account that this ad belongs to.
    NULL AS impressions, -- The number of impressions the ad had on the given day.
    NULL AS inline_link_clicks, -- The number of clicks the ad had on the given day.
    NULL AS spend, -- The spend on the ad in the given day.
    NULL AS reach, -- The number of people who saw any content from your Page or about your Page. This metric is estimated.
    NULL AS frequency, -- The average number of times each person saw your ad; it is calculated as impressions divided by reach.
    NULL AS _fivetran_synced -- {{ doc('_fivetran_synced') }}
FROM UNKNOWN
