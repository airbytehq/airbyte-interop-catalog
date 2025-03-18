# Morph Usage Guide

This document provides instructions on how to use the Morph tool to generate and transform data schemas.

## Generating dbt Projects from Mapping Files

Morph can generate dbt projects from mapping files that define transformations between source and target schemas.

### Example: Building HubSpot dbt Project Artifacts

The following steps demonstrate how to generate a dbt project for HubSpot data:

1. **Generate the dbt project**

   Use the `generate-dbt-project` command to create a dbt project from the HubSpot mapping files and catalog:

   ```bash
   python -m morph.cli.main generate-dbt-project \
     catalog/hubspot \
     catalog/hubspot/airbyte-source/catalog.json \
     --output-dir catalog/hubspot/generated \
     --mapping-dir catalog/hubspot/transforms/fivetran-compat \
     --source-name hubspot
   ```

   This command:
   - Takes the HubSpot catalog directory as the first argument
   - Takes the Airbyte catalog.json file as the second argument
   - Specifies the output directory for the generated dbt project
   - Points to the directory containing the mapping files
   - Sets the source name for the dbt project

3. **Test the generated dbt project**

   Install dbt and test the project:

   ```bash
   # Install dbt
   pip install dbt-core dbt-duckdb

   # Navigate to the generated project
   cd catalog/hubspot/generated/dbt_project

   # Install dependencies
   dbt deps --profiles-dir profiles

   # Compile the project
   dbt compile --profiles-dir profiles
   ```

## JSON Schema to dbt Sources

Morph can also convert JSON schema files to dbt source definitions:

```bash
python -m morph.cli.main json-to-dbt \
  --catalog \
  --source-name hubspot \
  --output catalog/hubspot/generated/src_airbyte_hubspot.yml \
  catalog/hubspot/airbyte-source/catalog.json
```

This command:
- Converts an Airbyte catalog file to dbt sources
- Names the source "hubspot"
- Outputs the result to the specified file

## Additional Resources

For more information on the available commands and options, use the `--help` flag:

```bash
python -m morph.cli.main --help
python -m morph.cli.main generate-dbt-project --help
python -m morph.cli.main json-to-dbt --help
```
