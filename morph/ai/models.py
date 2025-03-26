"""Models for AI-related functionality."""

from pydantic import BaseModel


class NoConfidenceChoice(BaseModel):
    """Represents a choice to not make a selection.

    This is used instead of choosing a specific source schema, because the AI
    does not have any good options to choose from.
    """

    reason: str
    """Explanation of why the AI did not make a selection."""

    bad_choice_if_forced: str | None = None
    """The next-best path to take if the user forces a selection."""


class DbtSourceColumn(BaseModel):
    """Represents a column in a source table schema."""

    name: str
    """The name of the column."""

    description: str | None = None
    """A description of the column."""

    data_type: str
    """The data type of the column."""


class DbtSourceTable(BaseModel):
    """Represents a source table schema in a dbt project."""

    name: str
    """The name of the table."""

    description: str | None = None
    """A description of the table."""

    columns: list[DbtSourceColumn]
    """The columns in the table."""


class FieldMapping(BaseModel):
    """Represents a field mapping with its properties."""

    name: str
    """The name of the field."""

    expression: str | bool | float | int
    """The expression used to generate the field.

    The text `MISSING` is used to indicate that the field is not mapped to any field in the source.
    """

    description: str | None = None
    """A description of the field."""


class MappingConfidence(BaseModel):
    """Represents the confidence score and explanation for a mapping."""

    score: float
    """The confidence score for the mapping."""

    explanation: str
    """An explanation of the confidence score."""

    field_scores: dict[str, float]
    """A dictionary of field names and their confidence scores."""
