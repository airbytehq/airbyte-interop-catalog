# Rejected Mappings

These mappings did not meet the approval criteria and are not included in the default dbt build.

[Return to main README](./README.md)

### Mapping: Airbyte `issue_labels` to Fivetran `issue_label`


- Table Match Confidence Score: ❌ _0.00_
- Table Completion Score: ❌ _0.00_
- Summary Self-Evaluation: _Both mappings have set their expression to 'MISSING', indicating a complete lack of confidence. There is no evidence to suggest a reliable match or mapping validity due to the absence of specified expressions._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `issue_id` | Foreign key that references the issue table | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `label_id` | Unique identifier of the used label | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `reviews` to Fivetran `requested_reviewer_history`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table match is highly confident due to the similarity of the source and target schemas originating from similar source APIs, indicating they likely describe the same subject matter. However, the completion score is reduced due to the missing mappings for several fields which could not find a good match._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `pull_request_id` | Foreign key that references the pull request table. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | Timestamp of when the review was submitted. | `reviews.created_at` | 🟢 _1.00_ | *Exact field expression match.* |
| `requested_id` | Foreign key that references the user table, representing the user that was requested to review a PR. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `removed` | Boolean variable indicating if the requester was removed from the PR (true) or added to the PR (false). | `MISSING` | ❌ _0.00_ | *No good match found.* |
