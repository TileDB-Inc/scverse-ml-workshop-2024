from ..aliased_group import AliasedGroup
from ..base import cli


@cli.group(cls=AliasedGroup)
def nb():
    """Notebook-CRUD TileDB-Cloud commands for the `scverse-ml-workshop-2024` namespace."""
    pass


