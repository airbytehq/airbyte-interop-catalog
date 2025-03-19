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

## Next Steps

1. Implement the recommended streams in the Morph project
2. Create appropriate schema mappings for each stream
3. Set up end-to-end integration tests
4. Document the implementation for users

## References

- [HubSpot API Documentation](https://developers.hubspot.com/docs/api/overview)
- Airbyte HubSpot Connector: `/airbyte-integrations/connectors/source-hubspot/`
