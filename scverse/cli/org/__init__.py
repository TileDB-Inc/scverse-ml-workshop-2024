from click import argument, pass_context
from functools import partial
from tiledb import cloud
from tiledb.cloud.client import client, user_profile
from tiledb.cloud.rest_api import UserApi
from typing import cast

from scverse.cli.aliased_group import AliasedGroup
from scverse.cli.base import cli
from scverse.cli.command import command, json_output


@cli.group(cls=AliasedGroup)
@pass_context
def org(ctx):
    """Manage a TileDB-Cloud organization / namespace."""
    if ctx.invoked_subcommand is None:
        ctx.invoke(show)


org = cast(AliasedGroup, org)
cmd = partial(command, org)


@cmd('info', no_args_is_help=False)
def show(namespace):
    """Print a TileDB-Cloud organization."""
    print(cloud.organization(namespace))
