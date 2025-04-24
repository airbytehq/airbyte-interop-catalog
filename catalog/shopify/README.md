# Mapping Guide: Airbyte-to-Fivetran

The below guide will help you map Airbyte schemas to corresponding Fivetran schemas. Guidance is AI-generated and includes confidence scores (with explanation) for each table and field mapping.

## Companion Project for `dbt` Users

Please see the companion [airbyte-interop-dbt-project](./airbyte-interop-dbt-project) directory, which contains a `dbt` project with ready-to-use SQL models for each of the below mappings.

## Table-Level Mappings

### How to Use these Mappings

The below guides, and the companion dbt project, will help you shape your new Airbyte datasets to more closely match your legacy Fivetran dataset schemas.

This can be helpful if:

1. You have existing code that relies on Fivetran-shaped datasets.
2. You have one or more dependencies on Fivetran-managed dbt packages.
3. You have custom code that needs to be updated to leverage Airbyte data schemas, where you previously ingested Fivetran-shaped datasets.

In any of these cases, you can use the below mapping logic to shape your new data to fit old data schema requirements and **save time** in your migration.

> ![Tip]
> Use the right-hand navigation to quickly browse available dataset mappings.

> ![Warning]
> AI-generated results may contain errors. Please sanity check results and adapt these resources to your needs accordingly.


### Mapping: Airbyte `abandoned_checkouts` to Fivetran `abandoned_checkout`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mappings are evaluated to be of high confidence as they describe the same subject matter in both source and target implementations._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `abandoned_checkouts._airbyte_extracted_at` | 🟢 _1.00_ | *_fivetran_synced is correctly mapped to _airbyte_extracted_at.* |
| `total_duties` | The total duties of the checkout in presentment currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `discount_codes` to Fivetran `order_discount_code`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table mapping is of moderate quality with certain fields perfectly mapped, some fields with potential mappings, and others missing entirely. A score of 0.8 reflects that the table structure is very likely describing the same subject matter, but not entirely complete due to missing field mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `discount_codes._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping: `_fivetran_synced` to `_airbyte_extracted_at`, always scores 1.00.* |
| `amount` | The amount that's deducted from the order total. | `discount_codes.total_sales.amount` | 🟢 _0.70_ | *Mapping `amount` to `discount_codes.total_sales.amount` is potentially correct given context, but exact match not certain.* |
| `code` | This property returns the discount code that was entered at checkout. Otherwise this property returns the title of the discount that was applied. | `discount_codes.code` | 🟢 _0.70_ | *Mapping `code` to `discount_codes.code` is likely correct based on contextual description of discount application.* |
| `order_id` | Associated order ID. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `type` | The type of discount - `fixed_amount`, `percentage`, or `shipping`. | `discount_codes.discount_type` | 🟢 _0.70_ | *Mapping `type` to `discount_codes.discount_type` appears valid given context of discount type enumeration.* |
| `index` | Pairs with `order_id` to provide unique identifier for order discount code. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `collects` to Fivetran `collection_product`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mapping was evaluated with a high table match score as the subject matter aligns closely between source and target, hence a match score of 0.70. The completion score is 0.80, indicating some fields have good mapping and coverage from source to target with a slight room for improvement._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `collects._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to the source stream's _airbyte_extracted_at column.* |
| `collection_id` | ID referencing the `collection` the product belongs to. | `collects.collection_id` | 🟢 _0.70_ | *ID referencing the `collection` has a relevant mapping. Given score reflects strong, but not perfect match due to potential contextual differences.* |
| `product_id` | ID referencing the `product`. | `collects.product_id` | 🟢 _0.70_ | *ID referencing the `product` aligns closely in purpose but may differ slightly in context in some implementations, hence the score.* |

### Mapping: Airbyte `products` to Fivetran `product`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The mapping configuration aligns well with the expected target schema. High confidence mappings like '_fivetran_synced' to 'products._airbyte_extracted_at' contribute positively. Missing mappings like '_fivetran_deleted' are penalized. Field mappings suggest a strong match with exceptions handled appropriately._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | Whether the record has been deleted in the source system. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `products._airbyte_extracted_at` | 🟢 _1.00_ | *Mapped to 'products._airbyte_extracted_at' as a standard mapping.* |
| `created_at` | The date and time when the product was created. | `products.created_at` | 🟢 _0.80_ | *'products.created_at' is a good match for 'created_at'.* |
| `handle` | A unique human-friendly string for the product. Automatically generated from the product's title. | `products.handle` | 🟢 _0.80_ | *'products.handle' maps well to 'handle'.* |
| `id` | An unsigned 64-bit integer that's used as a unique identifier for the product. Each id is unique across the Shopify system. No two products will have the same id, even if they're from different shops. | `products.id` | 🟢 _0.90_ | *'products.id' is a strong match for 'id', capturing unique identifier role.* |
| `product_type` | A categorization for the product used for filtering and searching products. | `products.product_type` | 🟢 _0.70_ | *'products.product_type' is likely a match for 'product_type', but categorization can vary.* |
| `published_at` | The date and time (ISO 8601 format) when the product was published. Can be set to null to unpublish the product from the Online Store channel. | `products.published_at` | 🟢 _0.70_ | *'products.published_at' matches 'published_at', considering time format similarity.* |
| `published_scope` | Whether the product is published to the Point of Sale channel. | `products.published_scope` | 🟢 _0.80_ | *'products.published_scope' is aligned with 'published_scope', matching distribution scope.* |
| `title` | The name of the product. | `products.title` | 🟢 _0.90_ | *'products.title' accurately reflects 'title'.* |
| `updated_at` | The date and time when the product was last modified. | `products.updated_at` | 🟢 _0.80_ | *'products.updated_at' corresponds well to 'updated_at'.* |
| `vendor` | The name of the product's vendor. | `products.vendor` | 🟢 _0.90_ | *'products.vendor' is a precise match for 'vendor'.* |
| `status` | The status of the product. Valid values: - active: The product is ready to sell and is available to customers on the online store, sales channels, and apps. By default, existing products are set to active. - archived: The product is no longer being sold and isn't available to customers on sales channels and apps. - draft: The product isn't ready to sell and is unavailable to customers on sales channels and apps. By default, duplicated and unarchived products are set to draft.  | `products.status` | 🟢 _0.80_ | *'products.status' aligns well with 'status', acknowledging the valid status values.* |

### Mapping: Airbyte `metafield_shops` to Fivetran `metafield`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping matches closely with the expected schema based on the field names and their descriptions. Most fields have a direct match and the mappings are generally appropriate, with a few exceptions where 'MISSING' is used due to lack of good matches._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `metafield_shops._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to source stream's '_airbyte_extracted_at' column.* |
| `created_at` | The date and time (ISO 8601 format) when the metafield was created. | `metafield_shops.created_at` | 🟢 _0.95_ | *High confidence mapping based on field name and purpose of capturing creation date.* |
| `description` | A description of the information that the metafield contains. | `metafield_shops.description` | 🟢 _0.90_ | *Field matches closely based on description and typical usage.* |
| `id` | The unique ID of the metafield. | `metafield_shops.id` | 🟢 _1.00_ | *Direct match with unique identifier field.* |
| `key` | The key of the metafield. Keys can be up to 64 characters long and can contain alphanumeric characters, hyphens, underscores, and periods. | `metafield_shops.key` | 🟢 _0.85_ | *Field mapping based on key attributes; fits well with typical schema.* |
| `namespace` | A container for a group of metafields. Grouping metafields within a namespace prevents your metafields from conflicting with other metafields with the same key name. Must have between 3-255 characters. | `metafield_shops.namespace` | 🟢 _0.80_ | *Closely aligns with expected schema for group containers.* |
| `owner_id` | The unique ID of the resource that the metafield is attached to. | `metafield_shops.owner_id` | 🟢 _0.90_ | *High confidence mapping for field indicating owner relation.* |
| `owner_resource` | The type of resource (table) that the metafield is attached to. | `metafield_shops.owner_resource` | 🟢 _0.70_ | *Resource-type field matches well, although contextual evidence is moderate.* |
| `type` | The type of data that the metafield stores in the `value` field. Refer to the [list](https://shopify.dev/apps/metafields/types) of supported types. Use this instead of `value_type`. | `metafield_shops.type` | 🟢 _0.75_ | *Mapping is appropriate with regard to data type description.* |
| `updated_at` | The date and time (ISO 8601 format) when the metafield was last updated. | `metafield_shops.updated_at` | 🟢 _0.95_ | *High confidence mapping for a timestamp of last update.* |
| `value` | The data to store in the metafield. The value is always stored as a string, regardless of the metafield's type. | `metafield_shops.value` | 🟢 _0.90_ | *Typically used for storing string data, fits with equivalent field.* |
| `value_type` | DEPRECATED as of [June 2022](https://fivetran.com/docs/applications/shopify/changelog#june2022). Use `type` instead. | `metafield_shops.value_type` | ❌ _0.00_ | *No good match found; field is deprecated.* |

### Mapping: Airbyte `shop` to Fivetran `shop`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The table mapping evaluated to a high confidence score due to matching fields and descriptions aligning well with expected domains. A few fields could not be directly matched and are marked as 'MISSING'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `shop._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to _airbyte_extracted_at.* |
| `address_1` | The shop's street address. | `shop.address1` | 🟢 _1.00_ | *Exact match with 'shop.address1'.* |
| `address_2` | The optional second line of the shop's street address. | `shop.address2` | 🟢 _1.00_ | *Exact match with 'shop.address2'.* |
| `checkout_api_supported` | Boolean representing whether the shop is capable of accepting payments directly through the Checkout API. | `shop.checkout_api_supported` | 🟢 _0.95_ | *High confidence match.* |
| `city` | The shop's city. | `shop.city` | 🟢 _1.00_ | *Exact match with 'shop.city'.* |
| `cookie_consent_level` | The cookie consent level defined on the shop's online store. | `shop.cookie_consent_level` | 🟢 _1.00_ | *Exact match with 'shop.cookie_consent_level'.* |
| `country` | The shop's country. In most cases, this value matches the country_code. | `shop.country` | 🟢 _1.00_ | *Exact match with 'shop.country'.* |
| `country_code` | The two-letter country code corresponding to the shop's country. | `shop.country_code` | 🟢 _1.00_ | *Exact match with 'shop.country_code'.* |
| `country_name` | The shop's normalized country name. | `shop.country_name` | 🟢 _1.00_ | *Exact match with 'shop.country_name'.* |
| `county_taxes` | Boolean representing whether the shop is applying taxes on a per-county basis. Only applicable to shops based in the US. Either `true` or `null` (not false, according to Shopify API docs). | `shop.county_taxes` | 🟢 _0.90_ | *High confidence match with explanation from Shopify API.* |
| `created_at` | The date and time (ISO 8601) when the shop was created. | `shop.created_at` | 🟢 _1.00_ | *Exact match with 'shop.created_at'.* |
| `currency` | The three-letter code (ISO 4217 format) for the shop's default currency. | `shop.currency` | 🟢 _1.00_ | *Exact match with 'shop.currency'.* |
| `customer_email` | The contact email used for communication between the shop owner and the customer. | `shop.customer_email` | 🟢 _1.00_ | *Exact match with 'shop.customer_email'.* |
| `domain` | The shop's domain. | `shop.domain` | 🟢 _1.00_ | *Exact match with 'shop.domain'.* |
| `eligible_for_card_reader_giveaway` | Boolean representing whether the shop is eligible to receive a free credit card reader from Shopify. | `shop.eligible_for_card_reader_giveaway` | 🟢 _0.95_ | *High confidence match.* |
| `eligible_for_payments` | Boolean representing whether the shop is eligible to use Shopify Payments. | `shop.eligible_for_payments` | 🟢 _0.95_ | *High confidence match.* |
| `email` | The contact email used for communication between Shopify and the shop owner. | `shop.email` | 🟢 _1.00_ | *Exact match with 'shop.email'.* |
| `enabled_presentment_currencies` | An array of of enabled currencies (ISO 4217 format) that the shop accepts. Merchants can enable currencies from their Shopify Payments settings in the Shopify Admin. | `shop.enabled_presentment_currencies` | 🟢 _1.00_ | *Exact match with 'shop.enabled_presentment_currencies'.* |
| `force_ssl` | DEPRECATED. | `shop.force_ssl` | ❌ _0.00_ | *No good match found.* |
| `google_apps_domain` | The GSuite URL for the store, if applicable. | `shop.google_apps_domain` | 🟢 _1.00_ | *Exact match with 'shop.google_apps_domain'.* |
| `google_apps_login_enabled` | Boolean representing whether the GSuite login is enabled. Shops with this feature will be able to log in through the GSuite login page. Valid values are `true` and `null`. | `shop.google_apps_login_enabled` | 🟢 _0.95_ | *High confidence match.* |
| `has_discounts` | Boolean representing whether any active discounts exist for the shop. | `shop.has_discounts` | 🟢 _0.95_ | *High confidence match.* |
| `has_gift_cards` | Boolean representing whether any active gift cards exist for the shop. | `shop.has_gift_cards` | 🟢 _0.95_ | *High confidence match.* |
| `has_storefront` | Boolean representing whether this shop has an online store. | `shop.has_storefront` | 🟢 _0.95_ | *High confidence match.* |
| `iana_timezone` | The name of the timezone assigned by the [IANA](https://www.iana.org/time-zones). | `shop.iana_timezone` | 🟢 _1.00_ | *Exact match with 'shop.iana_timezone'.* |
| `id` | The ID for the shop. A 64-bit unsigned integer. | `shop.id` | 🟢 _1.00_ | *Exact match with 'shop.id'.* |
| `latitude` | The latitude of the shop's location. | `shop.latitude` | 🟢 _1.00_ | *Exact match with 'shop.latitude'.* |
| `longitude` | The longitude of the shop's location. | `shop.longitude` | 🟢 _1.00_ | *Exact match with 'shop.longitude'.* |
| `money_format` | A string representing the way currency is formatted when the currency isn't specified. | `shop.money_format` | 🟢 _1.00_ | *Exact match with 'shop.money_format'.* |
| `money_in_emails_format` | A string representing the way currency is formatted in email notifications when the currency isn't specified. | `shop.money_in_emails_format` | 🟢 _1.00_ | *Exact match with 'shop.money_in_emails_format'.* |
| `money_with_currency_format` | A string representing the way currency is formatted when the currency is specified. | `shop.money_with_currency_format` | 🟢 _1.00_ | *Exact match with 'shop.money_with_currency_format'.* |
| `money_with_currency_in_emails_format` | A string representing the way currency is formatted in email notifications when the currency is specified. | `shop.money_with_currency_in_emails_format` | 🟢 _1.00_ | *Exact match with 'shop.money_with_currency_in_emails_format'.* |
| `multi_location_enabled` | DEPRECATED and hard-coded to `true`. | `shop.multi_location_enabled` | 🟢 _1.00_ | *Exact match with 'shop.multi_location_enabled'.* |
| `myshopify_domain` | The shop's .myshopify.com domain. | `shop.myshopify_domain` | 🟢 _1.00_ | *Exact match with 'shop.myshopify_domain'.* |
| `name` | The name of the shop. | `shop.name` | 🟢 _1.00_ | *Exact match with 'shop.name'.* |
| `password_enabled` | Boolean representing whether the password protection page is enabled on the shop's online store. | `shop.password_enabled` | 🟢 _1.00_ | *Exact match with 'shop.password_enabled'.* |
| `phone` | The contact phone number for the shop. | `shop.phone` | 🟢 _1.00_ | *Exact match with 'shop.phone'.* |
| `plan_display_name` | The display name of the Shopify plan the shop is on. | `shop.plan_display_name` | 🟢 _1.00_ | *Exact match with 'shop.plan_display_name'.* |
| `plan_name` | The name of the Shopify plan the shop is on. | `shop.plan_name` | 🟢 _1.00_ | *Exact match with 'shop.plan_name'.* |
| `pre_launch_enabled` | Boolen representing whether the pre-launch page is enabled on the shop's online store. | `shop.pre_launch_enabled` | 🟢 _1.00_ | *Exact match with 'shop.pre_launch_enabled'.* |
| `primary_locale` | The shop's primary locale, as configured in the language settings of the shop's theme. | `shop.primary_locale` | 🟢 _1.00_ | *Exact match with 'shop.primary_locale'.* |
| `primary_location_id` | DEPRECATED. Formerly used for the ID of the shipping origin location. | `shop.primary_location_id` | ❌ _0.00_ | *No good match found.* |
| `province` | The shop's normalized province or state name. | `shop.province` | 🟢 _1.00_ | *Exact match with 'shop.province'.* |
| `province_code` | The two- or three-letter code for the shop's province or state. | `shop.province_code` | 🟢 _1.00_ | *Exact match with 'shop.province_code'.* |
| `requires_extra_payments_agreement` | Boolean representing whether the shop requires an extra Shopify Payments agreement. | `shop.requires_extra_payments_agreement` | 🟢 _0.95_ | *High confidence match.* |
| `setup_required` | Boolean representing whether the shop has any outstanding setup steps. | `shop.setup_required` | 🟢 _0.95_ | *High confidence match.* |
| `shop_owner` | The username of the shop owner. | `shop.shop_owner` | 🟢 _1.00_ | *Exact match with 'shop.shop_owner'.* |
| `source` | The handle of the partner account that referred the merchant to Shopify, if applicable. | `shop.source` | 🟢 _1.00_ | *Exact match with 'shop.source'.* |
| `tax_shipping` | Boolean representing whether taxes are charged for shipping. Valid values are true or false. | `shop.tax_shipping` | 🟢 _0.95_ | *High confidence match.* |
| `taxes_included` | Boolean representing whether applicable taxes are included in product prices. Valid values are true or null. | `shop.taxes_included` | 🟢 _0.95_ | *High confidence match.* |
| `timezone` | The name of the timezone the shop is in. | `shop.timezone` | 🟢 _1.00_ | *Exact match with 'shop.timezone'.* |
| `updated_at` | The date and time (ISO 8601) when the shop was last updated. | `shop.updated_at` | 🟢 _1.00_ | *Exact match with 'shop.updated_at'.* |
| `weight_unit` | The default unit of weight measurement for the shop. | `shop.weight_unit` | 🟢 _1.00_ | *Exact match with 'shop.weight_unit'.* |
| `zip` | The shop's zip or postal code. | `shop.zip` | 🟢 _1.00_ | *Exact match with 'shop.zip'.* |

### Mapping: Airbyte `price_rules` to Fivetran `price_rule`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The table mapping has a high confidence score because the source and target tables are derived from similar APIs with most fields properly mapped. All fields have either been mapped or identified as MISSING with a 0.00 confidence score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `price_rules._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping from '_fivetran_synced' to '_airbyte_extracted_at', always receives a score of 1.00.* |
| `allocation_limit` | The number of times the discount can be allocated on the cart - if eligible. For example a Buy 1 hat Get 1 hat for free discount can be applied 3 times on a cart having more than 6 hats,  where maximum of 3 hats get discounted - if the allocation_limit is 3. Empty (null) allocation_limit means unlimited number of allocations.  | `price_rules.allocation_limit` | 🟢 _0.90_ | *The field 'allocation_limit' is directly mapped and closely matches the source structure, with a high confidence level.* |
| `allocation_method` | The allocation method of the price rule. Valid values include `each` (the discount is applied to each of the entitled items. For example, for a price rule that takes $15 off, each entitled line item in a checkout will be discounted by $15) and `across` (the calculated discount amount will be applied across the entitled items. For example, for a price rule that takes $15 off, the discount will be applied across all the entitled items).  | `price_rules.allocation_method` | 🟢 _0.90_ | *The 'allocation_method' is directly mapped and closely matches the context of the source data.* |
| `created_at` | The date and time (ISO 8601 format) when the price rule was created. | `price_rules.created_at` | 🟢 _0.80_ | *The field 'created_at' has a direct mapping but the date format must be confirmed.* |
| `customer_selection` | The customer selection for the price rule. Valid values include `all` (the price rule is valid for all customers) and `prerequisite`  (the customer must either belong to one of the customer segments specified by customer_segment_prerequisite_ids, or be one of the customers specified by prerequisite_customer_ids).  | `price_rules.customer_selection` | 🟢 _0.85_ | *'customer_selection' shows a strong contextual match with predefined valid values.* |
| `ends_at` | The date and time (ISO 8601 format) when the price rule ends. Must be after starts_at. | `price_rules.ends_at` | 🟢 _0.80_ | *The field 'ends_at' closely matches the source, consider checking the date format.* |
| `id` | The ID for the price rule. | `price_rules.id` | 🟢 _0.95_ | *Id fields generally have a high confidence due to unique identity matching.* |
| `once_per_customer` | Boolean representing whether the generated discount code will be valid only for a single use per customer. This is tracked using customer ID. | `price_rules.once_per_customer` | 🟢 _0.90_ | *Boolean values generally have a straightforward mapping, resulting in a high score.* |
| `prerequisite_quantity_range` | If `customer_selection` is `prerequisite`, the minimum number of items for the price rule to be applicable. The quantity of an entitled cart item must be greater than or equal to this value. | `price_rules.prerequisite_quantity_range` | 🟢 _0.85_ | *This field matches with regard to the prerequisite quantity contextual information.* |
| `prerequisite_shipping_price_range` | If `customer_selection` is `prerequisite`, the maximum shipping price for the price rule to be applicable. The shipping price must be less than or equal to this value | `price_rules.prerequisite_shipping_price_range` | 🟢 _0.85_ | *Closely mapped based on prerequisites.* |
| `prerequisite_subtotal_range` | If `customer_selection` is `prerequisite`, the minimum subtotal for the price rule to be applicable. The subtotal of the entitled cart items must be greater than or equal to this value for the discount to apply. | `price_rules.prerequisite_subtotal_range` | 🟢 _0.85_ | *Contextual matching with subtotal range for prerequisites.* |
| `prerequisite_to_entitlement_purchase_prerequisite_amount` | If `customer_selection` is `prerequisite`, the prerequisite purchase for a Buy X Get Y discount. The minimum purchase amount required to be entitled to the discount. | `price_rules.prerequisite_to_entitlement_purchase.prerequisite_amount` | 🟢 _0.75_ | *The field matches but contains a nested prerequisite structure to evaluate.* |
| `quantity_ratio_entitled_quantity` | If `customer_selection` is `prerequisite`, in a Buy/Get ratio for a Buy X Get Y discount, this is the offered 'get' quantity. | `price_rules.prerequisite_to_entitlement_quantity_ratio.entitled_quantity` | 🟢 _0.80_ | *Matching within a nested structure with 'entitled_quantity' context.* |
| `quantity_ratio_prerequisite_quantity` | If `customer_selection` is `prerequisite`, in a Buy/Get ratio for a Buy X Get Y discount, this defines the necessary 'buy' quantity. | `price_rules.prerequisite_to_entitlement_quantity_ratio.prerequisite_quantity` | 🟢 _0.80_ | *Similar nested match with 'prerequisite_quantity' context.* |
| `starts_at` | The date and time (ISO 8601 format) when the price rule starts. | `price_rules.starts_at` | 🟢 _0.80_ | *Close match observed, confirm date and time are represented correctly.* |
| `target_selection` | The target selection method of the price rule. Valid values include `all` (the price rule applies the discount to all line items in the checkout) and  `entitled` (the price rule applies the discount to selected entitlements only).  | `price_rules.target_selection` | 🟢 _0.85_ | *High contextual relevance from given target selection options.* |
| `target_type` | The target type that the price rule applies to. Valid values include `line_item` (the price rule applies to the cart's line items) and `shipping_line` (the price rule applies to the cart's shipping lines). | `price_rules.target_type` | 🟢 _0.85_ | *Matches well with the target type and its discretized values.* |
| `title` | The title of the price rule. This is used by the Shopify admin search to retrieve discounts. It is also displayed on the Discounts page of the Shopify admin for bulk discounts.  Shopify recommends that this map onto the associated `discount_code.code`.  | `price_rules.title` | 🟢 _0.90_ | *Titles of price rules likely match directly across systems.* |
| `updated_at` | The date and time (ISO 8601 format) when the price rule was updated. | `price_rules.updated_at` | 🟢 _0.80_ | *Ensure date formatting consistency for the updated_at field.* |
| `usage_limit` | The maximum number of times the price rule can be used, per discount code. | `price_rules.usage_limit` | 🟢 _0.90_ | *Represents a confidently mapped numerical field with usage limitations.* |
| `value` | The value of the price rule. If if the value of `target_type` is `shipping_line`, then only -100 is accepted. The value must be negative. | `price_rules.value` | 🟢 _0.70_ | *Requires considering negative values unique to context but maps well.* |
| `value_type` | The value type of the price rule. Valid values include `fixed_amount` (applies a discount of value as a unit of the store's currency. For example, if value is -30 and the store's currency is USD, then $30 USD is deducted when the discount is applied) and `percentage` (applies a percentage discount of value. For example, if value is -30, then 30% will be deducted when the discount is applied). If `target_type` is `shipping_line`, then only `percentage` is accepted.  | `price_rules.value_type` | 🟢 _0.85_ | *Valid values for 'value_type' show strong mapping consistency.* |

### Mapping: Airbyte `fulfillments` to Fivetran `fulfillment`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table mapping shows a high level of confidence as most fields have clear matches between the source and target. The mapping from `_fivetran_synced` to `_airbyte_extracted_at` achieves a perfect score of 1.00 as a standard mapping agreement. Other fields, such as `created_at`, `id`, `status`, and `tracking_number`, have clear semantic consistency, scoring above 0.85. Some fields like `shipment_status` and `service` could have slightly lower scores due to potential ambiguity, but still fall within the 0.70-0.85 range as they seem contextually accurate. `MISSING` mappings are assigned a score of 0.00 and explained with 'No good match found.'_

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `fulfillments._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of `_fivetran_synced` to `_airbyte_extracted_at`.* |
| `created_at` | The date and time when the fulfillment was created. The API returns this value in ISO 8601 format. | `fulfillments.created_at` | 🟢 _0.90_ | *High confidence as the field directly corresponds to creation timestamp.* |
| `id` | The ID for the fulfillment. | `fulfillments.id` | 🟢 _0.95_ | *Direct match for fulfillment ID.* |
| `location_id` | The unique identifier of the location that the fulfillment was processed at. | `fulfillments.location_id` | 🟢 _0.85_ | *Clear mapping to location identifier, maintaining contextual integrity.* |
| `name` | The uniquely identifying fulfillment name, consisting of two parts separated by a .. The first part represents the order name and the second part represents the fulfillment number.  The fulfillment number automatically increments depending on how many fulfillments are in an order (e.g. #1001.1, #1001.2).  | `fulfillments.name` | 🟢 _0.80_ | *The naming structure seems intact with the order name and fulfillment number combined.* |
| `order_id` | The unique numeric identifier for the order. | `fulfillments.order_id` | 🟢 _0.90_ | *Direct correspondence of order identifier.* |
| `receipt_authorization` | The authorization code from the receipt. | `fulfillments.receipt.authorization` | 🟢 _0.70_ | *Potential match for receipt authorization, context considered.* |
| `service` | The fulfillment service associated with the fulfillment. | `fulfillments.service` | 🟢 _0.75_ | *Probable match for fulfillment service within the context.* |
| `shipment_status` | The current shipment status of the fulfillment. Valid values include: - label_printed: A label for the shipment was purchased and printed. - label_purchased: A label for the shipment was purchased, but not printed. - attempted_delivery: Delivery of the shipment was attempted, but unable to be completed. - ready_for_pickup: The shipment is ready for pickup at a shipping depot. - confirmed: The carrier is aware of the shipment, but hasn't received it yet. - in_transit: The shipment is being transported between shipping facilities on the way to its destination. - out_for_delivery: The shipment is being delivered to its final destination. - delivered: The shipment was succesfully delivered. - failure: Something went wrong when pulling tracking information for the shipment, such as the tracking number was invalid or the shipment was canceled.  | `fulfillments.shipment_status` | 🟢 _0.80_ | *Likely match based on available values for tracking shipment progress.* |
| `status` | The status of the fulfillment. Valid values include: - pending: Shopify has created the fulfillment and is waiting for the third-party fulfillment service to transition it to 'open' or 'success'. - open: The fulfillment has been acknowledged by the service and is in processing. - success: The fulfillment was successful. - cancelled: The fulfillment was cancelled. - error: There was an error with the fulfillment request. - failure: The fulfillment request failed.  | `fulfillments.status` | 🟢 _0.85_ | *Clear contextual match for fulfillment status.* |
| `tracking_company` | The name of the tracking company. | `fulfillments.tracking_company` | 🟢 _0.90_ | *The field correlates well with the shipping company's tracking.* |
| `tracking_number` | Primary tracking number for the order. | `fulfillments.tracking_number` | 🟢 _0.90_ | *Primary tracking number has a straightforward match.* |
| `tracking_numbers` | A list of tracking numbers, provided by the shipping company. | `fulfillments.tracking_numbers` | 🟢 _0.90_ | *Tracking numbers list maps accurately to shipping records.* |
| `tracking_urls` | The URLs of tracking pages for the fulfillment. | `fulfillments.tracking_urls` | 🟢 _0.90_ | *URLs for tracking correspond distinctly with the fulfillment tracking.* |
| `updated_at` | The date and time (ISO 8601 format) when the fulfillment was last modified. | `fulfillments.updated_at` | 🟢 _0.90_ | *Matches the timestamp for last modification accurately.* |

### Mapping: Airbyte `tender_transactions` to Fivetran `tender_transaction`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _All fields mapped successfully with high confidence according to provided rules and context. Mapping hypothetical fields between schemas across transformations without loss of meaning._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `tender_transactions._airbyte_extracted_at` | 🟢 _1.00_ | *Mapped to _airbyte_extracted_at as a standard mapping.* |
| `amount` | The amount of the tender transaction in the shop's currency. | `tender_transactions.amount` | 🟢 _1.00_ | *Direct match in field names and context (transaction amount).* |
| `currency` | The three-letter code (ISO 4217 format) for the currency used for the tender transaction. | `tender_transactions.currency` | 🟢 _1.00_ | *Direct match in field names and context (ISO currency code).* |
| `id` | The ID of the transaction. | `tender_transactions.id` | 🟢 _1.00_ | *Direct match in field names and context (transaction ID).* |
| `order_id` | The ID of the order that the tender transaction belongs to. | `tender_transactions.order_id` | 🟢 _1.00_ | *Direct match in field names and context (order ID).* |
| `payment_method` | Information about the payment method used for this transaction. Valid values include: - credit_card - cash - android_pay - apple_pay - google_pay - samsung_pay - shopify_pay - amazon - klarna - paypal - unknown - other  | `tender_transactions.payment_method` | 🟢 _1.00_ | *Direct match in field names and context (types of payment methods).* |
| `processed_at` | The date and time (ISO 8601 format) when the tender transaction was processed. | `tender_transactions.processed_at` | 🟢 _1.00_ | *Direct match in field names and context (date of transaction processing).* |
| `remote_reference` | The remote (gateway) reference associated with the tender. | `tender_transactions.remote_reference` | 🟢 _1.00_ | *Direct match in field names and context (reference associated with tender).* |
| `test` | Whether the tender transaction is a test transaction. | `tender_transactions.test` | 🟢 _1.00_ | *Direct match in field names and context (indicates if transaction is a test).* |
| `user_id` | The ID of the user logged into the Shopify POS device that processed the tender transaction, if applicable. | `tender_transactions.user_id` | 🟢 _1.00_ | *Direct match in field names and context (user ID processing the transaction).* |

### Mapping: Airbyte `orders` to Fivetran `order_tag`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table match score is relatively high because the `_fivetran_synced` was successfully mapped to `_airbyte_extracted_at`, a standard mapping. However, two of the field mappings have expressions set to 'MISSING', resulting in a lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `orders._airbyte_extracted_at` | 🟢 _1.00_ | *_fivetran_synced is always mapped to _airbyte_extracted_at with a perfect score of 1.00 as it is a standard mapping.* |
| `index` | Index (starting from 1) represnting when the tag was placed on the order. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING'. No good match found.* |
| `order_id` | ID of the order being tagged. | `orders.id` | 🟢 _0.70_ | *order_id is mapped to orders.id with a reasonable level of confidence.* |
| `value` | Value of the tag. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING'. No good match found.* |

### Mapping: Airbyte `order_refunds` to Fivetran `refund`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping shows high confidence since source and target tables are assumed to be derived from the same API, indicating they describe the same subject matter. The completion score is high as well, given all fields of significance in source are well mapped, except for the expected standard and one missing field._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The unique numeric identifier for the refund. | `order_refunds.id` | 🟢 _1.00_ | *Exact match found for the unique numeric identifier.* |
| `created_at` | Timestamp of the date when the refund was created. | `order_refunds.created_at` | 🟢 _1.00_ | *Exact match found for the creation timestamp.* |
| `processed_at` | Timestamp of the date when the refund was processed. | `order_refunds.processed_at` | 🟢 _1.00_ | *Exact match found for the processing timestamp.* |
| `note` | User generated note attached to the refund. | `order_refunds.note` | 🟢 _1.00_ | *Exact match found for the user-generated note.* |
| `restock` | Boolean indicating if the refund is a result of a restock. | `order_refunds.restock` | 🟢 _1.00_ | *Exact match found for the restock boolean.* |
| `user_id` | Reference to the user id which generated the refund. | `order_refunds.user_id` | 🟢 _1.00_ | *Exact match found for the user id reference.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `order_refunds._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping from '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `total_duties_set` | Record representing total duties set for the refund. | `order_refunds.total_duties_set` | 🟢 _1.00_ | *Exact match found for the total duties set record.* |
| `order_id` | Reference to the order which the refund is associated. | `order_refunds.order_id` | 🟢 _1.00_ | *Exact match found for the order id reference.* |

### Mapping: Airbyte `locations` to Fivetran `location`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The table mapping evaluation resulted in a high confidence score due to a close match between source and target schemas. The presence of exact mappings and the ability to identify synonymous fields contribute to the quality and coverage of the mapping._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `locations._airbyte_extracted_at` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `locations._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables.* |
| `active` | Boolean representing whether the location is active. If true, then the location can be used to sell products, stock inventory, and fulfill orders.  | `locations.active` | 🟢 _1.00_ | *The field 'active' has a clear one-to-one mapping, as it directly maps from the source to the target fields with no ambiguity.* |
| `address_1` | The location's street address. | `locations.address1` | 🟢 _1.00_ | *The field 'address_1' is directly mapped to the source, indicating a high degree of confidence in the mapping.* |
| `address_2` | The optional second line of the location's street address. | `locations.address2` | 🟢 _1.00_ | *'address_2' maps directly from the source, matching the field intent and data type.* |
| `city` | The city the location is in. | `locations.city` | 🟢 _1.00_ | *The 'city' field maps directly from the source to target schemas accurately.* |
| `country` | The country the location is in (two-letter code). | `locations.country` | 🟢 _1.00_ | *The field 'country' is an exact match between source and target.* |
| `country_code` | The two-letter code (ISO 3166-1 alpha-2 format) corresponding to country the location is in. | `locations.country_code` | 🟢 _1.00_ | *The 'country_code' field has a perfect mapping from source to target respecting the ISO standard.* |
| `country_name` | Full name of the location's country. | `locations.country_name` | 🟢 _1.00_ | *Direct mapping from source 'country_name' to target.* |
| `created_at` | The date and time (ISO 8601 format) when the location was created. | `locations.created_at` | 🟢 _1.00_ | *The 'created_at' field exists in both schemas and matches perfectly with ISO 8601 format indication.* |
| `id` | The ID of the location. | `locations.id` | 🟢 _1.00_ | *The 'id' is an exact match and critical field forming the primary key.* |
| `legacy` | Boolean representing whether this is a fulfillment service location. If true, then the location is a fulfillment service location.  If false, then the location was created by the merchant and isn't tied to a fulfillment service.  | `locations.legacy` | 🟢 _1.00_ | *The 'legacy' field maps accurately maintaining boolean context.* |
| `localized_country_name` | The localized name of the location's country. | `locations.localized_country_name` | 🟢 _1.00_ | *Direct and accurate mapping for localized country name.* |
| `localized_province_name` | The localized name of the location's region. Typically a province, state, or district. | `locations.localized_province_name` | 🟢 _1.00_ | *Perfect match for localized province name.* |
| `name` | The name of the location. | `locations.name` | 🟢 _1.00_ | *'Different schemas have identical field denoted by 'name', implying a perfect mapping.* |
| `phone` | The phone number of the location. This value can contain special characters, such as - or +. | `locations.phone` | 🟢 _1.00_ | *Accurate mapping keeping respect to phone field attribute consistency.* |
| `province` | The province, state, or district of the location. | `locations.province` | 🟢 _1.00_ | *'Province' is a direct match with no distinction.* |
| `province_code` | The province, state, or district code (ISO 3166-2 alpha-2 format) of the location. | `locations.province_code` | 🟢 _1.00_ | *Perfect match for province code with ISO format consideration.* |
| `updated_at` | The date and time (ISO 8601 format) when the location was last updated. | `locations.updated_at` | 🟢 _1.00_ | *Field 'updated_at' perfectly concurs with temporal data standards.* |
| `zip` | The zip or postal code. | `locations.zip` | 🟢 _1.00_ | *The 'zip' field forms an exact match with source schema definition.* |

### Mapping: Airbyte `inventory_levels` to Fivetran `inventory_level`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table has a strong correspondence between source and target, given shared fields and expressions. The completion score is high due to the presence of mappings for nearly all fields, though some fields are marked as deprecation or missing information._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `inventory_levels._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables between _fivetran_synced and _airbyte_extracted_at.* |
| `available` | (DEPRECATED 2025-01-06) The available quantity of an inventory item at the inventory level's associated location. Returns null if the inventory item is not tracked. | `inventory_levels.available` | ⚠️ _0.50_ | *The field is deprecated and may not have a direct corresponding field in the target.* |
| `inventory_item_id` | The ID of the inventory item associated with the inventory level. | `inventory_levels.inventory_item_id` | 🟢 _1.00_ | *The ID of the inventory item has a clear corresponding mapping.* |
| `location_id` | The ID of the location that the inventory level belongs to. | `inventory_levels.location_id` | 🟢 _1.00_ | *The ID for the location maps directly with high confidence.* |
| `updated_at` | The date and time (ISO 8601 format) when the inventory level was last modified. | `inventory_levels.updated_at` | 🟢 _1.00_ | *The date and time modified has a direct correspondence.* |
| `id` | A globally unique identifier for the inventory level. | `inventory_levels.id` | 🟢 _1.00_ | *Unique identifier has a direct map in the target schema.* |
| `can_deactivate` | Indicates whether the inventory item can be deactivated at the location. | `inventory_levels.can_deactivate` | 🟢 _0.70_ | *Possible match based on functionality, but not entirely certain.* |
| `created_at` | The date and time when the inventory level was created. | `inventory_levels.created_at` | 🟢 _1.00_ | *Creation timestamp matches directly.* |
| `deactivation_alert` | Provides an alert message when the inventory item is deactivated at the location. | `inventory_levels.deactivation_alert` | 🟢 _0.70_ | *Alert message likely corresponds, though there is some uncertainty.* |

### Mapping: Airbyte `order_refunds` to Fivetran `order_adjustment`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mapping has a high confidence level as most fields are well-matched with minor discrepancies. 'MISSING' fields are well addressed and the usual high-confidence mappings are adhered to._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The unique numeric identifier for the order adjustment. | `order_refunds.id` | 🟢 _0.90_ | *The mapping of 'id' to 'order_refunds.id' is strong due to similar naming and meaning.* |
| `order_id` | Reference to the order which the adjustment is associated. | `order_refunds.order_id` | 🟢 _0.90_ | *The mapping of 'order_id' to 'order_refunds.order_id' is strong due to direct correspondence in naming and meaning.* |
| `refund_id` | Reference to the refund which the adjustment is associated. | `order_refunds.return.id` | 🟢 _0.70_ | *The mapping of 'refund_id' to 'order_refunds.return.id' is moderate due to nested structure.* |
| `amount` | Amount of the adjustment. | `order_refunds.total_duties_set.shop_money.amount` | 🟢 _0.80_ | *The mapping of 'amount' to 'order_refunds.total_duties_set.shop_money.amount' is good due to relevant scope of the field despite nested structure.* |
| `tax_amount` | Tax amount applied to the order adjustment in shop currency. | `order_refunds.total_duties_set.presentment_money.amount` | 🟢 _0.80_ | *The mapping of 'tax_amount' to 'order_refunds.total_duties_set.presentment_money.amount' is good due to relevant context despite nested structure.* |
| `kind` | The kind of order adjustment (eg. refund, restock, etc.). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `reason` | The reason for the order adjustment. | `order_refunds.note` | 🟢 _0.75_ | *The mapping of 'reason' to 'order_refunds.note' is reasonable due to relevant meaning.* |
| `amount_set` | Amount set towards the order adjustment in shop and presentment currencies. | `order_refunds.total_duties_set` | 🟢 _0.70_ | *The mapping of 'amount_set' to 'order_refunds.total_duties_set' is moderate due to nested structure.* |
| `tax_amount_set` | Tax amount set towards the order adjustment in shop and presentment currencies. | `order_refunds.total_duties_set.presentment_money` | 🟢 _0.70_ | *The mapping of 'tax_amount_set' to 'order_refunds.total_duties_set.presentment_money' is moderate due to nested structure.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `order_refunds._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to '_airbyte_extracted_at'.* |

### Mapping: Airbyte `customers` to Fivetran `customer`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table match score is high due to the high similarity in subject matter between the source and target schemas, both concerned with customer information. While the completion score is even higher since most of the fields have precise mappings in the target schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `customers._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `accepts_marketing` | Whether the customer has consented to receive marketing material via email. Deprecated and will be coalesced with `email_marketing_consent_state`. | `customers.accepts_marketing` | ❌ _0.00_ | *No good match found.* |
| `created_at` | The date and time when the customer was created. | `customers.created_at` | 🟢 _0.80_ | *'created_at' has a direct equivalent in the target schema.* |
| `default_address_id` | The default address for the customer. | `customers.default_address.id` | 🟢 _0.80_ | *'default_address_id' matches structurally to 'customers.default_address.id'.* |
| `email` | The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error. | `customers.email` | 🟢 _0.90_ | *'email' is uniquely tied to 'customers.email' in a mapping.* |
| `first_name` | The customer's first name. | `customers.first_name` | 🟢 _0.90_ | *'first_name' has equivalent mapping to 'customers.first_name'.* |
| `id` | A unique identifier for the customer. | `customers.id` | 🟢 _1.00_ | *Exact match found with 'customers.id'.* |
| `last_name` | The customer's last name. | `customers.last_name` | 🟢 _0.90_ | *'last_name' found similar corresponding field 'customers.last_name'.* |
| `orders_count` | The number of orders associated with this customer. | `customers.orders_count` | 🟢 _0.85_ | *'orders_count' accurately reflects 'customers.orders_count'.* |
| `phone` | The unique phone number (E.164 format) for this customer. Attempting to assign the same phone number to multiple customers returns an error. | `customers.phone` | 🟢 _0.90_ | *Direct mapping with 'customers.phone'.* |
| `state` | The state of the customer's account with a shop. | `customers.state` | 🟢 _0.70_ | *Ambiguity exists, but current context favors this mapping to 'customers.state'.* |
| `tax_exempt` | Whether the customer is exempt from paying taxes on their order. If true, then taxes won't be applied to an order at checkout. If false, then taxes will be applied at checkout. | `customers.tax_exempt` | 🟢 _0.85_ | *Good match with 'customers.tax_exempt'. Similar domain.* |
| `total_spent` | The total amount of money that the customer has spent across their order history. | `customers.total_spent` | 🟢 _0.90_ | *Correlates well with 'customers.total_spent'.* |
| `updated_at` | The date and time when the customer information was last updated. | `customers.updated_at` | 🟢 _0.85_ | *Good mapping correspondence to 'customers.updated_at'.* |
| `verified_email` | Whether the customer has verified their email address. | `customers.verified_email` | 🟢 _0.85_ | *'verified_email' matches well with 'customers.verified_email'.* |
| `email_marketing_consent_state` | The current email marketing state for the customer. New version of `accepts_marketing` field. | `customers.email_marketing_consent.state` | 🟢 _0.70_ | *Some similarity with 'customers.email_marketing_consent.state'.* |
| `email_marketing_consent_opt_in_level` | The marketing subscription opt-in level, as described in the M3AAWG Sender Best Common Practices, that the customer gave when they consented to receive marketing material by email. New version of `marketing_opt_in_level` field. | `customers.email_marketing_consent.opt_in_level` | 🟢 _0.70_ | *Some similarity with 'customers.email_marketing_consent.opt_in_level'.* |
| `email_marketing_consent_consent_updated_at` | The date and time when the customer consented to receive marketing material by email. If no date is provided, then the date and time when the consent information was sent is used. New version of `accepts_marketing_updated_at` field. | `customers.email_marketing_consent.consent_updated_at` | 🟢 _0.70_ | *Some similarity with 'customers.email_marketing_consent.consent_updated_at'.* |
| `accepts_marketing_updated_at` | Deprecated. The package will coalesce with `email_marketing_consent_consent_updated_at`. | `customers.accepts_marketing_updated_at` | ❌ _0.00_ | *No good match found.* |
| `marketing_opt_in_level` | Deprecated. The package will coalesce with `email_marketing_consent_opt_in_level`. | `customers.marketing_opt_in_level` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `note` | A note about the customer. | `customers.note` | ⚠️ _0.60_ | *Marginal mapping match with 'customers.note'.* |
| `currency` | The three-letter code (ISO 4217 format) for the currency that the customer used when they paid for their last order. Defaults to the shop currency. Returns the shop currency for test orders. | `customers.currency` | 🟢 _0.80_ | *Matches well with 'customers.currency'.* |

### Mapping: Airbyte `discount_codes` to Fivetran `discount_code`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.86_
- Summary Self-Evaluation: _The table fields are generally well-aligned with their purposes clearly defined. The source fields such as 'code', 'created_at', 'id', 'price_rule_id', 'updated_at', and 'usage_count' align with expectations for discount codes in the context provided. '_fivetran_synced' is correctly mapped to a source stream's '_airbyte_extracted_at', providing a reliable match for synchronization tracking. There are no fields marked as 'MISSING', indicating an attempt has been made to map all relevant fields in the source schema to the target schema, resulting in a high score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `discount_codes._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to '_airbyte_extracted_at'.* |
| `code` | The case-insensitive discount code that customers use at checkout. Shopify recommends this map onto the associated `price_rule.title`. | `discount_codes.code` | 🟢 _0.80_ | *Matches the source and target purpose of representing the discount code as used at checkout.* |
| `created_at` | The date and time (ISO 8601 format) when the discount code was created. | `discount_codes.created_at` | 🟢 _0.90_ | *Correctly maps to the source's created timestamp for the discount code, aligning with typical data schema expectations.* |
| `id` | The ID for the discount code. | `discount_codes.id` | 🟢 _0.90_ | *Maps source's discount code ID, sufficient match given familiarity with common identification fields.* |
| `price_rule_id` | The ID for the price rule that this discount code belongs to. | `discount_codes.price_rule_id` | 🟢 _0.80_ | *Adequate match since it represents an ID for associated rules, a typical relational mapping.* |
| `updated_at` | The date and time (ISO 8601 format) when the discount code was updated. | `discount_codes.updated_at` | 🟢 _0.90_ | *Successfully maps update timestamps, common in schemas where record modifications are tracked.* |
| `usage_count` | The number of times that the discount code has been redeemed. | `discount_codes.usage_count` | 🟢 _0.80_ | *Reflects typical semantic usage tracking, indicating satisfactory mapping despite potential source differences.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
