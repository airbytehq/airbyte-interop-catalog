
-- account_history model
-- Generated from mapping: facebook_marketing.fivetran-interop/account_history
-- Description: Each record in this table reflects a version of a Facebook ad account.

WITH
account_historys AS (
    SELECT * FROM {{ source('facebook_marketing', 'account_historys') }}
)


SELECT
    NULL AS id, -- The ID of the ad account.
    NULL AS name, -- Name of the account.
    NULL AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    NULL AS account_status, -- Current status of account.
    NULL AS business_country_code, -- Country code of business associated to account.
    NULL AS created_time, -- The time account was created.
    NULL AS currency, -- Currency associated with account.
    NULL AS timezone_name -- Timezone associated with account.
FROM account_historys
