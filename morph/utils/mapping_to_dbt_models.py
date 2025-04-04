"""
Code to convert mapping files to dbt models.

This module provides functionality to generate dbt models from mapping files.
The generated models will be placed in the 'generated' folder of the catalog.
"""

from pathlib import Path
from typing import Any

from copier import run_copy
from jinja2 import Environment

from morph import resources
from morph.constants import (
    DEFAULT_PROJECT_NAME,
    DEFAULT_SQL_DIALECT,
    SQL_DIALECT_OPTIONS,
    VALID_TRAVERSAL_BY_DIALECT,
)
from morph.utils import text_utils
from morph.utils.markdown_utils import create_markdown_section, create_markdown_table


def load_mapping_file(mapping_file_path: str) -> dict[str, Any]:
    """Load a mapping file and return its contents as a dictionary."""
    return text_utils.load_yaml_file(Path(mapping_file_path))


def _extract_transform(mapping: dict[str, Any], transform_id: str) -> dict[str, Any]:
    """Extract a transform from a mapping by ID."""
    for t in mapping.get("transforms", []):
        if t.get("name") == transform_id:
            return t
    raise ValueError(f"Transform with ID '{transform_id}' not found in mapping")


def _process_source_item(source_key: str, source_value: str) -> dict[str, str]:
    """Process a single source item and return a source dict."""
    if "." in source_value:
        schema, table = source_value.split(".")
        return {"alias": source_key, "schema": schema, "table": table}
    return {"alias": source_key, "table": source_value}


def _extract_sources(transform: dict[str, Any]) -> list[dict[str, str]]:
    """Extract source tables from a transform."""
    sources = []
    from_data = transform.get("from", {})

    # Handle both list and dict formats for 'from' field
    if isinstance(from_data, list):
        for source_item in from_data:
            for source_key, source_value in source_item.items():
                sources.append(_process_source_item(source_key, source_value))
    else:
        for source_key, source_value in from_data.items():
            sources.append(_process_source_item(source_key, source_value))

    return sources


def _format_json_path(
    expression: str,
    sql_dialect: str = DEFAULT_SQL_DIALECT,
    subcolumn_traversal: str = "default",
) -> str:
    """Format a dot notation expression for the specified database type and traversal method.

    Args:
        expression: The field expression with dot notation (e.g., "hubspot.contacts.properties.email")
        sql_dialect: The SQL dialect to use (e.g., "duckdb", "bigquery")
        subcolumn_traversal: The subcolumn traversal method to use

    Returns:
        The formatted expression for the specified database type
    """
    min_dots_for_nested_field = 2
    dot_count = expression.count(".")

    if dot_count < min_dots_for_nested_field:
        return expression

    if subcolumn_traversal == "default":
        subcolumn_traversal = SQL_DIALECT_OPTIONS.get(sql_dialect, {}).get(
            "default_subcolumn_traversal",
            "bracket_notation",
        )

    if subcolumn_traversal not in {
        "bracket_notation",
        "dot_notation",
        "default",
        "portable",
    }:
        raise NotImplementedError(
            f"Traversal method '{subcolumn_traversal}' is not implemented yet. "
            "Currently only 'bracket_notation', 'portable', and 'default' are supported.",
        )

    if (
        sql_dialect in VALID_TRAVERSAL_BY_DIALECT
        and subcolumn_traversal not in VALID_TRAVERSAL_BY_DIALECT[sql_dialect]
    ):
        raise ValueError(
            f"Subcolumn traversal method '{subcolumn_traversal}' is not valid for SQL dialect '{sql_dialect}'. "
            f"Valid options are: {', '.join(VALID_TRAVERSAL_BY_DIALECT[sql_dialect])}",
        )

    parts = expression.split(".")
    table_alias = parts[0]
    column = parts[1]
    path = parts[2:]

    if not path:
        return expression

    return _apply_traversal_format(
        table_alias=table_alias,
        column=column,
        path=path,
        traversal_method=subcolumn_traversal,
    )


def _apply_traversal_format(
    table_alias: str,
    column: str,
    path: list[str],
    traversal_method: str,
) -> str:
    """Apply the specified traversal format to the table alias and path.

    Args:
        table_alias: The table alias
        column: The column name
        path: The path components (including nested fields)
        traversal_method: The traversal method to use

    Returns:
        The formatted expression
    """
    if traversal_method in {"dot_notation", "default"}:
        return _format_dot_notation(table_alias, column, path)
    if traversal_method in {"bracket_notation", "default"}:
        return _format_bracket_notation(table_alias, column, path)
    if traversal_method == "portable":
        return _format_portable(table_alias, column, path)
    raise NotImplementedError(
        f"Traversal method '{traversal_method}' is not implemented yet. "
        "Currently only 'bracket_notation', 'portable', and 'default' are supported.",
    )


def _format_bracket_notation(
    table_alias: str,
    column: str,
    path: list[str],
) -> str:
    """Format using bracket notation."""
    formatted = table_alias
    formatted += f".{column}"
    for part in path:
        formatted += f"['{part}']"
    return formatted


def _format_dot_notation(
    table_alias: str,
    column: str,
    path: list[str],
) -> str:
    return ".".join([table_alias, column, *path])


def _format_portable(
    table_alias: str,
    column: str,
    path: list[str],
) -> str:
    """Format using portable dbt macro."""
    path_str = ", ".join([f"'{p}'" for p in path])
    return f"{{{{ json_extract({table_alias}.{column}, [{path_str}]) }}}}"


def _extract_fields(
    transform: dict[str, Any],
    config: dict[str, Any] | None = None,
) -> list[dict[str, str]]:
    """Extract fields from a transform.

    Args:
        transform: The transform configuration
        config: The project configuration (from config.yml)

    Returns:
        List of field dictionaries with name, expression, and description
    """
    config = config or {}
    sql_dialect = config.get("sql_dialect", DEFAULT_SQL_DIALECT)
    subcolumn_traversal = config.get("subcolumn_traversal", "default")

    fields: list[dict[str, str]] = []
    for field_name, field_config in transform.get("fields", {}).items():
        expression = field_config.get("expression")

        if expression and isinstance(expression, str) and "." in expression:
            expression = _format_json_path(
                expression=expression,
                sql_dialect=sql_dialect,
                subcolumn_traversal=subcolumn_traversal,
            )

        fields.append(
            {
                "name": field_name,
                "expression": expression,
                "description": field_config.get("description", ""),
            },
        )
    return fields


def generate_model_sql(
    mapping: dict[str, Any],
    transform_id: str,
    config: dict[str, Any] | None = None,
) -> str:
    """Generate SQL for a dbt model based on a mapping transform.

    Args:
        mapping: The mapping configuration
        transform_id: The ID of the transform to generate SQL for
        config: The project configuration (from config.yml)

    Returns:
        The generated SQL for the dbt model
    """
    # Extract the transform configuration
    transform = _extract_transform(mapping, transform_id)

    # Extract source tables and fields
    sources = _extract_sources(transform)
    fields = _extract_fields(transform, config)

    # Generate SQL using a template
    sql_template = """
-- This file was autogenerated with Morph. Please do not modify directly.

WITH{% for source in sources %}
{{ source.alias }} AS (
    SELECT * FROM {{ "{{" }} source('{{ source.schema.replace('airbyte_raw_', '') if 'schema' in source else 'default' }}', '{{ source.table }}') {{ "}}" }}
){% if not loop.last %},{% endif %}
{% endfor %}

SELECT{% for field in fields %}
    {% if field.expression == "MISSING" %}NULL{% else %}{{ field.expression }}{% endif %} AS {{ field.name }}{% if field.description %}{% endif %}{% if not loop.last %},{% endif %}{% endfor %}
FROM {% for source in sources %}{{ source.alias }}{% if not loop.last %}, {% endif %}{% endfor %}

"""

    # Create a simple template environment
    env = Environment(autoescape=False)
    template = env.from_string(sql_template)

    # Render the template
    return template.render(
        model_name=transform_id,
        mapping_domain=mapping.get("domain", "unknown"),
        transform_id=transform_id,
        transform_display_name=transform.get("display_name", ""),
        sources=sources,
        fields=fields,
    )


def build_dbt_project_yml(
    catalog_name: str,
    models: list[str],
) -> str:
    """Generate dbt_project.yml content."""
    project_template = """
name: 'airbyte_{{ catalog_name }}'
version: '1.0.0'
config-version: 2

profile: 'default'

model-paths: ["models"]
analysis-paths: ["analyses"]
test-paths: ["tests"]
seed-paths: ["seeds"]
macro-paths: ["macros"]
snapshot-paths: ["snapshots"]

target-path: "target"
clean-targets:
  - "target"
  - "dbt_packages"

models:
  airbyte_{{ catalog_name }}:
    +materialized: view
    {% for model in models %}
    {{ model }}:
      +materialized: table
    {% endfor %}

vars:
  airbyte_{{ catalog_name }}_schema: "{{ catalog_name }}"
  airbyte_{{ catalog_name }}_database: "{{ catalog_name }}"
"""
    env = Environment(autoescape=False)
    template = env.from_string(project_template)

    return template.render(
        catalog_name=catalog_name,
        models=models,
    )


def build_readme(mapping_files: list[str], models_dir: Path) -> None:
    """Generate README.md with documentation from table mappings.

    Args:
        mapping_files: List of mapping file paths
        models_dir: Directory where the README.md should be written
    """
    sections: list[str] = []

    # Add header
    sections.append("# Generated dbt Models\n")
    sections.append("This directory contains automatically generated dbt models based on mapping files.\n")

    # Process each mapping file
    for mapping_file in mapping_files:
        mapping = load_mapping_file(mapping_file)

        # Process each transform
        for transform in mapping.get("transforms", []):
            transform_id = transform.get("name")
            if not transform_id:
                continue

            # Add section for this transform
            sections.append(create_markdown_section(
                title=transform_id,
                content="",
                level=2
            ))

            # Add source information
            sources = _extract_sources(transform)
            if sources:
                sections.append("\n### Source Tables\n")
                headers = ["Alias", "Schema", "Table"]
                rows = [
                    [
                        source["alias"],
                        source.get("schema", "default"),
                        source["table"]
                    ]
                    for source in sources
                ]
                sections.append(create_markdown_table(headers, rows))

            # Add fields table
            fields = _extract_fields(transform)
            if fields:
                sections.append("\n### Fields\n")
                headers = ["Name", "Expression", "Description"]
                rows = [
                    [
                        field["name"],
                        str(field["expression"]),
                        field["description"] or "",
                    ]
                    for field in fields
                ]
                sections.append(create_markdown_table(headers, rows))

            sections.append("\n")

    # Write README.md
    readme_path = models_dir / "README.md"
    readme_path.write_text("\n".join(sections))


def generate_dbt_package(
    source_name: str,
    *,
    project_name: str = DEFAULT_PROJECT_NAME,
    output_dir: str | None = None,
    mapping_dir: str | None = None,
) -> None:
    """Generate a dbt package from mapping files.

    Args:
        source_name: Name of the source (e.g., 'hubspot').
        project_name: Name of the project (e.g., 'fivetran-interop').
        output_dir: Path to the output directory.
        mapping_dir: Path to the mapping directory.
    """
    output_dir_path = output_dir or resources.get_generated_dir_root(source_name)
    mapping_dir_path = mapping_dir or resources.get_transforms_dir(source_name, project_name)
    config_path = resources.get_config_file_path(source_name, project_name)

    # Create output directories
    output_path = Path(output_dir_path)
    output_path.mkdir(parents=True, exist_ok=True)

    config = {}
    if config_path.exists():
        config = text_utils.load_yaml_file(config_path)

    # Find all mapping files
    mapping_files: list[str] = []
    mapping_path = Path(mapping_dir_path)
    for yaml_file in list(mapping_path.glob("**/*.yml")) + list(mapping_path.glob("**/*.yaml")):
        mapping_files.append(str(yaml_file))

    # Generate models for each mapping file
    generated_models: list[str] = []
    for mapping_file in mapping_files:
        mapping = load_mapping_file(mapping_file)

        # Process each transform in the mapping
        for transform in mapping.get("transforms", []):
            transform_id = transform.get("name")
            if not transform_id:
                continue

            # Add to list of generated models
            generated_models.append(transform_id)

    # Use copier to generate the dbt project scaffolding
    template_dir = Path(__file__).parent.parent.parent / "templates" / "dbt_project_template"

    # Prepare data for the template
    template_data = {
        "catalog_name": source_name,
        "models": generated_models,
    }

    # Run copier to generate the project scaffolding
    run_copy(
        src_path=str(template_dir),
        dst_path=str(output_path),
        data=template_data,
    )

    # Now generate the SQL models
    models_dir = output_path / "dbt_project" / "models"
    models_dir.mkdir(parents=True, exist_ok=True)

    # Generate SQL for each model
    for mapping_file in mapping_files:
        mapping = load_mapping_file(mapping_file)

        # Process each transform in the mapping
        for transform in mapping.get("transforms", []):
            transform_id = transform.get("name")
            if not transform_id:
                continue

            # Generate SQL model
            model_sql = generate_model_sql(mapping, transform_id, config)

            # Write model to file
            model_path = models_dir / f"{transform_id}.sql"
            model_path.write_text(model_sql)

    # Generate README.md with documentation
    build_readme(mapping_files, models_dir)
