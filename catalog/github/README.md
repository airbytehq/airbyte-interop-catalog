# Mapping Guide: Airbyte-to-Fivetran

The below guide will help you map Airbyte schemas to corresponding Fivetran schemas. Guidance is AI-generated and includes confidence scores (with explanation) for each table and field mapping.

## Companion Project for `dbt` Users

Please see the companion [airbyte-interop-dbt-project](./airbyte-interop-dbt-project) directory, which contains a `dbt` project with ready-to-use SQL models for each of the below mappings.

## Table-Level Mappings

### How to Use these Mappings

The below guides, and the companion dbt project, will help you shape your new Airbyte datasets to more closely match your legacy Fivetran dataset schemas.

This can be helpful if:

1. You have existing code that relies on Fivetran-shaped datasets.
2. You have one or more dependencies on Fivetran-managed dbt packages.
3. You have custom code that needs to be updated to leverage Airbyte data schemas, where you previously ingested Fivetran-shaped datasets.

In any of these cases, you can use the below mapping logic to shape your new data to fit old data schema requirements and **save time** in your migration.

> ![Tip]
> Use the right-hand navigation to quickly browse available dataset mappings.

> ![Warning]
> AI-generated results may contain errors. Please sanity check results and adapt these resources to your needs accordingly.


### Mapping: Airbyte `teams` to Fivetran `team`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The table match score is relatively high, indicating a good match in the semantics of the tables. The completion score is moderate, suggesting that while the mappings cover most fields, there may be a few mismatches or missing fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the team. | `teams.id` | 🟢 _1.00_ | *Exact match found.* |
| `description` | User created description of the team. | `teams.description` | 🟢 _0.90_ | *The expression directly matches the target field name, indicating high confidence.* |
| `name` | User created name of the team. | `teams.name` | 🟢 _0.90_ | *Direct match based on field name and description.* |
| `parent_id` | Reference to the parent team. | `teams.parent` | 🟢 _0.75_ | *The match likely refers to the same concept, but additional context could confirm this assumption.* |
| `privacy` | Type of privacy permissions associated with the team. | `teams.privacy` | 🟢 _0.80_ | *Field names and descriptions suggest that this is a matching concept, despite slight differences in the attribute's specific privacy settings.* |
| `slug` | Url friendly version of the team name. | `teams.slug` | 🟢 _0.85_ | *The slug is consistently used as a URL-friendly version of a name, highly likely to match.* |

### Mapping: Airbyte `review_comments` to Fivetran `pull_request_review`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: ⚠️ _0.60_
- Summary Self-Evaluation: _The table match score is high reflecting good overall mapping of source to target schema, but completion score is reduced due to missing fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the pull request review. | `review_comments.id` | 🟢 _1.00_ | *Direct mapping exists, perfect confidence.* |
| `pull_request_id` | Foreign key that references the pull request table. | `review_comments.pull_request_review_id` | 🟢 _1.00_ | *Direct mapping exists, perfect confidence.* |
| `submitted_at` | Timestamp of when the request for review was submitted. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `state` | Whether the review was an approval, request for change, comment, dismissal. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `user_id` | Foreign key that references the user table, representing the user that reviewed the pull request. | `review_comments.user.id` | 🟢 _1.00_ | *Direct mapping exists, perfect confidence.* |

### Mapping: Airbyte `pull_requests` to Fivetran `issue_merged`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The mappings largely align well with the target schema. Most fields have clear equivalents but a few are left unmatched or imprecisely matched, leading to a slightly lower completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `issue_id` | Foreign key that references the issue table.  This table will only reference issues that are pull requests | `pull_requests.id` | 🟢 _0.90_ | *Field maps directly to a corresponding field in the target schema, indicating a strong match and relational integrity.* |
| `merged_at` | Timestamp of when the code merge took place | `pull_requests.merged_at` | 🟢 _0.95_ | *Timestamp fields align perfectly in both format and context, providing very high confidence in their mapping.* |

### Mapping: Airbyte `repositories` to Fivetran `repository`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _The table match score is high due to a good correspondence between the source and target tables, specifically in their shared fields and structure. The completion score is perfect as all fields are accounted for and mapped appropriately._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the repository. | `repositories.id` | 🟢 _1.00_ | *Direct match of field names and types, indicating a perfect mapping.* |
| `created_at` | Timestamp of when the repository was created. | `repositories.created_at` | 🟢 _1.00_ | *Direct match of field names between the schema, along with equivalent data types, signifies an accurate mapping.* |
| `full_name` | The name of the git repository. | `repositories.full_name` | 🟢 _1.00_ | *The field names and purpose align correctly between source and target, ensuring an accurate mapping.* |
| `private` | Boolean field indicating whether the repository is private (true) or public (false). | `repositories.private` | 🟢 _1.00_ | *The Boolean nature of the field is consistent across both schemas, and the field names match, ensuring a fully accurate mapping.* |

### Mapping: Airbyte `comments` to Fivetran `issue_comment`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table mapping review shows that the fields partially align with the corresponding target schema. Mappings such as 'id' and 'user_id' are directly matched, while 'issue_id' having a 'MISSING' source indicates an incomplete schema mapping._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the issue comment. | `comments.id` | 🟢 _1.00_ | *Direct match found, expression accurately maps to the target field.* |
| `issue_id` | Foreign key that references the issue table | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `user_id` | Foreign key that references the user table | `comments.user_id` | 🟢 _0.90_ | *Direct match found, expression accurately maps to the target field.* |
| `created_at` | Timestamp of when the issue comment was created. | `comments.created_at` | 🟢 _0.80_ | *Direct match found, expression accurately maps to the target field.* |

### Mapping: Airbyte `issues` to Fivetran `issue`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The mapping of source schema to target schema seems to be fairly accurate and appropriate based on field evaluations considering field relevance and correct detections of data types without mismatches. Two fields marked as 'MISSING' impacted negatively on the completion score while the overall structure and relevance yielded a higher table match score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the issue.  This is not the number that appears in the URL. | `issues.id` | 🟢 _1.00_ | *Exact match of field name and content type.* |
| `body` | The text of the main description of the issue. | `issues.body` | 🟢 _1.00_ | *Exact match of field name and content type.* |
| `locked` | Boolean indicating whether the issue is locked. | `issues.locked` | 🟢 _1.00_ | *Exact match of field name and content type.* |
| `closed_at` | Timestamp of when the issue was closed, NULL for issues that are open. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `created_at` | Timestamp of when the issue was created. | `issues.created_at` | 🟢 _1.00_ | *Exact match of field name and content type.* |
| `milestone_id` | Foreign key that references the milestone table representing the current milestone the issue is in. | `issues.milestone.id` | 🟢 _0.90_ | *Close semantic match with minor ambiguity about specific milestones referenced.* |
| `number` | The issue number within a repository.  Is unique by repository, but not across repositories. | `issues.number` | 🟢 _1.00_ | *Exact match of field name and content type.* |
| `pull_request` | Boolean for is the issue is a pull request (true) ot regular issue (false) | `issues.pull_request` | 🟢 _1.00_ | *Exact match of field name and content type.* |
| `repository_id` | Foreign key that references the repository table. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `state` | Whether the issue is open or closed. | `issues.state` | 🟢 _1.00_ | *Exact match of field name and content type.* |
| `title` | Title of the issue. | `issues.title` | 🟢 _1.00_ | *Exact match of field name and content type.* |
| `updated_at` | Timestamp of when the last update was made to the issue. | `issues.updated_at` | 🟢 _1.00_ | *Exact match of field name and content type.* |
| `user_id` | Foreign key that references the user table, representing the user that created the issue. | `issues.user.id` | 🟢 _1.00_ | *Exact match of field name and content type.* |

### Mapping: Airbyte `issue_labels` to Fivetran `label`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.86_
- Summary Self-Evaluation: _The field mappings provide a high degree of confidence in aligning the source and target schemas, with most fields closely matching in both definition and context. Only minor discrepancies were present, mainly in the mapping of one of the non-critical metadata fields._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique identifier of the Github label | `issue_labels.id` | 🟢 _1.00_ | *Direct match based on the field description and usage context.* |
| `_fivetran_synced` | Timestamp of the record being synced by Fivetran | `issue_labels._airbyte_extracted_at` | 🟢 _1.00_ | *Standard mapping for synchronization timestamps.* |
| `color` | The color of the label | `issue_labels.color` | 🟢 _0.90_ | *Clear correlation in the property names and descriptions.* |
| `description` | The description of the label indicating the purpose | `issue_labels.description` | 🟢 _0.85_ | *Both fields refer to descriptions of labels, with minor discrepancies in precise usage.* |
| `is_default` | Boolean flagging if the label is default on creation | `issue_labels.default` | 🟢 _0.80_ | *Both fields refer to a default status setting, slightly unsure if they function identically.* |
| `name` | Name of the label | `issue_labels.name` | 🟢 _0.95_ | *Direct correlation with very minor variations in context.* |
| `url` | Url where the label was used | `issue_labels.url` | 🟢 _0.70_ | *Correct link fields between the schemas, although the specific usage context might differ slightly.* |

### Mapping: Airbyte `users` to Fivetran `user`


- Table Match Confidence Score: 🟢 _0.75_
- Table Completion Score: ⚠️ _0.50_
- Summary Self-Evaluation: _The table match score is moderately high due to some field mappings being accurate, but the completion score is lower as not all fields were successfully mapped, reflecting missing key field mappings._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the user. | `users.id` | 🟢 _1.00_ | *Direct match found.* |
| `login` | The alias the user uses to login to github. | `users.login` | 🟢 _1.00_ | *Direct match found.* |
| `name` | The name of the user | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `company` | The  company of the user. | `MISSING` | ❌ _0.00_ | *No good match found.* |

### Mapping: Airbyte `pull_requests` to Fivetran `pull_request`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _This table mapping shows a high level of confidence and a reasonably complete representation of field mappings. The field-level evaluations indicate a close correlation between the source and target schema contexts, with some mappings slighty lacking perfect confidence, reflecting a cautious approach in cases of ambiguity._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | System generated unique id for the pull request. | `pull_requests.id` | 🟢 _1.00_ | *Exact match on the field designation for a unique identifier.* |
| `issue_id` | Foreign key that references the issue table. | `pull_requests.issue_url` | ⚠️ _0.65_ | *Match considered based on URL linking to issue, invoking a slight risk of referencing a different context.* |
| `head_repo_id` | Foreign key that references the repository table, referencing the current branch. | `pull_requests.head.repo_id` | 🟢 _0.70_ | *This mapping is plausible with moderate certainty given the direct reference to repository ID under a branch.* |
| `head_user_id` | Foreign key that references the user table, referencing who created the current branch. | `pull_requests.head.user_id` | 🟢 _0.70_ | *Moderately confident matching, taking into account the direct relationship to 'user_id' in a specific branch context.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
