#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "requests<3",
#   "airbyte",
# ]
# ///

import re
from pathlib import Path

import airbyte as ab
import requests

# From prior executions:
AVAILABLE_DBT_SOURCES = [
    "amazon_ads",
    "amplitude",
    "apple_search_ads",
    "apple_store",
    "asana",
    "facebook_ads",
    "facebook_pages",
    "github",
    "google_ads",
    "google_play",
    "greenhouse",
    "hubspot",
    "instagram_business",
    "intercom",
    "iterable",
    "jira",
    "klaviyo",
    "lever",
    "linkedin_pages",
    "linkedin",
    "mailchimp",
    "marketo",
    "microsoft_ads",
    "netsuite",
    "outreach",
    "pardot",
    "pendo",
    "pinterest",
    "qualtrics",
    "quickbooks",
    "recharge",
    "recurly",
    "reddit_ads",
    "sage_intacct",
    "salesforce",
    "sap",
    "shopify",
    "snapchat_ads",
    "stripe",
    "survey_monkey",
    "tiktok_ads",
    "twilio",
    "twitter_organic",
    "twitter",
    "typeform",
    "xero",
    "youtube_analytics",
    "zendesk",
    "zuora",
]
AVAILABLE_DBT_PACKAGES: list[str] = [
    f"dbt_{source}_source"
    for source in AVAILABLE_DBT_SOURCES
]

# GitHub API endpoint for Fivetran's repositories
url = "https://api.github.com/orgs/fivetran/repos"
params = {
    "per_page": 100,  # Maximum number of repositories per page
    "type": "public"  # Only public repositories
}
headers = {
    "Accept": "application/vnd.github.v3+json"
}

matching_repos = []

while url:
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"GitHub API returned status code {response.status_code}: {response.text}")

    repos = response.json()
    for repo in repos:
        name = repo["name"]
        if re.match(r"^dbt_[a-z0-9_]+_source$", name):
            matching_repos.append(name)

    # Check for pagination
    if 'next' in response.links:
        url = response.links['next']['url']
        params = None  # Parameters are already included in the 'next' URL
    else:
        url = None


airbyte_sources = [s.replace("source-", "") for s in ab.get_available_connectors()]
print(f"Found {len(airbyte_sources)} Airbyte sources.")
for source_name in airbyte_sources:
    print(source_name)


matched_sources: list[str] = []
unmatched_sources: list[str] = []

print(f"Found {len(matching_repos)} matching repositories.")
# Output the list of matching repositories
for repo_name in matching_repos:
    fivetran_source = repo_name.replace("dbt_", "").replace("_source", "")
    if fivetran_source in airbyte_sources:
        matched_sources.append(fivetran_source)
    else:
        unmatched_sources.append(fivetran_source)

print(f"\nMatched {len(matched_sources)} sources:")
for source_name in matched_sources:
    print(source_name)

print(f"\nUnmatched {len(unmatched_sources)} sources:")
for source_name in unmatched_sources:
    print(source_name)

for source_name in matched_sources:
    config_yml = Path() / "src" / "transforms" / source_name / "config.yml"
    if config_yml.exists():
        print(f"Config file for '{source_name}' already exists.")
    else:
        print(f"Creating config file for '{source_name}'.")
        config_yml.parent.mkdir(parents=True, exist_ok=True)
        config_yml.write_text(
            "\n".join(
                [
                    f"project_id: {source_name}.fivetran-interop",
                    f"source_name: {source_name}",
                    f"# Target schema file snapshotted from: https://github.com/fivetran/dbt_{source_name}_source/blob/main/models/src_{source_name}.yml",
                    f"target_dbt_schema_url: https://raw.githubusercontent.com/fivetran/dbt_{source_name}_source/refs/heads/main/models/src_{source_name}.yml",
                    "# SQL dialect configuration",
                    "sql_dialect: duckdb",
                    "subcolumn_traversal: dot_notation",
                ],
            ),
        )
