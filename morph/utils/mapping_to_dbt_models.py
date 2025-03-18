"""
Code to convert mapping files to dbt models.

This module provides functionality to generate dbt models from mapping files.
The generated models will be placed in the 'generated' folder of the catalog.
"""

import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml
from jinja2 import Environment, FileSystemLoader


def load_mapping_file(mapping_file_path: str) -> Dict[str, Any]:
    """Load a mapping file and return its contents as a dictionary."""
    with open(mapping_file_path, "r") as f:
        return yaml.safe_load(f)


def generate_model_sql(mapping: Dict[str, Any], transform_id: str) -> str:
    """Generate SQL for a dbt model based on a mapping transform."""
    # Extract the transform configuration
    transform = None
    for t in mapping.get("transforms", []):
        if t.get("id") == transform_id:
            transform = t
            break
    
    if not transform:
        raise ValueError(f"Transform with ID '{transform_id}' not found in mapping")
    
    # Extract source tables
    sources = []
    from_data = transform.get("from", {})
    
    # Handle both list and dict formats for 'from' field
    if isinstance(from_data, list):
        for source_item in from_data:
            for source_key, source_value in source_item.items():
                if "." in source_value:
                    schema, table = source_value.split(".")
                    sources.append({"alias": source_key, "schema": schema, "table": table})
                else:
                    sources.append({"alias": source_key, "table": source_value})
    else:
        for source_key, source_value in from_data.items():
            if "." in source_value:
                schema, table = source_value.split(".")
                sources.append({"alias": source_key, "schema": schema, "table": table})
            else:
                sources.append({"alias": source_key, "table": source_value})
    
    # Extract fields
    fields = []
    for field_name, field_config in transform.get("fields", {}).items():
        fields.append({
            "name": field_name,
            "expression": field_config.get("expression"),
            "description": field_config.get("description", "")
        })
    
    # Generate SQL using a template
    sql_template = """
-- {{ model_name }} model
-- Generated from mapping: {{ mapping_domain }}/{{ transform_id }}
-- Description: {{ transform_display_name }}

WITH {% for source in sources %}
{{ source.alias }} AS (
    SELECT * FROM {{ "{{" }} source('{{ source.schema.replace('airbyte_raw_', '') if 'schema' in source else 'default' }}', '{{ source.table }}') {{ "}}" }}
){% if not loop.last %},{% endif %}
{% endfor %}

SELECT
{% for field in fields %}
    {{ field.expression }} AS {{ field.name }}{% if field.description %} -- {{ field.description }}{% endif %}{% if not loop.last %},{% endif %}
{% endfor %}
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
        fields=fields
    )


def generate_dbt_project_yml(catalog_name: str, models: List[str]) -> str:
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
"""
    env = Environment(autoescape=False)
    template = env.from_string(project_template)
    
    return template.render(
        catalog_name=catalog_name,
        models=models
    )


def generate_dbt_package(
    catalog_dir: str,
    output_dir: Optional[str] = None,
    mapping_dir: Optional[str] = None
) -> None:
    """Generate a dbt package from mapping files.
    
    Args:
        catalog_dir: Path to the catalog directory (e.g., 'catalog/hubspot')
        output_dir: Path to the output directory (defaults to '{catalog_dir}/generated')
        mapping_dir: Path to the mapping directory (defaults to '{catalog_dir}/transforms')
    """
    catalog_path = Path(catalog_dir)
    catalog_name = catalog_path.name
    
    # Set default directories if not provided
    if not output_dir:
        output_dir = str(catalog_path / "generated")
    if not mapping_dir:
        mapping_dir = str(catalog_path / "transforms")
    
    # Create output directories
    models_dir = os.path.join(output_dir, "models")
    os.makedirs(models_dir, exist_ok=True)
    
    # Find all mapping files
    mapping_files = []
    for root, _, files in os.walk(mapping_dir):
        for file in files:
            if file.endswith((".yml", ".yaml")):
                mapping_files.append(os.path.join(root, file))
    
    # Generate models for each mapping file
    generated_models = []
    for mapping_file in mapping_files:
        mapping = load_mapping_file(mapping_file)
        
        # Process each transform in the mapping
        for transform in mapping.get("transforms", []):
            transform_id = transform.get("id")
            if not transform_id:
                continue
            
            # Generate SQL model
            model_sql = generate_model_sql(mapping, transform_id)
            
            # Write model to file
            model_path = os.path.join(models_dir, f"{transform_id}.sql")
            with open(model_path, "w") as f:
                f.write(model_sql)
            
            generated_models.append(transform_id)
    
    # Generate dbt_project.yml
    project_yml = generate_dbt_project_yml(catalog_name, generated_models)
    project_path = os.path.join(output_dir, "dbt_project.yml")
    with open(project_path, "w") as f:
        f.write(project_yml)
    
    # Generate packages.yml if needed
    packages_yml = """
packages:
  - package: dbt-labs/dbt_utils
    version: 1.1.1
"""
    packages_path = os.path.join(output_dir, "packages.yml")
    with open(packages_path, "w") as f:
        f.write(packages_yml)
    
    # Create an empty py.typed file to mark the package as type-hint compliant
    py_typed_path = os.path.join(output_dir, "py.typed")
    with open(py_typed_path, "w") as f:
        pass
