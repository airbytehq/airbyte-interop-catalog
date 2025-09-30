"""Fact pipeline definition."""
from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_fct_product_sales, create_fct_user_purchases


def create_pipeline(**kwargs) -> Pipeline:
    """Create the fact aggregation pipeline."""
    return pipeline(
        [
            node(
                func=create_fct_user_purchases,
                inputs=["stg_users", "stg_purchases"],
                outputs="fct_user_purchases",
                name="aggregate_user_purchases",
            ),
            node(
                func=create_fct_product_sales,
                inputs=["stg_products", "stg_purchases"],
                outputs="fct_product_sales",
                name="aggregate_product_sales",
                ),
        ]
    )
