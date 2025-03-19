
-- product model
-- Generated from mapping: hubspot.fivetran-compat/product
-- Description: Fivetran Raw 'Product' Model

WITH 
products AS (
    SELECT * FROM {{ source('hubspot', 'products') }}
)


SELECT
    NULL AS _fivetran_synced, -- Timestamp of when this record was last synced by Fivetran.
    products.id AS id, -- The ID of the product.
    NULL AS portal_id, -- The HubSpot account ID.
    products.archived AS is_deleted, -- Whether the record was deleted.
    products.properties_name AS name, -- The name of the product.
    products.properties_description AS description, -- A description of the product.
    products.createdAt AS created_at, -- The date the product was created.
    products.updatedAt AS updated_at, -- The date the product was last updated.
    products.properties_price AS price, -- The price of the product.
    products.properties_hs_sku AS hs_sku, -- The SKU of the product.
    products.properties_hs_recurring_billing_period AS hs_recurring_billing_period, -- The recurring billing period of the product.
    products.properties_hs_product_type AS hs_product_type -- The type of the product.
FROM products