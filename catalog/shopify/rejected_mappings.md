# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `fulfillments` to Fivetran `fulfillment_event`


- Table Match Confidence Score: 🟢 _0.85_
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

### Mapping: Airbyte `customers` to Fivetran `customer_tag`


- Table Match Confidence Score: ⚠️ _0.60_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The mapping includes standard and missing field expressions. Standard mappings like '_fivetran_synced' were given a high score, while missing fields were penalized._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `customers._airbyte_extracted_at` | 🟢 _1.00_ | *Mapped to a source stream's '_airbyte_extracted_at' as per standard.* |
| `index` | Index (starting from 1) represnting when the tag was placed on the customer. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING'. No good match found.* |
| `customer_id` | ID of the customer being tagged. | `customers.default_address.customer_id` | 🟢 _0.70_ | *Mapped to 'customers.default_address.customer_id'. Considered a likely match with some uncertainty.* |
| `value` | Value of the tag. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING'. No good match found.* |

### Mapping: Airbyte `order_refunds` to Fivetran `order_line_refund`


- Table Match Confidence Score: 🟢 _0.70_
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


- Table Match Confidence Score: 🟢 _0.85_
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

### Mapping: Airbyte `discount_codes` to Fivetran `abandoned_checkout_discount_code`


- Table Match Confidence Score: 🟢 _0.70_
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

### Mapping: Airbyte `product_images` to Fivetran `product_image`


- Table Match Confidence Score: 🟢 _0.85_
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

### Mapping: Airbyte `metafield_orders` to Fivetran `order_url_tag`


- Table Match Confidence Score: ⚠️ _0.50_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table match score is 0.5 due to partial similarity between the source and target schemas. The completion score is 0.75 as most fields are mapped, but some are missing or poorly matched._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `metafield_orders._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at', always scores 1.0.* |
| `key` | Key of the tag pair. | `metafield_orders.key` | 🟢 _0.70_ | *Fields 'key' in source and 'key' in target are likely referring to the same entity, mapped with a score of 0.7.* |
| `order_id` | ID of the order url being tagged. | `MISSING` | ❌ _0.00_ | *Expression is 'MISSING', no good match found.* |
| `value` | Value of the tag. | `metafield_orders.value` | ⚠️ _0.60_ | *Fields 'value' in source and 'value' in target mapped with a lower confidence due to minimal contextual match.* |

### Mapping: Airbyte `transactions` to Fivetran `tax_line`


- Table Match Confidence Score: 🟢 _0.70_
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

### Mapping: Airbyte `inventory_levels` to Fivetran `inventory_quantity`


- Table Match Confidence Score: ⚠️ _0.65_
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

### Mapping: Airbyte `fulfillments` to Fivetran `order_shipping_line`


- Table Match Confidence Score: 🟢 _0.70_
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


- Table Match Confidence Score: ⚠️ _0.65_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table mapping reflects a moderate confidence level due to missing mappings. Field-level mappings include both perfect and missing entries._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `orders._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `name` | Name of the attribute. | `orders.name` | 🟢 _0.70_ | *Mapping 'name' to 'orders.name' is plausible with moderate confidence.* |
| `order_id` | ID referencing the order the note attribute belongs to. | `orders.id` | 🟢 _0.70_ | *Mapping 'order_id' to 'orders.id' is plausible with moderate confidence.* |
| `value` | Value of the attribute. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `order_refunds` to Fivetran `order_shipping_tax_line`


- Table Match Confidence Score: ⚠️ _0.60_
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

### Mapping: Airbyte `product_variants` to Fivetran `product_variant`


- Table Match Confidence Score: 🟢 _0.80_
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

### Mapping: Airbyte `custom_collections` to Fivetran `collection`


- Table Match Confidence Score: 🟢 _0.80_
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

### Mapping: Airbyte `abandoned_checkouts` to Fivetran `abandoned_checkout_shipping_line`


- Table Match Confidence Score: ⚠️ _0.50_
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

### Mapping: Airbyte `orders` to Fivetran `order`


- Table Match Confidence Score: 🟢 _0.95_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table mapping is evaluated to have a high table match score due to the comprehensive outline of field mappings that are appropriately correlated with reasonable confidence to the target schema. However, there are fields with 'MISSING' expressions which moderately reduce the completion score as they indicate where the source schema lacks equivalent or meaningful matches._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `orders._airbyte_extracted_at` | 🟢 _1.00_ | *The '_fivetran_synced' is mapped to the source stream's '_airbyte_extracted_at' column, which is a standard mapping and always gets a score of 1.00.* |
| `app_id` | The ID of the app that created the order. | `orders.app_id` | 🟢 _0.70_ | *The 'app_id' field is mapped directly to 'orders.app_id', which is correct given the context provided.* |
| `customer_id` | The ID of the order's customer. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `confirmed` | Whether inventory has been reserved for the order. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `presentment_currency` | The presentment currency that was used to display prices to the customer. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `products` to Fivetran `product_tag`


- Table Match Confidence Score: 🟢 _1.00_
- Table Completion Score: ❌ _0.25_
- Summary Self-Evaluation: _The mapping configuration exhibits a perfect table match with successful standard field mapping for '_fivetran_synced', but lacks completion with most fields having 'MISSING' expressions._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `_fivetran_synced` | {{ doc('_fivetran_synced') }} | `products._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping of '_fivetran_synced' to '_airbyte_extracted_at'.* |
| `index` | Index (starting from 1) represnting when the tag was placed on the product. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `product_id` | ID of the product being tagged. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `value` | Value of the tag. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `orders` to Fivetran `order_line`


- Table Match Confidence Score: ⚠️ _0.50_
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

### Mapping: Airbyte `inventory_items` to Fivetran `inventory_item`


- Table Match Confidence Score: 🟢 _0.70_
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
