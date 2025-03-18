#!/bin/bash

uv sync --directory=catalog/hubspot/generated/dbt_project --all-extras
uv run --directory=catalog/hubspot/generated/dbt_project dbt build --profiles-dir=profiles
uv run --project-root=catalog/hubspot/dbt_project/ dbt run --profiles-dir=profiles
