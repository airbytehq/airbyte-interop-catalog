"""Global constants for the morph project."""

HEADER_COMMENT = """# This file was auto-generated using the morph cli.
# Please do not edit manually.
"""

DEFAULT_PROJECT_NAME = "fivetran-interop"

MISSING = "MISSING"

SQL_DIALECT_OPTIONS = {
    "duckdb": {
        "name": "DuckDB",
        "default_subcolumn_traversal": "dot_notation",
    },
    "bigquery": {
        "name": "BigQuery",
        "default_subcolumn_traversal": "json_path",
    },
    "snowflake": {
        "name": "Snowflake",
        "default_subcolumn_traversal": "colon_notation",
    },
    "postgres": {
        "name": "PostgreSQL",
        "default_subcolumn_traversal": "arrow_notation",
    },
    "sqlserver": {
        "name": "SQL Server",
        "default_subcolumn_traversal": "json_path",
    },
    "portable": {
        "name": "Portable (dbt macros)",
        "default_subcolumn_traversal": "portable",
    },
}

DEFAULT_SQL_DIALECT = "duckdb"

SUBCOLUMN_TRAVERSAL_OPTIONS = [
    "bracket_notation",  # column['property']['nested']
    "json_path",  # JSON_EXTRACT(column, '$.property.nested')
    "colon_notation",  # column:property:nested
    "arrow_notation",  # column->'property'->>'nested'
    "dot_notation",  # column.property.nested (only supported in some dialects)
    "portable",  # Uses dbt macro for cross-database compatibility
    "default",  # Uses the default for the selected SQL dialect
]

VALID_TRAVERSAL_BY_DIALECT: dict[str, list[str]] = {
    "duckdb": ["dot_notation", "json_path", "portable", "default"],
    "bigquery": ["json_path", "dot_notation", "portable", "default"],
    "snowflake": ["colon_notation", "bracket_notation", "json_path", "portable", "default"],
    "postgres": ["arrow_notation", "json_path", "portable", "default"],
    "sqlserver": ["json_path", "portable", "default"],
    "portable": ["portable", "default"],
}

MIN_APPROVAL_SCORE = 0.7
MAX_MISSING_FIELDS = 2
