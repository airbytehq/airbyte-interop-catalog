
-- deal model
-- Generated from mapping: hubspot.fivetran-compat/deal
-- Description: Fivetran Raw 'Deal' Model

WITH 
deals AS (
    SELECT * FROM {{ source('hubspot', 'deals') }}
)


SELECT
    deals.id AS deal_id, -- The ID of the deal.
    deals.archived AS is_deleted, -- Whether the record was deleted.
    MISSING AS portal_id, -- The HubSpot account ID.
    deals.properties_pipeline AS deal_pipeline_id, -- The ID of the deal's pipeline.
    deals.properties_dealstage AS deal_pipeline_stage_id, -- The ID of the deal's pipeline stage.
    deals.properties_hubspot_owner_id AS owner_id, -- The ID of the deal's owner.
    CURRENT_TIMESTAMP() AS _fivetran_synced, -- Timestamp of when this record was last synced by Fivetran.
    deals.properties_dealname AS property_dealname, -- The name of the deal.
    deals.properties_description AS property_description, -- A description of the deal.
    deals.properties_createdate AS property_createdate, -- The date the deal was created in HubSpot.
    deals.properties_closedate AS property_closedate, -- The date the deal was closed.
    deals.properties_amount AS property_amount, -- The amount of the deal.
    deals.properties_dealstage AS property_dealstage, -- The stage of the deal in the pipeline.
    deals.properties_pipeline AS property_pipeline, -- The pipeline the deal is in.
    deals.properties_hubspot_owner_id AS property_hubspot_owner_id, -- The ID of the deal's owner.
    deals.properties_dealtype AS property_dealtype, -- The type of the deal.
    deals.properties_hs_lastmodifieddate AS property_hs_lastmodifieddate -- The date the deal was last modified.
FROM deals