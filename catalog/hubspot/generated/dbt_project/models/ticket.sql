
-- ticket model
-- Generated from mapping: hubspot.fivetran-interop/ticket
-- Description: Fivetran Raw 'Ticket' Model

WITH
tickets AS (
    SELECT * FROM {{ source('hubspot', 'tickets') }}
)


SELECT
    _airbyte_extracted_at AS _fivetran_synced, -- Timestamp of when this record was last synced by Fivetran.
    tickets.id AS id, -- ID of the ticket.
    False AS is_deleted, -- Whether the record was deleted (v2 endpoint).
    NULL AS _fivetran_deleted, -- Whether the record was deleted (v3 endpoint).
    NULL AS portal_id, -- The HubSpot account ID.
    tickets.properties_closed_date AS property_closed_date, -- The date the ticket was closed.
    tickets.createdAt AS property_createdate, -- The date the ticket was created.
    tickets.properties_first_agent_reply_date AS property_first_agent_reply_date, -- The date for the first agent reply on the ticket.
    tickets.properties_hs_pipeline AS property_hs_pipeline, -- The ID of the ticket's pipeline.
    tickets.properties_hs_pipeline_stage AS property_hs_pipeline_stage, -- The ID of the ticket's pipeline stage.
    tickets.properties_hs_ticket_priority AS property_hs_ticket_priority, -- The priority of the ticket.
    tickets.properties_hs_ticket_category AS property_hs_ticket_category, -- The category of the ticket.
    tickets.properties_hubspot_owner_id AS property_hubspot_owner_id, -- The ID of the deal's owner.
    tickets.properties_hs_email_subject AS property_subject, -- Short summary of ticket.
    tickets.properties_content AS property_content -- Text in body of the ticket.
FROM tickets
