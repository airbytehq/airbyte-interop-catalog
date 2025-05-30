
-- This file was autogenerated with Morph. Please do not modify directly.

WITH
contacts_merged_audit AS (
    SELECT * FROM {{ source('hubspot', 'contacts_merged_audit') }}
)


SELECT
    contacts_merged_audit._airbyte_extracted_at AS _fivetran_synced,
    contacts_merged_audit.canonical_vid AS canonical_vid,
    NULL AS contact_id,
    contacts_merged_audit.entity_id AS entity_id,
    contacts_merged_audit.first_name AS first_name,
    contacts_merged_audit.last_name AS last_name,
    contacts_merged_audit.num_properties_moved AS num_properties_moved,
    contacts_merged_audit.timestamp AS timestamp,
    contacts_merged_audit.user_id AS user_id,
    contacts_merged_audit.vid_to_merge AS vid_to_merge
FROM contacts_merged_audit
