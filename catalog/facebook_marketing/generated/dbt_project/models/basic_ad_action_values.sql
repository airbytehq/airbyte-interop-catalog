
-- basic_ad_action_values model
-- Generated from mapping: facebook_marketing.fivetran-interop/basic_ad_action_values
-- Description: Each record represents the daily conversion values associated with an ad in Facebook. This is the prebuilt `basic_ad` report broken down by `action_type` and `action_value`.

WITH
UNKNOWN AS (
    SELECT * FROM {{ source('default', 'UNKNOWN') }}
)


SELECT
    NULL AS _7_d_click, -- Conversion metric value using an attribution window of "7 days after clicking the ad". Not included in downstream models by default, but can be added using the `facebook_ads__basic_ad_actions_passthrough_metrics` var.
    NULL AS _fivetran_id, -- Defunct field.
    NULL AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    NULL AS action_type, -- The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions prepended by app_custom_event come from mobile app events and actions prepended by offsite_conversion come from the Facebook Pixel.

    NULL AS ad_id, -- The ID of the ad the report relates to.
    NULL AS date, -- The date of the reported performance.
    NULL AS index, -- Index reflecting the `action_type` tracked for this ad on this day. Column of not much consequence.
    NULL AS value -- Monetary value associated with the convesion action using the default attribution window.
FROM UNKNOWN
