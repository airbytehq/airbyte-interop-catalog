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


### Mapping: Airbyte `account_coupon_redemptions` to Fivetran `coupon_redemption_history`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _The table mapping demonstrates a high correlation between source and target schema, indicative of a good level of understanding and stringent application of mapping criteria. The majority of fields are accurately mapped, though some non-critical fields lack mapping which slightly reduces the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier for the coupon redemption created. | `account_coupon_redemptions.id` | 🟢 _1.00_ | *Direct mapping of unique identifiers provided optimal confidence.* |
| `account_id` | Account associated with the coupon being redeemed. | `account_coupon_redemptions.account.id` | 🟢 _0.95_ | *Correct mapping to 'account.id'; minor discrepancy in path hints minimal risk of misinterpretation.* |
| `coupon_id` | Coupon being redeemed. | `account_coupon_redemptions.coupon.id` | 🟢 _0.95_ | *Proper alignment with 'coupon.id', showing compatibility of ID fields across schemas.* |
| `created_at` | Time coupon was being redeemed. | `account_coupon_redemptions.created_at` | 🟢 _1.00_ | *Exact match based on field use and naming, representing creation timestamp.* |
| `currency` | 3-letter ISO 4217 currency code (USD for US Dollar). | `account_coupon_redemptions.currency` | 🟢 _0.70_ | *Identical currency code usage ensures a high confidence match despite potential variations in field labeling across regions.* |
| `discounted` | Amount discounted from coupon redemption. | `account_coupon_redemptions.discounted` | 🟢 _0.95_ | *Close semantics between the sources, represented accurately.* |
| `removed_at` | If a coupon is removed from a customer, time of removal. | `account_coupon_redemptions.removed_at` | 🟢 _0.80_ | *Slightly ambiguous mapping due to commonality of timestamp fields, yet highly relevant within context.* |
| `state` | Current state of coupon redemption (usually active or inactive) | `account_coupon_redemptions.state` | 🟢 _0.75_ | *Mapped suitably, though the generic nature of state descriptors necessitates slight caution.* |
| `updated_at` | Time coupon redemption last updated. | `account_coupon_redemptions.updated_at` | 🟢 _1.00_ | *Timestamp fields precisely mapped ensuring continuous timeline integrity across systems.* |

### Mapping: Airbyte `plans` to Fivetran `plan_history`


- Table Match Confidence Score: 🟢 _0.95_
- Table Completion Score: 🟢 _0.85_
- Summary Self-Evaluation: _All the field mappings provided align well with the target schema, showing a good understanding of the fields' purposes and matching them accurately to the target fields. The source and target tables are based on similar or shared APIs, ensuring a high degree of similarity in the data context. However, there are minor discrepancies in complete field coverage, reducing the completion score slightly._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier for the object. | `plans.id` | 🟢 _1.00_ | *Direct mapping exists.* |
| `updated_at` | When the plan was updated. | `plans.updated_at` | 🟢 _1.00_ | *Direct mapping exists.* |
| `accounting_code` | Accounting code for invoice line items for the plan. If no value is provided, it defaults to plan's code. | `plans.accounting_code` | 🟢 _0.95_ | *Direct mapping with minor differences in defaults.* |
| `auto_renew` | Subscriptions will automatically inherit this value once they are active.  If auto_renew is true, then a subscription will automatically renew its term at renewal.  If auto_renew is false, then a subscription will expire at the end of its term.  auto_renew can be overridden on the subscription record itself. Default: true  | `plans.auto_renew` | 🟢 _0.90_ | *Direct mapping though boolean interpretation needs checking in context.* |
| `code` | Unique code to identify the plan. This is used in Hosted Payment Page URLs and in the invoice exports. | `plans.code` | 🟢 _0.95_ | *Direct mapping with unique identifiers.* |
| `created_at` | When the plan was created. | `plans.created_at` | 🟢 _1.00_ | *Direct mapping exists.* |
| `deleted_at` | When the plan was deleted. | `plans.deleted_at` | 🟢 _0.80_ | *Mapping valid but less common field.* |
| `description` | Optional description, not displayed. | `plans.description` | 🟢 _0.80_ | *Optional field with mapping available.* |
| `hosted_pages_bypass_confirmation` | Returns true if you use Recurly's Hosted Payment Pages and use custom return URL. | `plans.hosted_pages.bypass_confirmation` | 🟢 _0.90_ | *Map nested fields accurately but verify integration.* |
| `hosted_pages_cancel_url` | If customer cancels subscription via Hosted Page, Recurly redirects customer to specific URL. | `plans.hosted_pages.cancel_url` | 🟢 _0.90_ | *Valid mapping, contextual integration needed.* |
| `hosted_pages_display_quantity` | Number of hosted pages under plan. | `plans.hosted_pages.display_quantity` | 🟢 _0.85_ | *Mapping accurate, ensure counting consistency.* |
| `hosted_pages_success_url` | If customer successfully subscribes via Hosted Page, Recurly redirects customer to specific URL | `plans.hosted_pages.success_url` | 🟢 _0.95_ | *Matching URL follows expected pattern for successful actions.* |
| `interval_length` | Length of the plan's billing interval in interval_unit. Default: 1  | `plans.interval_length` | 🟢 _0.95_ | *Direct match with defaults aligned.* |
| `interval_unit` | Unit for the plan's billing interval. Default: "months" Enum: "days", "months"  | `plans.interval_unit` | 🟢 _0.95_ | *Direct match, units are consistent.* |
| `name` | This name describes your plan and will appear on the Hosted Payment Page and the subscriber's invoice. | `plans.name` | 🟢 _1.00_ | *Exact match crucial for identification and links.* |
| `setup_fee_accounting_code` | Accounting code for invoice line items for the plan's setup fee. If no value is provided, it defaults to plan's accounting code. | `plans.setup_fee_accounting_code` | 🟢 _0.85_ | *Mapping reflects default pattern but check source values.* |
| `state` | The current state of the plan. Enum: "active", "inactive"  | `plans.state` | 🟢 _0.95_ | *State fields match with high confidence, enum values consistent.* |
| `tax_code` | Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system.  If you are using Recurly’s EU VAT feature you can use unknown, physical, or digital.  | `plans.tax_code` | ⚠️ _0.60_ | *Mapping could be correct, depends on the tax system integrations.* |
| `tax_exempt` | true exempts tax on the plan, false applies tax on the plan. | `plans.tax_exempt` | 🟢 _0.90_ | *Direct boolean match, but ensure policy consistency between systems.* |
| `total_billing_cycles` | Automatically terminate subscriptions after a defined number of billing cycles.  Number of billing cycles before the plan automatically stops renewing, defaults to null for continuous, automatic renewal.  | `plans.total_billing_cycles` | 🟢 _0.80_ | *Field aligns well, check if implemented consistently across business logic.* |
| `trial_length` | Length of plan's trial period in trial_units. 0 means no trial. Default: 0  | `plans.trial_length` | 🟢 _1.00_ | *Direct match with default values aligned.* |
| `trial_unit` | Units for the plan's trial period. Default: "months" Enum: "days", "months"  | `plans.trial_unit` | 🟢 _1.00_ | *Direct match, units consist with target schema.* |

### Mapping: Airbyte `credit_payments` to Fivetran `credit_payment_history`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table match score is relatively high as the source and target tables are likely describing related financial transactions related to credit payments, though not all fields are populated, hence the lower completion score. The field mappings are well-matched, accounting for differences in field naming conventions and hierarchy._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier for the credit payment. | `credit_payments.id` | 🟢 _0.95_ | *Direct match found.* |
| `account_id` | The id of the account the credit payment is associated with. | `credit_payments.account.id` | 🟢 _0.90_ | *Direct match considering the same source and target IDs.* |
| `action` | The action that resulted in the credit payment being created. Enum: "payment", "gift_card", "write_off", "reduction", "refund"   | `credit_payments.action` | 🟢 _0.85_ | *Direct match with correct enumeration handling.* |
| `amount` | The amount of the credit payment, which will always be positive. | `credit_payments.amount` | 🟢 _0.95_ | *Direct match for the field representing a numeric value.* |
| `applied_to_invoice_id` | The invoice the credit payment was applied to.  If action is payment, gift_card, or write_off, this is a charge invoice.  If action is reduction or refund, this is a credit invoice.  | `credit_payments.applied_to_invoice.id` | 🟢 _0.90_ | *Direct match for ID field, appropriate consideration given to different types of invoices.* |
| `created_at` | The date and time the credit payment was created. | `credit_payments.created_at` | 🟢 _0.95_ | *Direct match for date/time field.* |
| `currency` | 3-letter ISO 4217 currency code (USD for US Dollar). | `credit_payments.currency` | 🟢 _0.95_ | *Direct match for ISO currency code.* |
| `original_credit_payment_id` | The unique id of the credit payment the refund action credit payment is refunding.  Will only populate if the action on the row is "refund".  | `credit_payments.original_credit_payment_id` | 🟢 _0.85_ | *Direct match but conditionally populated based on action type.* |
| `original_invoice_id` | The invoice of the credit invoice the credit payment came from. | `credit_payments.original_invoice.id` | 🟢 _0.85_ | *Good match, slightly nuanced based on invoice types.* |
| `refund_transaction_id` | The unique id of the new refund transaction the refund action credit payment is transferring value to.  Will only populate if the action on the row is "refund".  | `credit_payments.refund_transaction.id` | 🟢 _0.75_ | *Conditional field based on specific action, reasonably matched.* |
| `updated_at` | Time credit payment last updated. | `credit_payments.updated_at` | 🟢 _0.95_ | *Direct match for timestamp update.* |
| `uuid` | Unique id of credit payment. | `credit_payments.uuid` | 🟢 _0.95_ | *Direct match for universal identifier.* |
| `voided_at` | Time when a credit payment is voided. | `credit_payments.voided_at` | 🟢 _0.90_ | *Direct match, considering the specific context of voiding dates.* |

### Mapping: Airbyte `transactions` to Fivetran `transaction_subscription`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _Both mappings point towards a transaction-related context, implying a reasonably high likelihood that they refer to the same data context. Although the expressions involve IDs linked with transactions and subscriptions, which are usually tightly connected, the specific distinction ensures a less than perfect score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `transaction_id` | The id of the transaction associated with the subscription. | `transactions.id` | 🟢 _0.90_ | *The expression 'transactions.id' indicates a direct and meaningful mapping for 'transaction_id'.* |
| `subscription_id` | The id of the subscription associated with the transaction. | `transactions.subscription_ids` | ⚠️ _0.60_ | *While 'transactions.subscription_ids' signifies a potential match for 'subscription_id', the pluralization in 'subscription_ids' might suggest an array or multiple entries, presenting some uncertainty.* |

### Mapping: Airbyte `account_notes` to Fivetran `account_note_history`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.86_
- Summary Self-Evaluation: _The mappings are mostly accurate, but some fields such as 'account_updated_at' reflect missing data, reducing the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Uniquely identifies the account note created. | `account_notes.id` | 🟢 _1.00_ | *Perfect direct mapping.* |
| `account_id` | Account associated with the note created. | `account_notes.account_id` | 🟢 _1.00_ | *Perfect direct mapping.* |
| `account_updated_at` | Last time the account note was updated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | Date/time When the note was created. | `account_notes.created_at` | 🟢 _1.00_ | *Perfect direct mapping.* |
| `message` | Contents of the note created. | `account_notes.message` | 🟢 _1.00_ | *Perfect direct mapping.* |
| `object` | Object type of account note. | `account_notes.object` | 🟢 _1.00_ | *Perfect direct mapping.* |
| `user_id` | Id associated with who created the note. | `account_notes.user.id` | 🟢 _0.90_ | *Good match with some contextual evidence.* |
| `user_email` | Email associated with who created the note. | `account_notes.user.email` | 🟢 _0.90_ | *Good match with some contextual evidence.* |

### Mapping: Airbyte `coupons` to Fivetran `coupon_discount`


- Table Match Confidence Score: 🟢 _0.82_
- Table Completion Score: 🟢 _0.93_
- Summary Self-Evaluation: _The table matching for coupon discounts appears to be highly accurate with both source and target covering similar aspects of discount details, though lacking some fields in either implementation. Hence a slightly lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `coupon_id` | Unique identifier for the coupon created. | `coupons.id` | 🟢 _1.00_ | *Exact match for identifiers in both schemas, ensuring a unique reference.* |
| `fivetran_id` | Combined unique surrogate key for the model. | `coupons.id` | 🟢 _0.95_ | *Almost exact match, minor discrepancies may be due to naming conventions.* |
| `amount` | Fixed amount discount being applied, if applicable. Percentage would be null if amount exists. | `coupons.discount` | 🟢 _0.90_ | *Close match with slight possibility due to different formatting or data presentation in source vs. target.* |
| `currency` | 3-letter ISO 4217 currency code (USD for US Dollar). | `coupons.discount.currencies` | 🟢 _0.90_ | *Correct identification of currency, with minor uncertainty in structural representation between source and target.* |
| `percentage` | Percentage discount being applied, if applicable. Amount would be null if percentage exists. | `coupons.discount.percent` | 🟢 _0.90_ | *Direct match for data type and purpose, but small variances in implementation or detail might exist.* |
| `trial_length` | Period of time that coupon will discount eligible purchases by customer. | `coupons.discount.trial.length` | 🟢 _0.87_ | *Overall good match, but could vary slightly in terms of exact value or unit interpretation in different contexts.* |
| `trial_unit` | Unit of time associated with trial time ('day', 'week', 'month') | `coupons.discount.trial.unit` | 🟢 _0.87_ | *Correct category match, some differences may arise on how units are possibly categorized or abbreviated.* |
| `type` | Delineates between which type of discount is being applied ('fixed' for amount discount, 'percent' for percentage discount) | `coupons.discount.type` | 🟢 _0.85_ | *Correct type matching although there might be minor distinctions in how types are defined or utilized across schemas.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
