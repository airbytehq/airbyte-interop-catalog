
-- campaign_history model
-- Generated from mapping: facebook_marketing.fivetran-interop/campaign_history
-- Description: Each record in this table reflects a version of a Facebook campaign.

WITH
campaigns AS (
    SELECT * FROM {{ source('facebook_marketing', 'campaigns') }}
)


SELECT
    campaigns.id AS id, -- The ID of the campaign.
    campaigns.account_id AS account_id, -- The ID of the ad account that this campaign belongs to.
    campaigns.name AS name, -- The name of the campaign.
    _airbyte_extracted_at AS _fivetran_synced, -- {{ doc('_fivetran_synced') }}
    campaigns.updated_time AS updated_time, -- {{ doc('updated_time') }}
    campaigns.created_time AS created_time, -- The time the campaign was created.
    campaigns.start_time AS start_time, -- Timestamp of designated campaign start time.
    campaigns.stop_time AS stop_time, -- Timestamp of designated campaign end time.
    campaigns.daily_budget AS daily_budget, -- Daily budget of campaign.
    campaigns.budget_remaining AS budget_remaining, -- Remaining budget of campaign.
    campaigns.lifetime_budget AS lifetime_budget, -- Lifetime budget of the campaign.
    campaigns.status AS status -- Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'.
FROM campaigns
