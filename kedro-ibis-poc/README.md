# Kedro+Ibis POC

A proof-of-concept demonstrating scalable data pipeline patterns using [Kedro](https://kedro.org/) workflow orchestration with [Ibis](https://ibis-project.org/)'s universal data interface.

## Overview

This POC integrates:
- **Kedro**: Pipeline orchestration and workflow management
- **Ibis**: Universal Python dataframe API with deferred execution
- **PyAirbyte**: Data extraction from source-faker connector
- **DuckDB**: Fast analytical database backend

## Architecture

Three-stage pipeline:
1. **Extract**: PyAirbyte source-faker → raw tables (users, products, purchases)
2. **Staging**: Raw tables → cleaned staging tables/views
3. **Fact**: Staging tables → aggregated fact tables

## Quick Start

```bash
cd kedro-ibis-poc
uv sync
kedro run
```

## References

- [Building scalable data pipelines with Kedro and Ibis (blog post)](https://kedro.org/blog/building-scalable-data-pipelines-with-kedro-and-ibis)
- [Kedro Documentation](https://docs.kedro.org/)
- [Ibis Documentation](https://ibis-project.org/)
- [PyAirbyte Documentation](https://docs.airbyte.com/using-airbyte/pyairbyte/getting-started)
