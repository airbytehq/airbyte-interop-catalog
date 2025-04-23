# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `MISSING` to Fivetran `repository`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _All field mappings have been set to 'MISSING' indicating there is no confidence in the field mappings. No good matches have been found, thus the table match and completion scores are 0._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the repository. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | Timestamp of when the repository was created. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `full_name` | The name of the git repository. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `private` | Boolean field indicating whether the repository is private (true) or public (false). | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `issue_timeline_events` to Fivetran `issue_closed_history`


- Table Match Confidence Score: ⚠️ _0.50_
- Table Completion Score: ❌ _0.33_
- Summary Self-Evaluation: _The mappings provided include missing expressions signifying no good match found for some required fields, leading to a lower completion score. The table match score is moderate, indicating a potential match but with uncertainty._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `issue_id` | Foreign key that references the issue table | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `updated_at` | Timestamp of when the action took place | `issue_timeline_events.comment.updated_at` | 🟢 _1.00_ | *Direct mapping confirmed, ensuring high confidence.* |
| `closed` | Boolean variable for if the issue was closed (true) or re-opened (false) | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `MISSING` to Fivetran `issue_assignee`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _No valid mappings could be established based on the provided field mappings which are all marked as 'MISSING'._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `issue_id` | Foreign key that references the issue table | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `user_id` | Foreign key that references the user table | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `issue_labels` to Fivetran `issue_label`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _Given the mappings provided, both fields are set to 'MISSING' indicating no good match found for any of the fields, leading to a total lack of reliable field mappings and thus a complete absence of confidence in this table mapping._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `issue_id` | Foreign key that references the issue table | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `label_id` | Unique identifier of the used label | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `MISSING` to Fivetran `requested_reviewer_history`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _No good matches found for any fields. All expressions are set to 'MISSING', indicating a lack of proper mapping information, leading to zero confidence scores._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `pull_request_id` | Foreign key that references the pull request table. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | Timestamp of when the review was submitted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `requested_id` | Foreign key that references the user table, representing the user that was requested to review a PR. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `removed` | Boolean variable indicating if the requester was removed from the PR (true) or added to the PR (false). | `MISSING` | ❌ _0.00_ | *No good match found.* |
