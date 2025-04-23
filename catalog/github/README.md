# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping: Airbyte `teams` to Fivetran `team`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table mapping has high confidence as both source and target tables refer to team data and correspond well in terms of context. However, complete mapping coverage is not achieved as some source implementations do not serialize all fields matched to the target, leading to a slightly lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the team. | `teams.id` | 🟢 _1.00_ | *Perfect match for system generated unique ID.* |
| `description` | User created description of the team. | `teams.description` | 🟢 _0.95_ | *Direct relationship between the source and target description fields.* |
| `name` | User created name of the team. | `teams.name` | 🟢 _0.95_ | *Direct relationship between the source and target names, indicative of exact data purpose match.* |
| `parent_id` | Reference to the parent team. | `teams.parent` | 🟢 _0.90_ | *Proper referral to the parent team.* |
| `privacy` | Type of privacy permissions associated with the team. | `teams.privacy` | 🟢 _0.85_ | *Privacy permissions match contextually between source and target.* |
| `slug` | Url friendly version of the team name. | `teams.slug` | 🟢 _0.90_ | *URL friendly names align perfectly between source team name and target team slug.* |

### Mapping: Airbyte `reviews` to Fivetran `pull_request_review`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The overall table match score is high, indicating a strong alignment between the source and target schemas. However, the completion score has modest room for improvement due to some fields not being perfectly aligned._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the pull request review. | `reviews.id` | 🟢 _1.00_ | *Perfect match for 'id' as it maps directly to 'reviews.id'.* |
| `pull_request_id` | Foreign key that references the pull request table. | `reviews.pull_request_url` | 🟢 _0.80_ | *High mapping score, appropriately linking 'pull_request_id' to 'reviews.pull_request_url'.* |
| `submitted_at` | Timestamp of when the request for review was submitted. | `reviews.submitted_at` | 🟢 _1.00_ | *Direct mapping of 'submitted_at' to 'reviews.submitted_at' displays excellent confidence.* |
| `state` | Whether the review was an approval, request for change, comment, dismissal. | `reviews.state` | 🟢 _1.00_ | *The field 'state' maps precisely to 'reviews.state', indicating a perfect match with unwavering confidence.* |
| `user_id` | Foreign key that references the user table, representing the user that reviewed the pull request. | `reviews.user.id` | ❌ _0.30_ | *Low confidence due to potential semantic difference between 'user_id' in target and 'reviews.user.id' in source; case of likely different entities.* |

### Mapping: Airbyte `repositories` to Fivetran `repository`


- Table Match Confidence Score: 🟢 _0.95_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The mappings provided are highly reliable and follow the target schema closely, ensuring a high degree of confidence that the source and target tables describe the same entities accurately, though not every field could be fully mapped._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the repository. | `repositories.id` | 🟢 _1.00_ | *Direct mapping between 'repositories.id' to 'id', representing the same unique repository identifier, ensuring high confidence.* |
| `created_at` | Timestamp of when the repository was created. | `repositories.created_at` | 🟢 _1.00_ | *Direct mapping between 'repositories.created_at' to 'created_at', accurately capturing the creation timestamp of the repository.* |
| `full_name` | The name of the git repository. | `repositories.full_name` | 🟢 _1.00_ | *Direct mapping between 'repositories.full_name' to 'full_name', accurately reflecting the repository's full name.* |
| `private` | Boolean field indicating whether the repository is private (true) or public (false). | `repositories.private` | 🟢 _1.00_ | *Direct mapping from 'repositories.private' to 'private', correctly represents the repository's privacy status.* |

### Mapping: Airbyte `comments` to Fivetran `issue_comment`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The table evaluates well in terms of match quality, however, lacking complete field mappings. The 'issue_id' being 'MISSING' degrades the completion score slightly._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the issue comment. | `comments.id` | 🟢 _1.00_ | *Perfect match for 'comments.id' with 'id'.* |
| `issue_id` | Foreign key that references the issue table | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `user_id` | Foreign key that references the user table | `comments.user_id` | 🟢 _0.90_ | *High confidence for 'comments.user_id' correlating well with 'user_id'.* |
| `created_at` | Timestamp of when the issue comment was created. | `comments.created_at` | 🟢 _1.00_ | *Perfect mapping from 'comments.created_at' to 'created_at'.* |

### Mapping: Airbyte `issue_labels` to Fivetran `issue_label`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table and fields show some alignment, but not entirely complete or perfectly matched due to one MISSING expression._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `issue_id` | Foreign key that references the issue table | `issue_labels.id` | 🟢 _0.80_ | *Properly mapped to a corresponding field in the target schema, likely referring to the same entity. Relatively high confidence in match, but some ambiguity remains.* |
| `label_id` | Unique identifier of the used label | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `issues` to Fivetran `issue`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _The mappings provide a high level of confidence that the source and target schema fields are well-aligned, capturing the essential relationships and meaning of the data. Most field mappings are accurately represented, with clear expressions and descriptions suitable for data transformation tasks between the platforms._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the issue.  This is not the number that appears in the URL. | `issues.id` | 🟢 _1.00_ | *Direct match found on identifier fields.* |
| `body` | The text of the main description of the issue. | `issues.body` | 🟢 _0.90_ | *Literal and semantic match on the main issue description.* |
| `locked` | Boolean indicating whether the issue is locked. | `issues.locked` | 🟢 _1.00_ | *Boolean values for locking status are literally and contextually matched.* |
| `closed_at` | Timestamp of when the issue was closed, NULL for issues that are open. | `issues.closed_at` | 🟢 _0.90_ | *Direct mapping on timestamp fields for issue closure, slight ambiguity might arise from date format expectations.* |
| `created_at` | Timestamp of when the issue was created. | `issues.created_at` | 🟢 _0.90_ | *Direct mapping on creation timestamp, slight ambiguity might arise from date format expectations.* |
| `milestone_id` | Foreign key that references the milestone table representing the current milestone the issue is in. | `issues.milestone.id` | 🟢 _0.80_ | *Good match on foreign key representation for milestones, minor misalignment possible in schema details.* |
| `number` | The issue number within a repository.  Is unique by repository, but not across repositories. | `issues.number` | 🟢 _0.90_ | *Literal match found with slight potential for misinterpretation across different repositories.* |
| `pull_request` | Boolean for is the issue is a pull request (true) ot regular issue (false) | `issues.pull_request` | 🟢 _1.00_ | *Explicit match on issue type as boolean indicating pull request or regular issue.* |
| `repository_id` | Foreign key that references the repository table. | `issues.repository` | 🟢 _0.90_ | *Direct mapping on foreign keys for repositories, slight ambiguity with repository grouping or identifier uniqueness.* |
| `state` | Whether the issue is open or closed. | `issues.state` | 🟢 _1.00_ | *Exact match on the issue state, open or closed.* |
| `title` | Title of the issue. | `issues.title` | 🟢 _0.90_ | *Literal match on the title of the issue, minor potential for misalignment in text processing or format.* |
| `updated_at` | Timestamp of when the last update was made to the issue. | `issues.updated_at` | 🟢 _0.90_ | *Direct mapping on update timestamps, slight ambiguities due to different timezone or format expectations.* |
| `user_id` | Foreign key that references the user table, representing the user that created the issue. | `issues.user.id` | 🟢 _0.90_ | *Good match on user identifiers with slight potential for confusion if user table schema differs slightly.* |

### Mapping: Airbyte `issue_labels` to Fivetran `label`


- Table Match Confidence Score: 🟢 _0.95_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _High confidence in table match due to the strong alignment of field names and descriptions between the source and target schemas. All fields have been mapped appropriately, ensuring data integrity and meaning are preserved._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier of the Github label | `issue_labels.id` | 🟢 _0.90_ | *Direct match with minimal transformation needed.* |
| `_fivetran_synced` | Timestamp of the record being synced by Fivetran | `issue_labels._airbyte_extracted_at` | 🟢 _1.00_ | *Standard field for syncing timestamps, direct mapping from '_airbyte_extracted_at' to '_fivetran_synced'.* |
| `color` | The color of the label | `issue_labels.color` | 🟢 _1.00_ | *Exact match of field names and usage context.* |
| `description` | The description of the label indicating the purpose | `issue_labels.description` | 🟢 _0.90_ | *Direct correlation between descriptions in source and target, minimal semantic difference.* |
| `is_default` | Boolean flagging if the label is default on creation | `issue_labels.default` | 🟢 _0.90_ | *Boolean fields match directly between source and target, reflecting the same property.* |
| `name` | Name of the label | `issue_labels.name` | 🟢 _1.00_ | *Identical field names and purposes across both schemas.* |
| `url` | Url where the label was used | `issue_labels.url` | 🟢 _0.80_ | *High relevance and match of URLs used in both contexts, though slight differences in formatting.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
