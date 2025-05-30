
-- This file was autogenerated with Morph. Please do not modify directly.

WITH
pull_requests AS (
    SELECT * FROM {{ source('github', 'pull_requests') }}
)


SELECT
    pull_requests.id AS id,
    pull_requests.issue_url AS issue_id,
    pull_requests.head.repo_id AS head_repo_id,
    pull_requests.head.user_id AS head_user_id
FROM pull_requests
