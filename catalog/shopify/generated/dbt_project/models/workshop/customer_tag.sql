
-- This file was autogenerated with Morph. Please do not modify directly.

WITH
customers AS (
    SELECT * FROM {{ source('shopify', 'customers') }}
)


SELECT
    customers._airbyte_extracted_at AS _fivetran_synced,
    NULL AS index,
    customers.default_address.customer_id AS customer_id,
    NULL AS value
FROM customers
