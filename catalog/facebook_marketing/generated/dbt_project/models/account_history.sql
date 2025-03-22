
-- account_history model
-- Generated from mapping: facebook_marketing.fivetran-interop/account_history
-- Description: Each record in this table reflects a version of a Facebook ad account.

WITH
ad_account AS (
    SELECT * FROM {{ source('facebook_marketing', 'ad_account') }}
)


SELECT
    ad_account.id AS id, -- The ID of the ad account.
    ad_account.name AS name, -- Name of the account.
    ad_account.account_status AS account_status, -- Status of the account.
    ad_account.business_country_code AS business_country_code, -- Country code of the business.
    ad_account.created_time AS created_time, -- Time the account was created.
    ad_account.currency AS currency, -- Currency of the account.
    _airbyte_extracted_at AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    ad_account.timezone_name AS timezone_name -- Timezone of the account.
FROM ad_account
