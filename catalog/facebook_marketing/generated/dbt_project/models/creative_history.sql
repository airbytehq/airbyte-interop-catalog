
-- creative_history model
-- Generated from mapping: facebook_marketing.fivetran-interop/creative_history
-- Description: Each record in this table reflects a version of a Facebook creative.

WITH
UNKNOWN AS (
    SELECT * FROM {{ source('default', 'UNKNOWN') }}
)


SELECT
    NULL AS _fivetran_id, -- Unique record identifier
    NULL AS page_link, -- URL destination of Facebook ads.
    NULL AS template_page_link, -- URL destination of Facebook dynamic ads.
    NULL AS id, -- Unique ID for an ad creative.
    NULL AS account_id, -- Ad account ID for the account this ad creative belongs to.
    NULL AS name, -- Name of this ad creative as seen in the ad account's library.
    NULL AS url_tags, -- A set of query string parameters which will replace or be appended to urls clicked from page post ads, message of the post, and canvas app install creatives only.
    NULL AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    NULL AS asset_feed_spec_link_urls, -- Link to the asset feed spec
    NULL AS object_story_link_data_child_attachments, -- Link of the object story child attachments
    NULL AS object_story_link_data_caption, -- Link of the object story caption
    NULL AS object_story_link_data_description, -- Link of the object story description
    NULL AS object_story_link_data_link, -- Link of the object story link
    NULL AS object_story_link_data_message, -- Link of the object story message
    NULL AS template_app_link_spec_ios, -- Link of the object story spec for ios
    NULL AS template_app_link_spec_ipad, -- Link of the template app spec for ipad
    NULL AS template_app_link_spec_android, -- Link of the template app for android
    NULL AS template_app_link_spec_iphone -- Link of the template app for iphone
FROM UNKNOWN
