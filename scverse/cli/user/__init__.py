from click import argument, pass_context
from functools import partial
from tiledb import cloud
from tiledb.cloud.client import client, user_profile
from tiledb.cloud.rest_api import UserApi
from typing import cast
from utz import err

from scverse.cli.aliased_group import AliasedGroup
from scverse.cli.base import cli, role_opt, src_nb_opt, image_opt, region_opt, size_opt
from scverse.cli.command import command, json_output
from scverse.cli import invite
from scverse.cli.nb.cp import cp as nb_cp
from scverse.cli.nb.set_defaults import set_defaults as nb_set_defaults


@cli.group(cls=AliasedGroup)
@pass_context
def user(ctx):
    """Manage a scverse TileDB-Cloud user."""
    if ctx.invoked_subcommand is None:
        ctx.invoke(show)


user = cast(AliasedGroup, user)
cmd = partial(command, user)


@cmd(no_args_is_help=False)
@json_output
@argument('username', required=False)
def show(username):
    """Show a TileDB-Cloud user."""
    if username:
        user = client.build(UserApi).get_user_with_username(username)
    else:
        user = user_profile()
    return user.to_dict()


@cmd(no_args_is_help=False)
@json_output
def ls(namespace):
    """List users in a TileDB-Cloud organization."""
    org = cloud.organization(namespace)
    return [
        user.to_dict()
        for user in org.users
    ]


@cmd()
@role_opt
@src_nb_opt
@image_opt
@region_opt
@size_opt
@argument('emails', nargs=-1)
def add(
    namespace,
    credential_name,
    role,
    src_notebook_name,
    image,
    region,
    size,
    emails,
):
    """Add and initialize (notebook copy + defaults) one or more users to a TileDB-Cloud namespace."""
    for email in emails:
        err("Inviting", email, "to", namespace, "with role", role)
        invite.do(
            namespace=namespace,
            role=role,
            emails=(email,),
        )
        err("Copying", src_notebook_name, "to", namespace, "for", email)
        [nb_name] = nb_cp(
            namespace=namespace,
            credential_name=credential_name,
            dry_run=False,
            src_notebook_name=src_notebook_name,
            emails=(email,),
        )
        err("Setting", email, "defaults")
        nb_set_defaults(
            namespace=namespace,
            image=image,
            region=region,
            size=size,
            nb_name=nb_name,
        )
