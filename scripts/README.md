# Utility Scripts

This directory contains utility scripts for the Morph project.

## JSON Schema to dbt Sources.yml Converter

`json_to_dbt_sources.py` is a utility script that converts JSON schema files to dbt sources.yml format.

### Usage

```bash
python json_to_dbt_sources.py <json_schema_file_or_directory> [--source-name SOURCE_NAME] [--output OUTPUT_FILE]
```

### Example

```bash
python json_to_dbt_sources.py schemas/ --source-name my_source --output models/sources.yml
```

### Features

- Converts JSON schema types to dbt column types
- Preserves descriptions from JSON schema
- Handles format-specific type conversions (e.g., date-time to timestamp)
- Can process a single JSON schema file or a directory of schema files
- Generates a properly formatted dbt sources.yml file
