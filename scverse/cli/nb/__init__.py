from functools import partial

from typing import cast

from ..aliased_group import AliasedGroup
from ..base import cli
from ..command import command


def nb():
    """Notebook-CRUD TileDB-Cloud commands for the `scverse-ml-workshop-2024` namespace."""
    pass


nb = cast(AliasedGroup, cli.group(cls=AliasedGroup)(nb))
cmd = partial(command, nb)


# Register `nb` subcommands
from . import cp, get, ls, md, put, rm, set_defaults
