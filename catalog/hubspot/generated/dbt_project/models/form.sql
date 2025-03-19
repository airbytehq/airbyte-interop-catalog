
-- form model
-- Generated from mapping: hubspot.fivetran-compat/form
-- Description: Fivetran Raw 'Form' Model

WITH 
forms AS (
    SELECT * FROM {{ source('hubspot', 'forms') }}
)


SELECT
    False AS _fivetran_deleted, -- Boolean to mark rows that were deleted in the source database.
    CURRENT_TIMESTAMP() AS _fivetran_synced, -- Timestamp of when this record was last synced by Fivetran.
    forms.id AS id, -- The ID of the form.
    MISSING AS portal_id, -- The HubSpot account ID.
    forms.name AS name, -- The name of the form.
    forms.createdAt AS created_at, -- The date the form was created.
    MISSING AS css_class, -- The CSS class of the form.
    forms.updatedAt AS updated_at, -- The date the form was last updated.
    forms.publishedAt AS published_at, -- The date the form was published.
    forms.archivedAt AS archived_at, -- The date the form was archived.
    forms.style AS style, -- The style settings of the form.
    forms.submitText AS submit_text, -- The text displayed on the submit button.
    forms.redirectUrl AS redirect_url, -- The URL to redirect to after form submission.
    forms.internalTitle AS internal_title, -- The internal title of the form.
    forms.archived = false AS is_published, -- Whether the form is published.
    MISSING AS follow_up_id, -- The ID of the follow-up form.
    MISSING AS guid, -- The globally unique identifier for the form.
    MISSING AS lead_nurturing_campaign_id, -- The ID of the lead nurturing campaign associated with the form.
    MISSING AS method, -- The HTTP method used by the form.
    MISSING AS notify_recipients, -- Recipients to notify when the form is submitted.
    MISSING AS redirect -- Whether the form redirects after submission.
FROM forms