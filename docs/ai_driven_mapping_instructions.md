# AI-Driven Mapping Instructions for Morph

## Introduction and Purpose

This guide provides instructions for creating and maintaining mappings between Airbyte source connectors and Fivetran-compatible target schemas in the Morph repository. The purpose of these mappings is to enable data engineers to extract data using Airbyte connectors while maintaining compatibility with Fivetran transformation models.

The guide is designed to be used by AI agents or developers who need to create or update mappings for new or existing connectors. It captures the process, best practices, and lessons learned from mapping the Facebook Marketing connector.

## Mapping Process Overview

The mapping process involves the following high-level steps:

1. **Identify Source and Target Schemas**: Locate the source schema (Airbyte connector) and target schema (Fivetran-compatible) YAML files.
2. **Create Mapping Reference Chart**: Document the relationships between source streams and target tables.
3. **Update Transform Files**: Modify the "from" clauses in transform files to correctly map source streams to target tables.
4. **Update Field Expressions**: Map source fields to target fields, ensuring data types and semantics match.
5. **Verify Mappings**: Ensure all mappings are complete and accurate.

## Source and Target Schema Analysis

### Locating Schema Files

For a connector named `{connector_name}`, the key schema files are:

- **Source Schema**: `catalog/{connector_name}/generated/dbt_project/models/sources.yml`
- **Target Schema**: `catalog/{connector_name}/requirements/fivetran-interop/src_{target_name}.yml`

For example, for the Facebook Marketing connector:
- Source: `catalog/facebook_marketing/generated/dbt_project/models/sources.yml`
- Target: `catalog/facebook_marketing/requirements/fivetran-interop/src_facebook_ads.yml`

### Analyzing Schema Structures

1. **Source Schema Structure**:
   - Contains tables under `sources` > `tables`
   - Each table has columns with name, type, and description
   - Represents the raw data extracted by Airbyte

2. **Target Schema Structure**:
   - Contains tables under `sources` > `tables`
   - Each table has columns with name and description
   - Represents the Fivetran-compatible schema

3. **Key Differences**:
   - Naming conventions may differ (e.g., `ads` vs `ad_history`)
   - Field structures may vary (e.g., nested vs flattened)
   - Some fields may exist in one schema but not the other

## Mapping Creation Steps and Best Practices

### Step 1: Identify Source-to-Target Table Mappings

1. Review the `config.yml` file to identify source streams and target tables:
   ```yaml
   source_streams:
     - activities
     - ad_account
     - ad_creatives
     # ...
   
   target_tables:
     - account_history
     - ad_history
     - ad_set_history
     # ...
   ```

2. Match source streams to target tables based on:
   - Similar naming patterns (e.g., `ad_account` → `account_history`)
   - Similar field structures
   - Similar descriptions and purposes

3. Document these mappings in a reference chart for clarity.

### Step 2: Update Transform Files

1. Locate transform files in `catalog/{connector_name}/src/fivetran-interop/transforms/`.

2. Update the "from" clause in each transform file to map to the correct source stream:
   ```yaml
   from:
     - account: facebook_marketing.ad_account
   ```

3. Use a consistent alias pattern for source tables (e.g., singular form of the entity).

### Step 3: Map Standard Fields

1. Map standard Fivetran fields to Airbyte equivalents:
   - `_fivetran_synced` → `_airbyte_extracted_at`
   - `_fivetran_deleted` → Source deletion indicator (e.g., `archived`)

2. Example:
   ```yaml
   _fivetran_synced:
     expression: _airbyte_extracted_at
     description: '{{ doc(''_fivetran_synced'') }}'
   ```

### Step 4: Map Entity-Specific Fields

1. Map ID fields directly:
   ```yaml
   id:
     expression: account.id
     description: "The ID of the ad account."
   ```

2. Map name fields directly:
   ```yaml
   name:
     expression: account.name
     description: "Name of the account."
   ```

3. For fields that don't have a direct mapping, use `MISSING` and document in annotations:
   ```yaml
   some_field:
     expression: MISSING
     description: "Description of the field."
   ```

## Verification and Testing Recommendations

1. **Completeness Check**:
   - Ensure all transform files have updated "from" clauses
   - Ensure all `_fivetran_synced` fields are mapped to `_airbyte_extracted_at`
   - Ensure all required fields have expressions (not `MISSING`)

2. **Consistency Check**:
   - Ensure consistent naming patterns for source aliases
   - Ensure consistent field mapping patterns across files

3. **Testing**:
   - Generate the dbt project using the updated mappings
   - Verify that the generated SQL correctly references the source tables
   - Run tests to ensure the mappings produce valid transformations

## Examples from the Facebook Marketing Mapping Project

### Example 1: Account History Mapping

```yaml
domain: facebook_marketing.fivetran-interop
transforms:
- display_name: Each record in this table reflects a version of a Facebook ad account.
  id: account_history
  from:
  - account: facebook_marketing.ad_account
  fields:
    id:
      expression: account.id
      description: The ID of the ad account.
    name:
      expression: account.name
      description: Name of the account.
    _fivetran_synced:
      expression: _airbyte_extracted_at
      description: '{{ doc(''_fivetran_synced'') }}'
    # Additional fields...
```

### Example 2: Basic Ad Mapping

```yaml
domain: facebook_marketing.fivetran-interop
transforms:
- display_name: Each record represents the daily performance of an ad in Facebook.
  id: basic_ad
  from:
  - insights: facebook_marketing.ads_insights
  fields:
    ad_id:
      expression: insights.ad_id
      description: The ID of the ad the report relates to.
    # Additional fields...
    _fivetran_synced:
      expression: _airbyte_extracted_at
      description: '{{ doc(''_fivetran_synced'') }}'
```

## Common Challenges and Solutions

### Challenge 1: Missing Source Fields

**Problem**: The target schema requires fields that don't exist in the source schema.

**Solution**:
- Mark these fields with `expression: MISSING`
- Document them in the `annotations` section
- Consider adding custom transformations if the data can be derived

### Challenge 2: Different Naming Conventions

**Problem**: Source and target schemas use different naming conventions.

**Solution**:
- Create consistent mapping patterns (e.g., `properties_firstname` → `property_firstname`)
- Document these patterns in the mapping reference chart
- Use explicit mappings rather than assuming patterns

### Challenge 3: Complex Transformations

**Problem**: Some fields require complex transformations beyond simple mapping.

**Solution**:
- Use SQL expressions in the mapping when needed
- Break down complex transformations into multiple steps
- Document the transformation logic

## Conclusion

Creating accurate and complete mappings between Airbyte sources and Fivetran-compatible targets is essential for the Morph tool to generate correct dbt transformations. By following this guide, AI agents and developers can create consistent, maintainable mappings that enable seamless data transformation workflows.

Remember to document your mapping process, patterns, and decisions to help future maintainers understand and extend your work.
