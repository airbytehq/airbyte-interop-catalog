# SQL Dialect Configuration

The morph project supports configuring SQL dialect and subcolumn traversal methods to handle nested JSON fields in different database systems.

## Configuration Options

Add the following options to your `config.yml` file:

```yaml
# SQL dialect configuration
sql_dialect: duckdb  # Default is "duckdb"
subcolumn_traversal: default  # Default is "default" (uses the default for the selected dialect)
```

## SQL Dialect Options

The following SQL dialects are supported:

| Dialect | Description | Default Subcolumn Traversal |
|---------|-------------|----------------------------|
| `duckdb` | DuckDB | `bracket_notation` |
| `bigquery` | Google BigQuery | `json_path` |
| `snowflake` | Snowflake | `colon_notation` |
| `postgres` | PostgreSQL | `arrow_notation` |
| `sqlserver` | SQL Server | `json_path` |
| `portable` | Portable (uses dbt macros) | `portable` |

## Subcolumn Traversal Options

The following subcolumn traversal methods are supported:

| Method | Example | Description |
|--------|---------|-------------|
| `bracket_notation` | `column['property']['nested']` | Uses bracket notation for JSON traversal |
| `json_path` | `JSON_EXTRACT(column, '$.property.nested')` | Uses JSON_EXTRACT function |
| `colon_notation` | `column:property:nested` | Uses colon notation (Snowflake) |
| `arrow_notation` | `column->'property'->>'nested'` | Uses arrow operators (PostgreSQL) |
| `dot_notation` | `column.property.nested` | Uses dot notation (only supported in some dialects) |
| `portable` | `{{ json_extract(column, ['property', 'nested']) }}` | Uses dbt macro for cross-database compatibility |
| `default` | (varies by dialect) | Uses the default method for the selected SQL dialect |

## Compatibility

Not all traversal methods are compatible with all SQL dialects. The following table shows the valid combinations:

| Dialect | Valid Traversal Methods |
|---------|------------------------|
| `duckdb` | `bracket_notation`, `json_path`, `portable`, `default` |
| `bigquery` | `json_path`, `dot_notation`, `portable`, `default` |
| `snowflake` | `colon_notation`, `bracket_notation`, `json_path`, `portable`, `default` |
| `postgres` | `arrow_notation`, `json_path`, `portable`, `default` |
| `sqlserver` | `json_path`, `portable`, `default` |
| `portable` | `portable`, `default` |

If an incompatible combination is specified, an error will be raised.

## Example

```yaml
# config.yml
sql_dialect: bigquery
subcolumn_traversal: json_path
```

This configuration will use BigQuery's JSON_EXTRACT function for nested field traversal.
