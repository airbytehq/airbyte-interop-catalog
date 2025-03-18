
-- company model
-- Generated from mapping: hubspot.fivetran-compat/company
-- Description: Fivetran Raw 'Company' Model

WITH 
companies AS (
    SELECT * FROM {{ source('hubspot', 'companies') }}
)


SELECT
    CURRENT_TIMESTAMP() AS _fivetran_synced -- Timestamp of when this record was last synced by Fivetran.,
    companies.id AS id -- The ID of the company.,
    MISSING AS portal_id -- The HubSpot account ID.,
    companies.archived AS is_deleted -- Whether the record was deleted.,
    companies.properties_name AS property_name -- The name of the company.,
    companies.properties_description AS property_description -- A short statement about the company's mission and goals.,
    companies.properties_createdate AS property_createdate -- The date the company was added to your account.,
    companies.properties_industry AS property_industry -- The type of business the company performs.,
    companies.properties_address AS property_address -- The street address of the company.,
    companies.properties_address2 AS property_address_2 -- Additional address information for the company.,
    companies.properties_city AS property_city -- The city where the company is located.,
    companies.properties_state AS property_state -- The state where the company is located.,
    companies.properties_country AS property_country -- The country where the company is located.,
    companies.properties_annualrevenue AS property_annualrevenue -- The actual or estimated annual revenue of the company.
FROM companies