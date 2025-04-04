# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping: Airbyte `discount_codes` to Fivetran `order_discount_code`


- Table Match Confidence Score: 🟢 _0.80__
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

### Mapping: Airbyte `discount_codes` to Fivetran `discount_code`


- Table Match Confidence Score: 🟢 _0.90__
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

### Mapping: Airbyte `customers` to Fivetran `customer`


- Table Match Confidence Score: 🟢 _0.80__
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

### Mapping: Airbyte `order_refunds` to Fivetran `order_adjustment`


- Table Match Confidence Score: 🟢 _0.85__
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

### Mapping: Airbyte `metafield_shops` to Fivetran `metafield`


- Table Match Confidence Score: 🟢 _0.85__
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

### Mapping: Airbyte `locations` to Fivetran `location`


- Table Match Confidence Score: 🟢 _0.85__
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

### Mapping: Airbyte `tender_transactions` to Fivetran `tender_transaction`


- Table Match Confidence Score: 🟢 _1.00__
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

### Mapping: Airbyte `abandoned_checkouts` to Fivetran `abandoned_checkout`


- Table Match Confidence Score: 🟢 _1.00__
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mappings are evaluated to be of high confidence as they describe the same subject matter in both source and target implementations._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `abandoned_checkouts._airbyte_extracted_at` | 🟢 _1.00_ | *_fivetran_synced is correctly mapped to _airbyte_extracted_at.* |
| `total_duties` | The total duties of the checkout in presentment currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `shop` to Fivetran `shop`


- Table Match Confidence Score: 🟢 _0.80__
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

### Mapping: Airbyte `orders` to Fivetran `order_tag`


- Table Match Confidence Score: 🟢 _0.80__
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table match score is relatively high because the `_fivetran_synced` was successfully mapped to `_airbyte_extracted_at`, a standard mapping. However, two of the field mappings have expressions set to 'MISSING', resulting in a lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `orders._airbyte_extracted_at` | 🟢 _1.00_ | *_fivetran_synced is always mapped to _airbyte_extracted_at with a perfect score of 1.00 as it is a standard mapping.* |
| `index` | Index (starting from 1) represnting when the tag was placed on the order. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING'. No good match found.* |
| `order_id` | ID of the order being tagged. | `orders.id` | 🟢 _0.70_ | *order_id is mapped to orders.id with a reasonable level of confidence.* |
| `value` | Value of the tag. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING'. No good match found.* |

### Mapping: Airbyte `inventory_levels` to Fivetran `inventory_level`


- Table Match Confidence Score: 🟢 _0.85__
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

### Mapping: Airbyte `fulfillments` to Fivetran `fulfillment`


- Table Match Confidence Score: 🟢 _0.90__
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

### Mapping: Airbyte `price_rules` to Fivetran `price_rule`


- Table Match Confidence Score: 🟢 _0.90__
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

### Mapping: Airbyte `order_refunds` to Fivetran `refund`


- Table Match Confidence Score: 🟢 _0.80__
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

### Mapping: Airbyte `collects` to Fivetran `collection_product`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mapping was evaluated with a high table match score as the subject matter aligns closely between source and target, hence a match score of 0.70. The completion score is 0.80, indicating some fields have good mapping and coverage from source to target with a slight room for improvement._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `collects._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to the source stream's _airbyte_extracted_at column.* |
| `collection_id` | ID referencing the `collection` the product belongs to. | `collects.collection_id` | 🟢 _0.70_ | *ID referencing the `collection` has a relevant mapping. Given score reflects strong, but not perfect match due to potential contextual differences.* |
| `product_id` | ID referencing the `product`. | `collects.product_id` | 🟢 _0.70_ | *ID referencing the `product` aligns closely in purpose but may differ slightly in context in some implementations, hence the score.* |

### Mapping: Airbyte `products` to Fivetran `product`


- Table Match Confidence Score: 🟢 _0.80__
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

## Workshop Models

These models are in the workshop directory and are not yet approved.

### Mapping: Airbyte `custom_collections` to Fivetran `collection`


- Table Match Confidence Score: 🟢 _0.80__
- Table Completion Score: 🟢 _0.82_
- Summary Self-Evaluation: _The table match confidence is high due to the similarity in subject matter, but not all fields could be mapped, especially with some fields missing appropriate matches. The completion score reflects the proportion of fields that have meaningful mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `custom_collections._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to '_airbyte_extracted_at'.* |
| `disjunctive` | Boolean representing whether the `rules` or disjuctive (logical `OR`) or not. True = disjuctive, false = conjunctive (logical `AND`). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `handle` | A unique, human-readable string for the collection automatically generated from its title. This is used in themes by the Liquid templating language to refer to the collection. | `custom_collections.handle` | 🟢 _0.70_ | *Good match found with 'custom_collections.handle'.* |
| `id` | The ID for the collection. | `custom_collections.id` | 🟢 _0.70_ | *Good match found with 'custom_collections.id'.* |
| `published_at` | The time and date (ISO 8601 format) when the collection was made visible. Returns null for a hidden collection. | `custom_collections.published_at` | 🟢 _0.70_ | *Good match found with 'custom_collections.published_at'.* |
| `published_scope` | Whether the collection is published to the Point of Sale channel. Valid values `web` (the collection is published to the Online Store channel but not published to the Point of Sale channel) and `global` (the collection is published to both the Online Store channel and the Point of Sale channel).  | `custom_collections.published_scope` | 🟢 _0.70_ | *Good match found with 'custom_collections.published_scope'.* |
| `rules` | An array of rules that define what products go into the smart collection. Each rule (`column` -- `relation` --> `condition`) has these properties: - `column`: the property of a product being used to populate the smart collection. Ex: 'tag', 'type', 'vendor', 'variant_price', etc. - `relation`: The comparitive relationship between the column choice, and the condition ('equals', 'contains', 'greater_than', etc.) - condition: Select products for a smart collection using a condition. Values are either strings or numbers, depending on the relation value. See the [Shopify docs](https://shopify.dev/api/admin-rest/2022-10/resources/smartcollection#resource-object) for more.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sort_order` | The order of the products in the collection. Valid values inclide - `alpha-asc`: The products are sorted alphabetically from A to Z. - `alpha-des`: The products are sorted alphabetically from Z to A. - `best-selling`: The products are sorted by number of sales. - `created`: The products are sorted by the date they were created, from oldest to newest. - `created-desc`: The products are sorted by the date they were created, from newest to oldest. - `manual`: The products are manually sorted by the shop owner. - `price-asc`: The products are sorted by price from lowest to highest. - `price-desc`: The products are sorted by price from highest to lowest.  | `custom_collections.sort_order` | 🟢 _0.70_ | *Good match found with 'custom_collections.sort_order'.* |
| `title` | The name of the collection | `custom_collections.title` | 🟢 _0.70_ | *Good match found with 'custom_collections.title'.* |
| `updated_at` | The date and time (ISO 8601 format) when the collection was last modified. | `custom_collections.updated_at` | 🟢 _0.70_ | *Good match found with 'custom_collections.updated_at'.* |

### Mapping: Airbyte `inventory_items` to Fivetran `inventory_item`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: ⚠️ _0.52_
- Summary Self-Evaluation: _The table mappings have some missing fields and questionable matches. The '_fivetran_deleted' and several others are marked as 'MISSING'. Also, there are only a few fields that match perfectly, like '_fivetran_synced'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `inventory_items._airbyte_extracted_at` | 🟢 _1.00_ | *Mapped to the source stream's '_airbyte_extracted_at' column as a standard mapping.* |
| `country_code_of_origin` | The country code (ISO 3166-1 alpha-2) of where the item came from. | `inventory_items.country_code_of_origin` | 🟢 _0.90_ | *Likely a precise match due to standard naming.* |
| `created_at` | The date and time (ISO 8601 format) when the inventory item was created. | `inventory_items.created_at` | 🟢 _1.00_ | *ISO 8601 date-time creation is a good match.* |
| `id` | The ID of the inventory item. | `inventory_items.id` | 🟢 _1.00_ | *Unique inventory item identifier is a strong match.* |
| `province_code_of_origin` | The province code (ISO 3166-2 alpha-2) of where the item came from. The province code is only used if the shipping provider for the inventory item is Canada Post. | `inventory_items.province_code_of_origin` | 🟢 _0.70_ | *Possible match if considering Canada Post shipping references.* |
| `requires_shipping` | Boolean representing whether a customer needs to provide a shipping address when placing an order containing the inventory item. | `inventory_items.requires_shipping` | 🟢 _1.00_ | *Boolean values match perfectly with descriptions.* |
| `sku` | The unique SKU (stock keeping unit) of the inventory item. | `inventory_items.sku` | 🟢 _1.00_ | *Unique SKU matches well with the inventory mapping.* |
| `tracked` | Boolean representing whether inventory levels are tracked for the item. If true, then the inventory quantity changes are tracked by Shopify. | `inventory_items.tracked` | 🟢 _1.00_ | *Boolean tracking indicator is a perfect match.* |
| `updated_at` | The date and time (ISO 8601 format) when the inventory item was last modified. | `inventory_items.updated_at` | 🟢 _1.00_ | *ISO 8601 date-time modification field matches precisely.* |
| `duplicate_sku_count` | The number of inventory items that share the same SKU with this item. | `inventory_items.duplicate_sku_count` | 🟢 _1.00_ | *Clear match for counting duplicates of SKUs.* |
| `harmonized_system_code` | The harmonized system code of the item. | `inventory_items.harmonized_system_code` | 🟢 _0.90_ | *Likely code match based on naming and usage.* |
| `inventory_history_url` | The URL that points to the inventory history for the item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `legacy_resource_id` | The ID of the corresponding resource in the REST Admin API. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `measurement_id` | The unique identifier for the inventory item's measurement. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `measurement_weight_value` | The weight value of the inventory item's measurement. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `measurement_weight_unit` | The unit of measurement for the inventory item's weight. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tracked_editable_locked` | Indicates whether the 'tracked' field for the inventory item is locked from editing. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tracked_editable_reason` | Provides the reason why the 'tracked' field for the inventory item is locked from editing. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `unit_cost_amount` | Decimal money amount of the unit cost associated with the inventory item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `unit_cost_currency_code` | Currency of the unit cost associated with the inventory item. | `inventory_items.currency_code` | 🟢 _0.90_ | *Currency code match is likely correct.* |

### Mapping: Airbyte `metafield_orders` to Fivetran `order_url_tag`


- Table Match Confidence Score: ⚠️ _0.50__
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table match score is 0.5 due to partial similarity between the source and target schemas. The completion score is 0.75 as most fields are mapped, but some are missing or poorly matched._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `metafield_orders._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at', always scores 1.0.* |
| `key` | Key of the tag pair. | `metafield_orders.key` | 🟢 _0.70_ | *Fields 'key' in source and 'key' in target are likely referring to the same entity, mapped with a score of 0.7.* |
| `order_id` | ID of the order url being tagged. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING', no good match found.* |
| `value` | Value of the tag. | `metafield_orders.value` | ⚠️ _0.60_ | *Fields 'value' in source and 'value' in target mapped with a lower confidence due to minimal contextual match.* |

### Mapping: Airbyte `discount_codes` to Fivetran `abandoned_checkout_discount_code`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: ❌ _0.44_
- Summary Self-Evaluation: _The table mapping confidence score is moderate due to partial matches and the presence of several 'MISSING' expressions indicating incomplete mappings. Despite a few high-confidence mappings, the overall completion is low due to multiple unmapped fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `discount_codes._airbyte_extracted_at` | 🟢 _1.00_ | *_fivetran_synced is always mapped to _airbyte_extracted_at with a score of 1.00 as a standard mapping.* |
| `amount` | The amount of the discount in presentment currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `checkout_id` | ID of the checkout. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `code` | The discount code. | `discount_codes.code` | 🟢 _0.70_ | *discount_codes.code is likely a strong contextual match to 'code'.* |
| `created_at` | When the checkout discount application was created. | `discount_codes.created_at` | 🟢 _0.70_ | *discount_codes.created_at mapped to created_at with moderate confidence.* |
| `discount_id` | ID of the discount. Deprecated, use `code` instead. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `index` | Index (from 1) representing the application of the discount to the checkout. Use the latest (highest index) | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `type` | The type of discount. Valid values - percentage, shipping, fixed_amount. (default - fixed_amount) | `discount_codes.discount_type` | 🟢 _0.70_ | *discount_codes.discount_type mapped to type due to likely contextual match for discount types.* |
| `updated_at` | When the checkout's discount was last updated | `discount_codes.updated_at` | 🟢 _0.70_ | *discount_codes.updated_at mapped to updated_at with moderate confidence.* |

### Mapping: Airbyte `products` to Fivetran `product_tag`


- Table Match Confidence Score: 🟢 _1.00__
- Table Completion Score: ❌ _0.25_
- Summary Self-Evaluation: _The mapping configuration exhibits a perfect table match with successful standard field mapping for '_fivetran_synced', but lacks completion with most fields having 'MISSING' expressions._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `products._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `index` | Index (starting from 1) represnting when the tag was placed on the product. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `product_id` | ID of the product being tagged. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `value` | Value of the tag. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `customers` to Fivetran `customer_tag`


- Table Match Confidence Score: ⚠️ _0.60__
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The mapping includes standard and missing field expressions. Standard mappings like '_fivetran_synced' were given a high score, while missing fields were penalized._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `customers._airbyte_extracted_at` | 🟢 _1.00_ | *Mapped to a source stream's '_airbyte_extracted_at' as per standard.* |
| `index` | Index (starting from 1) represnting when the tag was placed on the customer. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING'. No good match found.* |
| `customer_id` | ID of the customer being tagged. | `customers.default_address.customer_id` | 🟢 _0.70_ | *Mapped to 'customers.default_address.customer_id'. Considered a likely match with some uncertainty.* |
| `value` | Value of the tag. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING'. No good match found.* |

### Mapping: Airbyte `product_variants` to Fivetran `product_variant`


- Table Match Confidence Score: 🟢 _0.80__
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table mapping is mostly consistent with the target schema, but there are several fields marked as 'MISSING' due to lack of good matches or differences in field representation. The overall table match score is high due to shared subject matter and relevant fields, but the completion score is lower reflecting these gaps._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `barcode` | The barcode, UPC, or ISBN number for the product. | `product_variants.barcode` | 🟢 _0.90_ | *The mapping of 'barcode' is strong as it directly corresponds to 'product_variants.barcode'.* |
| `compare_at_price` | The original price of the item before an adjustment or a sale in shop currency. | `product_variants.compare_at_price` | 🟢 _0.90_ | *The mapping of 'compare_at_price' is strong as it directly corresponds to 'product_variants.compare_at_price'.* |
| `created_at` | The date and time (ISO 8601 format) when the product variant was created. | `product_variants.created_at` | 🟢 _0.90_ | *The mapping of 'created_at' is strong as it directly corresponds to 'product_variants.created_at'.* |
| `fulfillment_service` | (DEPRECATED 2025-01-06) The fulfillment service associated with the product variant. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `grams` | (DEPRECATED 2025-01-06) The weight of the product variant in grams. | `product_variants.grams` | 🟢 _0.90_ | *The mapping of 'grams' is strong as it directly corresponds to 'product_variants.grams'.* |
| `id` | The unique numeric identifier for the product variant. | `product_variants.id` | 🟢 _0.90_ | *The mapping of 'id' is strong as it directly corresponds to 'product_variants.id'.* |
| `image_id` | The unique numeric identifier for a product's image. The image must be associated to the same product as the variant. | `product_variants.image_id` | 🟢 _0.90_ | *The mapping of 'image_id' is strong as it directly corresponds to 'product_variants.image_id'.* |
| `inventory_item_id` | The unique identifier for the inventory item, which is used in the Inventory API to query for inventory information. | `product_variants.inventory_item_id` | 🟢 _0.90_ | *The mapping of 'inventory_item_id' is strong as it directly corresponds to 'product_variants.inventory_item_id'.* |
| `inventory_management` | (DEPRECATED 2025-01-06) The fulfillment service that tracks the number of items in stock for the product variant. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `inventory_policy` | Whether customers are allowed to place an order for the product variant when it's out of stock. | `product_variants.inventory_policy` | 🟢 _0.90_ | *The mapping of 'inventory_policy' is strong as it directly corresponds to 'product_variants.inventory_policy'.* |
| `inventory_quantity` | An aggregate of inventory across all locations. To adjust inventory at a specific location, use the InventoryLevel resource. | `product_variants.inventory_quantity` | 🟢 _0.90_ | *The mapping of 'inventory_quantity' is strong as it directly corresponds to 'product_variants.inventory_quantity'.* |
| `old_inventory_quantity` | (DEPRECATED 2025-01-06) Use the InventoryLevel resource instead. | `product_variants.old_inventory_quantity` | 🟢 _0.90_ | *The mapping of 'old_inventory_quantity' is strong as it directly corresponds to 'product_variants.old_inventory_quantity'.* |
| `option_1` | (DEPRECATED 2025-01-06) The custom properties that a shop owner uses to define product variants. You can define three options for a product variant: option1, option2, option3.  | `product_variants.option1` | 🟢 _0.90_ | *The mapping of 'option_1' is strong as it directly corresponds to 'product_variants.option1'.* |
| `option_2` | (DEPRECATED 2025-01-06) The custom properties that a shop owner uses to define product variants. You can define three options for a product variant: option1, option2, option3.  | `product_variants.option2` | 🟢 _0.90_ | *The mapping of 'option_2' is strong as it directly corresponds to 'product_variants.option2'.* |
| `option_3` | (DEPRECATED 2025-01-06) The custom properties that a shop owner uses to define product variants. You can define three options for a product variant: option1, option2, option3.  | `product_variants.option3` | 🟢 _0.90_ | *The mapping of 'option_3' is strong as it directly corresponds to 'product_variants.option3'.* |
| `position` | The order of the product variant in the list of product variants. The first position in the list is 1. The position of variants is indicated by the order in which they are listed. | `product_variants.position` | 🟢 _0.90_ | *The mapping of 'position' is strong as it directly corresponds to 'product_variants.position'.* |
| `price` | The price of the product variant in shop currency. | `product_variants.price` | 🟢 _0.90_ | *The mapping of 'price' is strong as it directly corresponds to 'product_variants.price'.* |
| `product_id` | The unique numeric identifier for the product. | `product_variants.product_id` | 🟢 _0.90_ | *The mapping of 'product_id' is strong as it directly corresponds to 'product_variants.product_id'.* |
| `requires_shipping` | (DEPRECATED 2025-01-06) Use the `requires_shipping` property on the InventoryItem resource instead. | `product_variants.requires_shipping` | ❌ _0.00_ | *No good match found.* |
| `sku` | A unique identifier for the product variant in the shop. Required in order to connect to a FulfillmentService. | `product_variants.sku` | 🟢 _0.90_ | *The mapping of 'sku' is strong as it directly corresponds to 'product_variants.sku'.* |
| `taxable` | Whether a tax is charged when the product variant is sold. | `product_variants.taxable` | 🟢 _0.90_ | *The mapping of 'taxable' is strong as it directly corresponds to 'product_variants.taxable'.* |
| `tax_code` | This parameter applies only to the stores that have the Avalara AvaTax app installed. Specifies the Avalara tax code for the product variant. | `product_variants.tax_code` | 🟢 _0.90_ | *The mapping of 'tax_code' is strong as it directly corresponds to 'product_variants.tax_code'.* |
| `title` | The title of the product variant. The title field is a concatenation of the option1, option2, and option3 fields. You can only update title indirectly using the option fields. | `product_variants.title` | 🟢 _0.90_ | *The mapping of 'title' is strong as it directly corresponds to 'product_variants.title'.* |
| `updated_at` | The date and time when the product variant was last modified. Gets returned in ISO 8601 format. | `product_variants.updated_at` | 🟢 _0.90_ | *The mapping of 'updated_at' is strong as it directly corresponds to 'product_variants.updated_at'.* |
| `weight` | (DEPRECATED 2025-01-06) The weight of the product variant in the unit system specified with weight_unit. | `product_variants.weight` | 🟢 _0.90_ | *The mapping of 'weight' is strong as it directly corresponds to 'product_variants.weight'.* |
| `weight_unit` | (DEPRECATED 2025-01-06) The unit of measurement that applies to the product variant's weight. If you don't specify a value for weight_unit, then the shop's default unit of measurement is applied. Valid values: g, kg, oz, and lb.  | `product_variants.weight_unit` | 🟢 _0.90_ | *The mapping of 'weight_unit' is strong as it directly corresponds to 'product_variants.weight_unit'.* |
| `available_for_sale` | Indicates whether the product variant is available for sale. | `product_variants.available_for_sale` | 🟢 _0.90_ | *The mapping of 'available_for_sale' is strong as it directly corresponds to 'product_variants.available_for_sale'.* |
| `display_name` | The display name of the variant, based on the product's title and variant's title. | `product_variants.display_name` | 🟢 _0.90_ | *The mapping of 'display_name' is strong as it directly corresponds to 'product_variants.display_name'.* |
| `legacy_resource_id` | The ID of the corresponding resource in the REST Admin API. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `metafield` | A custom field, including its namespace and key, that's associated with a Shopify resource for the purposes of adding and storing additional information. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `requires_components` | Indicates whether a product variant requires components. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sellable_online_quantity` | The total sellable quantity of the variant for online channels. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `product_variants._airbyte_extracted_at` | 🟢 _1.00_ | *The mapping of '_fivetran_synced' to '_airbyte_extracted_at' is perfect and standard for all tables.* |

### Mapping: Airbyte `fulfillments` to Fivetran `fulfillment_event`


- Table Match Confidence Score: 🟢 _0.85__
- Table Completion Score: ❌ _0.30_
- Summary Self-Evaluation: _The table match score is high because most of the fields seem to relate to fulfillment events, matching the expected domain. However, many fields have 'MISSING' expressions, leading to a lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `fulfillments._airbyte_extracted_at` | 🟢 _1.00_ | *'_fivetran_synced' maps to '_airbyte_extracted_at' with full confidence.* |
| `address_1` | The street address where the fulfillment event occurred. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `city` | The city where the fulfillment event occurred. | `fulfillments.origin_address.city` | 🟢 _0.70_ | *'city' maps well to 'fulfillments.origin_address.city'.* |
| `country` | The country where the fulfillment event occurred. | `fulfillments.origin_address.country_code` | 🟢 _0.70_ | *'country' maps well to 'fulfillments.origin_address.country_code'.* |
| `created_at` | The date and time (ISO 8601 format) when the fulfillment event was created. | `fulfillments.created_at` | 🟢 _0.70_ | *'created_at' maps well to 'fulfillments.created_at'.* |
| `estimated_delivery_at` | The estimated delivery date based on the fulfillment's tracking number, as long as it's provided by one of the following carriers: USPS, FedEx, UPS, or Canada Post (Canada only).  Value is `null` if no tracking number is available or if the tracking number is from an unsupported carrier. This property is available only when carrier calculated rates are in use.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `fulfillment_id` | An ID for the fulfillment that's associated with the fulfillment event. | `fulfillments.id` | 🟢 _0.70_ | *'fulfillment_id' maps well to 'fulfillments.id'.* |
| `happened_at` | The date and time (ISO 8601 format) when the fulfillment event occurred. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | An ID for the fulfillment event. | `fulfillments.id` | 🟢 _0.70_ | *'id' maps well to 'fulfillments.id'.* |
| `latitude` | A geographic coordinate specifying the latitude of the fulfillment event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `longitude` | A geographic coordinate specifying the longitude of the fulfillment event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `message` | An arbitrary message describing the status. Can be provided by a shipping carrier. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `order_id` | The ID of the order that's associated with the fulfillment event. | `fulfillments.order_id` | 🟢 _0.70_ | *'order_id' maps well to 'fulfillments.order_id'.* |
| `province` | The province where the fulfillment event occurred. | `fulfillments.origin_address.province_code` | 🟢 _0.70_ | *'province' maps well to 'fulfillments.origin_address.province_code'.* |
| `shop_id` | An ID for the shop that's associated with the fulfillment event. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status` | The status of the fulfillment event. Valid values: - label_printed: A label for the shipment was purchased and printed. - label_purchased: A label for the shipment was purchased, but not printed. - attempted_delivery: Delivery of the shipment was attempted, but unable to be completed. - ready_for_pickup: The shipment is ready for pickup at a shipping depot. - picked_up: The fulfillment was successfully picked up. - confirmed: The carrier is aware of the shipment, but hasn't received it yet. - in_transit: The shipment is being transported between shipping facilities on the way to its destination. - out_for_delivery: The shipment is being delivered to its final destination. - delivered: The shipment was successfully delivered. - failure: Something went wrong when pulling tracking information for the shipment, such as the tracking number was invalid or the shipment was canceled.  | `fulfillments.shipment_status` | 🟢 _0.70_ | *'status' maps well to 'fulfillments.shipment_status'.* |
| `updated_at` | The date and time (ISO 8601 format) when the fulfillment event was updated. | `fulfillments.updated_at` | 🟢 _0.70_ | *'updated_at' maps well to 'fulfillments.updated_at'.* |
| `zip` | The zip code of the location where the fulfillment event occurred. | `fulfillments.origin_address.zip` | 🟢 _0.70_ | *The 'zip' field maps correctly to 'fulfillments.origin_address.zip'.* |

### Mapping: Airbyte `order_refunds` to Fivetran `order_shipping_tax_line`


- Table Match Confidence Score: ⚠️ _0.60__
- Table Completion Score: ❌ _0.14_
- Summary Self-Evaluation: _The field mapping includes one perfect match (`_fivetran_synced` to `_airbyte_extracted_at`), which always receives a score of 1.00. All other fields are marked as 'MISSING', indicating no good matches found, which lowers the completion score significantly._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `order_refunds._airbyte_extracted_at` | 🟢 _1.00_ | *Field `_fivetran_synced` is correctly mapped to `_airbyte_extracted_at`, which is a known perfect match.* |
| `index` | Index (from 1) representing the order of shipping lines per order. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `order_shipping_line_id` | ID of the order shipping line this recod is associated with. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `price` | The amount of tax, in shop currency, after discounts and before returns. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `price_set` | The amount of tax, in shop and presentment currencies, after discounts and before returns (JSON). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `rate` | The proportion of the line item price that the tax represents as a decimal. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `title` | The name of the tax. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `product_images` to Fivetran `product_image`


- Table Match Confidence Score: 🟢 _0.85__
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table mapping is based on shared API endpoints, suggesting a strong match. However, not all fields in the target schema are present in the source._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `product_images._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping from '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `created_at` | (DEPRECATED 2025-01-06) The date and time when the product image was created. The API returns this value in ISO 8601 format. | `product_images.created_at` | ⚠️ _0.60_ | *The mapping is likely correct given the typical structure of the source and target schemas.* |
| `height` | Height dimension of the image which is determined on upload. | `product_images.height` | 🟢 _0.70_ | *Height dimension is usually a directly mapped field.* |
| `id` | Unique numeric identifier of the product image. | `product_images.id` | 🟢 _0.70_ | *Unique identifiers are often directly mapped.* |
| `position` | (DEPRECATED 2025-01-06) The order of the product image in the list. The first product image is at position 1 and is the "main" image for the product. | `product_images.position` | ⚠️ _0.60_ | *Reasonable match for a potentially deprecated field.* |
| `product_id` | The id of the product associated with the image. | `product_images.product_id` | 🟢 _0.70_ | *This field commonly matches as a primary key reference.* |
| `src` | (DEPRECATED 2025-01-06) Specifies the location of the product image. This parameter supports URL filters that you can use to retrieve modified copies of the image. | `product_images.src` | ⚠️ _0.60_ | *Likely match for image source, albeit deprecated.* |
| `updated_at` | (DEPRECATED 2025-01-06) The date and time when the product image was last modified. The API returns this value in ISO 8601 format. | `product_images.updated_at` | ⚠️ _0.60_ | *Common match for modification timestamps, despite deprecation notice.* |
| `variant_ids` | (DEPRECATED 2025-01-06) An array of variant ids associated with the image. | `product_images.variant_ids` | ⚠️ _0.60_ | *Potentially correct for matching variant associations.* |
| `width` | Width dimension of the image which is determined on upload. | `product_images.width` | 🟢 _0.70_ | *Width dimension is usually a directly mapped field.* |
| `alt_text` | A word or phrase to share the nature or contents of an image. | `product_images.alt` | 🟢 _0.70_ | *Alt text fields often directly correspond.* |
| `media_id` | The unique identifier for the media associated with the product image. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status` | The status of the product image, indicating its availability or processing state. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `url` | The URL of the product image. | `product_images.shop_url` | 🟢 _0.70_ | *Likely match considering its use as image URL.* |

### Mapping: Airbyte `orders` to Fivetran `order_line`


- Table Match Confidence Score: ⚠️ _0.50__
- Table Completion Score: ❌ _0.10_
- Summary Self-Evaluation: _The table match is neutral due to generic field matching, with many fields having 'MISSING' values indicating no correspondence in the source data._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `orders._airbyte_extracted_at` | 🟢 _1.00_ | *Mapped to a standard column '_airbyte_extracted_at'.* |
| `fulfillable_quantity` | The amount available to fulfill, calculated as follows: quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `fulfillment_status` | How far along an order is in terms line items fulfilled. | `orders.fulfillment_status` | 🟢 _0.70_ | *Mapped to 'orders.fulfillment_status' which likely represents the same concept.* |
| `gift_card` | Whether the item is a gift card. If true, then the item is not taxed or considered for shipping charges. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `grams` | The weight of the item in grams. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | The ID of the line item. | `orders.id` | 🟢 _0.70_ | *Mapped to 'orders.id', assumes similar identity role.* |
| `name` | The name of the product variant. | `orders.name` | 🟢 _0.70_ | *Mapped to 'orders.name' likely representing the same concept.* |
| `order_id` | The ID of the related order. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `price` | The price of the item before discounts have been applied in the shop currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `product_id` | The ID of the product that the line item belongs to. Can be null if the original product associated with the order is deleted at a later date. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `quantity` | The number of items that were purchased. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `requires_shipping` | Whether the item requires shipping. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sku` | The item's SKU (stock keeping unit). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `taxable` | Whether the item was taxable. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `title` | The title of the product. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_discount` | The total amount of the discount allocated to the line item in the shop currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `variant_id` | The ID of the product variant. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `vendor` | The name of the item's supplier. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `index` | Index of the order line. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `pre_tax_price` | The pre tax price of the line item in shop currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `pre_tax_price_set` | The pre tax price of the line item in shop currency and presentment currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `price_set` | The price of the line item in shop and presentment currencies. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_code` | Tax code applied to the line item. As multiple taxes can apply to a line item, we recommend referring to `stg_shopify__tax_line`. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_discount_set` | The total amount allocated to the line item in the presentment currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `variant_title` | The title of the product variant. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `variant_inventory_management` | The fulfillment service that tracks the number of items in stock for the product variant. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `properties` | Line item properties. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `inventory_levels` to Fivetran `inventory_quantity`


- Table Match Confidence Score: ⚠️ _0.65__
- Table Completion Score: 🟢 _0.86_
- Summary Self-Evaluation: _The table match score reflects a fairly good match between the source and target table schemas, as they share related fields and concepts. However, it's not perfect due to field variations and expressions not directly matching for all fields. The completion score is high as most fields have corresponding expressions in the source schema, with '_fivetran_synced' correctly mapped to '_airbyte_extracted_at'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The unique identifier for the record. | `inventory_levels.id` | 🟢 _0.85_ | *The field 'id' from the target is matched with 'inventory_levels.id' from the source, which has a fairly high confidence as they both represent unique identifiers.* |
| `inventory_item_id` | The ID of the inventory item associated with this record. | `inventory_levels.inventory_item_id` | 🟢 _0.80_ | *The field 'inventory_item_id' is matched with 'inventory_levels.inventory_item_id', which likely represents the same concept.* |
| `inventory_level_id` | The ID of the inventory level where this item is stored. | `inventory_levels.location_id` | 🟢 _0.75_ | *The field 'inventory_level_id' is matched with 'inventory_levels.location_id'. Although they seem to relate to location, the exact match is less clear, warranting caution.* |
| `name` | The name of the inventory state associated with the record. [Link to list of expected values](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps#inventory-states). | `inventory_levels.locations_count` | ⚠️ _0.50_ | *The field 'name' is mapped to 'inventory_levels.locations_count'. This is a weaker match since 'name' typically denotes a text descriptor rather than a count.* |
| `quantity` | The available quantity of the inventory item. | `inventory_levels.available` | 🟢 _0.90_ | *The field 'quantity' is well matched with 'inventory_levels.available', both referring to the available quantity of an inventory item.* |
| `updated_at` | The timestamp of the last update to the inventory record. | `inventory_levels.updated_at` | 🟢 _0.95_ | *The field 'updated_at' is confidently mapped to 'inventory_levels.updated_at', reflecting the same timestamp for updates.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `inventory_levels._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping with 100% confidence as '_fivetran_synced' always maps to '_airbyte_extracted_at'.* |

### Mapping: Airbyte `order_refunds` to Fivetran `order_line_refund`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: ❌ _0.36_
- Summary Self-Evaluation: _The table matching is strong because both systems likely describe the same subject matter. However, many fields have missing expressions, resulting in a low completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `order_refunds._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables from '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `id` | The unique identifier of the line item in the refund. | `order_refunds.id` | 🟢 _0.70_ | *Good match found for unique identifier of the line item in refund.* |
| `location_id` | TThe unique identifier of the location where the items will be restockedBD | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `order_line_id` | The ID of the related line item in the order. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `quantity` | The quantity of the associated line item that was returned. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `refund_id` | The ID of the related refund. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `restock_type` | How this refund line item affects inventory levels. | `order_refunds.restock` | 🟢 _0.70_ | *Matched to 'order_refunds.restock', indicative of inventory level impact.* |
| `subtotal` | Subtotal amount of the order line refund in shop currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_tax` | The total tax applied to the refund in shop currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `subtotal_set` | The subtotal of the refund line item in shop and presentment currencies. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_tax_set` | The total tax of the line item in shop and presentment currencies. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `transactions` to Fivetran `transaction`


- Table Match Confidence Score: 🟢 _0.85__
- Table Completion Score: 🟢 _0.72_
- Summary Self-Evaluation: _The table match score is high due to strong similarity in table subject matter. The completion score reflects some missing mappings, lowering overall confidence._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The ID for the transaction. | `transactions.id` | 🟢 _1.00_ | *Exact match with source field.* |
| `order_id` | The ID for the order that the transaction is associated with. | `transactions.order_id` | 🟢 _1.00_ | *Exact match with source field.* |
| `refund_id` | The ID associated with a refund in the refund table. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `amount` | The amount of money included in the transaction. | `transactions.amount` | 🟢 _1.00_ | *Exact match with source field.* |
| `authorization` | The authorization code associated with the transaction. | `transactions.authorization` | 🟢 _1.00_ | *Exact match with source field.* |
| `created_at` | The date and time when the transaction was created. | `transactions.created_at` | 🟢 _1.00_ | *Exact match with source field.* |
| `processed_at` | The date and time when a transaction was processed. | `transactions.processed_at` | 🟢 _1.00_ | *Exact match with source field.* |
| `device_id` | The ID for the device. | `transactions.device_id` | 🟢 _1.00_ | *Exact match with source field.* |
| `gateway` | The name of the gateway the transaction was issued through. | `transactions.gateway` | 🟢 _1.00_ | *Exact match with source field.* |
| `source_name` | The origin of the transaction. | `transactions.source_name` | 🟢 _1.00_ | *Exact match with source field.* |
| `message` | A string generated by the payment provider with additional information about why the transaction succeeded or failed. | `transactions.message` | 🟢 _1.00_ | *Exact match with source field.* |
| `currency` | The three-letter code (ISO 4217 format) for the currency used for the payment. | `transactions.currency` | 🟢 _1.00_ | *Exact match with source field.* |
| `location_id` | The ID of the physical location where the transaction was processed. | `transactions.location_id` | 🟢 _1.00_ | *Exact match with source field.* |
| `parent_id` | The ID of an associated transaction. | `transactions.parent_id` | 🟢 _1.00_ | *Exact match with source field.* |
| `payment_avs_result_code` | The response code from the address verification system. | `transactions.payment_details.avs_result_code` | 🟢 _1.00_ | *Exact match with source field.* |
| `payment_credit_card_bin` | The issuer identification number (IIN), formerly known as bank identification number (BIN) of the customer's credit card. | `transactions.payment_details.credit_card_bin` | 🟢 _1.00_ | *Exact match with source field.* |
| `payment_cvv_result_code` | The response code from the credit card company indicating whether the customer entered the card security code, or card verification value, correctly. | `transactions.payment_details.cvv_result_code` | 🟢 _1.00_ | *Exact match with source field.* |
| `payment_credit_card_number` | The customer's credit card number, with most of the leading digits redacted. | `transactions.payment_details.credit_card_number` | 🟢 _1.00_ | *Exact match with source field.* |
| `payment_credit_card_company` | The name of the company that issued the customer's credit card. | `transactions.payment_details.credit_card_company` | 🟢 _1.00_ | *Exact match with source field.* |
| `kind` | The transaction's type. | `transactions.kind` | 🟢 _1.00_ | *Exact match with source field.* |
| `receipt` | A transaction receipt attached to the transaction by the gateway. | `transactions.receipt` | 🟢 _1.00_ | *Exact match with source field.* |
| `currency_exchange_id` | The ID of the adjustment. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `currency_exchange_adjustment` | The difference between the amounts on the associated transaction and the parent transaction. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `currency_exchange_original_amount` | The amount of the parent transaction in the shop currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `currency_exchange_final_amount` | The amount of the associated transaction in the shop currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `currency_exchange_currency` | The shop currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `error_code` | A standardized error code, independent of the payment provider. | `transactions.error_code` | 🟢 _1.00_ | *Exact match with source field.* |
| `status` | The status of the transaction. | `transactions.status` | 🟢 _1.00_ | *Exact match with source field.* |
| `test` | Whether the transaction is a test transaction. | `transactions.test` | 🟢 _1.00_ | *Exact match with source field.* |
| `user_id` | The ID for the user who was logged into the Shopify POS device when the order was processed, if applicable. | `transactions.user_id` | 🟢 _1.00_ | *Exact match with source field.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `transactions._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for synchronization fields.* |
| `authorization_expires_at` | The date and time (ISO 8601 format) when the Shopify Payments authorization expires. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `abandoned_checkouts` to Fivetran `abandoned_checkout_shipping_line`


- Table Match Confidence Score: ⚠️ _0.50__
- Table Completion Score: ❌ _0.05_
- Summary Self-Evaluation: _Only one field mapping is accurate with perfect confidence, the rest have 'MISSING' as expressions, indicating no matches found._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `abandoned_checkouts._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping from _fivetran_synced to _airbyte_extracted_at.* |
| `carrier_identifier` | A reference to the carrier service that provided the rate. Present when the rate was computed by a third-party carrier service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `checkout_id` | ID of the checkout that was abandoned. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `code` | A reference to the shipping method. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `delivery_category` | The general classification of the delivery method. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `delivery_expectation_range` | Expected delivery date range. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `delivery_expectation_range_max` | Latest expected delivery date. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `delivery_expectation_range_min` | Earliest possible expected delivery date. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `delivery_expectation_type` | Type of expected delivery. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `discounted_price` | The pre-tax shipping price with discounts applied in _presentment_ (customer) currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | Unique ID of the abandoned checkout shipping line. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `index` | Index of the line amongst shipping lines for this checkout. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `original_shop_price` | The pre-tax shipping price without any discounts applied in _presentment_ (customer) currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `phone` | The phone number at the shipping address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `price` | The price of the shipping method in presentment currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `requested_fulfillment_service_id` | The fulfillment service requested for the shipping method. Present if the shipping method requires processing by a third party fulfillment service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `source` | The channel where the checkout originated. Example value - shopify. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `title` | The title of the shipping method. Example value - International Shipping. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `transactions` to Fivetran `tax_line`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: ⚠️ _0.57_
- Summary Self-Evaluation: _The table mapping quality is relatively high, given that most field names have corresponding expressions from similar schemas. However, several fields are marked as 'MISSING,' indicating incomplete field mappings and reducing the completion score. The standard mapping of '_fivetran_synced' to '_airbyte_extracted_at' boosts confidence significantly. The lack of a logical or exact match for 'index', 'order_line_id', and 'rate' fields decreases the completion score as they are marked 'MISSING'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `transactions._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping to '_airbyte_extracted_at' with perfect confidence.* |
| `index` | The index of the tax line. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `order_line_id` | The order line that this tax line is associated with. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `price` | The amount of tax, in shop currency, after discounts and before returns. | `transactions.amount` | 🟢 _0.70_ | *'transactions.amount' correlates well with 'price', assuming it represents a monetary value which matches the description.* |
| `price_set` | The amount of tax, in shop and presentment currencies, after discounts and before returns. | `transactions.total_unsettled_set` | 🟢 _0.70_ | *'transactions.total_unsettled_set' aligns with 'price_set', inferring a comparable financial value matching the requirements.* |
| `rate` | The proportion of the line item price that the tax represents as a decimal. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `title` | The name of the tax. | `transactions.source_name` | 🟢 _0.70_ | *'transactions.source_name' is presumed to align with 'title' based on context, dealing with tax-related naming.* |

### Mapping: Airbyte `orders` to Fivetran `order`


- Table Match Confidence Score: 🟢 _0.95__
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table mapping is evaluated to have a high table match score due to the comprehensive outline of field mappings that are appropriately correlated with reasonable confidence to the target schema. However, there are fields with 'MISSING' expressions which moderately reduce the completion score as they indicate where the source schema lacks equivalent or meaningful matches._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `orders._airbyte_extracted_at` | 🟢 _1.00_ | *The '_fivetran_synced' is mapped to the source stream's '_airbyte_extracted_at' column, which is a standard mapping and always gets a score of 1.00.* |
| `app_id` | The ID of the app that created the order. | `orders.app_id` | 🟢 _0.70_ | *The 'app_id' field is mapped directly to 'orders.app_id', which is correct given the context provided.* |
| `customer_id` | The ID of the order's customer. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `confirmed` | Whether inventory has been reserved for the order. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `presentment_currency` | The presentment currency that was used to display prices to the customer. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `fulfillments` to Fivetran `order_shipping_line`


- Table Match Confidence Score: 🟢 _0.70__
- Table Completion Score: ❌ _0.21_
- Summary Self-Evaluation: _The table mapping has a partial match with high confidence for standardized fields like '_fivetran_synced'. Several fields are missing a good match, affecting the completion score significantly. The high-confidence mapping of '_fivetran_synced' to '_airbyte_extracted_at' contributes positively to the table match score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `fulfillments._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at' with high confidence.* |
| `carrier_identifier` | A reference to the carrier service that provided the rate. Present when the rate was computed by a third-party carrier service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `code` | A reference to the shipping method. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `delivery_category` | The general classification of the delivery method. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `discounted_price` | The pre-tax shipping price with discounts applied in the shop currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `discounted_price_set` | The pre-tax shipping price with discounts applied (JSON) in presentment and shop currencies. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | A globally-unique identifier. | `fulfillments.id` | 🟢 _0.70_ | *Matched 'id' with partial confidence as global unique identifier.* |
| `order_id` | ID of the associated order. | `fulfillments.order_id` | 🟢 _0.70_ | *Matched 'order_id' with partial confidence to fulfillment order ID.* |
| `phone` | The phone number at the shipping address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `price` | Returns the price of the shipping line in shop currency. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `price_set` | Returns the price of the shipping line (JSON) in presentment and shop currencies. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `requested_fulfillment_service_id` | The fulfillment service requested for the shipping method. Present if the shipping method requires processing by a third party fulfillment service. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `source` | Returns the rate source for the shipping line. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `title` | Returns the title of the shipping line. | `fulfillments.name` | 🟢 _0.70_ | *Matched 'title' with partial confidence as the title of the shipping line.* |

### Mapping: Airbyte `orders` to Fivetran `order_note_attribute`


- Table Match Confidence Score: ⚠️ _0.65__
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table mapping reflects a moderate confidence level due to missing mappings. Field-level mappings include both perfect and missing entries._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `orders._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `name` | Name of the attribute. | `orders.name` | 🟢 _0.70_ | *Mapping 'name' to 'orders.name' is plausible with moderate confidence.* |
| `order_id` | ID referencing the order the note attribute belongs to. | `orders.id` | 🟢 _0.70_ | *Mapping 'order_id' to 'orders.id' is plausible with moderate confidence.* |
| `value` | Value of the attribute. | `MISSING` | ❌ _0.00_ | *No good match found.* |
