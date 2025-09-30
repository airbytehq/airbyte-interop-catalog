"""Staging transformation nodes."""
import ibis


def create_stg_users(raw_users: ibis.Table) -> ibis.Table:
    """Transform raw users to staging."""
    return raw_users.select(
        raw_users.id.name("user_id"),
        raw_users.name.name("user_name"),
        raw_users.email,
        raw_users.address,
        raw_users.occupation,
        raw_users.gender,
        raw_users.age,
        raw_users.created_at,
        raw_users.updated_at,
    )


def create_stg_products(raw_products: ibis.Table) -> ibis.Table:
    """Transform raw products to staging."""
    return raw_products.select(
        raw_products.id.name("product_id"),
        raw_products.name.name("product_name"),
        raw_products.price.cast("decimal(10,2)").name("price"),
        raw_products.year,
        raw_products.make,
        raw_products.model,
        raw_products.created_at,
        raw_products.updated_at,
    )


def create_stg_purchases(raw_purchases: ibis.Table) -> ibis.Table:
    """Transform raw purchases to staging."""
    return raw_purchases.select(
        raw_purchases.id.name("purchase_id"),
        raw_purchases.user_id,
        raw_purchases.product_id,
        raw_purchases.purchased_at.name("purchase_timestamp"),
        raw_purchases.returned_at.name("return_timestamp"),
        raw_purchases.added_to_cart_at.name("cart_timestamp"),
        raw_purchases.created_at,
    )
