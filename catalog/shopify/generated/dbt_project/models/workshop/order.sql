
-- This file was autogenerated with Morph. Please do not modify directly.

WITH
orders AS (
    SELECT * FROM {{ source('shopify', 'orders') }}
)


SELECT
    orders._airbyte_extracted_at AS _fivetran_synced,
    orders.app_id AS app_id,
    orders.billing_address.address1 AS billing_address_address_1,
    orders.billing_address.address2 AS billing_address_address_2,
    orders.billing_address.city AS billing_address_city,
    orders.billing_address.company AS billing_address_company,
    orders.billing_address.country AS billing_address_country,
    orders.billing_address.country_code AS billing_address_country_code,
    orders.billing_address.first_name AS billing_address_first_name,
    orders.billing_address.last_name AS billing_address_last_name,
    orders.billing_address.latitude AS billing_address_latitude,
    orders.billing_address.longitude AS billing_address_longitude,
    orders.billing_address.name AS billing_address_name,
    orders.billing_address.phone AS billing_address_phone,
    orders.billing_address.province AS billing_address_province,
    orders.billing_address.province_code AS billing_address_province_code,
    orders.billing_address.zip AS billing_address_zip,
    orders.browser_ip AS browser_ip,
    orders.buyer_accepts_marketing AS buyer_accepts_marketing,
    orders.cancel_reason AS cancel_reason,
    orders.cancelled_at AS cancelled_at,
    orders.cart_token AS cart_token,
    orders.closed_at AS closed_at,
    orders.created_at AS created_at,
    orders.currency AS currency,
    NULL AS customer_id,
    orders.email AS email,
    orders.financial_status AS financial_status,
    orders.fulfillment_status AS fulfillment_status,
    orders.id AS id,
    orders.landing_site AS landing_site_base_url,
    orders.location_id AS location_id,
    orders.name AS name,
    orders.note AS note,
    orders.number AS number,
    orders.order_number AS order_number,
    orders.processed_at AS processed_at,
    orders.referring_site AS referring_site,
    orders.shipping_address.address1 AS shipping_address_address_1,
    orders.shipping_address.address2 AS shipping_address_address_2,
    orders.shipping_address.city AS shipping_address_city,
    orders.shipping_address.company AS shipping_address_company,
    orders.shipping_address.country AS shipping_address_country,
    orders.shipping_address.country_code AS shipping_address_country_code,
    orders.shipping_address.first_name AS shipping_address_first_name,
    orders.shipping_address.last_name AS shipping_address_last_name,
    orders.shipping_address.latitude AS shipping_address_latitude,
    orders.shipping_address.longitude AS shipping_address_longitude,
    orders.shipping_address.name AS shipping_address_name,
    orders.shipping_address.phone AS shipping_address_phone,
    orders.shipping_address.province AS shipping_address_province,
    orders.shipping_address.province_code AS shipping_address_province_code,
    orders.shipping_address.zip AS shipping_address_zip,
    orders.source_name AS source_name,
    orders.subtotal_price AS subtotal_price,
    orders.taxes_included AS taxes_included,
    orders.test AS test,
    orders.token AS token,
    orders.total_discounts AS total_discounts,
    orders.total_line_items_price AS total_line_items_price,
    orders.total_price AS total_price,
    orders.total_tax AS total_tax,
    orders.total_weight AS total_weight,
    orders.updated_at AS updated_at,
    orders.user_id AS user_id,
    orders.checkout_token AS checkout_token,
    NULL AS confirmed,
    orders.customer_locale AS customer_locale,
    orders.checkout_id AS checkout_id,
    orders.order_status_url AS order_status_url,
    NULL AS _fivetran_deleted,
    orders.total_tip_received AS total_tip_received,
    orders.device_id AS device_id,
    NULL AS presentment_currency,
    orders.total_shipping_price_set AS total_shipping_price_set,
    orders.client_details.user_agent AS client_details_user_agent,
    orders.total_tax_set AS total_tax_set,
    orders.total_discounts_set AS total_discounts_set,
    orders.total_line_items_price_set AS total_line_items_price_set,
    orders.total_price_set AS total_price_set,
    orders.confirmed AS is_confirmed,
    orders.source_identifier AS source_identifier
FROM orders
