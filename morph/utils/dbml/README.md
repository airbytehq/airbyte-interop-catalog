# DBML Generator

This module provides functionality to generate DBML (Database Markup Language) files from DbtSourceFile objects.
Generated DBML files can be used to visualize database schemas as Entity Relationship Diagrams (ERDs).

## Usage

```python
from morph.utils.dbml.dbml_generator import (
    generate_dbml_from_dbt_source_file,
    generate_source_dbml,
    generate_target_dbml,
)

# Generate DBML from a DbtSourceFile object
generate_dbml_from_dbt_source_file(dbt_source_file, output_file)

# Generate DBML for a source
generate_source_dbml(source_name="hubspot")

# Generate DBML for a target schema
generate_target_dbml(source_name="hubspot")
```

## Output Location

By default, DBML files are generated in:

- Source schema: `catalog/{source_name}/generated/erd/source.dbml`
- Target schema: `catalog/{source_name}/generated/erd/target.dbml`

## Visualization

The generated DBML files can be visualized using tools like:

- [dbdiagram.io](https://dbdiagram.io/d) - Paste the DBML content
- [dbdocs.io](https://dbdocs.io/) - For publishing documentation
