from os.path import basename, splitext
from typing import Optional

from click import option, argument
from tiledb import cloud
from utz import err

from . import cmd
from ..base import get_arrays


@cmd('upload')
@option('-d', '--delete', is_flag=True, help='If True, delete the notebook after uploading (e.g. for testing uploading/deleting)')
@argument('src')
@argument('dst-name', required=False)
def put(
    delete: bool,
    namespace: str,
    credential_name: str,
    storage_path: str,
    src: str,
    dst_name: Optional[str],
):
    """Upload a notebook to TileDB-Cloud."""
    if dst_name is None:
        dst_name = splitext(basename(src))[0]

    err(f"Uploading {src} to {dst_name} in namespace {namespace} with credential {credential_name}")
    cloud.upload_notebook_from_file(
        src,
        array_name=dst_name,
        namespace=namespace,
        storage_path=storage_path,
        storage_credential_name=credential_name,
    )

    arrs1 = get_arrays(namespace)
    err("Arrays after adding:")
    err('\t' + '\n\t'.join([ arr.name for arr in arrs1 ]))
    [arr] = [arr for arr in arrs1 if arr.name == dst_name]

    if delete:
        cloud.array.delete_array(arr.tiledb_uri)
        arrs2 = get_arrays(namespace)
        err("Arrays after deleting:")
        err('\t' + '\n\t'.join([ arr.name for arr in arrs2 ]))
