
-- This file was autogenerated with Morph. Please do not modify directly.

WITH
abandoned_checkouts AS (
    SELECT * FROM {{ source('shopify', 'abandoned_checkouts') }}
)


SELECT
    NULL AS _fivetran_deleted,
    abandoned_checkouts._airbyte_extracted_at AS _fivetran_synced,
    abandoned_checkouts.abandoned_checkout_url AS abandoned_checkout_url,
    abandoned_checkouts.billing_address.address1 AS billing_address_address_1,
    abandoned_checkouts.billing_address.address2 AS billing_address_address_2,
    abandoned_checkouts.billing_address.city AS billing_address_city,
    abandoned_checkouts.billing_address.company AS billing_address_company,
    abandoned_checkouts.billing_address.country AS billing_address_country,
    abandoned_checkouts.billing_address.country_code AS billing_address_country_code,
    abandoned_checkouts.billing_address.first_name AS billing_address_first_name,
    abandoned_checkouts.billing_address.last_name AS billing_address_last_name,
    abandoned_checkouts.billing_address.latitude AS billing_address_latitude,
    abandoned_checkouts.billing_address.longitude AS billing_address_longitude,
    abandoned_checkouts.billing_address.name AS billing_address_name,
    abandoned_checkouts.billing_address.phone AS billing_address_phone,
    abandoned_checkouts.billing_address.province AS billing_address_province,
    abandoned_checkouts.billing_address.province_code AS billing_address_province_code,
    abandoned_checkouts.billing_address.zip AS billing_address_zip,
    abandoned_checkouts.buyer_accepts_marketing AS buyer_accepts_marketing,
    abandoned_checkouts.cart_token AS cart_token,
    abandoned_checkouts.closed_at AS closed_at,
    abandoned_checkouts.created_at AS created_at,
    abandoned_checkouts.currency AS currency,
    abandoned_checkouts.customer.default_address.customer_id AS customer_id,
    abandoned_checkouts.customer_locale AS customer_locale,
    abandoned_checkouts.device_id AS device_id,
    abandoned_checkouts.email AS email,
    abandoned_checkouts.gateway AS gateway,
    abandoned_checkouts.id AS id,
    abandoned_checkouts.landing_site AS landing_site_base_url,
    abandoned_checkouts.location_id AS location_id,
    abandoned_checkouts.name AS name,
    abandoned_checkouts.note AS note,
    abandoned_checkouts.phone AS phone,
    abandoned_checkouts.presentment_currency AS presentment_currency,
    abandoned_checkouts.referring_site AS referring_site,
    abandoned_checkouts.shipping_address.address1 AS shipping_address_address_1,
    abandoned_checkouts.shipping_address.address2 AS shipping_address_address_2,
    abandoned_checkouts.shipping_address.city AS shipping_address_city,
    abandoned_checkouts.shipping_address.company AS shipping_address_company,
    abandoned_checkouts.shipping_address.country AS shipping_address_country,
    abandoned_checkouts.shipping_address.country_code AS shipping_address_country_code,
    abandoned_checkouts.shipping_address.first_name AS shipping_address_first_name,
    abandoned_checkouts.shipping_address.last_name AS shipping_address_last_name,
    abandoned_checkouts.shipping_address.latitude AS shipping_address_latitude,
    abandoned_checkouts.shipping_address.longitude AS shipping_address_longitude,
    abandoned_checkouts.shipping_address.name AS shipping_address_name,
    abandoned_checkouts.shipping_address.phone AS shipping_address_phone,
    abandoned_checkouts.shipping_address.province AS shipping_address_province,
    abandoned_checkouts.shipping_address.province_code AS shipping_address_province_code,
    abandoned_checkouts.shipping_address.zip AS shipping_address_zip,
    abandoned_checkouts.source_name AS source_name,
    abandoned_checkouts.subtotal_price AS subtotal_price,
    abandoned_checkouts.taxes_included AS taxes_included,
    abandoned_checkouts.token AS token,
    abandoned_checkouts.total_discounts AS total_discounts,
    NULL AS total_duties,
    abandoned_checkouts.total_line_items_price AS total_line_items_price,
    abandoned_checkouts.total_price AS total_price,
    abandoned_checkouts.total_tax AS total_tax,
    abandoned_checkouts.total_weight AS total_weight,
    abandoned_checkouts.updated_at AS updated_at,
    abandoned_checkouts.user_id AS user_id
FROM abandoned_checkouts
