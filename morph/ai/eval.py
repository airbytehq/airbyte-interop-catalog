"""Mapping confidence evaluation using Instructor AI."""

from instructor import OpenAISchema
from pydantic import BaseModel, Field
from openai import OpenAI
import instructor


class FieldMapping(BaseModel):
    """Represents a field mapping with its properties."""

    name: str
    expression: str | bool | float | int
    description: str | None = None
    tests: list[dict[str, str]] | None = None


class MappingConfidence(OpenAISchema):
    """Represents the confidence score and explanation for a mapping."""

    score: float = Field(description="Overall confidence score between 0.00 and 1.00")
    explanation: str = Field(description="Detailed explanation of the confidence score")
    field_scores: dict[str, float] = Field(description="Individual confidence scores per field")


def get_mapping_confidence(
    mappings: list[dict],
) -> MappingConfidence:
    """Get confidence score for a mapping configuration.

    Args:
        fields: List of field mappings

    Returns:
        MappingConfidence object with confidence score and explanation

    Raises:
        Exception: If all retries fail
    """
    field_mappings = [FieldMapping(**mapping) for mapping in mappings]
    client = instructor.from_openai(OpenAI())
    prompt = generate_eval_prompt(field_mappings)
    
    # TODO: We should enforce "strict" mode here, so that the LLM always generates valid JSON output.
    # For now, we retry because the AI is not always reliable at generating the JSON output.
    max_retries = 5
    latest_exception = None
    
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                model="gpt-4",  # Choose appropriate model
                response_model=MappingConfidence,
                messages=[
                    {"role": "user", "content": prompt}
                ],
            )
        except Exception as e:
            latest_exception = e
            if attempt == max_retries - 1:  # Last attempt
                raise Exception(
                    f"Failed to evaluate mapping confidence after {max_retries} attempts"
                ) from e
    
    if latest_exception:
        raise latest_exception
    
    # This should never happen due to the exception handling above
    raise Exception("Failed to evaluate mapping confidence")


def generate_eval_prompt(field_mappings: list[FieldMapping]) -> str:
    """Generate a prompt for the LLM to evaluate field mappings.
    
    Args:
        field_mappings: List of field mappings to evaluate
        
    Returns:
        String prompt for the LLM
    """
    mappings_str = "\n".join([
        f"Field: {mapping.name}\n"
        f"Expression: {mapping.expression}\n"
        f"Description: {mapping.description or 'None'}\n"
        for mapping in field_mappings
    ])
    
    return f"""Evaluate the confidence of the following field mappings:

{mappings_str}

Provide a confidence score between 0.00 and 1.00 for each field mapping, where:
- 0.00 means no confidence (the expression doesn't match the field description at all)
- 1.00 means complete confidence (the expression perfectly matches the field description)

Also provide an overall confidence score and explanation for the entire mapping configuration.
"""
