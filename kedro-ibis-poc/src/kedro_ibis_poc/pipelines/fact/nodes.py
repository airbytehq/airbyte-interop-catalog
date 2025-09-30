"""Fact aggregation nodes."""
import ibis


def create_fct_user_purchases(
    stg_users: ibis.Table, stg_purchases: ibis.Table
) -> ibis.Table:
    """Create user purchase summary fact table."""
    user_purchases = stg_users.left_join(
        stg_purchases, stg_users.user_id == stg_purchases.user_id
    )

    return user_purchases.group_by(
        [user_purchases.user_id, user_purchases.user_name, user_purchases.email]
    ).aggregate(
        total_purchases=user_purchases.purchase_id.count(),
        first_purchase_date=user_purchases.purchase_timestamp.min(),
        last_purchase_date=user_purchases.purchase_timestamp.max(),
        total_returned=user_purchases.return_timestamp.count(),
    )


def create_fct_product_sales(
    stg_products: ibis.Table, stg_purchases: ibis.Table
) -> ibis.Table:
    """Create product sales summary fact table."""
    product_sales = stg_products.left_join(
        stg_purchases, stg_products.product_id == stg_purchases.product_id
    )

    return product_sales.group_by(
        [
            product_sales.product_id,
            product_sales.product_name,
            product_sales.price,
            product_sales.make,
            product_sales.model,
        ]
    ).aggregate(
        total_sales=product_sales.purchase_id.count(),
        total_revenue=(product_sales.price * product_sales.purchase_id.count()),
        total_returns=product_sales.return_timestamp.count(),
        first_sale_date=product_sales.purchase_timestamp.min(),
        last_sale_date=product_sales.purchase_timestamp.max(),
    )
