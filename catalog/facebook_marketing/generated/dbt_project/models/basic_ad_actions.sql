-- basic_ad_actions model
-- Generated from mapping: facebook_marketing.fivetran-interop/basic_ad_actions
-- Description: Each record represents the daily conversion performance of an ad in Facebook. This is the prebuilt `basic_ad` report broken down by `action_type`.

WITH
ads_insights_action_type AS (
    SELECT * FROM {{ source('facebook_marketing', 'ads_insights_action_type') }}
)


SELECT
    NULL AS _1_d_view, -- Conversion metric value using a 1-day view attribution window.
    NULL AS _28_d_click, -- Conversion metric value using a 28-day click attribution window.
    NULL AS _28_d_view, -- Conversion metric value using a 28-day view attribution window.
    NULL AS _7_d_click, -- Conversion metric value using a 7-day click attribution window.
    NULL AS _7_d_view, -- Conversion metric value using a 7-day view attribution window.
    NULL AS _dda, -- Defunct field.
    _airbyte_extracted_at AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    ads_insights_action_type.action_type AS action_type, -- The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they did not click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions are counted when they occur within 1 day after a person sees your ad or within 28 days after a person clicks on your ad.
    ads_insights_action_type.ad_id AS ad_id, -- The ID of the ad the report relates to.
    NULL AS date, -- The date of the reported performance.
    NULL AS inline_post_engagement, -- The number of post engagements the ad had on the given day.
    NULL AS offsite_conversion_fb_pixel_add_to_cart, -- The number of add to cart conversions the ad had on the given day. Not included in downstream models by default, but can be added using the facebook_ads__basic_ad_actions_passthrough_metrics var.
    NULL AS unique_actions, -- The number of unique actions taken on the ad itself. Not included in downstream models by default, but can be added using the facebook_ads__basic_ad_actions_passthrough_metrics var.
    ads_insights_action_type.value AS value -- Conversion metric value using the default attribution window.
FROM ads_insights_action_type
