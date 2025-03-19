# HubSpot Streams Research and Recommendations

This document outlines the research and recommendations for implementing HubSpot streams in the Morph project.

## Overview

The goal was to identify the most popular and widely used HubSpot streams that would be valuable to implement in the Morph project, focusing on basic streams, company, and ticket handling. The research involved analyzing the HubSpot connector source code to understand available streams and their properties.

## Research Process

1. **Source Code Analysis**: Examined the HubSpot connector source code in the Airbyte repository to identify all available streams.
   - Location: `/airbyte-integrations/connectors/source-hubspot/source_hubspot/streams.py`
   - Identified over 50 stream classes representing different HubSpot entities

2. **Stream Classification**: Categorized streams based on their functionality and business domain:
   - Core CRM entities (Contacts, Companies, Deals, Tickets)
   - Marketing-related streams (Forms, Campaigns, Email Events)
   - Sales-related streams (Engagements, Line Items, Products)
   - Automation streams (Workflows)
   - User management streams (Owners)

3. **Selection Criteria**: Prioritized streams based on:
   - Simplicity of implementation
   - Widespread usage across HubSpot customers
   - Business value for analytics
   - Avoiding high-volume streams that could cause performance issues

## Recommendations

Based on the research and user requirements (excluding company and ticket which are already implemented), the following streams were recommended:

1. **Contacts** - Core CRM entity that stores all contact information including email, name, phone, and custom properties.

2. **Deals** - Tracks sales opportunities with stages, amounts, and close dates. Critical for sales pipeline analysis and revenue forecasting.

3. **Owners** - HubSpot users who can be assigned to contacts, companies, deals, and tickets. Important for attribution and ownership analysis.

4. **Forms** - Marketing forms used to capture lead information. Essential for marketing analytics and lead generation tracking.

5. **Products** - Product catalog items that can be associated with deals. Important for e-commerce and product-based businesses.

6. **Workflows** - Automation sequences that trigger based on contact actions or properties. Important for marketing automation analysis.

## Implementation Considerations

When implementing these streams in Morph, consider:

1. **Incremental Sync Support**: Most recommended streams support incremental sync, which should be leveraged for efficiency.

2. **Associations**: Many streams have associations with other entities (e.g., Deals with Contacts and Companies) that should be preserved.

3. **Schema Complexity**: Some streams have complex schemas with nested objects that will require careful mapping.

4. **API Limitations**: Be aware of HubSpot API rate limits and pagination requirements.

## Implementation

The implementation of the recommended HubSpot streams in the Morph project followed a four-step process:

1. **Added Canonical Stream Names**: Updated `scripts/create_hubspot_data.py` to include the canonical stream names for the six recommended streams (Contacts, Deals, Owners, Forms, Products, Workflows).
   - Created a `HUBSPOT_STREAMS` list to centralize stream definitions
   - Modified the `sync_source()` function to accept optional stream parameters
   - Updated the `main()` function to use the canonical stream list

2. **Created Schema Mappings**: Developed mapping files in `catalog/hubspot/src/transforms/fivetran-interop/` for each stream following the pattern established for existing streams.
   - Created mapping files: `contact.yml`, `deal.yml`, `owner.yml`, `form.yml`, `product.yml`, `workflow.yml`
   - Mapped Airbyte source fields to Fivetran target schema fields
   - Used `MISSING` expression for fields not available in the source schema
   - Documented field descriptions and annotations for unused source fields

3. **Updated Unit Tests**: Extended the parametrized pytest unit test to include the new streams.
   - Added new streams to the test parameters in `tests/test_hubspot_mappings.py`
   - Verified mapping completeness against target schema requirements
   - Iteratively fixed mapping files to include all required target fields

4. **Regenerated DBT Project**: Used the Morph CLI to regenerate the dbt project with the new stream mappings.
   - Generated SQL models for each stream: `contact.sql`, `deal.sql`, `owner.sql`, `form.sql`, `product.sql`, `workflow.sql`
   - Updated `sources.yml` to include the new streams
   - Verified the generated models follow the expected patterns

### Implementation Challenges

Several challenges were encountered during the implementation:

1. **Schema Mapping Completeness**: The target schema required fields that weren't immediately obvious from the source schema. Multiple iterations were needed to identify and add all required fields.

2. **Field Expression Mapping**: For some fields, determining the appropriate expression was challenging due to differences in naming conventions between Airbyte and Fivetran.

3. **Missing Fields**: Some target schema fields had no direct equivalent in the source schema, requiring the use of `MISSING` expressions as placeholders.

## Next Steps

1. Test the implementation with real HubSpot data
2. Optimize the mappings based on performance metrics
3. Document the implementation for users
4. Consider adding more HubSpot streams in the future

## References

- [HubSpot API Documentation](https://developers.hubspot.com/docs/api/overview)
- Airbyte HubSpot Connector: `/airbyte-integrations/connectors/source-hubspot/`
