
-- contact model
-- Generated from mapping: hubspot.fivetran-compat/contact
-- Description: Fivetran Raw 'Contact' Model

WITH 
contacts AS (
    SELECT * FROM {{ source('hubspot', 'contacts') }}
)


SELECT
    contacts.archived AS _fivetran_deleted, -- Boolean to mark rows that were deleted in the source database.
    NULL AS _fivetran_synced, -- Timestamp of when this record was last synced by Fivetran.
    contacts.id AS id, -- The ID of the contact.
    NULL AS portal_id, -- The HubSpot account ID.
    contacts.properties_firstname AS property_firstname, -- The first name of the contact.
    contacts.properties_lastname AS property_lastname, -- The last name of the contact.
    contacts.properties_email AS property_email, -- The email address of the contact.
    NULL AS property_email_1, -- The secondary email address of the contact.
    contacts.properties_phone AS property_phone, -- The phone number of the contact.
    contacts.properties_address AS property_address, -- The street address of the contact.
    contacts.properties_city AS property_city, -- The city where the contact is located.
    contacts.properties_state AS property_state, -- The state where the contact is located.
    contacts.properties_zip AS property_zip, -- The zip code where the contact is located.
    contacts.properties_country AS property_country, -- The country where the contact is located.
    contacts.properties_company AS property_company, -- The company the contact works for.
    contacts.properties_jobtitle AS property_jobtitle, -- The job title of the contact.
    contacts.properties_createdate AS property_createdate, -- The date the contact was created in HubSpot.
    contacts.properties_lastmodifieddate AS property_lastmodifieddate, -- The date the contact was last modified.
    contacts.properties_hubspot_owner_id AS property_hubspot_owner_id, -- The ID of the contact's owner.
    contacts.properties_lifecyclestage AS property_lifecyclestage, -- The lifecycle stage of the contact.
    NULL AS property_annualrevenue, -- The annual revenue of the contact's company.
    NULL AS property_hs_calculated_merged_vids -- The calculated merged visitor IDs for the contact.
FROM contacts