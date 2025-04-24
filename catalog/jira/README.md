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

> [!Tip]
> Use the right-hand navigation to quickly browse available dataset mappings.

> [!Warning]
> AI-generated results may contain errors. Please sanity check results and adapt these resources to your needs accordingly.


### Mapping: Airbyte `projects` to Fivetran `project`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: ⚠️ _0.57_
- Summary Self-Evaluation: _The table match is moderately confident due to consistent naming and contextual overlap, but the completion score is lowered by two 'MISSING' mappings which indicate incomplete data correspondence._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the project. | `projects.id` | 🟢 _1.00_ | *Direct match on naming and usage context.* |
| `description` | Description of the project, if given. | `projects.description` | 🟢 _1.00_ | *Direct match on naming and usage context.* |
| `key` | UI-facing ID of the project. This becomes the default prefix for tasks created within this project. | `projects.key` | 🟢 _1.00_ | *Direct match on naming and usage context.* |
| `lead_id` | Foreign key referencing the ID of the `user` who leads this project. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `name` | Title of the project. | `projects.name` | 🟢 _1.00_ | *Direct match on naming and usage context.* |
| `permission_scheme_id` | Foreign key referencing the ID of the `permission_scheme` that the project ascribes to. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `project_category_id` | Foreign key referencing the ID of the `project_category` that the project is associated with, if any. | `projects.projectCategory` | 🟢 _1.00_ | *Direct match on naming and usage context.* |
| `project_type_key` | ID of the type of project (ie 'software'). | `projects.projectTypeKey` | 🟢 _0.70_ | *Moderate confidence due to partial match of wording and use case, although there might be contextually different uses in different systems.* |

### Mapping: Airbyte `project_components` to Fivetran `component`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping between project_components and a similar schema is highly aligned with a small disparity in field completeness._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | ID of the component. | `project_components.id` | 🟢 _1.00_ | *Direct match found for 'id' as 'project_components.id'.* |
| `description` | Description given to the component. | `project_components.description` | 🟢 _0.95_ | *Direct match found for 'description' as 'project_components.description', aligning perfectly with the schema requirement.* |
| `name` | UI-facing name of the component. | `project_components.name` | 🟢 _0.90_ | *Direct mapping located for 'name' as 'project_components.name', fitting well within schema requirements.* |
| `project_id` | Foreign key referencing the id of the component's `project`. | `project_components.projectId` | 🟢 _0.70_ | *Mapped 'project_id' to 'project_components.projectId', likely same due to context but presence of 'project' in both field names indicates a close but not perfect match.* |

### Mapping: Airbyte `workflow_status_categories` to Fivetran `status_category`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _Mapping confidence is moderately high with some matching issues due to possibly differing meanings, though the fields 'id' and 'name' are well aligned with respective schema requirements. 70% confidence is based on the possibility that 'id' and 'name' correctly correspond to target schema fields, but there remains some uncertainty._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the status category. | `workflow_status_categories.id` | 🟢 _0.70_ | *The 'id' from 'workflow_status_categories.id' matches standard ID conventions in the target schema, though exact table match cannot be fully confirmed.* |
| `name` | Title of the status category. | `workflow_status_categories.name` | 🟢 _0.70_ | *The 'name' mapping from 'workflow_status_categories.name' aligns well by naming convention, suggesting a proper descriptor role in the target schema.* |

### Mapping: Airbyte `issue_priorities` to Fivetran `priority`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.70_
- Summary Self-Evaluation: _The field mappings are close and compatible with the target schema, and most source fields have been successfully mapped, suggesting a high degree of confidence in the table match._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the priority level. | `issue_priorities.id` | 🟢 _0.90_ | *Direct mapping of 'issue_priorities.id' to 'id' with perfect structural and semantic alignment.* |
| `description` | Description of the priority level. | `issue_priorities.description` | 🟢 _0.90_ | *Direct mapping of 'issue_priorities.description' to 'description' ensures semantic integrity maintained.* |
| `name` | Name of the priority as it appears in the UI. | `issue_priorities.name` | 🟢 _0.90_ | *Direct mapping of 'issue_priorities.name' to 'name' accurately reflects the UI representation.* |

### Mapping: Airbyte `sprints` to Fivetran `sprint`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The table match score is high, indicating a strong match between the source and target tables. The completion score reflects that most fields are accurately mapped, although there are some fields not perfectly aligned._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the sprint. | `sprints.id` | 🟢 _1.00_ | *Exact match on field names and description.* |
| `board_id` | Foreign key referencing the ID of the `board` that the sprint lives in. | `sprints.boardId` | 🟢 _1.00_ | *Fields directly match by description and name alignment.* |
| `complete_date` | Timestamp of when the sprint was completed. | `sprints.completeDate` | 🟢 _0.95_ | *High confidence match due to identical column naming conventions and compatible data format.* |
| `end_date` | Timestamp of when the sprint is planned to end. | `sprints.endDate` | 🟢 _0.95_ | *High confidence due to identical definitions across schemas.* |
| `name` | Title of the sprint. | `sprints.name` | 🟢 _1.00_ | *Direct match on field name with exact alignment in meaning.* |
| `start_date` | Timestamp of when the sprint began. | `sprints.startDate` | 🟢 _0.90_ | *The field names are nearly identical, and descriptions suggest the same usage scenario.* |

### Mapping: Airbyte `issue_comments` to Fivetran `comment`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.95_
- Summary Self-Evaluation: _Given the matching criteria and the context provided, the table match and individual field mapping scores indicate a high confidence that the source and target data are describing the same entities. The individual fields have been carefully matched with consideration for potential variances in meaning, ensuring a robust mapping configuration._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the comment. | `issue_comments.id` | 🟢 _1.00_ | *Direct match on the unique identifier for both source and target schemas.* |
| `author_id` | Foreign key referencing the `user` id of the comment's author. | `issue_comments.author` | 🟢 _0.95_ | *The 'author' closely corresponds to the author_id in the target schema, highly suggesting that these are the same fields.* |
| `body` | Content of the comment. | `issue_comments.body` | 🟢 _0.90_ | *Direct match, text content of comments aligns exactly between source and target.* |
| `created` | Timestamp of when the comment was created. | `issue_comments.created` | 🟢 _0.90_ | *Timestamp for creation matches perfectly across the schemas.* |
| `is_public` | Boolean that is true if the comment is visible to all users. | `issue_comments.jsdPublic` | 🟢 _0.80_ | *The expression 'issue_comments.jsdPublic' and the target 'is_public' likely refer to the same concept with high certainty, despite slight naming variations.* |
| `issue_id` | Foreign key referencing the id of the `issue` that was commented on. | `issue_comments.issueId` | 🟢 _0.95_ | *Clearly the same concept, referring to the issue which the comments are linked to in both schemas.* |
| `update_author_id` | Foreign key referencing the id of the `user` who last updated this comment. | `issue_comments.updateAuthor` | 🟢 _0.95_ | *High probability of match as both refer to the id of the user last updating the comment.* |
| `updated` | Timestamp of when the comment was last updated. | `issue_comments.updated` | 🟢 _0.90_ | *Timestamp fields clearly align, indicating they are identical intents in both schemas.* |

### Mapping: Airbyte `issue_custom_field_options` to Fivetran `issue_field_history`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The mappings show a strong correlation between the source and target schemas, with good recognition of key fields. However, one crucial field mapping (`issue_id`) is missing, leading to a deduction in the completion score._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `field_id` | Foreign key referencing the ID of the `field` that was changed. | `issue_custom_field_options.fieldId` | 🟢 _0.90_ | *Correct mapping of `field_id` to `issue_custom_field_options.fieldId`.* |
| `issue_id` | Foreign key referencing the ID of the `issue` whose field was updated. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `time` | Timestamp of when the issue field was set to this value. | `issue_custom_field_options._airbyte_extracted_at` | 🟢 _1.00_ | *Perfect match of `time` to `issue_custom_field_options._airbyte_extracted_at` as per standard practices.* |
| `value` | Content of the value of that the field was set to. | `issue_custom_field_options.value` | 🟢 _0.80_ | *Strong match of `value` to `issue_custom_field_options.value`, aligning data context appropriately.* |

### Mapping: Airbyte `project_versions` to Fivetran `version`


- Table Match Confidence Score: 🟢 _0.95_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table mapping configuration evaluates to a high level of confidence with field mappings closely matching their intended targets, well-aligned semantic meanings, and no major mismatches identified._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `archived` | Boolean that is true if the project version has been archived. | `project_versions.archived` | 🟢 _0.70_ | *Direct match with consistent naming and meaning.* |
| `description` | The optional description given to the version. | `project_versions.description` | 🟢 _0.90_ | *Direct match, very high confidence in mapping.* |
| `id` | Unique ID of the version. | `project_versions.id` | 🟢 _1.00_ | *Perfect identifier match.* |
| `name` | Unique name of the version. | `project_versions.name` | 🟢 _1.00_ | *Perfect name alignment.* |
| `overdue` | Boolean that is true if the version is past its optional release date, false if it is not or if it does not have a due date. | `project_versions.overdue` | 🟢 _0.80_ | *Good semantic match, close field descriptions.* |
| `project_id` | Foreign key referencing the `PROJECT` to which this version is attached. | `project_versions.projectId` | 🟢 _0.90_ | *High confidence, straightforward foreign key mapping.* |
| `release_date` | The optional release date of the version. Expressed in ISO 8601 format (yyyy-mm-dd). | `project_versions.releaseDate` | 🟢 _0.70_ | *Date formatting aligns well, good semantic match.* |
| `released` | Boolean that is true if the version has been released. If the version is released a request to release again is ignored | `project_versions.released` | ⚠️ _0.60_ | *Sufficient semantic match despite potential ambiguity.* |
| `start_date` | The start date of the version. Expressed in ISO 8601 format (yyyy-mm-dd). | `project_versions.startDate` | 🟢 _0.70_ | *Aligns well in terms of date formatting and relevancy.* |

### Mapping: Airbyte `issue_types` to Fivetran `issue_type`


- Table Match Confidence Score: 🟢 _0.90_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table match score is high due to the strong mapping between the source and target schemas. However, the completion score is slightly lower as not all source fields have been populated perfectly._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the issue type. | `issue_types.id` | 🟢 _1.00_ | *Perfect match for identity column.* |
| `description` | Project-level description given to the issue type. | `issue_types.description` | 🟢 _0.80_ | *Good lexical match for descriptive fields.* |
| `name` | Name of the issue type (ie Epic, Task, Subtask, any custom types) | `issue_types.name` | 🟢 _0.90_ | *Exact textual match with very clear meaning alignment.* |
| `subtask` | Boolean that is true if this type of issue is a subtask. | `issue_types.subtask` | 🟢 _1.00_ | *Direct and clear corresponding boolean field with identical purpose.* |

### Mapping: Airbyte `issue_resolutions` to Fivetran `resolution`


- Table Match Confidence Score: 🟢 _0.70_
- Table Completion Score: 🟢 _0.90_
- Summary Self-Evaluation: _The table match score is high as the source and target tables appear to describe the same type of information about issue resolutions. Completion score is good, reflecting the complete mapping of all major fields which hold significant information and meaning between the source and target schemes. The given expressions map directly to the source fields, ensuring a high integrity of data translation._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the resolution type. | `issue_resolutions.id` | 🟢 _1.00_ | *Perfect direct mapping from 'issue_resolutions.id' to 'id' with exact field name match and alignment in meaning.* |
| `description` | Description given to the resolution. | `issue_resolutions.description` | 🟢 _1.00_ | *Direct mapping from 'issue_resolutions.description' to 'description'. The expressions and meanings are identical.* |
| `name` | Display name of the resolution. | `issue_resolutions.name` | 🟢 _1.00_ | *Direct mapping from 'issue_resolutions.name' to 'name'. The field names and meanings align perfectly.* |

### Mapping: Airbyte `issues` to Fivetran `issue`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _0.80_
- Summary Self-Evaluation: _The target schema closely reflects the source schema with minor differences in field serialization and naming conventions. Most fields are mapped accurately, though some are marked as 'MISSING' due to lack of exact correspondence. The understanding of the project context and additional mapping instructions has been pivotal in generating precise mappings and providing reasonable confidence levels._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the issue. | `issues.id` | 🟢 _1.00_ | *Direct match found with precise correlation.* |
| `_fivetran_deleted` | Boolean that is true if the row has been soft-deleted from the source. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `assignee` | Foreign key referencing the ID of the `user` currently assigned to this task. | `issues.fields.assignee.accountId` | 🟢 _0.80_ | *Nested identifiers match correctly with the project schema.* |
| `created` | Timestamp of when the issue was created (in UTC). | `issues.fields.created` | 🟢 _0.90_ | *Direct and precise mapping of timestamp fields.* |
| `creator` | Foreign key referencing the `user` who first created the issue. Cannot be changed. | `issues.fields.creator.accountId` | 🟢 _0.80_ | *Foreign key relation mapped with high confidence.* |
| `description` | The issue description, if given. | `issues.fields.description.content` | 🟢 _0.70_ | *Content descriptor matches well within contextual boundaries.* |
| `due_date` | Calendar day on which the issue is due, if a due date is provided. | `issues.fields.duedate` | 🟢 _0.90_ | *Field matches directly to the target date field, highly accurate.* |
| `environment` | Text field describing the environment in which the issue occurred (ie "IE9 on Windows 7"). | `issues.fields.environment` | 🟢 _0.70_ | *Broad match, acceptable within similar applications.* |
| `issue_type` | Foreign key referencing the ID of the `issue_type`. | `issues.fields.issuetype.id` | 🟢 _0.70_ | *ID matching provides reasonable assurance of proper mapping.* |
| `key` | UI-facing id of the issue. | `issues.key` | 🟢 _1.00_ | *Identifiers match perfectly.* |
| `last_viewed` | Timestamp of when the user who set up the connector last viewed the issue. | `issues.fields.lastViewed` | 🟢 _0.90_ | *Timestamp fields align directly.* |
| `original_estimate` | The original estimate of how long working on this issue would take, in seconds. | `issues.fields.timeoriginalestimate` | 🟢 _0.90_ | *Time-related fields match appropriately with validating units.* |
| `parent_id` | Self-referencing ID of the parent `issue`. | `MISSING` | ❌ _0.00_ | *No good match found.* |
| `priority` | Foreign key referencing the ID of the issue's current `priority`. | `issues.fields.priority.id` | 🟢 _0.80_ | *Direct match with source data ensuring the integrity of priority linkage.* |
| `project` | Foreign key referencing the ID of the `project` that the issue belongs to. | `issues.fields.project.id` | 🟢 _0.80_ | *Direct match of foreign key references ensures accurate project mapping.* |
| `remaining_estimate` | The estimate of how much longer working on this issue will take, in seconds. | `issues.fields.timeestimate` | 🟢 _0.90_ | *The correlation between estimated time fields is high due to similar units and naming conventions.* |
| `reporter` | Foreign key referencing the ID of the `user` who reported the issue. This differs from the `creator` column  in that the reporter can be changed in-app.  | `issues.fields.reporter.accountId` | 🟢 _0.75_ | *Foreign key references match but with lesser confidence than creator.* |
| `resolution` | Foreign key referencing the ID of the issue's type of `resolution`. | `issues.fields.resolution.id` | 🟢 _0.70_ | *The type and ID fields correspond reasonably well.* |
| `resolved` | Timestamp of when the issue was resolved (ie completed, marked as duplicate). If an  issue is marked as un-resolved, this is null.  | `issues.fields.resolutiondate` | 🟢 _0.90_ | *Resolved dates match precisely between source and target.* |
| `status` | Foreign key referencing the ID of the issue's `status` (the step that the issue is currently at  in the project's workflow).  | `issues.fields.status.id` | 🟢 _0.70_ | *Matching status identifiers with high relevance to the workflow states.* |
| `status_category_changed` | Timestamp of when the status was last changed. | `issues.fields.statuscategorychangedate` | 🟢 _0.90_ | *Timestamp for status changes align closely between the models.* |
| `summary` | Title of the issue. | `issues.fields.summary` | 🟢 _1.00_ | *Exact match of issue titles.* |
| `time_spent` | The time that was spent working on this issue, in seconds. | `issues.fields.timespent` | 🟢 _0.90_ | *Time logging fields align perfectly.* |
| `updated` | Timestamp of when the issue was last updated in some way. | `issues.fields.updated` | 🟢 _0.90_ | *Update timestamps correlate directly between source and target.* |
| `work_ratio` | The percentage of work that has been logged against the issue (time_spent) vs the original estimate of worktime. Equals -1.0 when the fields required for calculation are not provided.  | `issues.fields.workratio` | ⚠️ _0.60_ | *Approximated mapping based on available data calculations.* |

### Mapping: Airbyte `workflow_statuses` to Fivetran `status`


- Table Match Confidence Score: 🟢 _0.80_
- Table Completion Score: 🟢 _0.75_
- Summary Self-Evaluation: _The table mapping shows strong correlation among the mentioned fields aligning nicely with the target schema, with good coverage but with some fields having ambiguous mappings not fully covered._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the project status. | `workflow_statuses.id` | 🟢 _1.00_ | *Exact match of ID fields, perfect mapping.* |
| `description` | Description of the project status. Different projects may all have a status called "Backlog", but their definitions  of "backlog" may differ.  | `workflow_statuses.description` | 🟢 _0.90_ | *Good match in descriptions, slight differences might be present in context but not significant.* |
| `name` | Title of the status. | `workflow_statuses.name` | 🟢 _1.00_ | *Exact match of Name fields, clear mapping.* |
| `status_category_id` | Foreign key referencing the ID of the `status_category` that this project status falls under. | `workflow_statuses.statusCategory.id` | 🟢 _0.70_ | *Correct alignment based on foreign key relationship, although requires additional context to ensure accuracy.* |

### Mapping: Airbyte `users` to Fivetran `user`


- Table Match Confidence Score: 🟢 _0.85_
- Table Completion Score: 🟢 _1.00_
- Summary Self-Evaluation: _Overall, the mappings provided are both comprehensive and accurately matched to relevant fields. Each field from the source aligns closely with the intended target mapping, ensuring data integrity and meaning are maintained._

| Field | Description | Expression | Confidence | Evaluation |
| --- | --- | --- | --- | --- |
| `id` | Unique ID of the user. | `users.accountId` | 🟢 _1.00_ | *Perfect one-to-one mapping of unique identifiers.* |
| `email` | Email associated with the user account. | `users.emailAddress` | 🟢 _1.00_ | *Direct correspondence between user emails.* |
| `locale` | The Java locale of the user. | `users.locale` | 🟢 _0.95_ | *Locale settings matched exactly, minor considerations for format differences.* |
| `name` | Name of the user as it appears in the UI. | `users.name` | 🟢 _0.95_ | *Names are mapped directly and effectively.* |
| `time_zone` | The user's timezone, as defined in their settings. | `users.timeZone` | 🟢 _0.95_ | *Timezone data matched with high confidence.* |
| `username` | Account username. | `users.key` | 🟢 _0.90_ | *Username keys are matched, slight ambiguity in term usage but highly likely to be correct.* |

See [Rejected Mappings](./rejected_mappings.md) for mappings that did not meet approval criteria.
