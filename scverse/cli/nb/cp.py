from os import path

import re
from click import argument
from tiledb.cloud.client import client
from tiledb.cloud.rest_api.api.notebook_api import NotebookApi
from tiledb.cloud.rest_api.models.notebook_copy import NotebookCopy
from typing import Tuple
from utz import err, decos

from . import cmd
from ..base import get_arrays, dry_run_opt, src_nb_opt, PARTICIPANTS_NB_DIR


def sanitize_email(email: str) -> str:
    return re.sub(r'\W', '-', email.lower().strip())


def cp(
    namespace: str,
    credential_name: str,
    dry_run: bool,
    src_notebook_name: str,
    emails: Tuple[str],
):
    """Create one or more copies of a "template" notebook, with names corresponding to provided email addresses."""
    notebook_api = client.build(NotebookApi)

    dsts = [
        sanitize_email(email)
        for email in emails
    ]
    for dst in dsts:
        notebook_copy = NotebookCopy(
            namespace=namespace,
            name=dst,
            output_uri=path.join(f"s3://tiledb-conferences-us-west-2/{namespace}", PARTICIPANTS_NB_DIR, dst)
        )
        if dry_run:
            err(f"Would copy {src_notebook_name} to {dst}")
        else:
            notebook_api.handle_copy_notebook(
                namespace=namespace,
                array=src_notebook_name,
                notebook_copy=notebook_copy,
                x_tiledb_cloud_access_credentials_name=credential_name,
            )

    arrs1 = get_arrays(namespace)
    err("Arrays after copying:")
    err('\t' + '\n\t'.join([ arr.name for arr in arrs1 ]))

    return dsts


_cp = decos(
    cmd('copy'),
    dry_run_opt,
    src_nb_opt,
    argument('emails', nargs=-1),
)(cp)
