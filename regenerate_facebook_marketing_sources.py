"""Script to regenerate Facebook Marketing dbt sources file with normalized field names."""

from pathlib import Path

from morph.constants import HEADER_COMMENT
from morph.models import DbtSourceFile
from morph.utils import text_utils

catalog_file = Path("/home/ubuntu/repos/morph/catalog/facebook_marketing/generated/airbyte-catalog.json")
output_file = Path("/home/ubuntu/repos/morph/catalog/facebook_marketing/generated/src_airbyte_facebook_marketing_new.yml")

dbt_file = DbtSourceFile.from_airbyte_catalog_json(
    catalog_file=catalog_file,
    source_name="facebook_marketing",
)

sources_yml = dbt_file.to_dict()
sources_yml_with_header = f"{HEADER_COMMENT}\n{text_utils.dump_yaml_str(sources_yml)}"

output_file.write_text(sources_yml_with_header)
print(f"Generated dbt sources file at {output_file}")
