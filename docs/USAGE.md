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
5. Create a new file `src/transforms/{new_connector}/config.yml` file which populates the info above into the following example:

   ```yaml
   project_id: {new_connector}.airbyte-interop
   source_name: {new_connector}
   source_streams:
     # TODO: list streams to include in the source here

   # Target schema file snapshotted from: https://github.com/fivetran/dbt_{fivetran_source_name}_source/blob/main/models/src_{fivetran_source_name}.yml
   target_dbt_schema: https://raw.githubusercontent.com/fivetran/dbt_{fivetran_source_name}_source/refs/heads/main/models/src_{fivetran_source_name}.yml
   target_tables: []  # Will be added later
   ```

6. Generate the project scaffold using the morph CLI:

   - This will generate the Airbyte catalog, mapping files, and dbt project.
   - Optionally, you can skip certain steps by using the `--no-airbyte-catalog`, `--no-transforms`, or `--no-dbt-project` flags. (See `morph build --help` for more information.)

   ```bash
   uv run morph build {source_name}
   ```

7. Generated Airbyte schema for the source.

   - The first time you run this it will require creds in a `GCP_GSM_CREDENTIALS` env var.
     ```bash
     uv run morph sync {source_name} --with-data
     ```
   - Subsequent executions can be run without creds, using the generated catalog.
     ```bash
     uv run morph sync {source_name} --with-data --no-creds
     ```

8. Optionally extract the raw data. This will require creds and may take a while.
   ```bash
   uv run morph sync {source_name}
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
   │   └── airbyte-interop/
   ├── requirements/
   │   └── airbyte-interop/
   └── examples/
   ```

2. Add the target schema definition in `requirements/airbyte-interop/src_new_connector.yml`. You can download this from the Fivetran "Source" dbt package that maps to the source.

3. Generate the `airbyte-catalog.json` file for the source. You can see an example in the `scripts` folder.

4. Extract the data into a local DuckDB database for the source. You can see an example in the `scripts` directory.

5. Create mapping files in `src/transforms/airbyte-interop/` for each table to transform:

   - Define the domain (e.g., `new_connector.airbyte-interop`)
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

- `domain`: Namespace for the transforms (e.g., `hubspot.airbyte-interop`)
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
   uv run morph create_airbyte_data hubspot airbyte-interop
   ```

2. **Generate the Airbyte catalog**

   ```bash
   uv run morph create_airbyte_catalog hubspot airbyte-interop
   ```

3. **Generate the dbt project**

   Use the `generate-dbt-project` command to create a dbt project from the HubSpot mapping files and catalog:

   ```bash
   uv run morph generate-dbt-project \
     catalog/hubspot \
     catalog/hubspot/generated/airbyte-catalog.json \
     --output-dir catalog/hubspot/generated \
     --mapping-dir catalog/hubspot/src/transforms/airbyte-interop \
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

## Lock Files

When generating a project, Morph creates a `morph-lock.toml` file in the `catalog/{source_name}/src/` directory. This file tracks:

- Unused source streams: Streams in the source schema that aren't used in any mapping files
- Unused source fields: Fields in the source streams that aren't used in any mapping
- Unmapped target tables: Tables in the target schema that don't have corresponding mapping files
- Omitted target fields: Fields in the target schema that aren't mapped in the transformation

The lock file helps identify gaps in your transformations and can be used for tracking and documentation purposes.

To generate only the lock file without rebuilding the entire project, use the `lock` command:

```bash
uv run morph lock [source_name] [project_name]
```

To skip generating the lock file during project generation, use the `--no-lock-file` flag with the `build` command.

## DBML and ERD Generation

Morph can generate DBML (Database Markup Language) files from source and target schemas. These files can be used to visualize the database schema as Entity Relationship Diagrams (ERDs).

### Generating DBML Files

DBML files are automatically generated when you build a dbt project:

```bash
# Build project (includes DBML generation)
uv run morph build source_name --project-name project_name
```

### DBML File Location

By default, DBML files are generated in:

- Source schema: Adjacent to the generated source file at `catalog/{source_name}/generated/src_airbyte_{source_name}.dbml`
- Target schema: Adjacent to the target schema file at `catalog/{source_name}/requirements/{project_name}/src_dbt_requirements.dbml`

### Visualizing ERDs

Morph can automatically visualize DBML files as SVG images using a Docker-based solution. When DBML files are generated, Morph will attempt to render them to SVG images in the same directory.

**Requirements:**
- Docker must be installed and available on your system

**Automatic Visualization:**
- SVG files are automatically generated alongside DBML files during the build process
- Source schema: `catalog/{source_name}/generated/src_airbyte_{source_name}.svg`
- Target schema: `catalog/{source_name}/requirements/{project_name}/src_dbt_requirements.svg`

**Manual Visualization:**
```bash
# Visualize specific DBML files
uv run morph visualize-dbml catalog/hubspot/generated/src_airbyte_hubspot.dbml
```

You can also use online tools to visualize DBML files:
- [dbdiagram.io](https://dbdiagram.io/d) - Paste the DBML content
- [dbdocs.io](https://dbdocs.io/) - For publishing documentation

## JSON Schema to dbt Sources

Morph can convert JSON schema files to dbt source definitions with field name normalization:

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
- Automatically normalizes field names (replacing special characters with underscores)
- Preserves original field names in the meta section when normalization changes the name

### Regenerating Source Files

To regenerate source files with normalized field names for existing connectors:

```bash
# For Hubspot
uv run morph json-to-dbt \
  --catalog \
  --source-name hubspot

# For Facebook Marketing
uv run morph json-to-dbt \
  --catalog \
  --source-name facebook_marketing
```

## Mapping Confidence Evaluation

The mapping confidence evaluation tool uses AI to analyze field mappings and provide a confidence score for the transformation. This is particularly useful when working with complex data transformations or when you want to validate your mapping configurations.

### Basic Usage

```bash
# Using poe
poe eval-mapping path/to/mapping.json

# Or directly
uv run morph eval-mapping path/to/mapping.json
```

### Options

- `--source-type`: Specify the source data type (default: "JSON")
- `--target-type`: Specify the target data type (default: "dbt model")

Example with custom types:

```bash
poe eval-mapping path/to/mapping.json --source-type CSV --target-type "PostgreSQL table"
```

### Input Format

The mapping file should be a YAML file in dbt transform format. The file should contain:

- `domain`: The namespace for the transforms
- `transforms`: List of transformations, each containing:
  - `id`: Identifier for the transform
  - `display_name`: Human-readable name
  - `from`: Source tables
  - `fields`: Field mappings with:
    - `expression`: SQL expression or source field reference
    - `description`: Field description
    - `tests`: (optional) Test configurations

Example:

```yaml
domain: facebook_marketing.airbyte-interop
transforms:
  - display_name: Each record in this table reflects a version of a Facebook ad.
    id: ad_history
    from:
      - ads: facebook_marketing.ads
    fields:
      id:
        expression: ads.id
        description: The ID of this ad.
      name:
        expression: ads.name
        description: Name of the ad.
```

### Output

The tool provides:

1. Overall confidence score (0.00 to 1.00)
2. Detailed explanation of the score
3. Field-by-field confidence analysis including:
   - Field name
   - Expression used
   - Field description
   - Confidence score

Example output:

```
Overall Confidence Score: 0.85

Explanation: The mapping shows good field coverage and appropriate transformations...

Field-by-Field Analysis:
┌──────────┬──────────────┬──────────────────────┬────────────┐
│ Field    │ Expression   │ Description          │ Confidence │
├──────────┼──────────────┼──────────────────────┼────────────┤
│ id       │ ads.id       │ The ID of this ad    │ 0.95       │
│ name     │ ads.name     │ Name of the ad       │ 0.90       │
└──────────┴──────────────┴──────────────────────┴────────────┘
```

### Best Practices

1. Use descriptive field names and expressions
2. Include field descriptions when possible
3. Add appropriate tests for data quality
4. Review the confidence scores and explanations
5. Address any low-confidence mappings before deployment

## SQL Dialect Configuration

Morph supports configuring SQL dialect and subcolumn traversal methods to handle nested JSON fields in different database systems.

### Configuration Options

Add the following options to your `config.yml` file:

```yaml
# SQL dialect configuration
sql_dialect: duckdb # Default is "duckdb"
subcolumn_traversal: default # Default is "default" (uses the default for the selected dialect)
```

### SQL Dialect Options

The following SQL dialects are supported:

| Dialect     | Description                | Default Subcolumn Traversal |
| ----------- | -------------------------- | --------------------------- |
| `duckdb`    | DuckDB                     | `bracket_notation`          |
| `bigquery`  | Google BigQuery            | `json_path`                 |
| `snowflake` | Snowflake                  | `colon_notation`            |
| `postgres`  | PostgreSQL                 | `arrow_notation`            |
| `sqlserver` | SQL Server                 | `json_path`                 |
| `portable`  | Portable (uses dbt macros) | `portable`                  |

### Subcolumn Traversal Options

The following subcolumn traversal methods are supported:

| Method             | Example                                              | Description                                          |
| ------------------ | ---------------------------------------------------- | ---------------------------------------------------- |
| `bracket_notation` | `column['property']['nested']`                       | Uses bracket notation for JSON traversal             |
| `json_path`        | `JSON_EXTRACT(column, '$.property.nested')`          | Uses JSON_EXTRACT function                           |
| `colon_notation`   | `column:property:nested`                             | Uses colon notation (Snowflake)                      |
| `arrow_notation`   | `column->'property'->>'nested'`                      | Uses arrow operators (PostgreSQL)                    |
| `dot_notation`     | `column.property.nested`                             | Uses dot notation (only supported in some dialects)  |
| `portable`         | `{{ json_extract(column, ['property', 'nested']) }}` | Uses dbt macro for cross-database compatibility      |
| `default`          | (varies by dialect)                                  | Uses the default method for the selected SQL dialect |

### Compatibility

Not all traversal methods are compatible with all SQL dialects. The following table shows the valid combinations:

| Dialect     | Valid Traversal Methods                                                  |
| ----------- | ------------------------------------------------------------------------ |
| `duckdb`    | `bracket_notation`, `json_path`, `portable`, `default`                   |
| `bigquery`  | `json_path`, `dot_notation`, `portable`, `default`                       |
| `snowflake` | `colon_notation`, `bracket_notation`, `json_path`, `portable`, `default` |
| `postgres`  | `arrow_notation`, `json_path`, `portable`, `default`                     |
| `sqlserver` | `json_path`, `portable`, `default`                                       |
| `portable`  | `portable`, `default`                                                    |

If an incompatible combination is specified, an error will be raised.

### Example

```yaml
# config.yml
sql_dialect: bigquery
subcolumn_traversal: json_path
```

This configuration will use BigQuery's JSON_EXTRACT function for nested field traversal.

## Environment Variables

Morph supports loading environment variables from a `.env` file in your current working directory. This is particularly useful for storing secrets like API keys that you don't want to commit to version control.

### Using .env Files

1. Create a `.env` file in the root of your project by copying the template:

   ```bash
   cp .env.template .env
   ```

2. Edit the `.env` file and add your environment variables:

   ```
   OPENAI_API_KEY=your-openai-api-key-here
   ```

3. Morph will automatically load these variables when you run any CLI command.

4. For AI-assisted functionality (mapping generation and evaluation), the `OPENAI_API_KEY` variable is required.

## Additional Resources

For more information on the available commands and options, use the `--help` flag:

```bash
uv run morph --help
uv run morph generate-dbt-project --help
uv run morph json-to-dbt --help
```
