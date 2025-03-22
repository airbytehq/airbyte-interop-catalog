-- basic_ad_action_values model
-- Generated from mapping: facebook_marketing.fivetran-interop/basic_ad_action_values
-- Description: Each record represents the daily conversion value of an ad in Facebook. This is the prebuilt `basic_ad` report broken down by `action_type` and `action_value`.

WITH
ads_insights_action_type AS (
    SELECT * FROM {{ source('facebook_marketing', 'ads_insights_action_type') }}
)


SELECT
    NULL AS _7_d_click, -- Conversion metric value using a 7-day click attribution window.
    NULL AS _7_d_view, -- Conversion metric value using a 7-day view attribution window.
    NULL AS _dda, -- Defunct field.
    _airbyte_extracted_at AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    ads_insights_action_type.action_type AS action_type, -- The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they did not click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions are counted when they occur within 1 day after a person sees your ad or within 28 days after a person clicks on your ad.
    ads_insights_action_type.ad_id AS ad_id, -- The ID of the ad the report relates to.
    NULL AS date, -- The date of the reported performance.
    NULL AS index, -- Index reflecting the `action_type` tracked for this ad on this day. Column of not much consequence.
    ads_insights_action_type.value AS value -- Monetary value associated with the convesion action using the default attribution window.
FROM ads_insights_action_type
