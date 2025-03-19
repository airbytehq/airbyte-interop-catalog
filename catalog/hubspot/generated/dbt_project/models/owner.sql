
-- owner model
-- Generated from mapping: hubspot.fivetran-interop/owner
-- Description: Fivetran Raw 'Owner' Model

WITH
owners AS (
    SELECT * FROM {{ source('hubspot', 'owners') }}
)


SELECT
    _airbyte_extracted_at AS _fivetran_synced, -- Timestamp of when this record was last synced by Fivetran.
    owners.id AS owner_id, -- The ID of the owner.
    NULL AS portal_id, -- The HubSpot account ID.
    NULL AS type, -- The type of owner.
    False AS is_deleted, -- Whether the record was deleted.
    owners.email AS email, -- The email address of the owner.
    owners.firstName AS first_name, -- The first name of the owner.
    owners.lastName AS last_name, -- The last name of the owner.
    owners.createdAt AS created_at, -- The date the owner was created in HubSpot.
    owners.updatedAt AS updated_at, -- The date the owner was last updated.
    owners.userId AS user_id, -- The user ID of the owner.
    owners.archived = false AS is_active, -- Whether the owner is active.
    owners.teams AS teams -- The teams the owner belongs to.
FROM owners
