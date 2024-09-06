import json
from click import argument, option
from functools import partial, wraps
from tiledb import cloud
from tiledb.cloud import invites  # required for `cloud.invites` to resolve
from tiledb.cloud.client import client
from tiledb.cloud.rest_api import InvitationApi, InvitationOrganizationJoinEmail, ApiException
from tiledb.cloud.tiledb_cloud_error import maybe_wrap
from typing import cast, Any, Optional, Sequence
from utz import err, decos

from ..aliased_group import AliasedGroup
from ..base import cli, compact_opt, dry_run_opt, role_opt
from ..command import command
from ...util.json import DateTimeEncoder


@cli.group(cls=AliasedGroup)
def invite():
    """Create/List invitations to a TileDB-Cloud namespace."""
    pass


invite = cast(AliasedGroup, invite)
cmd = partial(command, invite)


def get_invites(namespace: str, emails: Optional[list[str]] = None) -> list[dict]:
    invites = cloud.invites.fetch_invitations(organization=namespace).invitations or []
    if emails is not None:
        invites = [ i for i in invites if i.email in emails ]
    return [ i.to_dict() for i in invites ]


def get_invites_by_email(namespace: str) -> dict[str, list[dict]]:
    invites = {}
    for invite in get_invites(namespace):
        email = invite['email']
        if email not in invites:
            invites[email] = []
        invites[email].append(invite)
    return invites


@cmd('list', no_args_is_help=False)
@compact_opt
def ls(namespace, compact):
    """List a TileDB-Cloud namespace's outstanding invitations"""
    invites = get_invites(namespace)
    json_kwargs: dict[str, Any] = dict(cls=DateTimeEncoder)
    if not compact:
        json_kwargs.update(indent=2)
    print(json.dumps(invites, **json_kwargs))


def invite_to_organization(
    organization: str,
    *,
    recipients: Sequence[str],
    role: str,
    actions: Optional[Sequence[str]] = None,
) -> None:
    """
    Sends email to multiple recipients with joining information
    regarding an organization. Copied from TileDB-Cloud-Py, to
    incorporate the fix from https://github.com/TileDB-Inc/TileDB-Cloud-Py/pull/637.

    :param organization: name or UUID of organization.
    :param recipients: list of recipient emails/usernames.
    :param role: role assigned to the recipient.
    :param actions: list of actions assigned to the recipient.
    :return: None
    """
    invitation_api = client.build(InvitationApi)
    email_invite = InvitationOrganizationJoinEmail(
        actions=actions, organization_role=role, invitee_email=recipients
    )
    try:
        return invitation_api.join_organization(organization, email_invite)
    except ApiException as exc:
        raise maybe_wrap(exc)


def do(namespace, role, emails):
    """Invite a user to a TileDB-Cloud namespace."""
    invite_to_organization(namespace, recipients=emails, role=role)


_do = decos(
    cmd('send'),
    role_opt,
    argument('emails', nargs=-1),
    wraps(do),
)(do)


@cmd()
@dry_run_opt
@option('-S', '--no-strict', is_flag=True, help="Raise and exit if any email is not found, without revoking any invites")
@argument('emails', nargs=-1)
def rm(namespace, dry_run, no_strict, emails):
    """Revoke one or more outstanding invitations to a TileDB-Cloud namespace"""
    invites_by_email = get_invites_by_email(namespace)
    if not no_strict:
        for email in emails:
            if email not in invites_by_email:
                raise RuntimeError(f"No invitation found for {email}")
    for email in emails:
        if no_strict and email not in invites_by_email:
            err(f"No invitation found for {email}")
            continue
        invites = invites_by_email[email]
        for invite in invites:
            id = invite['id']
            if dry_run:
                err(f"Would cancel invite {id} to {email}")
            else:
                cloud.invites.cancel_invite_to_organization(namespace, invitation_id=id)
                err(f"Revoked invite {id} to {email}")
