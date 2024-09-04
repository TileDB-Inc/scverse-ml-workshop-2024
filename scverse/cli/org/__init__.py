import json
from click import argument, pass_context
from functools import partial
from tiledb import cloud
from tiledb.cloud.client import client, user_profile
from tiledb.cloud.rest_api import UserApi
from typing import cast

from scverse.cli.aliased_group import AliasedGroup
from scverse.cli.base import cli, namespace_opt, compact_opt
from scverse.cli.command import command


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


@cmd(no_args_is_help=False)
@compact_opt
def users(compact, namespace):
    """List users in a TileDB-Cloud organization."""
    org = cloud.organization(namespace)
    users = [
        user.to_dict()
        for user in org.users
    ]
    json_kwargs = dict() if compact else dict(indent=2)
    print(json.dumps(users, **json_kwargs))


@cmd(no_args_is_help=False)
@compact_opt
@argument('username', required=False)
def user(compact, username):
    """Show a TileDB-Cloud user."""
    if username:
        user = client.build(UserApi).get_user_with_username(username)
    else:
        user = user_profile()
    json_kwargs = dict() if compact else dict(indent=2)
    print(json.dumps(user.to_dict(), **json_kwargs))
