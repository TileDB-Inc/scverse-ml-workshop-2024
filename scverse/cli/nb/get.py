from click import argument
from tiledb import cloud
from utz import err

from . import cmd
from ..base import get_arrays


@cmd('download', no_args_is_help=False)
@argument('nb-name')
@argument('dst', required=False)
def get(namespace, nb_name, dst):
    """Download a TileDB-Cloud notebook; [DST] of "-" prints to stdout."""
    arrs = get_arrays(namespace)
    [arr] = [arr for arr in arrs if arr.name == nb_name]
    if dst is None:
        dst = arr.name
        if not dst.endswith('.ipynb'):
            dst += '.ipynb'

    if dst == '-':
        nb = cloud.download_notebook_contents(tiledb_uri=arr.tiledb_uri)
        print(nb)
    else:
        cloud.download_notebook_to_file(
            tiledb_uri=arr.tiledb_uri,
            ipynb_file_name=dst,
        )
        err(f"Downloaded {arr.tiledb_uri} to {dst}")
