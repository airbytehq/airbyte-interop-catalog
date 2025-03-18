# HubSpot JSON Schemas

This directory contains JSON schema files from the Airbyte HubSpot connector.

## Source

These schema files are sourced from the Airbyte repository:

- Repository: [airbytehq/airbyte](https://github.com/airbytehq/airbyte)
- Path: `airbyte-integrations/connectors/source-hubspot/source_hubspot/schemas/`

## Updating Schemas

To refresh these schemas with the latest versions from the Airbyte repository:

1. Clone or update the Airbyte repository:

   ```bash
   # If you haven't cloned the repo yet
   git clone https://github.com/airbytehq/airbyte.git ~/repos/airbyte

   # If you already have the repo
   cd ~/repos/airbyte
   git checkout main
   git pull
   ```

2. Copy the latest schemas to this directory:

   ```bash
   # Create the directory if it doesn't exist
   mkdir -p ~/repos/morph/catalog/hubspot/airbyte-source/schemas

   # Copy all schema files
   cp -r ~/repos/airbyte/airbyte-integrations/connectors/source-hubspot/source_hubspot/schemas/* ~/repos/morph/catalog/hubspot/airbyte-source/schemas/
   ```

3. Commit and push the changes to your branch:
   ```bash
   cd ~/repos/morph
   git add catalog/hubspot/airbyte-source/schemas/
   git commit -m "chore: Update HubSpot schemas from Airbyte"
   git push
   ```

## Usage

These schema files can be used with the JSON schema to dbt sources.yml converter script in the `scripts` directory to generate dbt sources for HubSpot data.

Example:

```bash
python ~/repos/morph/scripts/json_to_dbt_sources.py ~/repos/morph/catalog/hubspot/airbyte-source/schemas/ --source-name hubspot --output ~/repos/morph/catalog/hubspot/sources.yml
```
