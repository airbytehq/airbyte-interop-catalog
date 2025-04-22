#!/bin/bash

# Simulate the generate command workflow
echo "Testing generate command workflow"

# Parameters
SOURCE_NAME=${1:-"hubspot"}
PROJECT_NAME="airbyte-interop"

echo "Source: $SOURCE_NAME"
echo "Project: $PROJECT_NAME"

# Simulate success case
echo "Generate command succeeded"
echo "generate_success=true"

# Simulate changes
echo "Changes found after running generate command"
echo "generate_changes=true"

# Simulate PR creation
if [ "$SOURCE_NAME" == "hubspot" ]; then
  echo "PR created: https://github.com/airbytehq/airbyte-morph-catalog/pull/123"
  exit 0
else
  echo "Generate command failed with exit code 1"
  echo "PR created with error details: https://github.com/airbytehq/airbyte-morph-catalog/pull/124"
  exit 1
fi
