# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `team_memberships` to Fivetran `repo_team`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _There are no mappings provided for necessary fields, indicating an absence of matching between the source and target schemas._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `repository_id` | Reference to the respective repository for the record. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `team_id` | Reference to the respective team for the record. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `pull_requests` to Fivetran `issue_merged`


- Table Match Confidence Score: ⚠️ _0.50_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The mapping evaluation produced mixed results. The 'merged_at' field has a good matching expression, suggesting a reasonable level of confidence in its similarity to the target schema. However, the 'issue_id' field is marked as 'MISSING', indicating no good match was found, significantly reducing the overall confidence and completion scores._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `issue_id` | Foreign key that references the issue table.  This table will only reference issues that are pull requests | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `merged_at` | Timestamp of when the code merge took place | `pull_requests.merged_at` | 🟢 _0.70_ | *Good match found with target schema field 'pull_requests.merged_at'.* |

### Mapping: Airbyte `users` to Fivetran `user`


- Table Match Confidence Score: ⚠️ _0.65_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The fields mostly match with some differences causing lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the user. | `users.id` | 🟢 _1.00_ | *matches directly to target with clear mapping.* |
| `login` | The alias the user uses to login to github. | `users.login` | 🟢 _1.00_ | *matches directly to target with clear mapping.* |
| `name` | The name of the user | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `company` | The  company of the user. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `pull_requests` to Fivetran `pull_request`


- Table Match Confidence Score: ⚠️ _0.65_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table match score reflects a moderate confidence that the source and target tables describe similar subject matter, despite some missing field mappings. The completion score is reduced due to incomplete data serialization between the source and target._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the pull request. | `pull_requests.id` | 🟢 _1.00_ | *Direct match found, high confidence.* |
| `issue_id` | Foreign key that references the issue table. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `head_repo_id` | Foreign key that references the repository table, referencing the current branch. | `pull_requests.head.repo_id` | 🟢 _0.70_ | *Likely refers to the same entity due to similar context and structure.* |
| `head_user_id` | Foreign key that references the user table, referencing who created the current branch. | `pull_requests.head.user_id` | 🟢 _0.70_ | *Likely refers to the same entity due to similar context and structure.* |
