# Utility Scripts

This directory contains utility scripts for the Morph project.

## JSON Schema to dbt Sources.yml Converter

The `json-to-dbt` command in the Morph CLI converts JSON schema files to dbt sources.yml format.

### Usage

```bash
uv run morph json-to-dbt <schema_path> [--catalog] [--source-name SOURCE_NAME] [--database DATABASE] [--schema SCHEMA] [--output OUTPUT_FILE]
```

### Options

- `schema_path`: Path to a JSON schema file or directory containing schema files
- `--catalog`: Treat input as an Airbyte catalog file
- `--source-name`: Name for the dbt source (default: "default_source")
- `--database`: Database name for the source
- `--schema`: Schema name for the source
- `--output`: Output file path (default: "sources.yml")

### Examples

Convert a directory of JSON schema files:

```bash
uv run morph json-to-dbt schemas/ --source-name my_source --output models/src_my_source.yml
```

Convert an Airbyte catalog file:

```bash
uv run morph json-to-dbt catalog/hubspot/airbyte-source/catalog.json --catalog --source-name hubspot --output catalog/hubspot/generated/src_airbyte_hubspot.yml
```

### Features

- Converts JSON schema types to dbt column types
- Preserves descriptions from JSON schema
- Handles format-specific type conversions (e.g., date-time to timestamp)
- Can process a single JSON schema file or a directory of schema files
- Can process Airbyte catalog files
- Generates a properly formatted dbt sources.yml file with header comments
