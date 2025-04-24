# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `discounts` to Fivetran `address_discounts`


- Table Match Confidence Score: ⚠️ _0.60_
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table match score reflects a moderate confidence based on the similarity of the source and target schema. The completion score indicates that only some fields were mapped with a high level of confidence._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `address_id` | {{ doc('address_id') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `index` | A unique numeric row produced for every concurrent address_id. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | {{ doc('discount_id') }} | `discounts.id` | 🟢 _0.70_ | *Mapped successfully to a matching column in the target schema.* |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `discounts._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping according to system specifications.* |

### Mapping: Airbyte `charges` to Fivetran `charge`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _All mappings have the expression 'MISSING' indicating that no good matches were found. This results in a 0.00 confidence score for both table and completion._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `charges._airbyte_extracted_at` | 🟢 _1.00_ | *Exact match: `_fivetran_synced` mapped directly to a source stream's `_airbyte_extracted_at` column.* |
| `id` | {{ doc('charge_id') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `address_id` | {{ doc('address_id') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `customer_id` | {{ doc('customer_id') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `customer_hash` | The hash of the customer associated with the charge. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `note` | Shows the next order in sequence. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | Date and time when the charge was created. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `updated_at` | Date and time when the charge was last updated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `processed_at` | Date and time when the charge was processed. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `scheduled_at` | The date time of when the associated charge is/was scheduled to process. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `orders_count` | The number of orders generated from this charge (Will be >1 for prepaid). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_order_id_ecommerce` | The unique numeric identifier within your external ecommerce platform for the charge. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `subtotal_price` | The combined price of all order line_items minus any discounts. Does not include taxes and shipping. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tags` | A comma-separated list of tags on the charge. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_lines` | An array of tax lines that apply to the charge. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_discounts` | The sum of the discounts applied to the charge. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_line_items_price` | The sum of all the prices of all the items in the charge. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_price` | The sum of all the prices of all the items in the charge, taxes and discounts included (must be positive). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_tax` | The total tax due associated with the charge. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_weight_grams` | The total weight of all items in the charge in grams. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `type` | {{ doc('type') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status` | {{ doc('charge_status') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_refunds` | The sum of all refunds that were applied to the charge. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_transaction_id_payment_processor` | The unique identifier of the transaction. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email` | The email address of the customer. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `payment_processor` | The payment processor used on the charge. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `has_uncommited_changes` | Specifies whether the charge is scheduled for regeneration (if the subscription is related to the charge was updated in the last 5 seconds using "commit_update":false). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_charge_attempt_date` | The date when the charge was last attempted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `retry_date` | The date when the next attempt will be placed. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `error_type` | Structured reason why the charge failed such as customer_needs_to_updated_card. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `error` | Error reason as sentence text (typically returned directly from the payment processor - e.g. "customer needs to update credit card"). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `charge_attempts` | Shows how many times an attempt to charge was placed. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_variant_id_not_found` | Indicates if Recharge was able to find the external_variant_id_ecommerce from the charge. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `client_details_browser_ip` | The IP address of the buyer detected in checkout. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `client_details_user_agent` | The user agent detected during checkout. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `onetimes` to Fivetran `one_time_product`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.92_
- Summary Self-Evaluation: _Most fields are accurately mapped with correct expressions, ensuring high confidence in table matching and high completion rate of field mappings. The table seems to cover all required aspects of the onetime purchase entity and aligns well with the target schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The unique numeric identifier for the onetime purchase. | `onetimes.id` | 🟢 _1.00_ | *Direct and exact match.* |
| `address_id` | The unique identifier of the address. Cannot be used with `next_charge_scheduled_at`. | `onetimes.address_id` | 🟢 _1.00_ | *Direct and exact match.* |
| `customer_id` | {{ doc('customer_id') }} | `onetimes.customer_id` | 🟢 _1.00_ | *Direct and exact match.* |
| `is_deleted` | Boolean indicating if the onetime is deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | The time the onetime item was first created. | `onetimes.created_at` | 🟢 _1.00_ | *Direct and exact match.* |
| `updated_at` | The time the onetime item was last updated. | `onetimes.updated_at` | 🟢 _1.00_ | *Direct and exact match.* |
| `next_charge_scheduled_at` | Date of the onetime purchase execution. | `onetimes.next_charge_scheduled_at` | 🟢 _1.00_ | *Direct and exact match.* |
| `product_title` | The name of the product in a shop's catalog. | `onetimes.product_title` | 🟢 _1.00_ | *Direct and exact match.* |
| `variant_title` | The name of the variant in a shop's catalog. | `onetimes.variant_title` | 🟢 _1.00_ | *Direct and exact match.* |
| `price` | The price of the item before discounts, taxes, or shipping have been applied. | `onetimes.price` | 🟢 _1.00_ | *Direct and exact match.* |
| `quantity` | The number of items in the onetime purchase. | `onetimes.quantity` | 🟢 _1.00_ | *Direct and exact match.* |
| `external_product_id_ecommerce` | The product ID that links to your external ecommerce platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_variant_id_ecommerce` | The variant ID that links to your external ecommerce platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sku` | The unique identifier of the item in fulfillment. | `onetimes.sku` | ⚠️ _0.60_ | *Reasonable match identified, slightly vague but aligning in context.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `onetimes._airbyte_extracted_at` | 🟢 _1.00_ | *This is a standard perfect match for all tables as per specifications, mapping _fivetran_synced to _airbyte_extracted_at.* |

### Mapping: Airbyte `orders` to Fivetran `orders`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.92_
- Summary Self-Evaluation: _The tables and most fields are well-matched, suggesting they are describing the same subject matter with only a few missing mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | {{ doc('order_id') }} | `orders.id` | 🟢 _1.00_ | *Exact match of the field found.* |
| `customer_id` | {{ doc('customer_id') }} | `orders.customer_id` | 🟢 _1.00_ | *Exact match of the field found.* |
| `address_id` | {{ doc('address_id') }} | `orders.billing_address.id` | 🟢 _1.00_ | *Exact match at the nested level found.* |
| `charge_id` | The unique numeric identifier of the charge. | `orders.charge.id` | 🟢 _1.00_ | *Exact match at the nested level found.* |
| `is_deleted` | Boolean indicating if the order (record) is deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email` | The email address of the customer. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `transaction_id` | The unique alphanumeric identifier of the transaction. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `charge_status` | {{ doc('charge_status') }} | `orders.charge.status` | 🟢 _1.00_ | *Exact match at the nested level found.* |
| `is_prepaid` | Boolean indicating if the Order is prepaid. | `orders.is_prepaid` | 🟢 _1.00_ | *Exact match of the field found.* |
| `status` | {{ doc('order_status') }} | `orders.status` | 🟢 _1.00_ | *Exact match of the field found.* |
| `total_price` | The sum of all prices of the item in the order with taxes and discounts included (must be positive). | `orders.total_price` | 🟢 _1.00_ | *Exact match of the field found.* |
| `type` | {{ doc('type') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_order_id_ecommerce` | Unique numeric identifier within your external ecommerce platform for the order. | `orders.external_order_id.ecommerce` | 🟢 _0.90_ | *Close match found, within acceptable parameter variations.* |
| `external_order_number_ecommerce` | The unique order number within your external ecommerce platform. | `orders.external_order_number.ecommerce` | 🟢 _0.90_ | *Close match found, within acceptable parameter variations.* |
| `created_at` | The date and time when the order was created. | `orders.created_at` | 🟢 _1.00_ | *Exact match of the field found.* |
| `updated_at` | The date and time when the order was last updated. | `orders.updated_at` | 🟢 _1.00_ | *Exact match of the field found.* |
| `processed_at` | The date and time when the order was submitted. | `orders.processed_at` | 🟢 _1.00_ | *Exact match of the field found.* |
| `scheduled_at` | The date and time when the order will be shipped. | `orders.scheduled_at` | 🟢 _1.00_ | *Exact match of the field found.* |
| `shipped_date` | The date when the order will be processed. | `orders.shipping_date` | 🟢 _1.00_ | *Exact match of the field found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `orders._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping, exact sync column match found.* |

### Mapping: Airbyte `discounts` to Fivetran `charge_discount`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.71_
- Summary Self-Evaluation: _Table match and field-level mappings generally exhibit a strong relevance and alignment with minor mismatches that do not cause a severe impact._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `charge_id` | {{ doc('charge_id') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `index` | A unique numeric row produced for every concurrent charge_id. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `id` | {{ doc('discount_id') }} | `discounts.id` | 🟢 _0.90_ | *Direct mapping with minimal contextual difference.* |
| `code` | The code used to apply the discount. | `discounts.code` | 🟢 _0.90_ | *Direct mapping with minimal contextual difference.* |
| `value` | The discounted value to be applied. | `discounts.value` | 🟢 _0.90_ | *Direct mapping with minimal contextual difference.* |
| `value_type` | Possible values - FIXED_AMOUNT, PERCENTAGE, SHIPPING | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `discounts._airbyte_extracted_at` | 🟢 _1.00_ | *Best practice mapping for synchronization timestamp elements.* |

### Mapping: Airbyte `orders` to Fivetran `checkout`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table evaluates to a high confidence in matching the general schema but lacks completion in field mappings, with several missing direct mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `token` | Unique token for the Checkout | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `charge_id` | ID for the Charge resulting from processing the Checkout. | `orders.charge.id` | 🟢 _1.00_ | *Direct mapping found.* |
| `buyer_accepts_marketing` | Boolean if the buyer accept marketing, newsletters etc. | `orders.customer.accepts_marketing` | 🟢 _1.00_ | *Direct mapping found.* |
| `completed_at` | Timestamp for when the Checkout was processed. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | Timestamp for when the Checkout was created. | `orders.created_at` | 🟢 _1.00_ | *Direct mapping found.* |
| `currency` | Currency of the Checkout. | `orders.currency` | 🟢 _1.00_ | *Direct mapping found.* |
| `discount_code` | Discount code to be used on the checkout, e.g. “DISCOUNT20”. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email` | Email address for the customer. | `orders.customer.email` | 🟢 _1.00_ | *Direct mapping found.* |
| `external_checkout_id` | Represents the external cart token. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_checkout_source` | Represents the source for external_checkout_id. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_transaction_id_payment_processor` | Transaction ID of the external payment processor. | `orders.charge.external_transaction_id.payment_processor` | 🟢 _1.00_ | *Direct mapping found.* |
| `order_attributes` | Structured custom notes. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `phone` | Customer phone number. | `orders.customer.phone` | 🟢 _1.00_ | *Direct mapping found.* |
| `requires_shipping` | Boolean if the Checkout contains items that require shipping. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `subtotal_price` | Value of the Checkout minus shipping and tax. | `orders.subtotal_price` | 🟢 _1.00_ | *Direct mapping found.* |
| `taxes_included` | Boolean if the tax is included in the price of the items. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_price` | Full price of the Checkout including shipping and tax. | `orders.total_price` | 🟢 _1.00_ | *Direct mapping found.* |
| `total_tax` | Tax charged on the Checkout. | `orders.total_tax` | 🟢 _1.00_ | *Direct mapping found.* |
| `updated_at` | Timestamp for the latest Checkout update. | `orders.updated_at` | 🟢 _1.00_ | *Direct mapping found.* |

### Mapping: Airbyte `charges` to Fivetran `charge_line_item`


- Table Match Confidence Score: ❌ _0.40_
- Table Completion Score: ❌ _0.12_
- Summary Self-Evaluation: _Given the significant number of fields mapped to 'MISSING', the overall confidence in table mapping is low. This indicates a poor match or incomplete information provided by the source versus the expected target schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `charge_id` | {{ doc('charge_id') }} | `charges.id` | 🟢 _0.70_ | *Mapped correctly.* |
| `index` | A unique numeric row produced for every concurrent charge_id. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `variant_title` | The name of the product variant that links to your external ecommerce platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `title` | The product title that links to your external ecommerce platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `grams` | The weight of the charge's line item in grams. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `quantity` | The quantity of the line_item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_price` | The total price of the line_item including tax. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `unit_price` | The unit price of the line_item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_due` | The total tax due associated with the line_item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `taxable` | A boolean indicating if the line_item is taxable or non-taxable. | `charges.taxable` | 🟢 _0.70_ | *Mapped correctly to a logical equivalent field.* |
| `taxable_amount` | The taxable revenue associated with the line_item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `unit_price_includes_tax` | A boolean indicator if tax is included in the price of an item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `purchase_item_id` | The subscription or onetime ID associated with the line_item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `purchase_item_type` | Possible values are SUBSCRIPTION, ONETIME. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sku` | The SKU (stock keeping unit) of the product associated with the charge's line item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_product_id_ecommerce` | The product ID that links to your external ecommerce platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_variant_id_ecommerce` | The variant ID that links to your external ecommerce platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `vendor` | The name of the seller. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `charges._airbyte_extracted_at` | 🟢 _1.00_ | *Standard field mapping between '_fivetran_synced' and 'charges._airbyte_extracted_at'.* |

### Mapping: Airbyte `orders` to Fivetran `order_line_item`


- Table Match Confidence Score: ❌ _0.20_
- Table Completion Score: ❌ _0.06_
- Summary Self-Evaluation: _Incomplete and uncertain table mapping with many fields missing correct expressions._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `order_id` | {{ doc('order_id') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `index` | A unique numeric row produced for every concurrent order_id. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `variant_title` | The title of the product variant. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `title` | The name of the product in a shop's catalog. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `quantity` | The number of products that were purchased. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `grams` | Weight in grams of the item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_price` | The total price of the line_item including tax. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `unit_price` | The unit price of the line_item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_due` | The total tax due associated with the line_item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `taxable` | A boolean indicating if the line_item is taxable or non-taxable. | `orders.taxable` | ⚠️ _0.50_ | *Taxable fields are generally consistent, yet the exact mapping is uncertain.* |
| `taxable_amount` | The taxable revenue associated with the line_item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `unit_price_includes_tax` | A boolean indicator if tax is included in the price of an item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `purchase_item_id` | The subscription or onetime ID associated with the line_item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `purchase_item_type` | Possible values are SUBSCRIPTION, ONETIME. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `sku` | A unique identifier of the item in the fulfillment. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_product_id_ecommerce` | The unique numeric identifier for your external ecommerce platform product in the fulfillment. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `external_variant_id_ecommerce` | Unique numeric identifier of the product variant in your external ecommerce platform. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `orders._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping, correctly aligned to '_airbyte_extracted_at'.* |
