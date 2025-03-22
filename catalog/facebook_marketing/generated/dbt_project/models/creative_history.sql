
-- creative_history model
-- Generated from mapping: facebook_marketing.fivetran-interop/creative_history
-- Description: Each record in this table reflects a version of a Facebook creative.

WITH
ad_creatives AS (
    SELECT * FROM {{ source('facebook_marketing', 'ad_creatives') }}
)


SELECT
    NULL AS _fivetran_id, -- Unique record identifier
    ad_creatives.link_url AS page_link, -- URL destination of Facebook ads.
    ad_creatives.template_url AS template_page_link, -- URL destination of Facebook dynamic ads.
    ad_creatives.id AS id, -- Unique ID for an ad creative.
    ad_creatives.account_id AS account_id, -- Ad account ID for the account this ad creative belongs to.
    ad_creatives.name AS name, -- Name of this ad creative as seen in the ad account's library.
    ad_creatives.url_tags AS url_tags, -- A set of query string parameters which will replace or be appended to urls clicked from page post ads, message of the post, and canvas app install creatives only.
    _airbyte_extracted_at AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    NULL AS asset_feed_spec_link_urls, -- Link URLs from the asset feed spec.
    NULL AS call_to_action_type, -- The call to action button text and header text of legacy ads.
    NULL AS effective_object_story_id, -- The ID of the promoted post.
    NULL AS instagram_permalink_url, -- Permanent URL of an instagram media.
    NULL AS instagram_user_id, -- Instagram user ID.
    NULL AS link_destination_url, -- URL destination of Facebook ads.
    NULL AS link_url, -- URL destination of Facebook ads.
    NULL AS template_app_link_spec_android, -- Link of the template app for android
    NULL AS template_app_link_spec_ipad, -- Link of the template app for ipad
    NULL AS template_app_link_spec_iphone, -- Link of the template app for iphone
FROM ad_creatives
