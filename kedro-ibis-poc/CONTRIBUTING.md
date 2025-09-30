# Contributing to Kedro+Ibis POC

## Installation

```bash
cd kedro-ibis-poc
uv sync
```

## Project Structure

```
kedro-ibis-poc/
├── conf/
│   ├── base/                   # Version-controlled config
│   │   ├── catalog.yml         # Dataset definitions
│   │   ├── catalog_connections.yml  # Backend config
│   │   └── parameters.yml      # Pipeline parameters
│   └── local/                  # Local overrides (gitignored)
├── src/kedro_ibis_poc/
│   ├── pipelines/
│   │   ├── extract/            # PyAirbyte extraction
│   │   ├── staging/            # Staging transformations
│   │   └── fact/               # Fact aggregations
│   ├── pipeline_registry.py
│   └── settings.py
├── data/                       # DuckDB database (gitignored)
└── pyproject.toml
```

## Running Pipelines

Run all pipelines:
```bash
kedro run
```

Run individual pipelines:
```bash
kedro run --pipeline extract
kedro run --pipeline staging
kedro run --pipeline fact
```

## Configuration

### Backend Configuration

Edit `conf/base/catalog_connections.yml`:
```yaml
_duckdb:
  backend: duckdb
  database: data/kedro_ibis_poc.duckdb
  threads: 4
```

### Source-Faker Parameters

Edit `conf/base/parameters.yml`:
```yaml
source_faker:
  count: 1000      # Records per stream
  seed: 12345      # Random seed
  parallelism: 1   # Parallel workers
```

## Verifying Outputs

Query DuckDB directly:
```bash
duckdb data/kedro_ibis_poc.duckdb
```

```sql
-- Check raw tables
SELECT COUNT(*) FROM raw_users;

-- Check staging views
SELECT * FROM stg_users LIMIT 5;

-- Check fact tables
SELECT * FROM fct_user_purchases ORDER BY total_purchases DESC LIMIT 10;
SELECT * FROM fct_product_sales ORDER BY total_sales DESC LIMIT 10;
```

## Development

From morph repository root:

```bash
# Lint
poe lint

# Type check
poe type-check
```
