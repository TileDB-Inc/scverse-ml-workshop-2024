import json

from click import argument, Choice, option
from functools import partial
from tiledb import cloud
from tiledb.cloud import invites  # required for `cloud.invites` to resolve
from tiledb.cloud.rest_api.models import OrganizationRoles
from utz import err

from ...util.json import DateTimeEncoder

READ_WRITE = OrganizationRoles.READ_WRITE
ROLES = OrganizationRoles.allowable_values


from typing import cast, Any

from ..aliased_group import AliasedGroup
from ..base import cli, compact_opt, dry_run_opt
from ..command import command


@cli.group(cls=AliasedGroup)
def invite():
    """Create/List invitations to a TileDB-Cloud namespace."""
    pass


invite = cast(AliasedGroup, invite)
cmd = partial(command, invite)


def get_invites(namespace: str, emails: list[str] | None = None) -> list[dict]:
    invites = cloud.invites.fetch_invitations(organization=namespace).invitations or []
    if emails is not None:
        invites = [ i for i in invites if i.email in emails ]
    return [ i.to_dict() for i in invites ]


def get_invites_by_email(namespace: str) -> dict[str, dict]:
    return {
        invite['email']: invite
        for invite in get_invites(namespace)
    }


@cmd('list', no_args_is_help=False)
@compact_opt
def ls(namespace, compact):
    """List a TileDB-Cloud namespace's outstanding invitations"""
    invites = get_invites(namespace)
    json_kwargs: dict[str, Any] = dict(cls=DateTimeEncoder)
    if not compact:
        json_kwargs.update(indent=2)
    print(json.dumps(invites, **json_kwargs))


@cmd('send')
@option('-r', '--role', type=Choice(ROLES), default=READ_WRITE, help=f"Role to invite new user as (options: {ROLES}; default: {READ_WRITE})")
@argument('emails', nargs=-1)
def do(namespace, role, emails):
    """Invite a user to a TileDB-Cloud namespace"""
    cloud.invites.invite_to_organization(namespace, recipients=emails, role=role)


@cmd()
@dry_run_opt
@option('-S', '--no-strict', is_flag=True, help="Raise and exit if any email is not found, without revoking any invites")
@argument('emails', nargs=-1)
def rm(namespace, dry_run, no_strict, emails):
    """Revoke one or more outstanding invitations to a TileDB-Cloud namespace"""
    invites = get_invites_by_email(namespace)
    if not no_strict:
        for email in emails:
            if email not in invites:
                raise RuntimeError(f"No invitation found for {email}")
    for email in emails:
        if no_strict and email not in invites:
            err(f"No invitation found for {email}")
            continue
        invite = invites[email]
        id = invite['id']
        if dry_run:
            err(f"Would cancel invite {id} to {email}")
        else:
            cloud.invites.cancel_invite_to_organization(namespace, invitation_id=id)
            err(f"Revoked invite {id} to {email}")
