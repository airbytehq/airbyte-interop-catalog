"""Extract pipeline definition."""
from kedro.pipeline import Pipeline, node, pipeline

from .nodes import extract_source_faker_to_raw


def create_pipeline(**kwargs) -> Pipeline:
    """Create the extract pipeline."""
    return pipeline(
        [
            node(
                func=extract_source_faker_to_raw,
                inputs=[
                    "params:source_faker.count",
                    "params:source_faker.seed",
                    "params:source_faker.parallelism",
                ],
                outputs=["raw_users", "raw_products", "raw_purchases"],
                name="extract_source_faker",
            ),
        ]
    )
