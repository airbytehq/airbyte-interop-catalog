# Airbyte HubSpot Fivetran Compatibility

This dbt project provides Fivetran compatibility for Airbyte HubSpot connector.
It depends on the generated Airbyte HubSpot models and exposes them in a Fivetran-compatible format.

## Usage

This project depends on the generated Airbyte HubSpot models. To use it:

1. Install dependencies:
   ```
   dbt deps --profiles-dir profiles
   ```

2. Compile the project:
   ```
   dbt compile --profiles-dir profiles
   ```
