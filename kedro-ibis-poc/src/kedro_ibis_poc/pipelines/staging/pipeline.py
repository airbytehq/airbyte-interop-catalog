"""Staging pipeline definition."""
from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_stg_products, create_stg_purchases, create_stg_users


def create_pipeline(**kwargs) -> Pipeline:
    """Create the staging pipeline."""
    return pipeline(
        [
            node(
                func=create_stg_users,
                inputs="raw_users",
                outputs="stg_users",
                name="stage_users",
            ),
            node(
                func=create_stg_products,
                inputs="raw_products",
                outputs="stg_products",
                name="stage_products",
            ),
            node(
                func=create_stg_purchases,
                inputs="raw_purchases",
                outputs="stg_purchases",
                name="stage_purchases",
            ),
        ]
    )
