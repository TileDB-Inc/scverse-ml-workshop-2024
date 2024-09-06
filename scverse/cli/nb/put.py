from os.path import basename, splitext
from typing import Optional

from click import option, argument
from tiledb import cloud
from utz import err

from tiledb.cloud.files import upload

from tiledb.cloud.notebook import OnExists
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

    arrs = get_arrays(namespace)
    existing_arrays = [
        arr
        for arr in arrs
        if arr.name == dst_name
    ]
    if len(existing_arrays) > 1:
        raise RuntimeError(f"{len(existing_arrays)} arrays with name {dst_name} found in namespace {namespace}")
    elif len(existing_arrays) == 1:
        dest_uri = existing_arrays[0].tiledb_uri
        upload_kwargs = dict(
            dest_uri=dest_uri,
            on_exists=OnExists.OVERWRITE,
        )
        err(f"Array with name {dst_name} already exists in {namespace} ({dest_uri}); overwriting…")
    else:
        upload_kwargs = dict(
            array_name=dst_name,
            namespace=namespace,
        )
        err(f"Uploading {src} to {dst_name} in namespace {namespace} with credential {credential_name}")

    cloud.upload_notebook_from_file(
        src,
        **upload_kwargs,
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
