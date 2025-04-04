# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

## collection




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| custom_collections | shopify | custom_collections |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc('_fivetran_deleted') }} |
| _fivetran_synced | custom_collections._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| disjunctive | MISSING | Boolean representing whether the `rules` or disjuctive (logical `OR`) or not. True = disjuctive, false = conjunctive (logical `AND`). |
| handle | custom_collections.handle | A unique, human-readable string for the collection automatically generated from its title. This is used in themes by the Liquid templating language to refer to the collection. |
| id | custom_collections.id | The ID for the collection. |
| published_at | custom_collections.published_at | The time and date (ISO 8601 format) when the collection was made visible. Returns null for a hidden collection. |
| published_scope | custom_collections.published_scope | Whether the collection is published to the Point of Sale channel. Valid values `web` (the collection is published to the Online Store channel but not published to the Point of Sale channel) and `global` (the collection is published to both the Online Store channel and the Point of Sale channel).
 |
| rules | MISSING | An array of rules that define what products go into the smart collection. Each rule (`column` -- `relation` --> `condition`) has these properties: - `column`: the property of a product being used to populate the smart collection. Ex: 'tag', 'type', 'vendor', 'variant_price', etc. - `relation`: The comparitive relationship between the column choice, and the condition ('equals', 'contains', 'greater_than', etc.) - condition: Select products for a smart collection using a condition. Values are either strings or numbers, depending on the relation value. See the [Shopify docs](https://shopify.dev/api/admin-rest/2022-10/resources/smartcollection#resource-object) for more.
 |
| sort_order | custom_collections.sort_order | The order of the products in the collection. Valid values inclide - `alpha-asc`: The products are sorted alphabetically from A to Z. - `alpha-des`: The products are sorted alphabetically from Z to A. - `best-selling`: The products are sorted by number of sales. - `created`: The products are sorted by the date they were created, from oldest to newest. - `created-desc`: The products are sorted by the date they were created, from newest to oldest. - `manual`: The products are manually sorted by the shop owner. - `price-asc`: The products are sorted by price from lowest to highest. - `price-desc`: The products are sorted by price from highest to lowest.
 |
| title | custom_collections.title | The name of the collection |
| updated_at | custom_collections.updated_at | The date and time (ISO 8601 format) when the collection was last modified. |



## order_discount_code




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| discount_codes | shopify | discount_codes |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | discount_codes._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| amount | discount_codes.total_sales.amount | The amount that's deducted from the order total. |
| code | discount_codes.code | This property returns the discount code that was entered at checkout. Otherwise this property returns the title of the discount that was applied. |
| order_id | MISSING | Associated order ID. |
| type | discount_codes.discount_type | The type of discount - `fixed_amount`, `percentage`, or `shipping`. |
| index | MISSING | Pairs with `order_id` to provide unique identifier for order discount code. |



## inventory_item




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| inventory_items | shopify | inventory_items |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc('_fivetran_deleted') }} |
| _fivetran_synced | inventory_items._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| country_code_of_origin | inventory_items.country_code_of_origin | The country code (ISO 3166-1 alpha-2) of where the item came from. |
| created_at | inventory_items.created_at | The date and time (ISO 8601 format) when the inventory item was created. |
| id | inventory_items.id | The ID of the inventory item. |
| province_code_of_origin | inventory_items.province_code_of_origin | The province code (ISO 3166-2 alpha-2) of where the item came from. The province code is only used if the shipping provider for the inventory item is Canada Post. |
| requires_shipping | inventory_items.requires_shipping | Boolean representing whether a customer needs to provide a shipping address when placing an order containing the inventory item. |
| sku | inventory_items.sku | The unique SKU (stock keeping unit) of the inventory item. |
| tracked | inventory_items.tracked | Boolean representing whether inventory levels are tracked for the item. If true, then the inventory quantity changes are tracked by Shopify. |
| updated_at | inventory_items.updated_at | The date and time (ISO 8601 format) when the inventory item was last modified. |
| duplicate_sku_count | inventory_items.duplicate_sku_count | The number of inventory items that share the same SKU with this item. |
| harmonized_system_code | inventory_items.harmonized_system_code | The harmonized system code of the item. |
| inventory_history_url | MISSING | The URL that points to the inventory history for the item. |
| legacy_resource_id | MISSING | The ID of the corresponding resource in the REST Admin API. |
| measurement_id | MISSING | The unique identifier for the inventory item's measurement. |
| measurement_weight_value | MISSING | The weight value of the inventory item's measurement. |
| measurement_weight_unit | MISSING | The unit of measurement for the inventory item's weight. |
| tracked_editable_locked | MISSING | Indicates whether the 'tracked' field for the inventory item is locked from editing. |
| tracked_editable_reason | MISSING | Provides the reason why the 'tracked' field for the inventory item is locked from editing. |
| unit_cost_amount | MISSING | Decimal money amount of the unit cost associated with the inventory item. |
| unit_cost_currency_code | inventory_items.currency_code | Currency of the unit cost associated with the inventory item. |



## discount_code




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| discount_codes | shopify | discount_codes |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | discount_codes._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| code | discount_codes.code | The case-insensitive discount code that customers use at checkout. Shopify recommends this map onto the associated `price_rule.title`. |
| created_at | discount_codes.created_at | The date and time (ISO 8601 format) when the discount code was created. |
| id | discount_codes.id | The ID for the discount code. |
| price_rule_id | discount_codes.price_rule_id | The ID for the price rule that this discount code belongs to. |
| updated_at | discount_codes.updated_at | The date and time (ISO 8601 format) when the discount code was updated. |
| usage_count | discount_codes.usage_count | The number of times that the discount code has been redeemed. |



## order_url_tag




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| metafield_orders | shopify | metafield_orders |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | metafield_orders._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| key | metafield_orders.key | Key of the tag pair. |
| order_id | MISSING | ID of the order url being tagged. |
| value | metafield_orders.value | Value of the tag. |



## abandoned_checkout_discount_code




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| discount_codes | shopify | discount_codes |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | discount_codes._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| amount | MISSING | The amount of the discount in presentment currency. |
| checkout_id | MISSING | ID of the checkout. |
| code | discount_codes.code | The discount code. |
| created_at | discount_codes.created_at | When the checkout discount application was created. |
| discount_id | MISSING | ID of the discount. Deprecated, use `code` instead. |
| index | MISSING | Index (from 1) representing the application of the discount to the checkout. Use the latest (highest index) |
| type | discount_codes.discount_type | The type of discount. Valid values - percentage, shipping, fixed_amount. (default - fixed_amount) |
| updated_at | discount_codes.updated_at | When the checkout's discount was last updated |



## product_tag




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| products | shopify | products |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | products._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| index | MISSING | Index (starting from 1) represnting when the tag was placed on the product. |
| product_id | MISSING | ID of the product being tagged. |
| value | MISSING | Value of the tag. |



## customer




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| customers | shopify | customers |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | customers._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| accepts_marketing | customers.accepts_marketing | Whether the customer has consented to receive marketing material via email. Deprecated and will be coalesced with `email_marketing_consent_state`. |
| created_at | customers.created_at | The date and time when the customer was created. |
| default_address_id | customers.default_address.id | The default address for the customer. |
| email | customers.email | The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error. |
| first_name | customers.first_name | The customer's first name. |
| id | customers.id | A unique identifier for the customer. |
| last_name | customers.last_name | The customer's last name. |
| orders_count | customers.orders_count | The number of orders associated with this customer. |
| phone | customers.phone | The unique phone number (E.164 format) for this customer. Attempting to assign the same phone number to multiple customers returns an error. |
| state | customers.state | The state of the customer's account with a shop. |
| tax_exempt | customers.tax_exempt | Whether the customer is exempt from paying taxes on their order. If true, then taxes won't be applied to an order at checkout. If false, then taxes will be applied at checkout. |
| total_spent | customers.total_spent | The total amount of money that the customer has spent across their order history. |
| updated_at | customers.updated_at | The date and time when the customer information was last updated. |
| verified_email | customers.verified_email | Whether the customer has verified their email address. |
| email_marketing_consent_state | customers.email_marketing_consent.state | The current email marketing state for the customer. New version of `accepts_marketing` field. |
| email_marketing_consent_opt_in_level | customers.email_marketing_consent.opt_in_level | The marketing subscription opt-in level, as described in the M3AAWG Sender Best Common Practices, that the customer gave when they consented to receive marketing material by email. New version of `marketing_opt_in_level` field. |
| email_marketing_consent_consent_updated_at | customers.email_marketing_consent.consent_updated_at | The date and time when the customer consented to receive marketing material by email. If no date is provided, then the date and time when the consent information was sent is used. New version of `accepts_marketing_updated_at` field. |
| accepts_marketing_updated_at | customers.accepts_marketing_updated_at | Deprecated. The package will coalesce with `email_marketing_consent_consent_updated_at`. |
| marketing_opt_in_level | customers.marketing_opt_in_level | Deprecated. The package will coalesce with `email_marketing_consent_opt_in_level`. |
| _fivetran_deleted | MISSING | {{ doc('_fivetran_deleted') }} |
| note | customers.note | A note about the customer. |
| currency | customers.currency | The three-letter code (ISO 4217 format) for the currency that the customer used when they paid for their last order. Defaults to the shop currency. Returns the shop currency for test orders. |



## order_adjustment




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| order_refunds | shopify | order_refunds |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| id | order_refunds.id | The unique numeric identifier for the order adjustment. |
| order_id | order_refunds.order_id | Reference to the order which the adjustment is associated. |
| refund_id | order_refunds.return.id | Reference to the refund which the adjustment is associated. |
| amount | order_refunds.total_duties_set.shop_money.amount | Amount of the adjustment. |
| tax_amount | order_refunds.total_duties_set.presentment_money.amount | Tax amount applied to the order adjustment in shop currency. |
| kind | MISSING | The kind of order adjustment (eg. refund, restock, etc.). |
| reason | order_refunds.note | The reason for the order adjustment. |
| amount_set | order_refunds.total_duties_set | Amount set towards the order adjustment in shop and presentment currencies. |
| tax_amount_set | order_refunds.total_duties_set.presentment_money | Tax amount set towards the order adjustment in shop and presentment currencies. |
| _fivetran_synced | order_refunds._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |



## metafield




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| metafield_shops | shopify | metafield_shops |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | metafield_shops._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| created_at | metafield_shops.created_at | The date and time (ISO 8601 format) when the metafield was created. |
| description | metafield_shops.description | A description of the information that the metafield contains. |
| id | metafield_shops.id | The unique ID of the metafield. |
| key | metafield_shops.key | The key of the metafield. Keys can be up to 64 characters long and can contain alphanumeric characters, hyphens, underscores, and periods. |
| namespace | metafield_shops.namespace | A container for a group of metafields. Grouping metafields within a namespace prevents your metafields from conflicting with other metafields with the same key name. Must have between 3-255 characters. |
| owner_id | metafield_shops.owner_id | The unique ID of the resource that the metafield is attached to. |
| owner_resource | metafield_shops.owner_resource | The type of resource (table) that the metafield is attached to. |
| type | metafield_shops.type | The type of data that the metafield stores in the `value` field. Refer to the [list](https://shopify.dev/apps/metafields/types) of supported types. Use this instead of `value_type`. |
| updated_at | metafield_shops.updated_at | The date and time (ISO 8601 format) when the metafield was last updated. |
| value | metafield_shops.value | The data to store in the metafield. The value is always stored as a string, regardless of the metafield's type. |
| value_type | metafield_shops.value_type | DEPRECATED as of [June 2022](https://fivetran.com/docs/applications/shopify/changelog#june2022). Use `type` instead. |



## customer_tag




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| customers | shopify | customers |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | customers._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| index | MISSING | Index (starting from 1) represnting when the tag was placed on the customer. |
| customer_id | customers.default_address.customer_id | ID of the customer being tagged. |
| value | MISSING | Value of the tag. |



## location




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| locations | shopify | locations |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | locations._airbyte_extracted_at | {{ doc('_fivetran_deleted') }} |
| _fivetran_synced | locations._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| active | locations.active | Boolean representing whether the location is active. If true, then the location can be used to sell products, stock inventory, and fulfill orders.
 |
| address_1 | locations.address1 | The location's street address. |
| address_2 | locations.address2 | The optional second line of the location's street address. |
| city | locations.city | The city the location is in. |
| country | locations.country | The country the location is in (two-letter code). |
| country_code | locations.country_code | The two-letter code (ISO 3166-1 alpha-2 format) corresponding to country the location is in. |
| country_name | locations.country_name | Full name of the location's country. |
| created_at | locations.created_at | The date and time (ISO 8601 format) when the location was created. |
| id | locations.id | The ID of the location. |
| legacy | locations.legacy | Boolean representing whether this is a fulfillment service location. If true, then the location is a fulfillment service location.  If false, then the location was created by the merchant and isn't tied to a fulfillment service.
 |
| localized_country_name | locations.localized_country_name | The localized name of the location's country. |
| localized_province_name | locations.localized_province_name | The localized name of the location's region. Typically a province, state, or district. |
| name | locations.name | The name of the location. |
| phone | locations.phone | The phone number of the location. This value can contain special characters, such as - or +. |
| province | locations.province | The province, state, or district of the location. |
| province_code | locations.province_code | The province, state, or district code (ISO 3166-2 alpha-2 format) of the location. |
| updated_at | locations.updated_at | The date and time (ISO 8601 format) when the location was last updated. |
| zip | locations.zip | The zip or postal code. |



## product_variant




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| product_variants | shopify | product_variants |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| barcode | product_variants.barcode | The barcode, UPC, or ISBN number for the product. |
| compare_at_price | product_variants.compare_at_price | The original price of the item before an adjustment or a sale in shop currency. |
| created_at | product_variants.created_at | The date and time (ISO 8601 format) when the product variant was created. |
| fulfillment_service | MISSING | (DEPRECATED 2025-01-06) The fulfillment service associated with the product variant. |
| grams | product_variants.grams | (DEPRECATED 2025-01-06) The weight of the product variant in grams. |
| id | product_variants.id | The unique numeric identifier for the product variant. |
| image_id | product_variants.image_id | The unique numeric identifier for a product's image. The image must be associated to the same product as the variant. |
| inventory_item_id | product_variants.inventory_item_id | The unique identifier for the inventory item, which is used in the Inventory API to query for inventory information. |
| inventory_management | MISSING | (DEPRECATED 2025-01-06) The fulfillment service that tracks the number of items in stock for the product variant. |
| inventory_policy | product_variants.inventory_policy | Whether customers are allowed to place an order for the product variant when it's out of stock. |
| inventory_quantity | product_variants.inventory_quantity | An aggregate of inventory across all locations. To adjust inventory at a specific location, use the InventoryLevel resource. |
| old_inventory_quantity | product_variants.old_inventory_quantity | (DEPRECATED 2025-01-06) Use the InventoryLevel resource instead. |
| option_1 | product_variants.option1 | (DEPRECATED 2025-01-06) The custom properties that a shop owner uses to define product variants. You can define three options for a product variant: option1, option2, option3.
 |
| option_2 | product_variants.option2 | (DEPRECATED 2025-01-06) The custom properties that a shop owner uses to define product variants. You can define three options for a product variant: option1, option2, option3.
 |
| option_3 | product_variants.option3 | (DEPRECATED 2025-01-06) The custom properties that a shop owner uses to define product variants. You can define three options for a product variant: option1, option2, option3.
 |
| position | product_variants.position | The order of the product variant in the list of product variants. The first position in the list is 1. The position of variants is indicated by the order in which they are listed. |
| price | product_variants.price | The price of the product variant in shop currency. |
| product_id | product_variants.product_id | The unique numeric identifier for the product. |
| requires_shipping | product_variants.requires_shipping | (DEPRECATED 2025-01-06) Use the `requires_shipping` property on the InventoryItem resource instead. |
| sku | product_variants.sku | A unique identifier for the product variant in the shop. Required in order to connect to a FulfillmentService. |
| taxable | product_variants.taxable | Whether a tax is charged when the product variant is sold. |
| tax_code | product_variants.tax_code | This parameter applies only to the stores that have the Avalara AvaTax app installed. Specifies the Avalara tax code for the product variant. |
| title | product_variants.title | The title of the product variant. The title field is a concatenation of the option1, option2, and option3 fields. You can only update title indirectly using the option fields. |
| updated_at | product_variants.updated_at | The date and time when the product variant was last modified. Gets returned in ISO 8601 format. |
| weight | product_variants.weight | (DEPRECATED 2025-01-06) The weight of the product variant in the unit system specified with weight_unit. |
| weight_unit | product_variants.weight_unit | (DEPRECATED 2025-01-06) The unit of measurement that applies to the product variant's weight. If you don't specify a value for weight_unit, then the shop's default unit of measurement is applied. Valid values: g, kg, oz, and lb.
 |
| available_for_sale | product_variants.available_for_sale | Indicates whether the product variant is available for sale. |
| display_name | product_variants.display_name | The display name of the variant, based on the product's title and variant's title. |
| legacy_resource_id | MISSING | The ID of the corresponding resource in the REST Admin API. |
| metafield | MISSING | A custom field, including its namespace and key, that's associated with a Shopify resource for the purposes of adding and storing additional information. |
| requires_components | MISSING | Indicates whether a product variant requires components. |
| sellable_online_quantity | MISSING | The total sellable quantity of the variant for online channels. |
| _fivetran_synced | product_variants._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |



## fulfillment_event




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| fulfillments | shopify | fulfillments |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc('_fivetran_deleted') }} |
| _fivetran_synced | fulfillments._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| address_1 | MISSING | The street address where the fulfillment event occurred. |
| city | fulfillments.origin_address.city | The city where the fulfillment event occurred. |
| country | fulfillments.origin_address.country_code | The country where the fulfillment event occurred. |
| created_at | fulfillments.created_at | The date and time (ISO 8601 format) when the fulfillment event was created. |
| estimated_delivery_at | MISSING | The estimated delivery date based on the fulfillment's tracking number, as long as it's provided by one of the following carriers: USPS, FedEx, UPS, or Canada Post (Canada only).  Value is `null` if no tracking number is available or if the tracking number is from an unsupported carrier. This property is available only when carrier calculated rates are in use.
 |
| fulfillment_id | fulfillments.id | An ID for the fulfillment that's associated with the fulfillment event. |
| happened_at | MISSING | The date and time (ISO 8601 format) when the fulfillment event occurred. |
| id | fulfillments.id | An ID for the fulfillment event. |
| latitude | MISSING | A geographic coordinate specifying the latitude of the fulfillment event. |
| longitude | MISSING | A geographic coordinate specifying the longitude of the fulfillment event. |
| message | MISSING | An arbitrary message describing the status. Can be provided by a shipping carrier. |
| order_id | fulfillments.order_id | The ID of the order that's associated with the fulfillment event. |
| province | fulfillments.origin_address.province_code | The province where the fulfillment event occurred. |
| shop_id | MISSING | An ID for the shop that's associated with the fulfillment event. |
| status | fulfillments.shipment_status | The status of the fulfillment event. Valid values: - label_printed: A label for the shipment was purchased and printed. - label_purchased: A label for the shipment was purchased, but not printed. - attempted_delivery: Delivery of the shipment was attempted, but unable to be completed. - ready_for_pickup: The shipment is ready for pickup at a shipping depot. - picked_up: The fulfillment was successfully picked up. - confirmed: The carrier is aware of the shipment, but hasn't received it yet. - in_transit: The shipment is being transported between shipping facilities on the way to its destination. - out_for_delivery: The shipment is being delivered to its final destination. - delivered: The shipment was successfully delivered. - failure: Something went wrong when pulling tracking information for the shipment, such as the tracking number was invalid or the shipment was canceled.
 |
| updated_at | fulfillments.updated_at | The date and time (ISO 8601 format) when the fulfillment event was updated. |
| zip | fulfillments.origin_address.zip | The zip code of the location where the fulfillment event occurred. |



## order_shipping_tax_line




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| order_refunds | shopify | order_refunds |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | order_refunds._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| index | MISSING | Index (from 1) representing the order of shipping lines per order. |
| order_shipping_line_id | MISSING | ID of the order shipping line this recod is associated with. |
| price | MISSING | The amount of tax, in shop currency, after discounts and before returns. |
| price_set | MISSING | The amount of tax, in shop and presentment currencies, after discounts and before returns (JSON). |
| rate | MISSING | The proportion of the line item price that the tax represents as a decimal. |
| title | MISSING | The name of the tax. |



## tender_transaction




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| tender_transactions | shopify | tender_transactions |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | tender_transactions._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| amount | tender_transactions.amount | The amount of the tender transaction in the shop's currency. |
| currency | tender_transactions.currency | The three-letter code (ISO 4217 format) for the currency used for the tender transaction. |
| id | tender_transactions.id | The ID of the transaction. |
| order_id | tender_transactions.order_id | The ID of the order that the tender transaction belongs to. |
| payment_method | tender_transactions.payment_method | Information about the payment method used for this transaction. Valid values include: - credit_card - cash - android_pay - apple_pay - google_pay - samsung_pay - shopify_pay - amazon - klarna - paypal - unknown - other
 |
| processed_at | tender_transactions.processed_at | The date and time (ISO 8601 format) when the tender transaction was processed. |
| remote_reference | tender_transactions.remote_reference | The remote (gateway) reference associated with the tender. |
| test | tender_transactions.test | Whether the tender transaction is a test transaction. |
| user_id | tender_transactions.user_id | The ID of the user logged into the Shopify POS device that processed the tender transaction, if applicable. |



## abandoned_checkout




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| abandoned_checkouts | shopify | abandoned_checkouts |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc('_fivetran_deleted') }} |
| _fivetran_synced | abandoned_checkouts._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| abandoned_checkout_url | abandoned_checkouts.abandoned_checkout_url | The recovery URL that's sent to a customer so they can recover their checkout. |
| billing_address_address_1 | abandoned_checkouts.billing_address.address1 | The street address of the billing address. |
| billing_address_address_2 | abandoned_checkouts.billing_address.address2 | An optional additional field for the street address of the billing address. |
| billing_address_city | abandoned_checkouts.billing_address.city | The city of the billing address. |
| billing_address_company | abandoned_checkouts.billing_address.company | The company of the person associated with the billing address. |
| billing_address_country | abandoned_checkouts.billing_address.country | The name of the country of the billing address. |
| billing_address_country_code | abandoned_checkouts.billing_address.country_code | The two-letter code (ISO 3166-1 alpha-2 format) for the country of the billing address. |
| billing_address_first_name | abandoned_checkouts.billing_address.first_name | The first name of the person associated with the payment method. |
| billing_address_last_name | abandoned_checkouts.billing_address.last_name | The last name of the person associated with the payment method. |
| billing_address_latitude | abandoned_checkouts.billing_address.latitude | The latitude of the billing address. |
| billing_address_longitude | abandoned_checkouts.billing_address.longitude | The longitude of the billing address. |
| billing_address_name | abandoned_checkouts.billing_address.name | The full name of the person associated with the payment method. |
| billing_address_phone | abandoned_checkouts.billing_address.phone | The phone number at the billing address. |
| billing_address_province | abandoned_checkouts.billing_address.province | The name of the state or province of the billing address. |
| billing_address_province_code | abandoned_checkouts.billing_address.province_code | The two-letter abbreviation of the state or province of the billing address. |
| billing_address_zip | abandoned_checkouts.billing_address.zip | The zip or postal code of the billing address. |
| buyer_accepts_marketing | abandoned_checkouts.buyer_accepts_marketing | Whether the customer would like to receive email updates from the shop. This is set by the 'I want to receive occasional emails about new products, promotions and other news' checkbox during checkout. |
| cart_token | abandoned_checkouts.cart_token | The ID for the cart that's attached to the checkout. |
| closed_at | abandoned_checkouts.closed_at | The date and time (ISO 8601 format) when the checkout was closed. If the checkout was not closed, then this value is null. |
| created_at | abandoned_checkouts.created_at | The date and time (ISO 8601 format) when the checkout was created. |
| currency | abandoned_checkouts.currency | The three-letter code (ISO 4217 format) of the shop's default currency at the time of checkout. For the currency that the customer used at checkout, see `presentment_currency`. |
| customer_id | abandoned_checkouts.customer.default_address.customer_id | ID of the customer with the abandoned checkout. |
| customer_locale | abandoned_checkouts.customer_locale | The two or three-letter language code, optionally followed by a region modifier. Example values - en, en-CA. |
| device_id | abandoned_checkouts.device_id | The ID of the Shopify POS device that created the checkout. |
| email | abandoned_checkouts.email | The customer's email address. |
| gateway | abandoned_checkouts.gateway | The payment gateway used by the checkout. |
| id | abandoned_checkouts.id | The ID for the checkout. |
| landing_site_base_url | abandoned_checkouts.landing_site | The URL for the page where the customer entered the shop. |
| location_id | abandoned_checkouts.location_id | The ID of the physical location where the checkout was processed. |
| name | abandoned_checkouts.name | Checkout order number. |
| note | abandoned_checkouts.note | The text of an optional note that a shop owner can attach to the order. |
| phone | abandoned_checkouts.phone | The customer's phone number for receiving SMS notifications. |
| presentment_currency | abandoned_checkouts.presentment_currency | The three-letter code (ISO 4217 format) of the currency that the customer used at checkout. For the shop's default currency, see `currency`. |
| referring_site | abandoned_checkouts.referring_site | The website that referred the customer to the shop. |
| shipping_address_address_1 | abandoned_checkouts.shipping_address.address1 | The street address of the shipping address. |
| shipping_address_address_2 | abandoned_checkouts.shipping_address.address2 | An optional additional field for the street address of the shipping address. |
| shipping_address_city | abandoned_checkouts.shipping_address.city | The city of the shipping address. |
| shipping_address_company | abandoned_checkouts.shipping_address.company | The company of the person associated with the shipping address. |
| shipping_address_country | abandoned_checkouts.shipping_address.country | The name of the country of the shipping address. |
| shipping_address_country_code | abandoned_checkouts.shipping_address.country_code | The two-letter code (ISO 3166-1 alpha-2 format) for the country of the shipping address. |
| shipping_address_first_name | abandoned_checkouts.shipping_address.first_name | The first name of the person associated with the shipping address. |
| shipping_address_last_name | abandoned_checkouts.shipping_address.last_name | The last name of the person associated with the shipping address. |
| shipping_address_latitude | abandoned_checkouts.shipping_address.latitude | The latitude of the shipping address. |
| shipping_address_longitude | abandoned_checkouts.shipping_address.longitude | The longitude of the shipping address. |
| shipping_address_name | abandoned_checkouts.shipping_address.name | The full name of the person associated with the shipping address. |
| shipping_address_phone | abandoned_checkouts.shipping_address.phone | The phone number at the shipping address. |
| shipping_address_province | abandoned_checkouts.shipping_address.province | The name of the state or province of the shipping address. |
| shipping_address_province_code | abandoned_checkouts.shipping_address.province_code | The two-letter abbreviation of the state or province of the shipping address. |
| shipping_address_zip | abandoned_checkouts.shipping_address.zip | The zip or postal code of the shipping address. |
| source_name | abandoned_checkouts.source_name | Where the checkout originated. Valid values include `web`, `pos`, `iphone`, `android`. |
| subtotal_price | abandoned_checkouts.subtotal_price | The price of the checkout in _presentment_ (customer) currency before shipping and taxes. |
| taxes_included | abandoned_checkouts.taxes_included | Boolean representing whether taxes are included in the price. |
| token | abandoned_checkouts.token | A unique ID for a checkout. |
| total_discounts | abandoned_checkouts.total_discounts | The total amount of discounts to be applied in presentment currency. |
| total_duties | MISSING | The total duties of the checkout in presentment currency. |
| total_line_items_price | abandoned_checkouts.total_line_items_price | The sum of the prices of all line items in the checkout in _presentment_ (customer) currency. |
| total_price | abandoned_checkouts.total_price | The sum of line item prices, all discounts, shipping costs, and taxes for the checkout in _presentment_ (customer) currency. |
| total_tax | abandoned_checkouts.total_tax | The sum of all the taxes applied to the checkout in _presentment_ (customer) currency. |
| total_weight | abandoned_checkouts.total_weight | The sum of all the weights in grams of the line items in the checkout. |
| updated_at | abandoned_checkouts.updated_at | The date and time (ISO 8601 format) when the checkout was last modified. |
| user_id | abandoned_checkouts.user_id | The ID of the user who created the checkout. |



## product_image




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| product_images | shopify | product_images |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc('_fivetran_deleted') }} |
| _fivetran_synced | product_images._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| created_at | product_images.created_at | (DEPRECATED 2025-01-06) The date and time when the product image was created. The API returns this value in ISO 8601 format. |
| height | product_images.height | Height dimension of the image which is determined on upload. |
| id | product_images.id | Unique numeric identifier of the product image. |
| position | product_images.position | (DEPRECATED 2025-01-06) The order of the product image in the list. The first product image is at position 1 and is the "main" image for the product. |
| product_id | product_images.product_id | The id of the product associated with the image. |
| src | product_images.src | (DEPRECATED 2025-01-06) Specifies the location of the product image. This parameter supports URL filters that you can use to retrieve modified copies of the image. |
| updated_at | product_images.updated_at | (DEPRECATED 2025-01-06) The date and time when the product image was last modified. The API returns this value in ISO 8601 format. |
| variant_ids | product_images.variant_ids | (DEPRECATED 2025-01-06) An array of variant ids associated with the image. |
| width | product_images.width | Width dimension of the image which is determined on upload. |
| alt_text | product_images.alt | A word or phrase to share the nature or contents of an image. |
| media_id | MISSING | The unique identifier for the media associated with the product image. |
| status | MISSING | The status of the product image, indicating its availability or processing state. |
| url | product_images.shop_url | The URL of the product image. |



## order_line




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| orders | shopify | orders |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | orders._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| fulfillable_quantity | MISSING | The amount available to fulfill, calculated as follows: quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity |
| fulfillment_status | orders.fulfillment_status | How far along an order is in terms line items fulfilled. |
| gift_card | MISSING | Whether the item is a gift card. If true, then the item is not taxed or considered for shipping charges. |
| grams | MISSING | The weight of the item in grams. |
| id | orders.id | The ID of the line item. |
| name | orders.name | The name of the product variant. |
| order_id | MISSING | The ID of the related order. |
| price | MISSING | The price of the item before discounts have been applied in the shop currency. |
| product_id | MISSING | The ID of the product that the line item belongs to. Can be null if the original product associated with the order is deleted at a later date. |
| quantity | MISSING | The number of items that were purchased. |
| requires_shipping | MISSING | Whether the item requires shipping. |
| sku | MISSING | The item's SKU (stock keeping unit). |
| taxable | MISSING | Whether the item was taxable. |
| title | MISSING | The title of the product. |
| total_discount | MISSING | The total amount of the discount allocated to the line item in the shop currency. |
| variant_id | MISSING | The ID of the product variant. |
| vendor | MISSING | The name of the item's supplier. |
| index | MISSING | Index of the order line. |
| pre_tax_price | MISSING | The pre tax price of the line item in shop currency. |
| pre_tax_price_set | MISSING | The pre tax price of the line item in shop currency and presentment currency. |
| price_set | MISSING | The price of the line item in shop and presentment currencies. |
| tax_code | MISSING | Tax code applied to the line item. As multiple taxes can apply to a line item, we recommend referring to `stg_shopify__tax_line`. |
| total_discount_set | MISSING | The total amount allocated to the line item in the presentment currency. |
| variant_title | MISSING | The title of the product variant. |
| variant_inventory_management | MISSING | The fulfillment service that tracks the number of items in stock for the product variant. |
| properties | MISSING | Line item properties. |



## shop




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| shop | shopify | shop |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | {{ doc('_fivetran_deleted') }} |
| _fivetran_synced | shop._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| address_1 | shop.address1 | The shop's street address. |
| address_2 | shop.address2 | The optional second line of the shop's street address. |
| checkout_api_supported | shop.checkout_api_supported | Boolean representing whether the shop is capable of accepting payments directly through the Checkout API. |
| city | shop.city | The shop's city. |
| cookie_consent_level | shop.cookie_consent_level | The cookie consent level defined on the shop's online store. |
| country | shop.country | The shop's country. In most cases, this value matches the country_code. |
| country_code | shop.country_code | The two-letter country code corresponding to the shop's country. |
| country_name | shop.country_name | The shop's normalized country name. |
| county_taxes | shop.county_taxes | Boolean representing whether the shop is applying taxes on a per-county basis. Only applicable to shops based in the US. Either `true` or `null` (not false, according to Shopify API docs). |
| created_at | shop.created_at | The date and time (ISO 8601) when the shop was created. |
| currency | shop.currency | The three-letter code (ISO 4217 format) for the shop's default currency. |
| customer_email | shop.customer_email | The contact email used for communication between the shop owner and the customer. |
| domain | shop.domain | The shop's domain. |
| eligible_for_card_reader_giveaway | shop.eligible_for_card_reader_giveaway | Boolean representing whether the shop is eligible to receive a free credit card reader from Shopify. |
| eligible_for_payments | shop.eligible_for_payments | Boolean representing whether the shop is eligible to use Shopify Payments. |
| email | shop.email | The contact email used for communication between Shopify and the shop owner. |
| enabled_presentment_currencies | shop.enabled_presentment_currencies | An array of of enabled currencies (ISO 4217 format) that the shop accepts. Merchants can enable currencies from their Shopify Payments settings in the Shopify Admin. |
| force_ssl | shop.force_ssl | DEPRECATED. |
| google_apps_domain | shop.google_apps_domain | The GSuite URL for the store, if applicable. |
| google_apps_login_enabled | shop.google_apps_login_enabled | Boolean representing whether the GSuite login is enabled. Shops with this feature will be able to log in through the GSuite login page. Valid values are `true` and `null`. |
| has_discounts | shop.has_discounts | Boolean representing whether any active discounts exist for the shop. |
| has_gift_cards | shop.has_gift_cards | Boolean representing whether any active gift cards exist for the shop. |
| has_storefront | shop.has_storefront | Boolean representing whether this shop has an online store. |
| iana_timezone | shop.iana_timezone | The name of the timezone assigned by the [IANA](https://www.iana.org/time-zones). |
| id | shop.id | The ID for the shop. A 64-bit unsigned integer. |
| latitude | shop.latitude | The latitude of the shop's location. |
| longitude | shop.longitude | The longitude of the shop's location. |
| money_format | shop.money_format | A string representing the way currency is formatted when the currency isn't specified. |
| money_in_emails_format | shop.money_in_emails_format | A string representing the way currency is formatted in email notifications when the currency isn't specified. |
| money_with_currency_format | shop.money_with_currency_format | A string representing the way currency is formatted when the currency is specified. |
| money_with_currency_in_emails_format | shop.money_with_currency_in_emails_format | A string representing the way currency is formatted in email notifications when the currency is specified. |
| multi_location_enabled | shop.multi_location_enabled | DEPRECATED and hard-coded to `true`. |
| myshopify_domain | shop.myshopify_domain | The shop's .myshopify.com domain. |
| name | shop.name | The name of the shop. |
| password_enabled | shop.password_enabled | Boolean representing whether the password protection page is enabled on the shop's online store. |
| phone | shop.phone | The contact phone number for the shop. |
| plan_display_name | shop.plan_display_name | The display name of the Shopify plan the shop is on. |
| plan_name | shop.plan_name | The name of the Shopify plan the shop is on. |
| pre_launch_enabled | shop.pre_launch_enabled | Boolen representing whether the pre-launch page is enabled on the shop's online store. |
| primary_locale | shop.primary_locale | The shop's primary locale, as configured in the language settings of the shop's theme. |
| primary_location_id | shop.primary_location_id | DEPRECATED. Formerly used for the ID of the shipping origin location. |
| province | shop.province | The shop's normalized province or state name. |
| province_code | shop.province_code | The two- or three-letter code for the shop's province or state. |
| requires_extra_payments_agreement | shop.requires_extra_payments_agreement | Boolean representing whether the shop requires an extra Shopify Payments agreement. |
| setup_required | shop.setup_required | Boolean representing whether the shop has any outstanding setup steps. |
| shop_owner | shop.shop_owner | The username of the shop owner. |
| source | shop.source | The handle of the partner account that referred the merchant to Shopify, if applicable. |
| tax_shipping | shop.tax_shipping | Boolean representing whether taxes are charged for shipping. Valid values are true or false. |
| taxes_included | shop.taxes_included | Boolean representing whether applicable taxes are included in product prices. Valid values are true or null. |
| timezone | shop.timezone | The name of the timezone the shop is in. |
| updated_at | shop.updated_at | The date and time (ISO 8601) when the shop was last updated. |
| weight_unit | shop.weight_unit | The default unit of weight measurement for the shop. |
| zip | shop.zip | The shop's zip or postal code. |



## inventory_quantity




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| inventory_levels | shopify | inventory_levels |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| id | inventory_levels.id | The unique identifier for the record. |
| inventory_item_id | inventory_levels.inventory_item_id | The ID of the inventory item associated with this record. |
| inventory_level_id | inventory_levels.location_id | The ID of the inventory level where this item is stored. |
| name | inventory_levels.locations_count | The name of the inventory state associated with the record. [Link to list of expected values](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps#inventory-states). |
| quantity | inventory_levels.available | The available quantity of the inventory item. |
| updated_at | inventory_levels.updated_at | The timestamp of the last update to the inventory record. |
| _fivetran_synced | inventory_levels._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |



## order_tag




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| orders | shopify | orders |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | orders._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| index | MISSING | Index (starting from 1) represnting when the tag was placed on the order. |
| order_id | orders.id | ID of the order being tagged. |
| value | MISSING | Value of the tag. |



## inventory_level




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| inventory_levels | shopify | inventory_levels |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | inventory_levels._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| available | inventory_levels.available | (DEPRECATED 2025-01-06) The available quantity of an inventory item at the inventory level's associated location. Returns null if the inventory item is not tracked. |
| inventory_item_id | inventory_levels.inventory_item_id | The ID of the inventory item associated with the inventory level. |
| location_id | inventory_levels.location_id | The ID of the location that the inventory level belongs to. |
| updated_at | inventory_levels.updated_at | The date and time (ISO 8601 format) when the inventory level was last modified. |
| id | inventory_levels.id | A globally unique identifier for the inventory level. |
| can_deactivate | inventory_levels.can_deactivate | Indicates whether the inventory item can be deactivated at the location. |
| created_at | inventory_levels.created_at | The date and time when the inventory level was created. |
| deactivation_alert | inventory_levels.deactivation_alert | Provides an alert message when the inventory item is deactivated at the location. |



## fulfillment




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| fulfillments | shopify | fulfillments |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | fulfillments._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| created_at | fulfillments.created_at | The date and time when the fulfillment was created. The API returns this value in ISO 8601 format. |
| id | fulfillments.id | The ID for the fulfillment. |
| location_id | fulfillments.location_id | The unique identifier of the location that the fulfillment was processed at. |
| name | fulfillments.name | The uniquely identifying fulfillment name, consisting of two parts separated by a .. The first part represents the order name and the second part represents the fulfillment number.  The fulfillment number automatically increments depending on how many fulfillments are in an order (e.g. #1001.1, #1001.2).
 |
| order_id | fulfillments.order_id | The unique numeric identifier for the order. |
| receipt_authorization | fulfillments.receipt.authorization | The authorization code from the receipt. |
| service | fulfillments.service | The fulfillment service associated with the fulfillment. |
| shipment_status | fulfillments.shipment_status | The current shipment status of the fulfillment. Valid values include: - label_printed: A label for the shipment was purchased and printed. - label_purchased: A label for the shipment was purchased, but not printed. - attempted_delivery: Delivery of the shipment was attempted, but unable to be completed. - ready_for_pickup: The shipment is ready for pickup at a shipping depot. - confirmed: The carrier is aware of the shipment, but hasn't received it yet. - in_transit: The shipment is being transported between shipping facilities on the way to its destination. - out_for_delivery: The shipment is being delivered to its final destination. - delivered: The shipment was succesfully delivered. - failure: Something went wrong when pulling tracking information for the shipment, such as the tracking number was invalid or the shipment was canceled.
 |
| status | fulfillments.status | The status of the fulfillment. Valid values include: - pending: Shopify has created the fulfillment and is waiting for the third-party fulfillment service to transition it to 'open' or 'success'. - open: The fulfillment has been acknowledged by the service and is in processing. - success: The fulfillment was successful. - cancelled: The fulfillment was cancelled. - error: There was an error with the fulfillment request. - failure: The fulfillment request failed.
 |
| tracking_company | fulfillments.tracking_company | The name of the tracking company. |
| tracking_number | fulfillments.tracking_number | Primary tracking number for the order. |
| tracking_numbers | fulfillments.tracking_numbers | A list of tracking numbers, provided by the shipping company. |
| tracking_urls | fulfillments.tracking_urls | The URLs of tracking pages for the fulfillment. |
| updated_at | fulfillments.updated_at | The date and time (ISO 8601 format) when the fulfillment was last modified. |



## order_line_refund




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| order_refunds | shopify | order_refunds |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | order_refunds._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| id | order_refunds.id | The unique identifier of the line item in the refund. |
| location_id | MISSING | TThe unique identifier of the location where the items will be restockedBD |
| order_line_id | MISSING | The ID of the related line item in the order. |
| quantity | MISSING | The quantity of the associated line item that was returned. |
| refund_id | MISSING | The ID of the related refund. |
| restock_type | order_refunds.restock | How this refund line item affects inventory levels. |
| subtotal | MISSING | Subtotal amount of the order line refund in shop currency. |
| total_tax | MISSING | The total tax applied to the refund in shop currency. |
| subtotal_set | MISSING | The subtotal of the refund line item in shop and presentment currencies. |
| total_tax_set | MISSING | The total tax of the line item in shop and presentment currencies. |



## price_rule




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| price_rules | shopify | price_rules |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | price_rules._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| allocation_limit | price_rules.allocation_limit | The number of times the discount can be allocated on the cart - if eligible. For example a Buy 1 hat Get 1 hat for free discount can be applied 3 times on a cart having more than 6 hats,  where maximum of 3 hats get discounted - if the allocation_limit is 3. Empty (null) allocation_limit means unlimited number of allocations.
 |
| allocation_method | price_rules.allocation_method | The allocation method of the price rule. Valid values include `each` (the discount is applied to each of the entitled items. For example, for a price rule that takes $15 off, each entitled line item in a checkout will be discounted by $15) and `across` (the calculated discount amount will be applied across the entitled items. For example, for a price rule that takes $15 off, the discount will be applied across all the entitled items).
 |
| created_at | price_rules.created_at | The date and time (ISO 8601 format) when the price rule was created. |
| customer_selection | price_rules.customer_selection | The customer selection for the price rule. Valid values include `all` (the price rule is valid for all customers) and `prerequisite`  (the customer must either belong to one of the customer segments specified by customer_segment_prerequisite_ids, or be one of the customers specified by prerequisite_customer_ids).
 |
| ends_at | price_rules.ends_at | The date and time (ISO 8601 format) when the price rule ends. Must be after starts_at. |
| id | price_rules.id | The ID for the price rule. |
| once_per_customer | price_rules.once_per_customer | Boolean representing whether the generated discount code will be valid only for a single use per customer. This is tracked using customer ID. |
| prerequisite_quantity_range | price_rules.prerequisite_quantity_range | If `customer_selection` is `prerequisite`, the minimum number of items for the price rule to be applicable. The quantity of an entitled cart item must be greater than or equal to this value. |
| prerequisite_shipping_price_range | price_rules.prerequisite_shipping_price_range | If `customer_selection` is `prerequisite`, the maximum shipping price for the price rule to be applicable. The shipping price must be less than or equal to this value |
| prerequisite_subtotal_range | price_rules.prerequisite_subtotal_range | If `customer_selection` is `prerequisite`, the minimum subtotal for the price rule to be applicable. The subtotal of the entitled cart items must be greater than or equal to this value for the discount to apply. |
| prerequisite_to_entitlement_purchase_prerequisite_amount | price_rules.prerequisite_to_entitlement_purchase.prerequisite_amount | If `customer_selection` is `prerequisite`, the prerequisite purchase for a Buy X Get Y discount. The minimum purchase amount required to be entitled to the discount. |
| quantity_ratio_entitled_quantity | price_rules.prerequisite_to_entitlement_quantity_ratio.entitled_quantity | If `customer_selection` is `prerequisite`, in a Buy/Get ratio for a Buy X Get Y discount, this is the offered 'get' quantity. |
| quantity_ratio_prerequisite_quantity | price_rules.prerequisite_to_entitlement_quantity_ratio.prerequisite_quantity | If `customer_selection` is `prerequisite`, in a Buy/Get ratio for a Buy X Get Y discount, this defines the necessary 'buy' quantity. |
| starts_at | price_rules.starts_at | The date and time (ISO 8601 format) when the price rule starts. |
| target_selection | price_rules.target_selection | The target selection method of the price rule. Valid values include `all` (the price rule applies the discount to all line items in the checkout) and  `entitled` (the price rule applies the discount to selected entitlements only).
 |
| target_type | price_rules.target_type | The target type that the price rule applies to. Valid values include `line_item` (the price rule applies to the cart's line items) and `shipping_line` (the price rule applies to the cart's shipping lines). |
| title | price_rules.title | The title of the price rule. This is used by the Shopify admin search to retrieve discounts. It is also displayed on the Discounts page of the Shopify admin for bulk discounts.  Shopify recommends that this map onto the associated `discount_code.code`.
 |
| updated_at | price_rules.updated_at | The date and time (ISO 8601 format) when the price rule was updated. |
| usage_limit | price_rules.usage_limit | The maximum number of times the price rule can be used, per discount code. |
| value | price_rules.value | The value of the price rule. If if the value of `target_type` is `shipping_line`, then only -100 is accepted. The value must be negative. |
| value_type | price_rules.value_type | The value type of the price rule. Valid values include `fixed_amount` (applies a discount of value as a unit of the store's currency. For example, if value is -30 and the store's currency is USD, then $30 USD is deducted when the discount is applied) and `percentage` (applies a percentage discount of value. For example, if value is -30, then 30% will be deducted when the discount is applied).
If `target_type` is `shipping_line`, then only `percentage` is accepted.
 |



## transaction




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| transactions | shopify | transactions |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| id | transactions.id | The ID for the transaction. |
| order_id | transactions.order_id | The ID for the order that the transaction is associated with. |
| refund_id | MISSING | The ID associated with a refund in the refund table. |
| amount | transactions.amount | The amount of money included in the transaction. |
| authorization | transactions.authorization | The authorization code associated with the transaction. |
| created_at | transactions.created_at | The date and time when the transaction was created. |
| processed_at | transactions.processed_at | The date and time when a transaction was processed. |
| device_id | transactions.device_id | The ID for the device. |
| gateway | transactions.gateway | The name of the gateway the transaction was issued through. |
| source_name | transactions.source_name | The origin of the transaction. |
| message | transactions.message | A string generated by the payment provider with additional information about why the transaction succeeded or failed. |
| currency | transactions.currency | The three-letter code (ISO 4217 format) for the currency used for the payment. |
| location_id | transactions.location_id | The ID of the physical location where the transaction was processed. |
| parent_id | transactions.parent_id | The ID of an associated transaction. |
| payment_avs_result_code | transactions.payment_details.avs_result_code | The response code from the address verification system. |
| payment_credit_card_bin | transactions.payment_details.credit_card_bin | The issuer identification number (IIN), formerly known as bank identification number (BIN) of the customer's credit card. |
| payment_cvv_result_code | transactions.payment_details.cvv_result_code | The response code from the credit card company indicating whether the customer entered the card security code, or card verification value, correctly. |
| payment_credit_card_number | transactions.payment_details.credit_card_number | The customer's credit card number, with most of the leading digits redacted. |
| payment_credit_card_company | transactions.payment_details.credit_card_company | The name of the company that issued the customer's credit card. |
| kind | transactions.kind | The transaction's type. |
| receipt | transactions.receipt | A transaction receipt attached to the transaction by the gateway. |
| currency_exchange_id | MISSING | The ID of the adjustment. |
| currency_exchange_adjustment | MISSING | The difference between the amounts on the associated transaction and the parent transaction. |
| currency_exchange_original_amount | MISSING | The amount of the parent transaction in the shop currency. |
| currency_exchange_final_amount | MISSING | The amount of the associated transaction in the shop currency. |
| currency_exchange_currency | MISSING | The shop currency. |
| error_code | transactions.error_code | A standardized error code, independent of the payment provider. |
| status | transactions.status | The status of the transaction. |
| test | transactions.test | Whether the transaction is a test transaction. |
| user_id | transactions.user_id | The ID for the user who was logged into the Shopify POS device when the order was processed, if applicable. |
| _fivetran_synced | transactions._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| authorization_expires_at | MISSING | The date and time (ISO 8601 format) when the Shopify Payments authorization expires. |



## refund




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| order_refunds | shopify | order_refunds |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| id | order_refunds.id | The unique numeric identifier for the refund. |
| created_at | order_refunds.created_at | Timestamp of the date when the refund was created. |
| processed_at | order_refunds.processed_at | Timestamp of the date when the refund was processed. |
| note | order_refunds.note | User generated note attached to the refund. |
| restock | order_refunds.restock | Boolean indicating if the refund is a result of a restock. |
| user_id | order_refunds.user_id | Reference to the user id which generated the refund. |
| _fivetran_synced | order_refunds._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| total_duties_set | order_refunds.total_duties_set | Record representing total duties set for the refund. |
| order_id | order_refunds.order_id | Reference to the order which the refund is associated. |



## abandoned_checkout_shipping_line




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| abandoned_checkouts | shopify | abandoned_checkouts |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | abandoned_checkouts._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| carrier_identifier | MISSING | A reference to the carrier service that provided the rate. Present when the rate was computed by a third-party carrier service. |
| checkout_id | MISSING | ID of the checkout that was abandoned. |
| code | MISSING | A reference to the shipping method. |
| delivery_category | MISSING | The general classification of the delivery method. |
| delivery_expectation_range | MISSING | Expected delivery date range. |
| delivery_expectation_range_max | MISSING | Latest expected delivery date. |
| delivery_expectation_range_min | MISSING | Earliest possible expected delivery date. |
| delivery_expectation_type | MISSING | Type of expected delivery. |
| discounted_price | MISSING | The pre-tax shipping price with discounts applied in _presentment_ (customer) currency. |
| id | MISSING | Unique ID of the abandoned checkout shipping line. |
| index | MISSING | Index of the line amongst shipping lines for this checkout. |
| original_shop_price | MISSING | The pre-tax shipping price without any discounts applied in _presentment_ (customer) currency. |
| phone | MISSING | The phone number at the shipping address. |
| price | MISSING | The price of the shipping method in presentment currency. |
| requested_fulfillment_service_id | MISSING | The fulfillment service requested for the shipping method. Present if the shipping method requires processing by a third party fulfillment service. |
| source | MISSING | The channel where the checkout originated. Example value - shopify. |
| title | MISSING | The title of the shipping method. Example value - International Shipping. |



## collection_product




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| collects | shopify | collects |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | collects._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| collection_id | collects.collection_id | ID referencing the `collection` the product belongs to. |
| product_id | collects.product_id | ID referencing the `product`. |



## tax_line




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| transactions | shopify | transactions |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | transactions._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| index | MISSING | The index of the tax line. |
| order_line_id | MISSING | The order line that this tax line is associated with. |
| price | transactions.amount | The amount of tax, in shop currency, after discounts and before returns. |
| price_set | transactions.total_unsettled_set | The amount of tax, in shop and presentment currencies, after discounts and before returns. |
| rate | MISSING | The proportion of the line item price that the tax represents as a decimal. |
| title | transactions.source_name | The name of the tax. |



## product




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| products | shopify | products |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_deleted | MISSING | Whether the record has been deleted in the source system. |
| _fivetran_synced | products._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| created_at | products.created_at | The date and time when the product was created. |
| handle | products.handle | A unique human-friendly string for the product. Automatically generated from the product's title. |
| id | products.id | An unsigned 64-bit integer that's used as a unique identifier for the product. Each id is unique across the Shopify system. No two products will have the same id, even if they're from different shops. |
| product_type | products.product_type | A categorization for the product used for filtering and searching products. |
| published_at | products.published_at | The date and time (ISO 8601 format) when the product was published. Can be set to null to unpublish the product from the Online Store channel. |
| published_scope | products.published_scope | Whether the product is published to the Point of Sale channel. |
| title | products.title | The name of the product. |
| updated_at | products.updated_at | The date and time when the product was last modified. |
| vendor | products.vendor | The name of the product's vendor. |
| status | products.status | The status of the product. Valid values: - active: The product is ready to sell and is available to customers on the online store, sales channels, and apps. By default, existing products are set to active. - archived: The product is no longer being sold and isn't available to customers on sales channels and apps. - draft: The product isn't ready to sell and is unavailable to customers on sales channels and apps. By default, duplicated and unarchived products are set to draft.
 |



## order




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| orders | shopify | orders |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | orders._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| app_id | orders.app_id | The ID of the app that created the order. |
| billing_address_address_1 | orders.billing_address.address1 | The street address of the billing address. |
| billing_address_address_2 | orders.billing_address.address2 | An optional additional field for the street address of the billing address. |
| billing_address_city | orders.billing_address.city | The city, town, or village of the billing address. |
| billing_address_company | orders.billing_address.company | The company of the person associated with the billing address. |
| billing_address_country | orders.billing_address.country | The name of the country of the billing address. |
| billing_address_country_code | orders.billing_address.country_code | The two-letter code (ISO 3166-1 format) for the country of the billing address. |
| billing_address_first_name | orders.billing_address.first_name | The first name of the person associated with the payment method. |
| billing_address_last_name | orders.billing_address.last_name | The last name of the person associated with the payment method. |
| billing_address_latitude | orders.billing_address.latitude | The latitude of the billing address. |
| billing_address_longitude | orders.billing_address.longitude | The longitude of the billing address. |
| billing_address_name | orders.billing_address.name | The full name of the person associated with the payment method. |
| billing_address_phone | orders.billing_address.phone | The phone number at the billing address. |
| billing_address_province | orders.billing_address.province | The name of the region (province, state, prefecture, …) of the billing address. |
| billing_address_province_code | orders.billing_address.province_code | The two-letter abbreviation of the region of the billing address. |
| billing_address_zip | orders.billing_address.zip | The postal code (zip, postcode, Eircode, …) of the billing address. |
| browser_ip | orders.browser_ip | The IP address of the browser used by the customer when they placed the order. |
| buyer_accepts_marketing | orders.buyer_accepts_marketing | Whether the customer consented to receive email updates from the shop. |
| cancel_reason | orders.cancel_reason | The reason why the order was canceled. |
| cancelled_at | orders.cancelled_at | The date and time when the order was canceled. |
| cart_token | orders.cart_token | The ID of the cart that's associated with the order. |
| closed_at | orders.closed_at | The date and time when the order was closed (archived). |
| created_at | orders.created_at | The autogenerated date and time when the order was created in Shopify. |
| currency | orders.currency | The three-letter code for the shop currency. |
| customer_id | MISSING | The ID of the order's customer. |
| email | orders.email | The customer's email address. |
| financial_status | orders.financial_status | The status of payments associated with the order. Can only be set when the order is created |
| fulfillment_status | orders.fulfillment_status | The order's status in terms of fulfilled line items. |
| id | orders.id | The ID of the order, used for API purposes. This is different from the order_number property, which is the ID used by the shop owner and customer. |
| landing_site_base_url | orders.landing_site | The URL for the page where the buyer landed when they entered the shop. |
| location_id | orders.location_id | The ID of the physical location where the order was processed. |
| name | orders.name | The order name, generated by combining the order_number property with the order prefix and suffix that are set in the merchant's general settings. |
| note | orders.note | An optional note that a shop owner can attach to the order. |
| number | orders.number | The order's position in the shop's count of orders. Numbers are sequential and start at 1. |
| order_number | orders.order_number | The order 's position in the shop's count of orders starting at 1001. Order numbers are sequential and start at 1001. |
| processed_at | orders.processed_at | The date and time when an order was processed. This value is the date that appears on your orders and that's used in the analytic reports. |
| referring_site | orders.referring_site | The website where the customer clicked a link to the shop. |
| shipping_address_address_1 | orders.shipping_address.address1 | The street address of the shipping address. |
| shipping_address_address_2 | orders.shipping_address.address2 | An optional additional field for the street address of the shipping address. |
| shipping_address_city | orders.shipping_address.city | The city, town, or village of the shipping address. |
| shipping_address_company | orders.shipping_address.company | The company of the person associated with the shipping address. |
| shipping_address_country | orders.shipping_address.country | The name of the country of the shipping address. |
| shipping_address_country_code | orders.shipping_address.country_code | The two-letter code (ISO 3166-1 format) for the country of the shipping address. |
| shipping_address_first_name | orders.shipping_address.first_name | The first name of the person associated with the shipping address. |
| shipping_address_last_name | orders.shipping_address.last_name | The last name of the person associated with the shipping address. |
| shipping_address_latitude | orders.shipping_address.latitude | The latitude of the shipping address. |
| shipping_address_longitude | orders.shipping_address.longitude | The longitude of the shipping address. |
| shipping_address_name | orders.shipping_address.name | The full name of the person associated with the payment method. |
| shipping_address_phone | orders.shipping_address.phone | The phone number at the shipping address. |
| shipping_address_province | orders.shipping_address.province | The name of the region (province, state, prefecture, …) of the shipping address. |
| shipping_address_province_code | orders.shipping_address.province_code | The two-letter abbreviation of the region of the shipping address. |
| shipping_address_zip | orders.shipping_address.zip | The postal code (zip, postcode, Eircode, …) of the shipping address. |
| source_name | orders.source_name | Where the order originated. Can be set only during order creation, and is not writeable afterwards. |
| subtotal_price | orders.subtotal_price | The price of the order in the shop currency after discounts but before shipping, taxes, and tips in the shop currency. |
| taxes_included | orders.taxes_included | Whether taxes are included in the order subtotal. |
| test | orders.test | Whether this is a test order. |
| token | orders.token | A unique token for the order. |
| total_discounts | orders.total_discounts | The total discounts applied to the price of the order in the shop currency. |
| total_line_items_price | orders.total_line_items_price | The sum of all line item prices in the shop currency. |
| total_price | orders.total_price | The sum of all line item prices, discounts, shipping, taxes, and tips in the shop currency. Must be positive. |
| total_tax | orders.total_tax | The sum of all the taxes applied to the order in th shop currency. Must be positive. |
| total_weight | orders.total_weight | The sum of all line item weights in grams. |
| updated_at | orders.updated_at | The date and time (ISO 8601 format) when the order was last modified. |
| user_id | orders.user_id | The ID of the user logged into Shopify POS who processed the order, if applicable. |
| checkout_token | orders.checkout_token | A unique value when referencing the checkout that's associated with the order. |
| confirmed | MISSING | Whether inventory has been reserved for the order. |
| customer_locale | orders.customer_locale | A two-letter or three-letter language code, optionally followed by a region modifier. |
| checkout_id | orders.checkout_id | ID of the order's checkout. |
| order_status_url | orders.order_status_url | The URL pointing to the order status web page, if applicable. |
| _fivetran_deleted | MISSING | {{ doc('_fivetran_deleted') }} |
| total_tip_received | orders.total_tip_received | The sum of all the tips in the order in the shop currency. |
| device_id | orders.device_id | The ID for the device. |
| presentment_currency | MISSING | The presentment currency that was used to display prices to the customer. |
| total_shipping_price_set | orders.total_shipping_price_set | The total shipping price of the order, excluding discounts and returns, in shop and presentment currencies. If taxes_included is set to true, then total_shipping_price_set includes taxes. |
| client_details_user_agent | orders.client_details.user_agent | Details of the browsing client, including software and operating versions. |
| total_tax_set | orders.total_tax_set | The total tax applied to the order in shop and presentment currencies. |
| total_discounts_set | orders.total_discounts_set | The total discounts applied to the price of the order in shop and presentment currencies. |
| total_line_items_price_set | orders.total_line_items_price_set | The total of all line item prices in shop and presentment currencies. |
| total_price_set | orders.total_price_set | The total price of the order in shop and presentment currencies. |
| is_confirmed | orders.confirmed | Whether the order is confirmed. |
| source_identifier | orders.source_identifier | The ID of the order placed on the originating platform. This value doesn't correspond to the Shopify ID that's generated from a completed draft. |



## order_shipping_line




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| fulfillments | shopify | fulfillments |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | fulfillments._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| carrier_identifier | MISSING | A reference to the carrier service that provided the rate. Present when the rate was computed by a third-party carrier service. |
| code | MISSING | A reference to the shipping method. |
| delivery_category | MISSING | The general classification of the delivery method. |
| discounted_price | MISSING | The pre-tax shipping price with discounts applied in the shop currency. |
| discounted_price_set | MISSING | The pre-tax shipping price with discounts applied (JSON) in presentment and shop currencies. |
| id | fulfillments.id | A globally-unique identifier. |
| order_id | fulfillments.order_id | ID of the associated order. |
| phone | MISSING | The phone number at the shipping address. |
| price | MISSING | Returns the price of the shipping line in shop currency. |
| price_set | MISSING | Returns the price of the shipping line (JSON) in presentment and shop currencies. |
| requested_fulfillment_service_id | MISSING | The fulfillment service requested for the shipping method. Present if the shipping method requires processing by a third party fulfillment service. |
| source | MISSING | Returns the rate source for the shipping line. |
| title | fulfillments.name | Returns the title of the shipping line. |



## order_note_attribute




### Source Tables

| Alias | Schema | Table |
| --- | --- | --- |
| orders | shopify | orders |


### Fields

| Name | Expression | Description |
| --- | --- | --- |
| _fivetran_synced | orders._airbyte_extracted_at | {{ doc('_fivetran_synced') }} |
| name | orders.name | Name of the attribute. |
| order_id | orders.id | ID referencing the order the note attribute belongs to. |
| value | MISSING | Value of the attribute. |


