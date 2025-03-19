
-- workflow model
-- Generated from mapping: hubspot.fivetran-compat/workflow
-- Description: Fivetran Raw 'Workflow' Model

WITH 
workflows AS (
    SELECT * FROM {{ source('hubspot', 'workflows') }}
)


SELECT
    CURRENT_TIMESTAMP() AS _fivetran_synced, -- Timestamp of when this record was last synced by Fivetran.
    workflows.id AS id, -- The ID of the workflow.
    MISSING AS portal_id, -- The HubSpot account ID.
    False AS is_deleted, -- Whether the record was deleted.
    workflows.name AS name, -- The name of the workflow.
    workflows.type AS type, -- The type of the workflow.
    workflows.enabled AS enabled, -- Whether the workflow is enabled.
    workflows.insertedAt AS inserted_at, -- The date the workflow was created.
    workflows.updatedAt AS updated_at, -- The date the workflow was last updated.
    workflows.actions AS actions, -- The actions performed by the workflow.
    workflows.allowContactToTriggerMultipleTimes AS allow_contact_to_trigger_multiple_times, -- Whether a contact can trigger the workflow multiple times.
    workflows.listeningTriggers AS listening_triggers, -- The triggers that the workflow is listening for.
    workflows.suppressed AS suppressed -- Whether the workflow is suppressed.
FROM workflows