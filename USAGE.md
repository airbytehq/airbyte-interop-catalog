# Morph Usage Guide

> ⚠️ _**Warning:** These docs are under development and are subject to frequent change._

This document provides instructions on how to use the Morph tool to generate and transform data schemas.

## Understanding Repo Structure

Below should help you navigate the repo.

- `.data` - A git-ignored directory where data assets and artifacts may be stored.
- `catalog` - This is source-specific assets and business logic. See the [Catalog Readme](catalog/README.md) for information on the `catalog` directory assets.
- `morph` - This is the app code that maintains our transformations.
- `scripts` - Specific helper scripts for certain functions.
- `templates` - A set of `copier` templates for generating projects.
- `tests` - Test code for `morph` and `catalogs`.

## Adding a new connector to the catalog

To add a new connector to the catalog, follow these steps:

1. Identify the canonical Airbyte source name for the connector. (E.g. `airbyte-source-facebook-marketing`).
2. Identify the canonical Fivetran source name for the connector. (E.g. `facebook_ads`).
3. Locate the Fivetran "Source" dbt package for the connector. (E.g. `https://github.com/fivetran/dbt_facebook_ads_source`).
4. Create a new directory `catalog/{new_connector}`, matching the canonical source name, excluding the "source-" prefix, and replacing hyphens with underscores. For example, "source-shopify" would be `catalog/shopify` and "source-facebook-marketing" would be `catalog/facebook_marketing`.
5. Create a new file `catalog/{new_connector}/src/fivetran-interop/config.yml` file which populates the info above into the following example:

   ```yaml
   project_id: {new_connector}.fivetran-interop
   source_name: {new_connector}
   source_streams: []  # Will be added later

   # Target schema file snapshotted from: https://github.com/fivetran/dbt_{fivetran_source_name}_source/blob/main/models/src_{fivetran_source_name}.yml
   target_dbt_schema: https://raw.githubusercontent.com/fivetran/dbt_{fivetran_source_name}_source/refs/heads/main/models/src_{fivetran_source_name}.yml
   target_tables: []  # Will be added later
   ```

6. Generate the project scaffold using the morph CLI:
   - This will generate the Airbyte catalog, mapping files, and dbt project.
   - Optionally, you can skip certain steps by using the `--no-airbyte-catalog`, `--no-transforms`, or `--no-dbt-project` flags. (See `morph generate-project --help` for more information.)

   ```bash
   uv run morph generate-project {new_connector}
   ```

7. Optionally, generate Airbyte data for the source.
   - This requires that you've selected one or more streams in the `config.yml` file.

   ```bash
   uv run morph create-airbyte-data {new_connector}
   ```

## Generating dbt Projects from Mapping Files

Morph can generate dbt projects from mapping files that define transformations between source and target schemas.

### Example: Building HubSpot dbt Project Artifacts

The following steps demonstrate how to generate a dbt project for HubSpot data:

To add a new connector to the catalog:

1. Create a directory structure following the pattern above:

   ```txt
   catalog/new_connector/
   ├── src/transforms/
   │   └── fivetran-interop/
   ├── requirements/
   │   └── fivetran-interop/
   └── examples/
   ```

2. Add the target schema definition in `requirements/fivetran-interop/src_new_connector.yml`. You can download this from the Fivetran "Source" dbt package that maps to the source.

3. Generate the `airbyte-catalog.json` file for the source. You can see an example in the `scripts` folder.

4. Extract the data into a local DuckDB database for the source. You can see an example in the `scripts` directory.

5. Create mapping files in `src/transforms/fivetran-interop/` for each table to transform:

   - Define the domain (e.g., `new_connector.fivetran-interop`)
   - Specify source tables and their aliasing
   - Map fields from source to target schema
   - Document field descriptions and unused fields

6. Generate the dbt project using the morph CLI:

   ```bash
   python -m morph generate-dbt-project catalog/new_connector catalog/new_connector/airbyte-catalog.json
   ```

7. Create example projects in the `examples/` directory to demonstrate usage

## Mapping File Structure

Mapping files define how to transform source data to target schemas. Key components:

- `domain`: Namespace for the transforms (e.g., `hubspot.fivetran-interop`)
- `transforms`: List of transformations to apply
  - `id`: Identifier for the transform (becomes the model name)
  - `display_name`: Human-readable name for the transform
  - `from`: Source tables to use in the transform
  - `fields`: Target fields and how to populate them
    - `expression`: SQL expression or source field reference
    - `description`: Description of the field's purpose
  - `annotations`: Additional metadata about the transform
    - `unused_source_fields`: Fields in source not used in the transform

When mapping fields:

- Direct mappings use dot notation: `table_alias.field_name`
- Missing fields use the `MISSING` placeholder to indicate NULL values
- Field descriptions should match those in the target schema

1. **Generate the raw data**

   ```bash
   uv run morph create_airbyte_data hubspot fivetran-interop
   ```

2. **Generate the Airbyte catalog**

   ```bash
   uv run morph create_airbyte_catalog hubspot fivetran-interop
   ```

3. **Generate the dbt project**

   Use the `generate-dbt-project` command to create a dbt project from the HubSpot mapping files and catalog:

   ```bash
   uv run morph generate-dbt-project \
     catalog/hubspot \
     catalog/hubspot/generated/airbyte-catalog.json \
     --output-dir catalog/hubspot/generated \
     --mapping-dir catalog/hubspot/src/transforms/fivetran-interop \
     --source-name hubspot
   ```

   This command:

   - Takes the HubSpot catalog directory as the first argument
   - Takes the Airbyte catalog.json file as the second argument
   - Specifies the output directory for the generated dbt project
   - Points to the directory containing the mapping files
   - Sets the source name for the dbt project

4. **Test the generated dbt project**

   Install dbt and test the project:

   ```bash
   # Navigate to the generated project
   cd catalog/hubspot/generated/dbt_project

   # Install dependencies
   uv sync --all-extras

   # Install dependencies
   uv run dbt deps --profiles-dir profiles

   # Compile the project
   uv run dbt compile --profiles-dir profiles
   ```

## JSON Schema to dbt Sources

Morph can also convert JSON schema files to dbt source definitions:

```bash
uv run morph json-to-dbt \
  --catalog \
  --source-name hubspot \
  --output catalog/hubspot/generated/src_airbyte_hubspot.yml \
  catalog/hubspot/airbyte-catalog.json
```

This command:

- Converts an Airbyte catalog file to dbt sources
- Names the source "hubspot"
- Outputs the result to the specified file

## Additional Resources

For more information on the available commands and options, use the `--help` flag:

```bash
uv run morph --help
uv run morph generate-dbt-project --help
uv run morph json-to-dbt --help
```
