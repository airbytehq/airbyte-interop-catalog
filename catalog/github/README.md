# Generated dbt Models

This directory contains automatically generated dbt models based on mapping files.

### Mapping: Airbyte `teams` to Fivetran `team`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.83_
- Summary Self-Evaluation: _The overall table match score is relatively high, indicating a good match between the source and target schema for the teams table; however, the completion score is not perfect, suggesting that not all field mappings have a high confidence level._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the team. | `teams.id` | 🟢 _1.00_ | *Perfect match of the field identifier across both schemas* |
| `description` | User created description of the team. | `teams.description` | 🟢 _0.90_ | *Fields match closely and the description data is identical, leading to high confidence* |
| `name` | User created name of the team. | `teams.name` | 🟢 _0.90_ | *The name fields align well between the schemas, showing a high level of confidence* |
| `parent_id` | Reference to the parent team. | `teams.parent` | ⚠️ _0.60_ | *The field references the same concept, but might not be perfectly aligned, thus the lower score* |
| `privacy` | Type of privacy permissions associated with the team. | `teams.privacy` | 🟢 _0.70_ | *Privacy settings fields have acknowledged similarities but differences in details reduce the score* |
| `slug` | Url friendly version of the team name. | `teams.slug` | 🟢 _0.80_ | *Closely matching URL-friendly name for the team, high confidence* |

### Mapping: Airbyte `reviews` to Fivetran `pull_request_review`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The mappings accurately reflect the intended target schema. The fields 'id', 'pull_request_id', 'submitted_at', and 'state' are well matched with appropriate descriptions; only minor mismatches are evident, keeping confidence high. The overall table configuration suits the requirements and guidelines set for data integrity and transformation accuracy._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the pull request review. | `reviews.id` | 🟢 _1.00_ | *Exact match to 'reviews.id'.* |
| `pull_request_id` | Foreign key that references the pull request table. | `reviews.pull_request_url` | 🟢 _0.95_ | *'pull_request_id' maps to 'reviews.pull_request_url', which is the correct reference for pull requests.* |
| `submitted_at` | Timestamp of when the request for review was submitted. | `reviews.submitted_at` | 🟢 _1.00_ | *Perfect alignment with 'reviews.submitted_at' indicating accurate timestamp mapping.* |
| `state` | Whether the review was an approval, request for change, comment, dismissal. | `reviews.state` | 🟢 _1.00_ | *Correctly captures the review state with 'reviews.state'.* |
| `user_id` | Foreign key that references the user table, representing the user that reviewed the pull request. | `reviews.user.id` | 🟢 _0.90_ | *'user_id' maps to 'reviews.user.id' correctly identifying the user involved in the review though slight semantic risk exists.* |

### Mapping: Airbyte `MISSING` to Fivetran `repo_team`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table mapping has a relatively high match quality. However, the completion of field mappings is partial since some field mappings remain undefined or unestablished._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `repository_id` | Reference to the respective repository for the record. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `team_id` | Reference to the respective team for the record. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `pull_requests` to Fivetran `issue_merged`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _Both fields have plausible targets suggesting sound mappings. The '_airbyte_extracted_at' field mapping convention is used systemically, indicating the validity of 'issue_id's relation to `pull_requests`. The mapping for 'merged_at' feels a bit weak since there's no explicit context linking this to an actual merge timestamp, but it retains partial correctness as it reflects the extraction timestamp which can coincide with merge events._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `issue_id` | Foreign key that references the issue table.  This table will only reference issues that are pull requests | `pull_requests._airbyte_extracted_at` | 🟢 _0.90_ | *Good conceptual match given that this field tracks issues specifically tied to pull requests.* |
| `merged_at` | Timestamp of when the code merge took place | `pull_requests._airbyte_extracted_at` | ⚠️ _0.60_ | *Mapped due to lack of better contextual data, assumes `_airbyte_extracted_at` might reflect the time of merging which is plausible but not guaranteed.* |

### Mapping: Airbyte `comments` to Fivetran `issue_comment`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table match score indicates a moderate confidence in the alignment, as fields generally correspond well in functionality though not perfectly. However, the 'issue_id' field lacks a direct counterpart, impacting the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the issue comment. | `comments.id` | 🟢 _1.00_ | *Direct match found: 'comments.id' matches 'id' perfectly.* |
| `issue_id` | Foreign key that references the issue table | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `user_id` | Foreign key that references the user table | `comments.user.id` | 🟢 _0.90_ | *High confidence match: 'comments.user.id' closely matches to 'user_id'.* |
| `created_at` | Timestamp of when the issue comment was created. | `comments.created_at` | 🟢 _1.00_ | *Direct match found: 'comments.created_at' matches 'created_at' perfectly.* |

### Mapping: Airbyte `issues` to Fivetran `issue`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _High confidence in table matching due to alignment of key structural elements and data types across fields. The majority of fields have strong and meaningful mappings, only a few fields have weaker correlations which affect the completion score slightly._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the issue.  This is not the number that appears in the URL. | `issues.id` | 🟢 _1.00_ | *Direct and clear mapping, unique identifier matched perfectly.* |
| `body` | The text of the main description of the issue. | `issues.body` | 🟢 _0.95_ | *Direct mapping, textual content aligns closely with the target schema requirements.* |
| `locked` | Boolean indicating whether the issue is locked. | `issues.locked` | 🟢 _1.00_ | *Direct mapping of boolean type, perfectly aligns with data expectations.* |
| `closed_at` | Timestamp of when the issue was closed, NULL for issues that are open. | `issues.closed_at` | 🟢 _0.95_ | *Timestamps directly match; slight deduction for potential format differences.* |
| `created_at` | Timestamp of when the issue was created. | `issues.created_at` | 🟢 _1.00_ | *Exact match for creation timestamp.* |
| `milestone_id` | Foreign key that references the milestone table representing the current milestone the issue is in. | `issues.milestone.id` | 🟢 _0.85_ | *Direct reference to milestone is matched, slight ambiguity in potential milestone structures across schemas.* |
| `number` | The issue number within a repository.  Is unique by repository, but not across repositories. | `issues.number` | 🟢 _0.90_ | *Issue number is unique within repositories, generally aligns well but slight penalty due to potential inter-repository uniqueness conflicts.* |
| `pull_request` | Boolean for is the issue is a pull request (true) ot regular issue (false) | `issues.pull_request` | 🟢 _1.00_ | *Boolean flag directly matches, distinguishing between pull requests and issues accurately.* |
| `repository_id` | Foreign key that references the repository table. | `issues.repository_id` | 🟢 _1.00_ | *Perfect match of repository identifiers.* |
| `state` | Whether the issue is open or closed. | `issues.state` | 🟢 _0.95_ | *State values (open/closed) match closely, minimal chance for misinterpretation.* |
| `title` | Title of the issue. | `issues.title` | 🟢 _0.95_ | *Direct textual match, representing the issue effectively.* |
| `updated_at` | Timestamp of when the last update was made to the issue. | `issues.updated_at` | 🟢 _0.95_ | *Timestamp matches with potential minor deviation in time recording.* |
| `user_id` | Foreign key that references the user table, representing the user that created the issue. | `issues.user.id` | 🟢 _0.85_ | *Direct user identifier match, slight risk due to different user representation potentially across data sources.* |

### Mapping: Airbyte `issue_labels` to Fivetran `label`


- Table Match Confidence Score: 🟢 _0.95_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _The mapping for table 'issue_labels' from source to target is highly accurate, with all fields properly accounted for._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier of the Github label | `issue_labels.id` | 🟢 _1.00_ | *Direct match on primary identifier fields.* |
| `_fivetran_synced` | Timestamp of the record being synced by Fivetran | `issue_labels._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for synchronization fields.* |
| `color` | The color of the label | `issue_labels.color` | 🟢 _1.00_ | *Direct match based on identical property names and purposes.* |
| `description` | The description of the label indicating the purpose | `issue_labels.description` | 🟢 _1.00_ | *Direct match, both serve as descriptives for the label purpose.* |
| `is_default` | Boolean flagging if the label is default on creation | `issue_labels.default` | 🟢 _1.00_ | *Exact match of default status fields.* |
| `name` | Name of the label | `issue_labels.name` | 🟢 _1.00_ | *Direct match with identical naming and usage.* |
| `url` | Url where the label was used | `issue_labels.url` | 🟢 _1.00_ | *Direct URL mapping, both refer to the location of usage.* |

### Mapping: Airbyte `users` to Fivetran `user`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table match score is high indicating a good correlation between source and target tables. However, the completion score is lower due to missing field mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the user. | `users.id` | 🟢 _1.00_ | *Direct match found: 'users.id' matches 'id'.* |
| `login` | The alias the user uses to login to github. | `users.login` | 🟢 _1.00_ | *Direct match found: 'users.login' matches 'login'.* |
| `name` | The name of the user | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `company` | The  company of the user. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `pull_requests` to Fivetran `pull_request`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The quality of table matching is high given the tightly related field mappings, showing strong subject matter similarity. The completion score reflects a mostly populated mapping but is not full due to some fields with 'MISSING' expressions._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the pull request. | `pull_requests.id` | 🟢 _1.00_ | *Direct match found with identical field names and purposes.* |
| `issue_id` | Foreign key that references the issue table. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `head_repo_id` | Foreign key that references the repository table, referencing the current branch. | `pull_requests.head.repo_id` | 🟢 _0.70_ | *Good match, referencing the current branch's repository. Close contextual alignment despite nested path.* |
| `head_user_id` | Foreign key that references the user table, referencing who created the current branch. | `pull_requests.head.user_id` | 🟢 _0.70_ | *Good match, referencing the creator of the current branch's user ID. Close contextual alignment despite nested path.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
