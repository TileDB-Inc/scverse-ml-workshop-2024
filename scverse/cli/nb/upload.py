from os.path import basename, splitext

from click import option, argument
from tiledb import cloud
from utz import err

from . import cmd
from ..base import get_arrays


@cmd('put')
@option('-d', '--delete', is_flag=True, help='If True, delete the notebook after uploading')
@option('-n', '--dst-name', help='Destination notebook name')
@argument('src')
def upload(
    dst_name: str | None,
    delete: bool,
    namespace: str,
    credential_name: str,
    src: str,
):
    """Upload a notebook to TileDB-Cloud."""
    if dst_name is None:
        dst_name = splitext(basename(src))[0]

    cloud.upload_notebook_from_file(
        src,
        array_name=dst_name,
        namespace=namespace,
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
