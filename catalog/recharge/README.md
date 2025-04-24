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

> [!Tip]
> Use the right-hand navigation to quickly browse available dataset mappings.

> [!Warning]
> AI-generated results may contain errors. Please sanity check results and adapt these resources to your needs accordingly.


### Mapping: Airbyte `customers` to Fivetran `customer`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table mapping demonstrates a high quality of alignment between the source and target schemas, indicating they are likely from similar data streams. The completion score is slightly lower due to some fields like '_fivetran_deleted' not having a proper mapping, indicating that not all fields from the source are currently being utilized or mapped in the target schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | The unique ID of the customer. | `customers.id` | 🟢 _1.00_ | *Direct mapping of customer IDs.* |
| `hash` | The unique string identifier used in a customer portal link. | `customers.hash` | 🟢 _1.00_ | *Direct mapping of unique identifier hashes.* |
| `external_customer_id_ecommerce` | External platform's unique identifier for the customer. | `customers.external_customer_id.ecommerce` | 🟢 _1.00_ | *Direct correlation to an external platform identifier for customers.* |
| `email` | The email address of the customer. | `customers.email` | 🟢 _1.00_ | *Direct mapping of customer email addresses.* |
| `created_at` | The date and time when the customer was created. | `customers.created_at` | 🟢 _1.00_ | *Direct mapping of the customer creation timestamp.* |
| `updated_at` | The date and time when the customer was last updated. | `customers.updated_at` | 🟢 _1.00_ | *Direct mapping of the last update timestamp.* |
| `first_charge_processed_at` | Date when first charge was processed for the customer. | `customers.first_charge_processed_at` | 🟢 _1.00_ | *Direct mapping to the date of first charge processing.* |
| `first_name` | The customer's first name. | `customers.first_name` | 🟢 _1.00_ | *Direct mapping of first names.* |
| `last_name` | The customer's last name. | `customers.last_name` | 🟢 _1.00_ | *Direct mapping of last names.* |
| `subscriptions_active_count` | The number of active subscriptions associated with the customer. | `customers.number_active_subscriptions` | 🟢 _0.70_ | *Likely mapping of active subscriptions, as the confidence is lower due to potential nuances in definitions between active subscriptions documented across platforms.* |
| `subscriptions_total_count` | The total number of subscriptions associated with the customer. | `customers.number_subscriptions` | 🟢 _0.70_ | *Likely mapping of total subscription counts, with a reduced confidence due to differences in the potential definition or coverage of 'total subscriptions' across implementations.* |
| `has_valid_payment_method` | Boolean indicating if the payment value is valid. | `customers.has_valid_payment_method` | 🟢 _1.00_ | *Direct mapping of a boolean indicator for valid payment methods.* |
| `has_payment_method_in_dunning` | Boolean indicating if the customer has a credit card in dunning. | `customers.has_card_error_in_dunning` | 🟢 _1.00_ | *Direct mapping of a boolean indicating credit card issues.* |
| `tax_exempt` | Boolean indicating if the customer is tax exempt. | `customers.tax_exempt` | 🟢 _1.00_ | *Direct mapping of tax exemption status.* |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `customers._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of extracted times to Airbyte sync times.* |

### Mapping: Airbyte `orders` to Fivetran `charge_order_attribute`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mapping is done accurately. Most of the field mappings are filled properly, with a high level of confidence in the accuracy of the mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `charge_id` | {{ doc('charge_id') }} | `orders.charge_id` | 🟢 _1.00_ | *Perfect mapping, direct match.* |
| `index` | A unique numeric row produced for every concurrent charge_id. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `order_attribute` | An array of name-value pairs of order attributes on the charge. | `orders.order_attributes` | 🟢 _0.70_ | *Matching field, slight differences in schema terminology.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `orders._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for synchronization timestamp.* |

### Mapping: Airbyte `subscriptions` to Fivetran `subscription`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.78_
- Summary Self-Evaluation: _The evaluation reflects a strong match in subject matter between the source and target schemas with the majority of fields mapped properly. However, some fields lack good matches, affecting the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | {{ doc('subscription_id') }} | `subscriptions.id` | 🟢 _1.00_ | *Direct mapping.* |
| `address_id` | {{ doc('address_id') }} | `subscriptions.address_id` | 🟢 _1.00_ | *Direct mapping.* |
| `customer_id` | {{ doc('customer_id') }} | `subscriptions.customer_id` | 🟢 _1.00_ | *Direct mapping.* |
| `created_at` | The date and time when the subscription was created. | `subscriptions.created_at` | 🟢 _1.00_ | *Direct mapping.* |
| `cancelled_at` | The date and time when the subscription was cancelled. | `subscriptions.cancelled_at` | 🟢 _1.00_ | *Direct mapping.* |
| `next_charge_scheduled_at` | Date of the next charge for the subscription. | `subscriptions.next_charge_scheduled_at` | 🟢 _1.00_ | *Direct mapping.* |
| `price` | The price of the item before discounts, taxes, or shipping have been applied. | `subscriptions.price` | 🟢 _1.00_ | *Direct mapping.* |
| `quantity` | The number of items in the subscription. | `subscriptions.quantity` | 🟢 _1.00_ | *Direct mapping.* |
| `status` | {{ doc('subscription_status') }} | `subscriptions.status` | 🟢 _1.00_ | *Direct mapping.* |
| `cancellation_reason` | Reason provided for cancellation. | `subscriptions.cancellation_reason` | 🟢 _1.00_ | *Direct mapping.* |
| `cancellation_reason_comments` | Additional comment for cancellation. | `subscriptions.cancellation_reason_comments` | 🟢 _1.00_ | *Direct mapping.* |
| `product_title` | The name of the product in a shop's catalog. | `subscriptions.product_title` | 🟢 _1.00_ | *Direct mapping.* |
| `variant_title` | The name of the variant in a shop's catalog. | `subscriptions.variant_title` | 🟢 _1.00_ | *Direct mapping.* |
| `external_product_id_ecommerce` | Unique numeric identifier of the product in your external ecommerce platform. | `subscriptions.external_product_id.ecommerce` | 🟢 _1.00_ | *Direct mapping.* |
| `external_variant_id_ecommerce` | Unique numeric identifier of the product variant in your external ecommerce platform. | `subscriptions.external_variant_id.ecommerce` | 🟢 _1.00_ | *Direct mapping.* |
| `sku` | A unique identifier of the item in fulfillment. | `subscriptions.sku` | 🟢 _1.00_ | *Direct mapping.* |
| `order_interval_unit` | The frequency with which a subscription should have the order created with (valid values are “day”, “week”, and “month”). | `subscriptions.order_interval_unit` | 🟢 _1.00_ | *Direct mapping.* |
| `order_interval_frequency` | The number of units (specified in order_interval_unit) between each order, e.g. order_interval_unit = 'month' and order_interval frequency = 3 indicates an order every 3 months. | `subscriptions.order_interval_frequency` | 🟢 _1.00_ | *Direct mapping.* |
| `charge_interval_frequency` | The number of units (specified in order_interval_unit) between each charge. | `subscriptions.charge_interval_frequency` | 🟢 _1.00_ | *Direct mapping.* |
| `order_day_of_week` | The set day of the week order is created. This is only applicable to subscriptions with order_interval_unit = “week”. | `subscriptions.order_day_of_week` | 🟢 _0.70_ | *Potential mismatch in underlined semantics despite similar names.* |
| `order_day_of_month` | The set day of the month order is created. This is only applicable to subscriptions with order_interval_unit = “month”. | `subscriptions.order_day_of_month` | 🟢 _0.70_ | *Potential mismatch in underlined semantics despite similar names.* |
| `expire_after_specific_number_of_charges` | Set number of charges until subscription expires. | `subscriptions.expire_after_specific_number_of_charges` | 🟢 _1.00_ | *Direct mapping.* |
| `updated_at` | The date and time when the subscription was created. | `subscriptions.updated_at` | 🟢 _1.00_ | *Direct mapping.* |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `subscriptions._airbyte_extracted_at` | 🟢 _1.00_ | *Exact match expected as a standard mapping.* |

### Mapping: Airbyte `orders` to Fivetran `order`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _Most field mappings have a strong alignment with the target schema, indicating a high likelihood that the source and target tables describe the same subject matter. However, some fields like 'is_deleted' lack a corresponding target field, slightly reducing the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | {{ doc('order_id') }} | `orders.id` | 🟢 _1.00_ | *Direct match found.* |
| `customer_id` | {{ doc('customer_id') }} | `orders.customer.id` | 🟢 _1.00_ | *Direct match found.* |
| `address_id` | {{ doc('address_id') }} | `orders.address_id` | 🟢 _1.00_ | *Direct match found.* |
| `charge_id` | The unique numeric identifier of the charge. | `orders.charge.id` | 🟢 _1.00_ | *Direct match found.* |
| `is_deleted` | Boolean indicating if the order (record) is deleted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email` | The email address of the customer. | `orders.email` | 🟢 _1.00_ | *Direct match found.* |
| `transaction_id` | The unique alphanumeric identifier of the transaction. | `orders.transaction_id` | 🟢 _1.00_ | *Direct match found.* |
| `charge_status` | {{ doc('charge_status') }} | `orders.charge.status` | 🟢 _1.00_ | *Direct match found.* |
| `is_prepaid` | Boolean indicating if the Order is prepaid. | `orders.is_prepaid` | 🟢 _1.00_ | *Direct match found.* |
| `status` | {{ doc('order_status') }} | `orders.status` | 🟢 _1.00_ | *Direct match found.* |
| `total_price` | The sum of all prices of the item in the order with taxes and discounts included (must be positive). | `orders.total_price` | 🟢 _1.00_ | *Direct match found.* |
| `type` | {{ doc('type') }} | `orders.type` | ⚠️ _0.50_ | *Matching options are not clear.* |
| `external_order_id_ecommerce` | Unique numeric identifier within your external ecommerce platform for the order. | `orders.external_order_id.ecommerce` | 🟢 _1.00_ | *Direct match found.* |
| `external_order_number_ecommerce` | The unique order number within your external ecommerce platform. | `orders.external_order_number.ecommerce` | 🟢 _1.00_ | *Direct match found.* |
| `created_at` | The date and time when the order was created. | `orders.created_at` | 🟢 _1.00_ | *Direct match found.* |
| `updated_at` | The date and time when the order was last updated. | `orders.updated_at` | 🟢 _1.00_ | *Direct match found.* |
| `processed_at` | The date and time when the order was submitted. | `orders.processed_at` | 🟢 _1.00_ | *Direct match found.* |
| `scheduled_at` | The date and time when the order will be shipped. | `orders.scheduled_at` | 🟢 _1.00_ | *Direct match found.* |
| `shipped_date` | The date when the order will be processed. | `orders.shipped_date` | 🟢 _1.00_ | *Direct match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `orders._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables. Direct match for '_airbyte_extracted_at'.* |

### Mapping: Airbyte `subscriptions` to Fivetran `subscription_history`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _Most mappings are conceptually aligned, indicating a high-quality match between source and target schema. A couple of fields show no direct correspondences or are set to 'MISSING', leading to a slightly lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `subscription_id` | {{ doc('subscription_id') }} | `subscriptions.id` | 🟢 _1.00_ | *Direct match found with precise field names matching.* |
| `updated_at` | The date time at which the purchase_item record was last updated. | `subscriptions.updated_at` | 🟢 _0.95_ | *Direct match found with time-based fields matching.* |
| `address_id` | {{ doc('address_id') }} | `subscriptions.address_id` | 🟢 _1.00_ | *Direct match found with precise field names matching.* |
| `customer_id` | {{ doc('customer_id') }} | `subscriptions.customer_id` | 🟢 _1.00_ | *Direct match found with precise field names matching.* |
| `created_at` | The date and time the subscription was created. | `subscriptions.created_at` | 🟢 _1.00_ | *Direct match found with time-based fields matching.* |
| `cancelled_at` | The date and time the subscription was cancelled. | `subscriptions.cancelled_at` | 🟢 _1.00_ | *Direct match found with time-based fields matching.* |
| `next_charge_scheduled_at` | Date of the next charge for the subscription. | `subscriptions.next_charge_scheduled_at` | 🟢 _1.00_ | *Direct match found with time-based fields matching.* |
| `price` | The price of the item before discounts, taxes, or shipping have been applied. | `subscriptions.price` | 🟢 _1.00_ | *Direct match found with monetary terms matching.* |
| `quantity` | The number of items in the subscription. | `subscriptions.quantity` | 🟢 _1.00_ | *Direct match found reflecting count.* |
| `cancellation_reason` | Reason provided for cancellation. | `subscriptions.cancellation_reason` | 🟢 _1.00_ | *Direct match found for description fields.* |
| `status` | {{ doc('subscription_status') }} | `subscriptions.status` | 🟢 _0.70_ | *Match found. Slight ambiguity in categorical status fields could bring variations but are generally reflective of similar attributes.* |
| `cancellation_reason_comments` | Additional comment for cancellation. | `subscriptions.cancellation_reason_comments` | 🟢 _1.00_ | *Direct match found for description fields.* |
| `product_title` | The name of the product in a store’s catalog. | `subscriptions.product_title` | 🟢 _1.00_ | *Direct match found reflecting item identification.* |
| `variant_title` | The name of the variant in a shop’s catalog. | `subscriptions.variant_title` | 🟢 _1.00_ | *Direct match found reflecting detailed item identification.* |
| `external_product_id_ecommerce` | An object containing the product id as it appears in external platforms. | `subscriptions.external_product_id.ecommerce` | ⚠️ _0.60_ | *Mapped with a nested structure indicating external ID connection, less confident due to nested fields but acceptable.* |
| `external_variant_id_ecommerce` | An object containing the variant id as it appears in external platforms. | `subscriptions.external_variant_id.ecommerce` | ⚠️ _0.60_ | *Mapped with a nested structure indicating external ID connection, less confident due to nested fields but acceptable.* |
| `sku` | A unique identifier of the item in the fulfillment. In cases where SKU is blank, it will be dynamically pulled whenever it is used. | `subscriptions.sku` | 🟢 _1.00_ | *Direct match found reflecting unique inventory identifier.* |
| `order_interval_unit` | The frequency unit used to determine when a subscription’s order is created. | `subscriptions.order_interval_unit` | ⚠️ _0.60_ | *Mapped considering similar function and conceptual usage in subscription settings.* |
| `order_interval_frequency` | The number of units (specified in order_interval_unit) between each order. For example, order_interval_unit = month and order_interval_frequency = 3, indicate order every 3 months. | `subscriptions.order_interval_frequency` | ⚠️ _0.60_ | *Mapped considering similar frequency determinations in subscription contexts.* |
| `charge_interval_frequency` | The number of units (specified in order_interval_unit) between each Charge. For example, order_interval_unit=month and charge_interval_frequency=3, indicate charge every 3 months. | `subscriptions.charge_interval_frequency` | ⚠️ _0.60_ | *Mapped considering similar frequency determinations in charge contexts.* |
| `order_day_of_week` | The set day of the week order is created. Default is that there isn’t a strict day of the week order is created. | `subscriptions.order_day_of_week` | 🟢 _1.00_ | *Direct match found considering identical specific day scheduling.* |
| `order_day_of_month` | The set day of the month order is created. Default is that there isn’t a strict day of the month when the order is created. | `subscriptions.order_day_of_month` | 🟢 _1.00_ | *Direct match found considering identical specific day scheduling.* |
| `expire_after_specific_number_of_charges` | Set the number of charges until subscription expires. | `subscriptions.expire_after_specific_number_of_charges` | 🟢 _1.00_ | *Direct match found considering identical charge condition.* |
| `_fivetran_deleted` | {{ doc('_fivetran_deleted') }} | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `subscriptions._airbyte_extracted_at` | 🟢 _1.00_ | *Direct mapping to '_airbyte_extracted_at' as per standard schema requirements.* |

### Mapping: Airbyte `discounts` to Fivetran `discount`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping effectively matches the source and target schema based on similar subject matter. All key fields have been appropriately mapped, with high confidence in the mapping's integrity._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | {{ doc('discount_id') }} | `discounts.id` | 🟢 _1.00_ | *Perfect match of field names and context.* |
| `created_at` | The date and time when the discount was created. | `discounts.created_at` | 🟢 _1.00_ | *Exact match of field name and context.* |
| `updated_at` | The date and time when the discount was last updated. | `discounts.updated_at` | 🟢 _1.00_ | *Exact match of field name and context.* |
| `starts_at` | The date when the discount becomes active. | `discounts.starts_at` | 🟢 _1.00_ | *Exact match of field names, accurately reflecting the intended usage.* |
| `ends_at` | The expiration time of the discount, past this time the discount can no longer be redeemed, once the time of the discount has passed the status of the discount will go from 'active' to 'disabled'. | `discounts.ends_at` | 🟢 _1.00_ | *Perfect alignment of field name and meaning.* |
| `code` | The code used to apply the discount. | `discounts.code` | 🟢 _1.00_ | *Direct correlation between the field names and usage.* |
| `value` | The discounted value to be applied. | `discounts.value` | 🟢 _1.00_ | *Field names and contexts are identical, ensuring a flawless mapping.* |
| `status` | {{ doc('discount_status') }} | `discounts.status` | 🟢 _1.00_ | *Field names and contexts align perfectly.* |
| `usage_limits` | An integer indicating how many times the discount can been used. | `discounts.usage_limit` | ⚠️ _0.60_ | *Adequate match with some differences in naming but similar context.* |
| `applies_to` | Indicates where the discount applies. | `discounts.applies_to` | ⚠️ _0.60_ | *Sufficient similarity in application context, despite minor differences.* |
| `applies_to_resource` | An indicator of the type of resource which applies_to_id refers. | `discounts.applies_to_resource` | ⚠️ _0.60_ | *Reasonable alignment, suitable for mapping despite slight variances.* |
| `applies_to_id` | A list of ids of the type indicated in applies_to_resource for which the discount can be applied. | `discounts.applies_to_id` | ⚠️ _0.60_ | *Enough similarities are present to justify mapping, with minor discrepancies.* |
| `applies_to_product_type` | Indicates which product types the discount applies to. | `discounts.applies_to_product_type` | ⚠️ _0.60_ | *Correspondence in function between the fields supports a viable mapping.* |
| `minimum_order_amount` | The minimum cart subtotal needed for the discount to be applicable. `duration` has to be `single_use` and the discount must apply to the entire order. | `discounts.prerequisite_subtotal_min` | ⚠️ _0.60_ | *Matches in intent and usage, suitable for mapping.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `discounts._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for all tables, perfectly matches the `_airbyte_extracted_at` column.* |

### Mapping: Airbyte `addresses` to Fivetran `address`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: 🟢 _0.93_
- Summary Self-Evaluation: _The table match score is high as the fields closely resemble each other from the source to the target. However, completion is slightly lowered due to one missing field mapping._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique numeric identifier for the address. | `addresses.id` | 🟢 _1.00_ | *Direct match found.* |
| `customer_id` | {{ doc('customer_id') }} | `addresses.customer_id` | 🟢 _0.70_ | *Fuzzy match found with acceptable contextual similarity.* |
| `first_name` | The customer's first name. | `addresses.first_name` | 🟢 _1.00_ | *Direct match found.* |
| `last_name` | The customer's last name. | `addresses.last_name` | 🟢 _1.00_ | *Direct match found.* |
| `address_1` | The street associated with the address. | `addresses.address1` | 🟢 _1.00_ | *Direct match found.* |
| `address_2` | Any additional information associated with the address. | `addresses.address2` | 🟢 _1.00_ | *Direct match found.* |
| `city` | The city associated with the address. | `addresses.city` | 🟢 _1.00_ | *Direct match found.* |
| `province` | The state or province associated with the address. | `addresses.province` | 🟢 _1.00_ | *Direct match found.* |
| `country_code` | The country code associated with the address. | `addresses.country_code` | 🟢 _1.00_ | *Direct match found.* |
| `zip` | The zip or postal code associated with the address. | `addresses.zip` | 🟢 _1.00_ | *Direct match found.* |
| `company` | The company associated with the address. | `addresses.company` | 🟢 _1.00_ | *Direct match found.* |
| `phone` | The phone number associated with the address. | `addresses.phone` | 🟢 _1.00_ | *Direct match found.* |
| `created_at` | The date and time when the address was created. | `addresses.created_at` | 🟢 _1.00_ | *Direct match found.* |
| `updated_at` | The date and time when the address was last updated. | `addresses.updated_at` | 🟢 _1.00_ | *Direct match found.* |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `addresses._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping as per requirements.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
