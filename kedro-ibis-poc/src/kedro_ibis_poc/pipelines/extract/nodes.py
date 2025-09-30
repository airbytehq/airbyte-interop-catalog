"""Extract nodes using PyAirbyte."""
import airbyte as ab
import ibis


def extract_source_faker_to_raw(
    count: int, seed: int, parallelism: int
) -> tuple[ibis.Table, ibis.Table, ibis.Table]:
    """Extract data from source-faker and return as Ibis tables."""
    source = ab.get_source(
        "source-faker",
        config={
            "count": count,
            "seed": seed,
            "parallelism": parallelism,
            "always_updated": False,
        },
        install_if_missing=True,
    )

    result = source.read()

    users = ibis.memtable(result["users"].to_pandas())
    products = ibis.memtable(result["products"].to_pandas())
    purchases = ibis.memtable(result["purchases"].to_pandas())

    return users, products, purchases
