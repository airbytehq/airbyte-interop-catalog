# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `accounts` to Fivetran `account_history`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: ❌ _0.40_
- Summary Self-Evaluation: _The table match score indicates a reasonable level of confidence that the source and target tables are describing the same subject matter, but the low completion score is due to many fields set to 'MISSING' indicating incomplete field mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Uniquely identifies your customers in Recurly. No two customers can share the same account id. Part of the PK | `accounts.id` | 🟢 _1.00_ | *Direct mapping available.* |
| `updated_at` | When the account was last changed. | `accounts.updated_at` | 🟢 _1.00_ | *Direct mapping available.* |
| `account_city` | The city the account was registered in. | `accounts.address.city` | 🟢 _1.00_ | *Direct mapping available.* |
| `account_country` | The country the account was registered in. | `accounts.address.country` | 🟢 _1.00_ | *Direct mapping available.* |
| `account_first_name` | The first name for who registered the account. | `accounts.billing_info.first_name` | 🟢 _1.00_ | *Direct mapping available.* |
| `account_last_name` | The last name for who registered the account. | `accounts.billing_info.last_name` | 🟢 _1.00_ | *Direct mapping available.* |
| `account_phone` | The contact phone number registered on the account. | `accounts.billing_info.address.phone` | 🟢 _1.00_ | *Direct mapping available.* |
| `account_postal_code` | The contact postal code registered on the account. | `accounts.billing_info.address.postal_code` | 🟢 _1.00_ | *Direct mapping available.* |
| `account_region` | The region registered with the account, like state in the US or province in Canada. | `accounts.billing_info.address.region` | 🟢 _1.00_ | *Direct mapping available.* |
| `account_street_1` | The first street line registered with the account. | `accounts.billing_info.address.street1` | 🟢 _1.00_ | *Direct mapping available.* |
| `account_street_2` | The second street line registered with the account. | `accounts.billing_info.address.street2` | 🟢 _1.00_ | *Direct mapping available.* |
| `bill_to` | An enumerable describing the billing behavior of the account,  specifically whether the account is self-paying or will rely on the parent account to pay.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cc_emails` | Additional email address that should receive account correspondence.  These should be separated only by commas.  These CC emails will receive all emails that the email field also receives.           | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `code` | The unique identifier of the account. This cannot be changed once the account is created. Provided during account creation.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `company` | The company related with the account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | When the account was created. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `deleted_at` | If present, when the account was last marked inactive. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `email` | The email address used for communicating with this customer.  The customer will also use this email address to log into your hosted account management pages.  This value does not need to be unique.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `exemption_certificate` | Exemption certificate to prove that the business is tax exempt.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `first_name` | The first name of the customer related to the account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `hosted_login_token` | Custom URL on your site that logs the user directly into their account | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `last_name` | The last name of the customer related to the account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `preferred_locale` | The language code and country code for this account, like en-US. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `state` | Accounts can be either active or inactive. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_exempt` | The tax status of the account. true exempts tax on the account, false applies tax on the account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `username` | A secondary value for the account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `vat_number` | The VAT number of the account (to avoid having the VAT applied). This is only used for manually collected invoices. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `transactions` to Fivetran `transaction`


- Table Match Confidence Score: ⚠️ _0.50_
- Table Completion Score: ❌ _0.20_
- Summary Self-Evaluation: _Most field mappings are set to 'MISSING' indicating lack of good matches or unavailability of fields, reflecting a low confidence in proper field correspondence. The table matching score suggests only moderate confidence that the source and target tables describe the same subject matter._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier for the object. | `transactions.account.id` | 🟢 _1.00_ | *Proper mapping of unique identifier.* |
| `account_id` | The account_id this transaction belongs to. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `amount` | Total transaction amount sent to the payment gateway. | `transactions.amount` | 🟢 _1.00_ | *Proper mapping of transaction amount.* |
| `avs_check` | When processed, result from checking the overall AVS on the transaction. Enum: "N", "P", "D"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_city` | Billing info - City | `transactions.billing_address.city` | 🟢 _1.00_ | *Correct city mapping in billing address.* |
| `billing_country` | Billing info - Country, 2-letter ISO code. | `transactions.billing_address.country` | 🟢 _1.00_ | *Correct country mapping in billing address.* |
| `billing_first_name` | Billing info - First name | `transactions.billing_address.first_name` | 🟢 _1.00_ | *Correct first name mapping in billing address.* |
| `billing_last_name` | Billing info - Last name | `transactions.billing_address.last_name` | 🟢 _1.00_ | *Correct last name mapping in billing address.* |
| `billing_phone` | Billing info - Phone | `transactions.billing_address.phone` | 🟢 _1.00_ | *Correct phone mapping in billing address.* |
| `billing_postal_code` | Billing info - Zip or postal code. | `transactions.billing_address.postal_code` | 🟢 _1.00_ | *Correct postal code mapping in billing address.* |
| `billing_region` | Billing info - State or province. | `transactions.billing_address.region` | 🟢 _1.00_ | *Correct region mapping in billing address.* |
| `billing_street_1` | Billing info - Address Street 1 | `transactions.billing_address.street1` | 🟢 _1.00_ | *Correct street address mapping in billing address.* |
| `billing_street_2` | Billing info - Address Street 2 | `transactions.billing_address.street2` | 🟢 _1.00_ | *Correct street address mapping for additional line in billing address.* |
| `collected_at` | When the transaction was collected. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `collection_method` | The method by which the payment was collected. Enum: "automatic", "manual"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | When the transaction was created. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `currency` | 3-letter ISO 4217 currency code. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `customer_message` | For declined (success=false) transactions, the message displayed to the customer. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `customer_message_locale` | Language code for the message | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `cvv_check` | When processed, result from checking the CVV/CVC value on the transaction. Enum: "M", "N"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `gateway_approval_code` | Transaction approval code from the payment gateway. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `gateway_message` | Transaction message from the payment gateway. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `gateway_reference` | Transaction reference number from the payment gateway. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `gateway_response_code` | For declined transactions (`success=false`), this field lists the gateway error code. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `gateway_response_time` | Time, in seconds, for gateway to process the transaction. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `gateway_response_values` | The values in this field will vary from gateway to gateway. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `invoice_id` | The invoice_id this transaction belongs to. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `ip_address_country` | When provided, the country associated with the IP address of customer's location when processing transaction. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `ip_address_v_4` | When provided, the IP address when processing transaction. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `origin` | Describes how the transaction was triggered. Enum: "api", "chargeback", "force_collect", "hpp", "merchant", "recurly_admin", "recurlyjs", "recurring", "refunded_externally", "transparent"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `original_transaction_id` | If this transaction is a refund (type=refund), this will be the ID of the original transaction on the invoice being refunded. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `payment_gateway_id` | Payment gateway id | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `payment_gateway_name` | Payment gateway name | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `payment_gateway_type` | Payment gateway type | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `payment_method_card_type` | Card type of payment method. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `payment_method_exp_month` | Expiration month of payment method. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `payment_method_exp_year` | Expiration year of payment method. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `payment_method_first_six` | First six numbers of payment method. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `payment_method_last_four` | Last four digits of payment method. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `payment_method_object` | Enum: "amazon", "amazon_billing_agreement", "apple_pay", "bank_account_info", "check", "credit_card", "eft",  "gateway_token", "iban_bank_account", "money_order", "other", "paypal", "paypal_billing_agreement", "roku",  "sepadirectdebit", "wire_transfer"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `refunded` | Indicates if part or all of this transaction was refunded. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status` | The current transaction status. Note that the status may change, e.g. a pending transaction may become declined or success may later become void. Enum: "chargeback", "declined", "error", "pending", "processing", "scheduled", "success", "void"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status_code` | Status code of the transaction | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `status_message` | For declined (success=false) transactions, the message displayed to the merchant. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `success` | Did this transaction complete successfully? | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `type` | Transaction types:   authorization - verifies billing information and places a hold on money in the customer's account.   capture - captures funds held by an authorization and completes a purchase.   purchase - combines the authorization and capture in one transaction.   refund - returns all or a portion of the money collected in a previous transaction to the customer.   verify - a $0 or $1 transaction used to verify billing information which is immediately voided. Enum: "authorization", "capture", "purchase", "refund", "verify"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `uuid` | The UUID is useful for matching data with the CSV exports and building URLs into Recurly's UI. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `voided_at` | When the transaction was voided. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `voided_by_invoice_id` | The invoice_id this transaction was voided. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `line_items` to Fivetran `line_item_history`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table match has a strong score as the core identifiers and business logic seem consistent, but the completion score is somewhat low due to several missing mappings where the fields from the source implementation could not be mapped appropriately to the target schema._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier for the object. | `line_items.id` | 🟢 _1.00_ | *Direct mapping of identifiers* |
| `updated_at` | When the line item was updated. | `line_items.updated_at` | 🟢 _1.00_ | *Direct mapping of date properties* |
| `account_id` | The account this line item belongs to. | `line_items.account.id` | 🟢 _1.00_ | *Correct relational mapping* |
| `accounting_code` | Internal accounting code to help you reconcile your revenue to the correct ledger. | `line_items.accounting_code` | 🟢 _1.00_ | *Direct mapping of account-specific properties* |
| `add_on_code` | If the line item is a charge or credit for an add-on, this is its code. | `line_items.add_on_code` | 🟢 _0.80_ | *High confidence for matching category* |
| `add_on_id` | If the line item is a charge or credit for an add-on this is its ID. | `line_items.add_on_id` | 🟢 _0.80_ | *High confidence for matching category* |
| `amount` | Total after discounts and taxes (quantity * unit_amount) - (discount + tax). | `line_items.amount` | 🟢 _1.00_ | *Direct computation or property matching* |
| `created_at` | When the line item was created. | `line_items.created_at` | 🟢 _1.00_ | *Direct mapping of date properties* |
| `credit_applied` | The amount of credit from this line item that was applied to the invoice. | `line_items.credit_applied` | ❌ _0.00_ | *No good match found.* |
| `credit_reason_code` | The reason the credit was given. | `line_items.credit_reason_code` | ❌ _0.00_ | *No good match found.* |
| `currency` | 3-letter ISO 4217 currency code. | `line_items.currency` | 🟢 _1.00_ | *Standard currency code matching* |
| `description` | Description that appears on the invoice. For subscription related items this will be filled in automatically. | `line_items.description` | 🟢 _1.00_ | *Direct text property assignment* |
| `discount` | The discount applied to the line item. | `line_items.discount` | 🟢 _1.00_ | *Matching financial terms* |
| `end_date` | If this date is provided, it indicates the end of a time range. | `line_items.end_date` | 🟢 _1.00_ | *Correct temporal mapping* |
| `invoice_id` | Once the line item has been invoiced this will be the invoice's ID. | `line_items.invoice_id` | 🟢 _1.00_ | *Direct referential matching* |
| `invoice_number` | Once the line item has been invoiced this will be the invoice's number.  If VAT taxation and the Country Invoice Sequencing feature are enabled,  invoices will have country-specific invoice numbers for invoices billed to EU countries (e.g. FR1001).  Non-EU invoices will continue to use the site-level invoice number sequence.  | `line_items.invoice_number` | 🟢 _1.00_ | *Direct referential matching* |
| `legacy_category` | Category to describe the role of a line item on a legacy invoice. “charges” refers to charges being billed for on this invoice.  | `line_items.legacy_category` | ❌ _0.00_ | *No good match found.* |
| `origin` | A credit created from an original charge will have the value of the charge's origin. Enum: "add_on", "add_on_trial", "carryforward", "coupon", "credit", "debit", "one_time",  "plan", "plan_trial", "setup_fee", "prepayment"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `original_line_item_invoice_id` | The invoice where the credit originated.  Will only have a value if the line item is a credit created from a previous credit,  or if the credit was created from a charge refund.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `plan_code` | If the line item is a charge or credit for a plan or add-on, this is the plan's code. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `plan_id` | If the line item is a charge or credit for a plan or add-on, this is the plan's ID. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `previous_line_item_id` | Will only have a value if the line item is a credit created from a previous credit,  or if the credit was created from a charge refund.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `product_code` | For plan-related line items this will be the plan's code, for add-on related line items it will be the add-on's code.  For item-related line items it will be the item's external_sku.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `proration_rate` | When a line item has been prorated, this is the rate of the proration.  Proration rates were made available for line items created after March 30, 2017.  For line items created prior to that date, the proration rate will be null, even if the line item was prorated.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `quantity` | This number will be multiplied by the unit amount to compute the subtotal before any discounts or taxes. Default: 1  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `refund` | true if the line item is refund, false if it is not. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `refunded_quantity` | For refund charges, the quantity being refunded. For non-refund charges, the total quantity refunded (possibly over multiple refunds). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `start_date` | If an end date is present, this is value indicates the beginning of a billing time range.  If no end date is present it indicates billing for a specific date.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `state` | Pending line items are charges or credits on an account that have not been applied to an invoice yet.  Invoiced line items will always have an invoice_id value. Enum: "invoiced", "pending"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `subscription_id` | If the line item is a charge or credit for a subscription, this is its ID. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `subtotal` | Total before discounts and taxes (quantity * unit_amount). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax` | The tax amount for the line item. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_code` | Used by Avalara, Vertex, and Recurly’s EU VAT tax feature. The tax code values are specific to each tax system.  If you are using Recurly’s EU VAT feature you can use unknown, physical, or digital.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_exempt` | true exempts tax on charges, false applies tax on charges. If not defined, then defaults to the Plan and Site settings.  This attribute does not work for credits (negative line items). Credits are always applied post-tax.  Pre-tax discounts should use the Coupons feature.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_rate` | Tax rate | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_region` | Provides the tax region applied on an invoice.  For U.S. Sales Tax, this will be the 2 letter state code.  For EU VAT this will be the 2 letter country code.  For all country level tax types, this will display the regional tax, like VAT, GST, or PST.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_type` | Provides the tax type as "vat" for EU VAT, "usst" for U.S. Sales Tax, or the 2 letter country code for country level tax types  like Canada, Australia, New Zealand, Israel, and all non-EU European countries.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `taxable` | true if the line item is taxable, false if it is not. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `type` | Charges are positive line items that debit the account.  Credits are negative line items that credit the account. Enum: "charge", "credit"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `unit_amount` | Positive amount for a charge, negative amount for a credit. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `uuid` | The UUID is useful for matching data with the CSV exports and building URLs into Recurly's UI. Used in HTB database. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `invoices` to Fivetran `invoice_history`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _Since all provided fields have an expression set to 'MISSING', indicating no mappings have been successfully established, the confidence in both the table match and the completion of field mappings is zero._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier for the object. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `updated_at` | When the invoice was updated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `account_id` | The account this invoice belongs to. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `amount` | Total after discounts and taxes (quantity * unit_amount) - (discount + tax). | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `balance` | The outstanding balance remaining on this invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `closed_at` | Date invoice was marked paid or failed. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `collection_method` | An automatic invoice means a corresponding transaction is run using the account's billing information  at the same time the invoice is created. Manual invoices are created without a corresponding transaction.  The merchant must enter a manual payment transaction or have the customer pay the invoice with an automatic method,  like credit card, PayPal, Amazon, or ACH bank payment. Default: "automatic" Enum: "automatic", "manual"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | When the invoice was created. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `currency` | 3-letter ISO 4217 currency code. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `customer_notes` | Notes section available for any details account wants to add. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `discount` | Total discounts applied to this invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `due_at` | Date invoice is due. This is the date the net terms are reached. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `invoice_city` | City of the customer's address on the invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `invoice_country` | The 2 letter country code for the country of the customer's address on the invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `invoice_first_name` | First name from account associated with that invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `invoice_last_name` | Last name from account associated with that invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `invoice_name_on_account` |  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `invoice_phone` | Phone number associated with that invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `invoice_postal_code` | Postal code of the customer's address on the invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `invoice_region` | State or province of the customer's address on the invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `invoice_street_1` | Address line 1 of the customer's address on the invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `invoice_street_2` | Address line 2 of the customer's address on the invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `net_terms` | Integer representing the number of days after an invoice's creation that the invoice will become past due.  If an invoice's net terms are set to '0', it is due 'On Receipt' and will become past due 24 hours after it’s created.  If an invoice is due net 30, it will become past due at 31 days exactly. Default: 0  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `number` | If VAT taxation and the Country Invoice Sequencing feature are enabled,  invoices will have country-specific invoice numbers for invoices billed to EU countries (e.g. FR1001).  Non-EU invoices will continue to use the site-level invoice number sequence.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `origin` | The event that created the invoice. Enum: "credit", "gift_card", "immediate_change", "line_item_refund", "open_amount_refund",  "purchase", "renewal", "termination", "write_off", "prepayment".  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `paid` | The total amount of successful payments transaction on this invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `po_number` | For manual invoicing, this identifies the PO number associated with the subscription. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `previous_invoice_id` | On refund invoices, this value will exist and show the invoice ID of the purchase invoice the refund was created from. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `refundable_amount` | The refundable amount on a charge invoice. It will be null for all other invoices. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `state` | The invoice state.  Enum: "open", "pending", "processing", "past_due", "paid", "closed", "failed", "voided"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `subtotal` | The summation of charges, discounts, and credits, before tax. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax` | The total tax on this invoice. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_rate` | The rate of the tax. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_region` | Provides the tax region applied on an invoice. For U.S. Sales Tax,  this will be the 2 letter state code.  For EU VAT this will be the 2 letter country code.  For all country level tax types, this will display the regional tax, like VAT, GST, or PST.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `tax_type` | Provides the tax type as "vat" for EU VAT, "usst" for U.S. Sales Tax,  or the 2 letter country code for country level tax types like Canada, Australia, New Zealand, Israel, and all non-EU European countries.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `terms_and_conditions` | A notes section available to you for any details you would like to add. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total` | The final total on this invoice. The summation of invoice charges, discounts, credits, and tax. Alternative the summation of subtotal and tax.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `type` | Invoices are either "charge", "credit", or "legacy" invoices. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `vat_reverse_charge_notes` | Notes section if you are using Recurly's EU VAT feature for tax collection. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `subscriptions` to Fivetran `subscription_history`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table mapping demonstrates a high level of confidence due to clear connections between commonly named attributes such as 'id', 'created_at', and 'updated_at', which are reliable indicators of a subscription-related table. However, there are several key fields missing, impacting the overall completion score. The fields that have direct matches exhibit well-mapped relations, suggesting that the source and target schemas are describing similar subscription-related information but the completeness of the field mapping is not fully achieved._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier for the object. | `subscriptions.id` | 🟢 _1.00_ | *Direct match on the field name and context.* |
| `updated_at` | When the subscription was updated. | `subscriptions.updated_at` | 🟢 _1.00_ | *Direct match on the field name and context.* |
| `account_id` | The account this subscription belongs to. | `subscriptions.account.id` | 🟢 _0.90_ | *The expressions and descriptions suggest a close mapping, though not perfectly identical.* |
| `activated_at` | When the subscription was activated. | `subscriptions.activated_at` | 🟢 _1.00_ | *Direct match on the field name and context.* |
| `add_ons_total` | Total price of add-ons. Greater or equal to 0. | `subscriptions.add_ons_total` | 🟢 _0.95_ | *Exact name match and similar context related to subscriptions.* |
| `auto_renew` | Whether the subscription renews at the end of its term. Default: true  | `subscriptions.auto_renew` | 🟢 _1.00_ | *Field name and meaning are perfectly aligned.* |
| `bank_account_authorized_at` | Merchants importing recurring subscriptions paid with ACH into Recurly can  backdate the subscription's authorization with this attribute using an ISO 8601 timestamp.  This timestamp is used for alerting customers to reauthorize in 3 years in accordance  with NACHA rules. If a subscription becomes inactive or the billing info is no longer  a bank account, this timestamp is cleared.  | `subscriptions.bank_account_authorized_at` | 🟢 _0.70_ | *The field names are slightly different but closely related in purpose within the context of subscriptions.* |
| `canceled_at` | When the subscription was canceled. Can take future dates | `subscriptions.canceled_at` | 🟢 _1.00_ | *Direct match on the field name and context.* |
| `collection_method` | Default: "automatic" Enum: "automatic", "manual"  | `subscriptions.collection_method` | 🟢 _0.80_ | *Very closely related, detailed in the enumeration values.* |
| `created_at` | When the subscription was created. | `subscriptions.created_at` | 🟢 _1.00_ | *Direct match on the field name and context.* |
| `currency` | 3-letter ISO 4217 currency code. | `subscriptions.currency` | 🟢 _0.90_ | *Very closely related in context and matches the field name.* |
| `current_period_ends_at` | Date/time current billing period ends at. | `subscriptions.current_period_ends_at` | 🟢 _1.00_ | *Direct match on the field name and context.* |
| `current_period_started_at` | Date/time current billing period started at. | `subscriptions.current_period_started_at` | 🟢 _1.00_ | *Direct match on the field name and context.* |
| `current_term_ends_at` | When the term ends. This is calculated by a plan's interval and total_billing_cycles in a term.  Subscription changes with a timeframe=renewal will be applied on this date.  | `subscriptions.current_term_ends_at` | 🟢 _0.90_ | *Alignment with billing cycle context despite slight naming variation.* |
| `current_term_started_at` | The start date of the term when the first billing period starts.  The subscription term is the length of time that a customer will be committed to a subscription.  A term can span multiple billing periods.  | `subscriptions.current_term_started_at` | 🟢 _0.90_ | *Alignment with billing cycle context despite slight naming variation.* |
| `customer_notes` | This will default to the Customer Notes text specified on the Invoice Settings page. Custom notes will stay with a subscription on all renewals.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `expiration_reason` | Expiration reason | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `expires_at` | When the subscription has expired. Can take future dates. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `net_terms` | Identifies the agreement associated with the subscription. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `object` | The object type, in this case only "subscription" | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `paused_at` | Null unless subscription is paused or will pause at the end of the current billing period. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `plan_id` | The plan this subscription belongs to. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `po_number` | For manual invoicing, this identifies the PO number associated with the subscription. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `quantity` | Subscription quantity. Greater or equal to 0. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `remaining_billing_cycles` | The remaining billing cycles in the current term. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `remaining_pause_cycles` | Null unless subscription is paused or will pause at the end of the current billing period. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `renewal_billing_cycles` | If auto_renew=true, when a term completes, total_billing_cycles takes this value as the length of subsequent terms.  Defaults to the plan's total_billing_cycles.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `shipping_address_id` | Unique id assigned to shipping address. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `state` | The current state of the subscription. Enum: "active", "canceled", "expired", "failed", "future", "paused"  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `subtotal` | Estimated total, before tax. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `terms_and_conditions` | Optional notes field.  This will default to the Terms and Conditions text specified on the Invoice Settings page.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `total_billing_cycles` | The number of cycles/billing periods in a term.  When remaining_billing_cycles=0, if auto_renew=true the subscription will renew and a new term will begin,  otherwise the subscription will expire.  | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `trial_ends_at` | Trial period ends at | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `trial_started_at` | Trial period started at | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `unit_amount` | Subscription unit price | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `uuid` | The UUID is useful for matching data with the CSV exports and building URLs into Recurly's UI. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `billing_infos` to Fivetran `billing_info_history`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The mapping adheres well to the source and target schema conventions with high confidence in the relationships between similarly defined tables. Despite some fields being marked 'MISSING', it is overall a robust mapping alignment.Detailed high confidence is evident in key identity and transactional fields, however, missing fields due to no good match found lower the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier for the billing info object. | `billing_infos.id` | 🟢 _1.00_ | *Direct mapping to source field, identical meaning and structure.* |
| `account_id` | Account identifier for the billing info. | `billing_infos.account_id` | 🟢 _1.00_ | *High confidence due to identical functional context.* |
| `payment_method_card_type` | Card type of payment method, like Visa or Mastercard. | `billing_infos.payment_method.card_type` | 🟢 _1.00_ | *High confidence from exact match and context relevance.* |
| `billing_city` | Billing city of the card on file for the account. | `billing_infos.address.city` | 🟢 _0.95_ | *Closely related fields and clear alignment in purpose.* |
| `billing_country` | Billing country of the card on file for the account. | `billing_infos.address.country` | 🟢 _0.95_ | *Closely related fields and clear alignment in purpose.* |
| `billing_postal_code` | Billing postal code of the card on file for the account. | `billing_infos.address.postal_code` | 🟢 _0.95_ | *Closely related fields and clear alignment in purpose.* |
| `billing_region` | Billing region of the card on file for the account, like state in the US or province in Canada. | `billing_infos.address.region` | 🟢 _0.95_ | *Closely related fields and clear alignment in purpose.* |
| `billing_street_1` | First address line of the card on file for the account. | `billing_infos.address.street1` | 🟢 _0.95_ | *Closely related fields and clear alignment in purpose.* |
| `billing_street_2` | Second address line of the card on file for the account. | `billing_infos.address.street2` | 🟢 _0.95_ | *Closely related fields and clear alignment in purpose.* |
| `company` | Company name of the account. | `billing_infos.company` | 🟢 _1.00_ | *Direct mapping validated by the identical functional context.* |
| `created_at` | Date customer's billing information was added to the account. | `billing_infos.created_at` | 🟢 _1.00_ | *Prefix matches and serves identical temporal contextual purpose.* |
| `first_name` | First name of the cardholder for the account. | `billing_infos.first_name` | 🟢 _1.00_ | *Exact match and contextually relevant.* |
| `last_name` | Last name of the cardholder for the account. | `billing_infos.last_name` | 🟢 _1.00_ | *Exact match and contextually relevant.* |
| `updated_at` | Date customer's billing information was last updated on the account. | `billing_infos.updated_at` | 🟢 _1.00_ | *Direct match providing identical function.* |
| `updated_by_country` | Country from which latest billing info update came from. | `billing_infos.updated_by.country` | 🟢 _0.95_ | *Direct match of region-specific data, high relevance.* |
| `updated_by_ip` | IP address from which latest billing info update came from. | `billing_infos.updated_by.ip` | 🟢 _0.95_ | *Exact contextual match for update provenance.* |
| `valid` | Is the card valid? Boolean object. | `billing_infos.valid` | 🟢 _0.90_ | *Direct boolean attribute mapping, high relevance.* |
| `vat_number` | (for EU companies), VAT number provider by customer. | `billing_infos.vat_number` | 🟢 _0.90_ | *Direct mapping of regulatory attribute, high confidence.* |
| `billing_phone` | Phone number of the account. | `billing_infos.address.phone` | 🟢 _0.90_ | *Direct match, strong relevance to billing information context.* |
| `payment_method_exp_month` | Month the payment method is expected to expire. | `billing_infos.payment_method.exp_month` | 🟢 _1.00_ | *Perfect alignment with expiry context in the payment schema.* |
| `payment_method_exp_year` | Year the payment method is expected to expire. | `billing_infos.payment_method.exp_year` | 🟢 _1.00_ | *Perfect alignment with expiry context in the payment schema.* |
| `payment_method_first_six` | First six numbers of the credit card used to process the transaction. | `billing_infos.payment_method.first_six` | 🟢 _0.95_ | *Direct match for payment card details, high functional similarity.* |
| `payment_method_last_four` | Last four digits of the credit card number stored on customer's account. | `billing_infos.payment_method.last_four` | 🟢 _0.95_ | *Direct match for payment card details, high functional similarity.* |
| `payment_method_object` | Object type of payment method, like credit card or debit card. | `billing_infos.payment_method.object` | 🟢 _0.90_ | *Direct match, high relevance in payment type classification.* |
| `billing_first_name` | First name at billing address on account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `billing_last_name` | Last name at billing address on account. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `fraud_decision` | Decision made on whether billing info triggers a fraud alert. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `fraud_risk_rules_triggered` | The rules that are triggered for fraud if an alert is raised. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `fraud_score` | Fraud score on card based on risk inquiries. | `MISSING` | ❌ _0.00_ | *No good match found.* |
